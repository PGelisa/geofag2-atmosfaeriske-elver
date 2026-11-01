# En elv i luften – lærerveiledning

Økt på 120 minutter i Geofag 2 om atmosfæriske elver. Opplegget bruker ekstremværet Jakob (30. oktober–1. november 2024) som eksempel. Elevene jobber i `atmosfaerisk_elv_jakob.ipynb` i JupyterLab i conda-miljøet `geofag2`. Notatboken bruker bare pakkene fra Miniforge-guiden (numpy, pandas, matplotlib, xarray, netcdf4, cartopy).

**Faglig innhold:** vanndamp og vanndamptransport (IVT), atmosfæriske elver langs kaldfronten i lavtrykk, orografisk nedbør og regnskygge, nullgradersgrensen og flomfare, Clausius–Clapeyron (omtrent 7 % mer vanndamp per grad), lange nedbørserier og varsling.

## Mappestruktur

```
atmosfaeriske-elver/
├── atmosfaerisk_elv_jakob.ipynb   elevnotatboken
├── hent_data_jakob.py             kjøres én gang av læreren
├── laererveiledning.md
└── data/                          fylles av skriptet
    ├── era5_jakob_kart.nc         IVT, vanndamp, trykk og 0-gradersnivå hver 3. time, 29.10–01.11.2024
    ├── era5_jakob_nedbor.nc       nedbør hver time og terrenghøyde over Sør-Norge
    ├── stasjon_<navn>_time.csv    timesnedbør fra Gullfjellet, Øvstedal og Haukedal (Frost)
    ├── stasjon_florida_dogn.csv   døgnnedbør Bergen – Florida fra ca. 1904 (Frost)
    └── punkt_bergen_nedbor.csv    døgnnedbør Bergen 1940–2026 fra ERA5 (Open-Meteo, reserve)
```

## Forberedelse (ca. 30 min, én gang)

1. Du trenger to ting.
   - **CDS-konto for ERA5.** Lag konto på Copernicus Climate Data Store (cds.climate.copernicus.eu), godta lisensen for ERA5, og legg API-nøkkelen i `~/.cdsapirc` slik det står på siden «How to API». Installer `cdsapi` med `conda install -c conda-forge cdsapi`.
   - **Frost-klient-ID for norske stasjoner.** Gratis på frost.met.no. Velg «Request client credentials», og du får en klient-ID på e-post.
2. Kjør skriptet fra mappen `atmosfaeriske-elver`:
   ```
   conda activate geofag2
   python hent_data_jakob.py --era5 --frost DIN-KLIENT-ID
   ```
   Skriptet slår opp stasjonsnumrene i Frost ut fra navnene og skriver ut treffene. Sjekk at det har valgt riktige stasjoner.
3. Åpne notatboken og kjør alle cellene. Fyll inn tallene merket ☐ nedenfor.

### ERA5 manuelt (hvis cdsapi ikke virker)

| Fil | Datasett | Variabler | Tid (UTC) | Område (N, V, S, Ø) | Rutenett |
|---|---|---|---|---|---|
| era5_jakob_kart | ERA5 hourly data on single levels | Vertical integral of eastward water vapour flux, Vertical integral of northward water vapour flux, Total column water vapour, Mean sea level pressure, Zero degree level | 29.10–01.11.2024, hver 3. time | 72, −50, 35, 25 | 0,5° × 0,5° |
| era5_jakob_nedbor | samme | Total precipitation, Geopotential | 29.10–01.11.2024, hver time | 64, 3, 57, 13 | 0,25° (standard) |

Skriptet gir variablene norske navn, gjør om trykk til hPa, nedbør til mm og geopotensial til meter.

## Tidsplan

| Tid | Del | Merknad |
|---|---|---|
| 0–10 | Oppstart og hypotese | Vis gjerne et satellittbilde (vanndampkanal) fra 31.10.2024 |
| 10–35 | Del 1 Elven i luften | 1a–1c. 1c gir det mest slående tallet |
| 35–60 | Del 2 Når elven treffer fjellene | 2a–2e. Kutt 2e hvis tiden blir knapp |
| 60–70 | Pause | |
| 70–100 | Del 3 Varmere luft, mer regn? | 3a Clausius–Clapeyron og 3b lange serier |
| 100–120 | Del 4 Oppsummering | Skriftlig svar med tre tall, og refleksjon om varsling |

## Fakta fra MET sin hendelsesrapport (MET info 37/2024)

- En lang vestlig luftstrøm førte varm og fuktig luft inn over Sør-Norge torsdag 31. oktober. Et høytrykk over De britiske øyer holdt regnbeltet nesten i ro over deler av Vestland i omtrent ett døgn. Sterk vind i høyden presset regnet langt inn i fjordene og fjellene.
- 29.10 sendte MET oransje farevarsel. 30.10 ble varselet oppgradert til rødt for midtre og indre strøk av Vestland (120–180 mm/24 t), og ekstremværet fikk navnet Jakob. Tersklene var gult 60–100, oransje 100–150 og rødt 120–180 mm/24 t.
- Mest nedbør på 24 timer (glidende) var 206,0 mm på Gullfjellet i Bergen. Over 15 stasjoner fikk ny novemberrekord for døgnnedbør, blant annet Øvstedal 175,5 mm og Haukedal 140,5 mm. Norske døgnverdier måles fra kl. 06 til kl. 06 UTC og dateres ved slutten av døgnet, så verdiene for 1. november gjelder i hovedsak regnet 31. oktober.
- Ni stasjoner fikk mer nedbør enn 50-årsverdien for 24 timer, alle i midtre og indre Vestland. Noen verdier tilsvarte hendelser som kommer sjeldnere enn hvert 50.–200. år.
- Natt til fredag 1. november snudde vinden til nordvest. Det ble byger og kaldere luft, og snøgrensen sank til ca. 800 m i nord og 1200 m i sør.
- Rundt 40 veier ble stengt, og Bergensbanen sto. Det var flomskader i Kinsarvik og Odda, og bruer ble tatt, blant annet på riksvei 550 i Ullensvang. Hotel Ullensvang og Jostedalsbreen nasjonalparksenter fikk store skader.

