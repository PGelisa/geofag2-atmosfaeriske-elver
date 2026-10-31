"""
Henter data om ekstremværet Jakob (atmosfærisk elv, 30. oktober–1. november 2024)
til elevoppgaven i Geofag 2.

Kjøres ÉN gang av læreren. Filene havner i mappen data/ ved siden av
skriptet og kan legges i repoet, slik at elevene slipper å laste ned noe.

Bruk (i terminalen, med miljøet aktivert):

    conda activate geofag2
    python hent_data_jakob.py                     # nedbørserie for Bergen (ingen konto)
    python hent_data_jakob.py --era5              # + ERA5-kart (krever CDS-konto)
    python hent_data_jakob.py --frost KLIENT-ID   # + stasjonsdata fra MET
    python hent_data_jakob.py --era5 --frost KLIENT-ID

Ekstra pakke som bare læreren trenger (for --era5):

    conda install -c conda-forge cdsapi

Datakilder
----------
- Kart: ERA5 timesdata (Copernicus Climate Data Store)
- Norske stasjoner: MET Norge, Frost API (gratis klient-ID på frost.met.no)
- Lang nedbørserie for Bergen: ERA5 via Open-Meteo (ingen konto)
"""

import argparse
from pathlib import Path

import pandas as pd
import requests
import xarray as xr

DATA = Path(__file__).resolve().parent / "data"
DATA.mkdir(exist_ok=True)

# Stasjoner fra MET sin hendelsesrapport (MET info 37/2024). Navnene slås opp i Frost.
STASJONER_TIME = ["Gullfjellet", "Øvstedal", "Haukedal"]
STASJON_LANG = "Bergen - Florida"
FROST = "https://frost.met.no"


def lagre(ds, fil):
    """Komprimert NetCDF med 32-biters tall (små filer)."""
    enc = {v: {"zlib": True, "complevel": 4, "dtype": "float32"} for v in ds.data_vars}
    ds.to_netcdf(fil, encoding=enc)


def filnavn(navn):
    navn = navn.lower().split(" - ")[-1]
    for a, b in [("ø", "o"), ("å", "a"), ("æ", "ae"), (" ", "_")]:
        navn = navn.replace(a, b)
    return navn


# ---------------------------------------------------------------------------
# 1 Lang nedbørserie for Bergen fra ERA5 (Open-Meteo)
# ---------------------------------------------------------------------------
def hent_punktserie():
    print("Henter nedbør i Bergen 1940–2026 (ERA5 via Open-Meteo) ...")
    r = requests.get("https://archive-api.open-meteo.com/v1/archive", timeout=300, params={
        "latitude": 60.38, "longitude": 5.33, "start_date": "1940-01-01",
        "end_date": "2026-09-30", "daily": "precipitation_sum",
        "timezone": "auto", "models": "era5"})
    r.raise_for_status()
    d = r.json()["daily"]
    pd.DataFrame({"dato": d["time"], "nedbor": d["precipitation_sum"]}).to_csv(
        DATA / "punkt_bergen_nedbor.csv", index=False)
    print("  punkt_bergen_nedbor.csv")


# ---------------------------------------------------------------------------
# 2 Stasjonsdata fra Frost (MET Norge)
# ---------------------------------------------------------------------------
def finn_stasjon(klient_id, navn):
    r = requests.get(f"{FROST}/sources/v0.jsonld", auth=(klient_id, ""), timeout=60,
                     params={"types": "SensorSystem", "name": navn.upper() + "*"})
    r.raise_for_status()
    treff = r.json()["data"]
    print(f"  {navn}: {', '.join(t['id'] + ' ' + t['name'] for t in treff[:4])}")
    return treff[0]["id"]


def frost_obs(klient_id, kilde, element, tid):
    r = requests.get(f"{FROST}/observations/v0.jsonld", auth=(klient_id, ""), timeout=300,
                     params={"sources": kilde, "elements": element, "referencetime": tid,
                             "timeoffsets": "default", "levels": "default"})
    if r.status_code != 200:
        print(f"    feil {r.status_code}: {r.text[:200]}")
        return None
    rader = [(d["referenceTime"], d["observations"][0]["value"]) for d in r.json()["data"]]
    return pd.DataFrame(rader, columns=["tid", "nedbor"]).drop_duplicates("tid")


