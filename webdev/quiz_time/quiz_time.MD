# Quiz App

## Introductie
Coder Dojo NL wilt graag een QuiZ app bouwen om de kennis te testen de deelnemers. Er is al een opzet gedaan, maar de logica van de applicatie moet nog gebouwd worden.

In deze opdracht ga je een webapplicatie afbouwen en verder uitbreiden. Dit doe je in iteraties (stappen) waarbij je aan het eind van iedere stap een deel van de quiz app afbouwd.

## Voorbereiding
- download de folder `sommen_maker` en plaats dit op een makkelijk vindbare plek.
- open de folder in vscode
- check of alles goed is geinstalleerd door `speeltuin.py` te runnen. Dit kan je doen door de ▶️ knop rechtboven in te drukken
- check dat de app geen fouten bevat door `quiz_time.py` te runnen. Ga naar `localhost:5000` en check of de pagina laadt.

## Iteraties

### 1. Vragen inlezen
Een quiz zonder vragen, is als een laptop zonder programma's. In de eerste stap gaan we de quiz vragen bedenken en gebruiken we Python om de vragen in te lezen (in het geheugen van de computer).

Coder Dojo wilt graag dat de data in `CSV` formaat ingelezen wordt, omdat dit makkelijk is bij te houden. `CSV` staat voor Comma Seperated Values, ofwel waardes worden gesplitst door middel van comma. Onder /data is een voorbeeld opgenomen. 

```CSV
vraag,a,b,c,antwoord
Wat is 1 + 1?,3,4,2,2
Wat is de hoofdstad van Nederland?,Maastricht,Den Haag,Amsterdam,Amsterdam
```
De eerste rij geeft aan wat de betekenis is van een kolom. We kunnen het ook anders bekijken:

vraag                               | a         | b         | c         | antwoord |
----------------------------------- |-----------|-----------|-----------|----------|
Wat is 1 + 1?                       | 3         | 4         | 2         | 2        |
Wat is de hoofdstad van Nederland?  | Maastricht| Den Haag  | Amsterdam | Amsterdam|

Voor het lezen van een bestand in Python moet je het bestand openen en de regels inlezen naar een variabele.

```Python
import csv

deelnemers_met_leeftijd = [] # lege lijst

with open('quiz_time/data/namen_en_leeftijd_deelnemers.csv') as deelnemers_bestand: # deze regelt open het bestand
    csv_lezer = csv.reader(deelnemers_bestand, delimiter=',') # laad de data

    next(csv_lezer) # eerste regel bevat geen data

    for regel in csv_lezer: # loop door iedere `regel`  in `csv_lezer`
        regels_bestand.append(regel) # voeg regel toe aan lege lijst

print(deelnemers_met_leeftijd) # output [['Pietje Puk', '8'], ['Joris de groen', '6']]
```

Python heeft een ingebouwde csv lezer dat csv bestanden voor je inleest. Hierboven zie je dat iedere regel in een aparte lijst is. Daardoor kan je bijvoorbeeld alle leeftijden in een andere lijst bij te houden:

```python
leeftijden_deelnemers = [] # lege lijst
leeftijden_per_deelnemerst = {} # lege dictionary

for deelnemer in deelnemers_met_leeftijd: # loop door iedere `regel`  in `csv_lezer`
        leeftijd = deelnemer[1] # # selecteer tweede `ding` in de regel. Ja computers tellen vanaf 0 ;)
        leeftijden_deelnemers.append(leeftijd) # voeg leeftijd toe aan lijst
        leeftijden_per_deelnemerst[deelnemer[0]] = leeftijd # {naam_deelnemer:leeftijd_deelnemer}

print(leeftijden_deelnemers) # Output: ['8', '6']
print(str(leeftijden_per_deelnemerst)) # Output: {'Pietje Puk': 8, 'Joris de groen': 6}
```

Probeer de bovenstaande code uit in `speeltuin.py` om er mee bekend te raken

### Opdracht 1.1
We hebben meer data nodig, een quiz met twee vragen is *zucht* te makkelijk. Voeg tenminste 5 vragen toe aan bestand `quiz_data.csv`, gebruik je fantasie! :)

### Opdracht 1.2
Je bent gewapend met de kennis om quiz data in te lezen. Maak de functie `laad_bestand()` af in `quiz_time.py`. Zorg ervoor dat je een `dictionary` data structuur gebruikt in plaats van een lijst, dit maakt het later makkelijk om antwoorden te vergelijken. 

### Opdracht 1.3
De route `/vragen` is een handige `endpoint` om te zien welke quiz vragen en antwoorden er bestaan. Maak de route af. 