## Løsningsforslag og stikkord

Fyll inn tallene merket ☐ når du har kjørt notatboken med ekte data.

**1a** ☐ lengde og bredde. Elven er typisk flere tusen km lang og noen hundre km bred. Den kommer fra sørvest, fra subtropisk Atlanterhav, og ligger i den varme luften foran kaldfronten, på sørsiden av lavtrykket. ☐ største IVT ved kysten og hvor lenge den lå over Vestlandet.

**1b** ☐ vanndampinnhold over Bergen. I en atmosfærisk elv ved norskekysten er det typisk noen titalls millimeter, altså mye mindre enn 206 mm. Vannet må altså strømme kontinuerlig inn, og det er transporten (vind × fuktighet) som gir nedbøren. IVT blir størst der både fuktigheten og vinden er stor, så maksimumene trenger ikke ligge samme sted.

**1c** ☐ transport i m³/s. En kraftig atmosfærisk elv frakter omtrent like mye vann som Amazonas, altså flere hundre ganger mer enn Glomma. Transporten varierer med hvor snittet ligger og hvor sterk elven er.

**2a–2b** ☐ hvor nedbøren var størst. Mest nedbør i midtre strøk og der luften først treffer høye fjell. Mindre øst for vannskillet (regnskygge). ERA5 viser lavere verdier enn stasjonene fordi terrenget og nedbøren er glattet ut på 25 km ruter. Under Jakob gjorde sterk vind i høyden at regnet ble presset langt inn, slik at også indre strøk fikk mye.

**2c** Med IVT 600 kg/(m·s), e = 0,4 og L = 150 km blir det omtrent 5,8 mm per time og 138 mm på 24 timer, altså samme størrelsesorden som det som ble målt. Andelen e er mest usikker. Høye og bratte fjell løfter luften kraftig og gir større e.

**2d** ☐ når det regnet mest og største timeverdi. Langvarig, jevnt og kraftig regn, ikke korte skybrudd. Det er varigheten som gir de store summene.

**2e** ☐ nullgradersgrensen. Mens elven lå over Vestlandet, var den høy (typisk over 2000 m), så det regnet også i fjellet. Regn i fjellet gir raskere avrenning enn snø, og det kan smelte snø som ligger der fra før. Etter at kaldfronten passerte, sank nullgradersgrensen fordi kaldere luft fra nordvest kom inn.

**3a** Omtrent 6–7 % per grad (6,9 % ved 10 °C). Med 2 °C varmere luft gir det rundt 14 % mer, det vil si omtrent 235 mm i stedet for 206 mm. Nedbøren kan øke mer, fordi ekstra latent varme kan forsterke oppdriften, eller mindre, hvis vinden eller banen til lavtrykkene endrer seg.

**3b** ☐ tall for Bergen. Bjerknessenteret fant at nedbøren i Norge har økt med om lag 20 % siden 1900, mest på Sørvestlandet, og at frontnedbøren ventes å øke med omtrent 5 % per grad oppvarming.

**Refleksjon** Varselet traff godt på hvor og når, og nivået (120–180 mm) var riktig for de fleste stasjonene. Lokale topper (206 mm) er vanskelige å treffe fordi små forskjeller i vindretning avgjør hvilke fjellsider som får mest.

## Om dataene

- **ERA5** har ruter på omtrent 25 km (kartene her er på 0,5°) og glatter ut fjellene. Derfor blir nedbøren lavere enn på stasjonene.
- **IVT** i ERA5 er regnet ut av ECMWF fra vind og fuktighet i alle modellnivåene.
- **Status for testingen.** Notatboken er kjørt fra start til slutt med syntetiske testdata, ikke med de ekte filene, fordi Copernicus, Frost og Open-Meteo ikke var tilgjengelige der notatboken ble laget. Første gang du kjører med ekte data, bør du se ekstra nøye på variabelnavnene for IVT i ERA5-fila (`viwve`/`viwvn`) og på stasjonene Frost finner.

## Kilder

- Meteorologisk institutt (2024). *Hendelsesrapport ekstremværet Jakob*. MET info 37/2024.
- Store norske leksikon. *Atmosfæriske elver*. snl.no
- Bjerknessenteret for klimaforskning. *A wild and wet future*. bjerknes.uib.no
- Michel mfl. (2021). Characterization of the atmospheric environment during extreme precipitation events associated with atmospheric rivers in Norway. *Weather and Climate Extremes* 34, 100370.
- Hersbach mfl. (2020). ERA5. *QJRMS* 146, 1999–2049.
