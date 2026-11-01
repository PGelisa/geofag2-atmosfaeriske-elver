# En elv i luften – atmosfæriske elver

Dataoppgave i Geofag 2 (REA3043) om atmosfæriske elver. Eksempelet er ekstremværet Jakob, som ga rødt farevarsel for ekstremt mye regn i Vestland 30. oktober–1. november 2024. Økten tar 120 minutter.

Elevene bruker ekte data til å se elven på kartet og regne ut hvor mye vann den fraktet. De ser også hvordan fjellene på Vestlandet gjorde vanndampen om til over 200 mm regn på ett døgn, og hva et varmere klima betyr for slike hendelser.

## For elever

Du trenger conda-miljøet `geofag2` fra guiden [Installere og åpne Jupyter Lab](https://pgelisa.github.io/geofag2-python-opendrift/).

**Hent filene**

1. Trykk den grønne knappen **Code** øverst på denne siden og velg **Download ZIP**.
2. Flytt zip-fila fra Nedlastinger til geofag-mappen din før du pakker den ut.
   - **Mac:** dobbeltklikk zip-fila i geofag-mappen.
   - **Windows:** høyreklikk zip-fila og velg **Pakk ut alle**. Velg geofag-mappen som mål.
3. Slett zip-fila fra Nedlastinger.

Kan du bruke git, går det også fint med `git clone`.

**Åpne notatboken**

```
conda activate geofag2
jupyter lab
```

Gå til mappen du pakket ut, og åpne `atmosfaerisk_elv_jakob.ipynb`. Mappen `data` må ligge ved siden av notatboken.

## For lærere

Se [laererveiledning.md](laererveiledning.md) for tidsplan, fakta fra MET, løsningsforslag og hvordan du henter dataene med `hent_data_jakob.py`.

## Datakilder

- ERA5 (Copernicus Climate Change Service, ECMWF)
- Stasjonsdata fra Meteorologisk institutt (Frost API)
- Nedbørserie for Bergen fra ERA5 via Open-Meteo (Weather data by Open-Meteo.com, CC BY 4.0)
- Bakgrunn: MET Norge, hendelsesrapport om ekstremværet Jakob (MET info 37/2024)

Laget av Elisabeth Engum, Amalie Skram videregående skole.