### 2. Vragen tonen
Vragen zijn ingeladen, de volgende stap is om de vragen te tonen aan de gebruiker. Met Flask kun je data sturen naar een HTML bestand en code toevoegen om voor iedere vraag, de antwoorden te laden in het scherm (zonder het correct antwoord uiteraard ;) ). 

De kale templates (HTML pagina's) zijn al voorbereid, zie `vragen.html`. Wat je zal opvallen in de template is het volgende deel: 

```HTML
        <ul>
            {% for vraag_en_antwoorden in vragen_en_antwoorden %}
            <li>
                <h2>{{ vraag_en_antwoorden[0] }}</h2>
                <ul>
                    <li>
                        <input type="radio" name="1_{{ vraag_en_antwoorden[0] }}" value="{{ vraag_en_antwoorden[1] }}">
                        {{ vraag_en_antwoorden[1] }}
                    </li>
                    <li>
                        <input type="radio" name="2_{{ vraag_en_antwoorden[0] }}" value="{{ vraag_en_antwoorden[1] }}">
                        {{ vraag_en_antwoorden[1] }}
                    </li>
                    <li>
                        <input type="radio" name="3_{{ vraag_en_antwoorden[0] }}" value="{{ vraag_en_antwoorden[1] }}">
                        {{ vraag_en_antwoorden[1] }}
                    </li>
                </ul>
            </li>
            {% endfor %}
        </ul>
```

`{% for vraag_en_antwoorden in vragen_en_antwoorden %}` is hoe je in flask voor iedere vragen_en_antwoorden, verstuurd vanuit Flask code, een X aantal HTML elementen kan genereren. Hiermee kunnen we voor iedere vraag, de antwoorden en vragen generen. Alles tussen `{{ }}` controleert flask of er variabele zijn meegegeven aan het template.

Variabelen meegeven aan het template gaat als volgt: 

```Python
render_template("vragen.html", naam_van_data_in_template=naam_variabele_dat_ingelezen_moet_worden, naam_van_data_in_template2=naam_variabele_dat_ingelezen_moet_worden2, ...)
```

render_template is een functie die vanuit Flask komt waarmee je een HTML pagina kan afwerken met data (hint hint, vragen en antwoorden zijn data). Bovenstaande code injecteerd de Python variabele `naam_variabele_dat_ingelezen_moet_worden` in `vragen.html` met naam `naam_van_data_in_template`. Daarna kan je de data gebruiken zoals je hierboven.

### Opdracht 2.1
Nu we de data hebben en we weten hoe we die moeten inladen, is het een kwestie van de data juist meegeven aan de HTML template. Stuur ingelezen vragen en antwoorden naar template `vragen.html` en render dit bij `/start`. Als de data is ingelezen, kan je door naar 2.2 (Yes er zit een fout :) )

### Opdracht 2.2
Oh nee, er zit een fout bij het laden van de vragen. Tijd om te debuggen! Probeer te achterhalen waar de fout vandaan komt en los het op.

### 3. Antwoorden checken en resultaten tonen
De gebruiker kan haar antwoorden sturen en we hebben een endpoint `/verzend_antwoorden`, maar waar zijn de antwoorden en hoe kan ik dit vinden? Doe je stoelriem om, nu wordt het interessant.

Wanneer je de knop sent drukt, stuur je de `form` data, wat een lijst van sleutel-waarde (sleutel is vraag, waarde is antwoord) op naar je web server. Deze data kan je vinden door `request.form()` functie aan te roepen in de betreffende endpoint. Daarmee heb je de antwoorden op de vragen en kan je dit controleren door het te vergelijken met de ingelezen quiz_vragen (laatste element in de lijst, dus [-1]).

### Opdracht 3
Vergelijk de antwoorden met het juiste antwoord in de geladen vragen. Doordat dit is opgeslagen in een dictionary, is het opzoeken van de data goed te doen. Houdt in gedacht dat alle elementen uit `request.form()` een bepaalde type hebben (tip, dit kan je checken met `type()`)

Zorg ervoor dat de dummy implementatie de juiste resultaten toont.

## Uitbreiding
De quiz App is af, maar in de wereld van IT is niks volledig af. Projecten moeten onderhouden worden en er kan altijd wel iets verbeterd worden (true story). Hieronder zijn wat mogelijke uitbreidingen om de quiz app nog beter te maken. De lijst hieronder is niet gesorteerd op prioriteit, jij kiest wat jij zou willen verbeteren.

De onderstaande verbeteringen zijn niet compleet, het kan zijn dat er een verbetering is die hieronder niet is opgenomen (User Interface mooier maken bijvoorbeeld)

### Toon welke vragen fout waren

### Antwoorden per poging opslaan en bijhouden op aparte pagina

### Vragen random selecteren

### Tijdslimiet instellen

### Meerdere Quizes

### Huidige status op te slaan per gebruiker

