# En elv i luften – atmosfæriske elver

Dataoppgave i Geofag 2 (REA3043) om atmosfæriske elver. Eksempelet er ekstremværet Jakob, som ga rødt farevarsel for ekstremt mye regn i Vestland 30. oktober–1. november 2024. Økten tar 120 minutter.

Elevene bruker ekte data til å se elven på kartet og regne ut hvor mye vann den fraktet. De ser også hvordan fjellene på Vestlandet gjorde vanndampen om til over 200 mm regn på ett døgn, og hva et varmere klima betyr for slike hendelser.

## For elever

**Se notatboken uten å installere noe.** Trykk på `atmosfaerisk_elv_jakob_kjort.ipynb` i fillisten ovenfor. Det er en ferdig kjørt versjon, så du ser alle figurene og tallene rett i nettleseren.

**Vil du kjøre koden selv**, trenger du conda-miljøet `geofag2` og mappen `Geofag2-filer` fra guiden [Installere og åpne Jupyter Lab](https://pgelisa.github.io/geofag2-python-opendrift/).

**Hent filene**

1. Trykk den grønne knappen **Code** øverst på denne siden og velg **Download ZIP**.
2. Flytt zip-filen fra Nedlastinger til mappen `Geofag2-filer` før du pakker den ut. Mappen lager du i steg 3 i guiden.
   - **Mac:** dobbeltklikk zip-filen i `Geofag2-filer`.
   - **Windows:** høyreklikk zip-filen og velg **Pakk ut alle**. Velg `Geofag2-filer` som mål.
3. Slett zip-filen fra Nedlastinger.

Finner du ikke `Geofag2-filer`? Skriv `cd Geofag2-filer` i Terminal (Mac) eller Miniforge Prompt (Windows), og deretter `open .` (Mac) eller `explorer .` (Windows). Da åpnes mappen i Finder eller Filutforsker.

Kan du bruke git, går det også fint med `git clone`.

**Åpne notatboken**

```
conda activate geofag2
cd Geofag2-filer
jupyter lab
```

Gå til mappen du pakket ut, og åpne `atmosfaerisk_elv_jakob.ipynb`. Mappen `data` må ligge ved siden av notatboken.

## Hva kan du endre?

I cellene merket 🔧 kan du endre verdier og kjøre cellen på nytt. Dataene dekker bare en bestemt periode og et bestemt område. Velger du et tidspunkt eller et sted utenfor, bruker notatboken det nærmeste som finnes i dataene. Da kan figuren se riktig ut selv om den viser noe annet enn du tror, så sjekk alltid tid og sted i figurtittelen.

| Del | Variabel | Dette kan du velge |
|---|---|---|
| 1a | `TIDER` | Tre tidspunkter fra 29.10 kl. 00 til 01.11 kl. 21 UTC, hver 3. time (kl. 00, 03, 06 og så videre) |
| 1b | `TID_B` | Et tidspunkt i samme periode |
| 1c | `LON_SNITT` | En lengdegrad fra 50° V til 25° Ø. Skriv vestlige lengdegrader som negative tall, for eksempel −20 |
| 1c | `TID_C` | Et tidspunkt i samme periode |
| 2a | `FRA`, `TIL` | En periode fra 29.10 kl. 00 til 01.11 kl. 23 UTC |
| 2b | `LAT_PROFIL` | En breddegrad fra 57° N til 64° N |
| 2c | `IVT_KYST`, `ANDEL`, `L_KM`, `TIMER` | Tallene i regnestykket. Her kan du velge fritt |
| 2e | `STED` | Bergen, Voss, Odda, Kinsarvik eller Førde |
| 3a | `T0` | En temperatur (°C) |
| 3b | `KILDE` | `"stasjon"` for Bergen – Florida fra 1983, eller `"era5"` for Bergen fra 1940 |
| 3b | `TERSKEL` | Grensen (mm per døgn) for kraftig nedbør |
| B | `TERSKEL_IVT` | Grensen (kg/(m·s)) for hva som regnes som elven |

**Hva dataene dekker**

| Data | Periode | Område | Oppløsning |
|---|---|---|---|
| IVT, vanndamp, trykk og nullgradersgrense (ERA5) | 29.10 kl. 00 til 01.11 kl. 21 UTC | 35–72° N, 50° V–25° Ø | Hver 3. time, 0,5° |
| Nedbør og terrenghøyde (ERA5) | 29.10 kl. 00 til 01.11 kl. 23 UTC | 57–64° N, 3–13° Ø | Hver time, 0,25° |
| Gullfjellet og Haukedal (MET) | 29.10 kl. 00 til 01.11 kl. 23 UTC | Stasjoner | Hver time |
| Bergen – Florida (MET) | 01.01.1983–30.09.2026 | Stasjon | Ett tall per døgn |
| Bergen (ERA5) | 01.01.1940–30.09.2026 | Én rute | Ett tall per døgn |

Snittet i 1c bruker bare breddegradene fra 50° N til 70° N. Øvstedal er nevnt i MET-rapporten, men timesdata for stasjonen kom ikke med i nedlastingen, så den er ikke med i 2d.

Stasjonsserien fra Bergen – Florida starter i 1983. Gjennomsnittet for 1961–1990 i 3b bygger derfor bare på årene 1983–1990, og det glidende 30-årsmiddelet starter først i 1988. Du kan bytte til ERA5-serien for Bergen med `KILDE = "era5"`. Den går tilbake til 1940, men jevner ut de største regnmengdene.

## For lærere

Se [laererveiledning.md](laererveiledning.md) for tidsplan, fakta fra MET, løsningsforslag og hvordan du henter dataene med `hent_data_jakob.py`.

## Datakilder

- ERA5 (Copernicus Climate Change Service, ECMWF)
- Stasjonsdata fra Meteorologisk institutt (Frost API)
- Nedbørserie for Bergen fra ERA5 via Open-Meteo (Weather data by Open-Meteo.com, CC BY 4.0)
- Bakgrunn: MET Norge, hendelsesrapport om ekstremværet Jakob (MET info 37/2024)

Laget av Elisabeth Engum, Amalie Skram videregående skole.
