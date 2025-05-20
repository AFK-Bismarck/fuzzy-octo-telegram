# Weather Bot | Projekta dokumentācija

# Laikapstākļu un Apģērba Ieteikumu Discord Bots

## Projekta uzdevums

Šī projekta mērķis ir izveidot Discord bota komandu, kas spēj sniegt aktuālu informāciju par laikapstākļiem izvēlētajās pilsētās (piemēram, Rīgā, Londonā, Berlīnē, Parīzē, Romā un Madridē), kā arī sniegt apģērba ieteikumus, balstoties uz konkrētajiem laika apstākļiem.

Lietotājs izvēlas pilsētu no saraksta, un bots atbild ar iekapsulētu ziņojumu (embed), kurā tiek attēlota informācija par:

Pašreizējo temperatūru

Sajūtu temperatūru

Minimālo un maksimālo temperatūru

Laikapstākļu aprakstu

Ieteicamo apģērbu

## Izmantotās Python bibliotēkas un to pielietojums

**requests** – izmanto, lai iegūtu datus no Open-Meteo API par laikapstākļiem.

**re** – izmanto regulāro izteiksmju apstrādei, lai no komandas iegūtu pilsētas vērtību.

**datetime** – pievienots iespējamai nākotnes funkcionalitātei, kas saistīta ar datumu un laiku.

**hikari** – bibliotēka Discord bota izveidei un embed ziņojumu sūtīšanai.

**lightbulb** – papildu bibliotēka, kas vienkāršo slash komandu izveidi un vadību ar hikari.

## Datu struktūras

Projektā tiek izmantotas šādas paša definētas datu struktūras:

**Vārdnīca (dictionary)**: ar laikapstākļu kodiem. Tā pārvērš laika kodus (piemēram, 0–99) saprotamā tekstā. Katrai kodu grupai ir pievienots skaidrojums, piemēram: "Rain", "Snow", "Clear sky".

**Tuple**: funkcija weather_data() atgriež piecu elementu tuple ar datiem: laika apraksts, temperatūra, minimālā temperatūra, maksimālā temperatūra, sajūtu temperatūra.

## Programmatūras izmantošana

Lietotājs Discord vidē izmanto slash komandu:

```bash
/weather city:Riga
```

Kad komanda tiek izsaukta:

Tiek nolasīta lietotāja izvēlētā pilsēta.

Tiek izsaukta funkcija weather_data(), lai saņemtu aktuālos datus no Open-Meteo API.

Balstoties uz temperatūru un apstākļiem, funkcija outfit_recommender() nosaka piemērotu apģērbu.

Bots atbild ar embed ziņojumu, kurā ietverta visa informācija.

## Nobeigums

Projekts apvieno datu iegūšanu no ārēja API, datu apstrādi un Discord mijiedarbību, izmantojot Python valodu un vairākas bibliotēkas. Tas kalpo kā labs piemērs praktiskai darbībai ar tīmekļa datiem un automatizētām atbildēm Discord vidē.