def hent_frost(klient_id):
    print("Henter stasjonsdata fra Frost (MET Norge) ...")
    for navn in STASJONER_TIME:
        sn = finn_stasjon(klient_id, navn)
        df = frost_obs(klient_id, sn, "sum(precipitation_amount PT1H)",
                       "2024-10-29T00:00:00Z/2024-11-02T00:00:00Z")
        if df is not None:
            df.to_csv(DATA / f"stasjon_{filnavn(navn)}_time.csv", index=False)
            print(f"    stasjon_{filnavn(navn)}_time.csv ({len(df)} timer, {sn})")

    sn = finn_stasjon(klient_id, STASJON_LANG)
    df = frost_obs(klient_id, sn, "sum(precipitation_amount P1D)", "1900-01-01/2026-10-01")
    if df is not None:
        df["dato"] = df.tid.str[:10]
        df[["dato", "nedbor"]].to_csv(DATA / "stasjon_florida_dogn.csv", index=False)
        print(f"    stasjon_florida_dogn.csv ({len(df)} døgn, {sn})")


# ---------------------------------------------------------------------------
# 3 ERA5 (krever konto på https://cds.climate.copernicus.eu og ~/.cdsapirc)
# ---------------------------------------------------------------------------
def apne(fil):
    ds = xr.open_dataset(fil).load()
    fil.unlink()
    navn = {"valid_time": "time", "latitude": "lat", "longitude": "lon"}
    ds = ds.rename({k: v for k, v in navn.items() if k in ds.variables})
    ds = ds.drop_vars([v for v in ["expver", "number"] if v in ds.variables])
    return ds.sortby("lat")


def hent_era5():
    import cdsapi

    c = cdsapi.Client()
    felles = {"product_type": ["reanalysis"], "year": ["2024"],
              "data_format": "netcdf", "download_format": "unarchived"}

    print("ERA5: vanndamptransport, vanndamp, trykk og 0-gradersnivå (hver 3. time) ...")
    tmp = DATA / "_tmp_kart.nc"
    c.retrieve("reanalysis-era5-single-levels", {
        **felles,
        "variable": ["vertical_integral_of_eastward_water_vapour_flux",
                     "vertical_integral_of_northward_water_vapour_flux",
                     "total_column_water_vapour", "mean_sea_level_pressure",
                     "zero_degree_level"],
        "month": ["10", "11"], "day": ["01", "29", "30", "31"],
        "time": [f"{h:02d}:00" for h in range(0, 24, 3)],
        "area": [72, -50, 35, 25], "grid": [0.5, 0.5]}, str(tmp))
    ds = apne(tmp)
    ds = ds.sel(time=slice("2024-10-29", "2024-11-01T23:00"))
    navn = {"viwve": "ivt_u", "p71.162": "ivt_u", "viwvn": "ivt_v", "p72.162": "ivt_v",
            "tcwv": "tcwv", "msl": "msl", "deg0l": "nullgrad"}
    ds = ds.rename({k: v for k, v in navn.items() if k in ds.data_vars})
    ds["msl"] = ds.msl / 100
    lagre(ds[["ivt_u", "ivt_v", "tcwv", "msl", "nullgrad"]], DATA / "era5_jakob_kart.nc")
    print("  era5_jakob_kart.nc")

    print("ERA5: nedbør hver time og terrenghøyde over Sør-Norge ...")
    tmp = DATA / "_tmp_nedbor.nc"
    c.retrieve("reanalysis-era5-single-levels", {
        **felles, "variable": ["total_precipitation", "geopotential"],
        "month": ["10", "11"], "day": ["01", "29", "30", "31"],
        "time": [f"{h:02d}:00" for h in range(24)],
        "area": [64, 3, 57, 13]}, str(tmp))
    ds = apne(tmp).sel(time=slice("2024-10-29", "2024-11-01T23:00"))
    ut = xr.Dataset({"nedbor": ds.tp * 1000,                          # m → mm per time
                     "hoyde": (ds.z.isel(time=0, drop=True) / 9.80665).clip(min=0)})
    lagre(ut, DATA / "era5_jakob_nedbor.nc")
    print("  era5_jakob_nedbor.nc")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--era5", action="store_true", help="hent ERA5-kart (CDS-konto)")
    p.add_argument("--frost", metavar="KLIENT_ID", help="hent stasjonsdata fra MET")
    a = p.parse_args()

    hent_punktserie()
    if a.frost:
        hent_frost(a.frost)
    if a.era5:
        hent_era5()
    print("\nFerdig. Filene ligger i", DATA)
