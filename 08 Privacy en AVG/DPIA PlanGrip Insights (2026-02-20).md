# GEGEVENSBESCHERMINGSEFFECTBEOORDELING (DPIA) PLANGRIP INSIGHTS
_kenmerk NOV-PRV-2026-002 – versie 1.0 – 20 februari 2026_

## Documentgegevens

| Onderdeel | Gegevens |
|---|---|
| Onderwerp | PlanGrip Insights, AI-module voor prognoses van capaciteit en verzuim |
| Opsteller | Lieke Dorrestein, legal & privacy officer |
| Inhoudelijke bijdragen | Marit Holtrop (senior developer, modelontwikkeling), Bas Hoekwater (security officer), Sem Loonstra (customer success) |
| Vastgesteld door | R.J. Okkersen, bestuurder (CTO) |
| Methode | Model DPIA Rijksdienst, aangevuld met EDPB-richtsnoeren WP248 rev.01 en de AP-lijst DPIA-verplichte verwerkingen |
| Gerelateerde documenten | TIA Dendra AI (NOV-PRV-2025-011), verwerkingsregister (NOV-PRV-2026-004), addendum Insights Rietvelden (NOV-VRK-2026-002), pentestrapport Schildwacht (9 februari 2026) |
| Status | Definitief |

## 1. Aanleiding en rolverdeling

Op 15 januari 2026 heeft Noviqo de module PlanGrip Insights gelanceerd. Insights voorspelt op basis van historische planningsdata capaciteitstekorten en pieken in ziekteverzuim, en genereert tekstuele samenvattingen met een taalmodel van Dendra AI Inc.
Voor de gegevens die klanten in PlanGrip invoeren is de klant verwerkingsverantwoordelijke en Noviqo verwerker. De DPIA-plicht van artikel 35 AVG rust formeel op de klant. Noviqo voert deze DPIA uit om drie redenen: (a) om klanten bijstand te verlenen als bedoeld in artikel 28 lid 3 sub f AVG; (b) omdat Noviqo als ontwikkelaar de ontwerpkeuzes maakt die het risico bepalen (privacy by design, artikel 25 AVG, waarvan de klant de naleving moet kunnen aantonen); en (c) omdat Noviqo voor de AI-verordening aanbieder van het AI-systeem is. Klanten kunnen deze DPIA gebruiken als basis voor hun eigen beoordeling, maar moeten die aanvullen met hun eigen context, zoals de wijze van gebruik, de informatie aan medewerkers en het advies van hun ondernemingsraad.

### 1.1 Is een DPIA verplicht?

De verwerking voldoet aan ten minste drie criteria uit WP248: gegevens van kwetsbare betrokkenen (werknemers in een afhankelijkheidsrelatie), gevoelige gegevens (verzuim als gezondheidsgegeven) en innovatief gebruik van technologie (machine learning en een groot taalmodel). Daarnaast staan op de AP-lijst onder meer "gezondheidsgegevens" en "monitoring van werknemers" als DPIA-verplichte categorieën. Een DPIA is daarom vereist bij klanten die de module gebruiken.

## 2. Systematische beschrijving

### 2.1 Functionaliteit

| Functie | Beschrijving | Uitvoer |
|---|---|---|
| Capaciteitsprognose | Voorspelt per team en per project voor de komende 2 tot 12 weken het verschil tussen benodigde en beschikbare uren | Grafiek en signaal "tekort verwacht" op team- of projectniveau |
| Verzuimprognose | Voorspelt per team de verwachte bandbreedte van afwezigheid wegens ziekte, op basis van seizoenspatronen en historische afwezigheid | Bandbreedte (bijvoorbeeld 4 tot 7 procent) per team, alleen bij teams van minimaal acht medewerkers |
| Samenvattingen | Genereert een wekelijkse tekstuele toelichting bij de prognoses voor planners | Tekst van circa 150 woorden, gemarkeerd als "gegenereerd door AI" |

De prognoses worden berekend met een door Noviqo ontwikkeld gradient-boostingmodel dat per klantomgeving (tenant) wordt getraind op uitsluitend de gegevens van die klant. Er is geen gezamenlijk model over klanten heen. Het model draait op de infrastructuur van Wolkenrand Hosting in Nederland.
Voor de samenvattingen stuurt Insights een gestructureerde prompt naar de API van Dendra AI. Die prompt bevat geaggregeerde cijfers, teamcodes en projectcodes. Namen, personeelsnummers en contactgegevens worden vóór verzending vervangen door pseudoniemen; de sleuteltabel blijft in Nederland. Vrije notities worden niet meegestuurd.

### 2.2 Gegevens, betrokkenen en bronnen

| Categorie | Voorbeelden | Bron | Gebruikt voor |
|---|---|---|---|
| Identificerende gegevens | Naam, personeelsnummer | Klant | Koppeling planning; niet naar Dendra |
| Functie en team | Functie, vaardigheden, teamindeling | Klant | Capaciteits- en verzuimprognose |
| Planning en uren | Geplande en gewerkte uren, projecttoewijzing | Klant en PlanGrip Veld | Capaciteitsprognose |
| Afwezigheid | Type afwezigheid (verlof, ziek, opleiding), begin- en einddatum | Klant | Verzuim- en capaciteitsprognose |
| Afgeleide gegevens | Prognoses per team en project | Insights | Weergave aan planners |

Betrokkenen zijn medewerkers, inhuurkrachten en onderaannemers van klanten. Bij de lancering gaat het om naar schatting 3.000 tot 4.000 personen; bij Installatiebedrijf Rietvelden B.V. alleen al 180 gebruikers en circa 220 geplande medewerkers. Het historisch venster bedraagt maximaal 24 maanden.

### 2.3 Gegevensstromen en partijen

| Stap | Partij | Locatie | Rol |
|---|---|---|---|
| Opslag planningsdata | Wolkenrand Hosting B.V. | Nederland | Subverwerker |
| Training en uitvoering prognosemodel | Noviqo op infrastructuur Wolkenrand | Nederland | Verwerker |
| Pseudonimisering en PII-filter | Noviqo | Nederland | Verwerker |
| Generatie samenvatting | Dendra AI Inc. | Ierland, met failover en misbruikmonitoring in de VS | Subverwerker |
| Weergave en gebruik | Klant (planners en leidinggevenden) | Bij klant | Verwerkingsverantwoordelijke |

### 2.4 Bewaartermijnen

Prognoses worden 12 maanden bewaard om de nauwkeurigheid te kunnen evalueren. Dendra bewaart invoer maximaal 30 dagen voor misbruikmonitoring en gebruikt deze niet voor training. Trainingsdatasets worden bij elke maandelijkse hertraining opnieuw opgebouwd uit de actuele productiedata en niet afzonderlijk bewaard.

## 3. Rechtmatigheid, noodzaak en proportionaliteit

### 3.1 Doelbinding en grondslag

Het doel van Insights is het verbeteren van personeelsplanning: tijdig zien waar capaciteit tekortschiet zodat de klant kan bijsturen met inhuur, herplanning of uitstel. De klant kan zich daarvoor in beginsel beroepen op het gerechtvaardigd belang (artikel 6 lid 1 sub f AVG). Toestemming van werknemers is als grondslag ongeschikt vanwege de afhankelijkheidsrelatie (EDPB-richtsnoeren 05/2020, randnummer 21).
De afweging valt anders uit voor de verzuimprognose. Het afwezigheidstype "ziek" is een gegeven over gezondheid in de zin van artikel 4 punt 15 AVG; dat de diagnose ontbreekt, verandert dat niet. Verwerking is alleen toegestaan als een uitzondering uit artikel 9 lid 2 AVG van toepassing is. Artikel 30 lid 1 UAVG staat werkgevers toe gezondheidsgegevens te verwerken voor zover noodzakelijk voor loondoorbetaling bij ziekte en re-integratie. Het voorspellen van verzuim voor planningsdoeleinden valt daar niet zonder meer onder.
Noviqo concludeert dat de verzuimprognose alleen verantwoord is als de uitvoer geen gezondheidsgegeven over een individuele, identificeerbare werknemer meer oplevert. Daarom is gekozen voor (a) uitsluitend geaggregeerde uitvoer op teamniveau, (b) een minimale groepsgrootte van acht medewerkers, (c) een bandbreedte in plaats van een puntvoorspelling, en (d) het ontbreken van iedere mogelijkheid om in te zoomen op individuen. De invoer blijft een gezondheidsgegeven. Het gebruik daarvan voor modeltraining wordt gezien als verdere verwerking binnen de verzuimadministratie die de klant al rechtmatig voert, met een verenigbaar doel (artikel 6 lid 4 AVG). Deze kwalificatie is niet zonder discussie; daarom adviseert Noviqo klanten de verzuimprognose pas in te schakelen na een eigen afweging en na instemming van de ondernemingsraad (artikel 27 lid 1 sub l WOR).

### 3.2 Subsidiariteit en minimalisatie

Alternatieven zijn overwogen: handmatige analyse door planners (al beschikbaar in standaard PlanGrip-rapportages, maar zonder voorspellend vermogen), een prognose uitsluitend op basis van seizoensgemiddelden zonder persoonsgegevens (onderzocht, maar onvoldoende nauwkeurig bij kleine teams) en een prognose zonder verzuimgegevens (dit is de standaardinstelling). De verzuimprognose staat bij levering uit en moet door de klantbeheerder actief worden ingeschakeld.

### 3.3 Transparantie en rechten van betrokkenen

Noviqo levert klanten een modeltekst voor de informatie aan medewerkers (artikelen 13 en 14 AVG), inclusief uitleg over de logica van de prognoses. Inzage, rectificatie en verwijdering lopen via de klant; de onderliggende planningsdata zijn al via PlanGrip in te zien en te corrigeren. Bezwaar (artikel 21 AVG) kan de klant honoreren door een medewerker uit te sluiten van de trainingsdata; die functie is beschikbaar sinds release 26.2.

## 4. Risico's voor betrokkenen

| Nr | Risico | Kans | Impact | Bruto risico |
|---|---|---|---|---|
| R1 | Heridentificatie van individueel verzuim uit teamprognoses, bijvoorbeeld bij kleine teams of door vergelijking van opeenvolgende periodes | Middel | Hoog | Hoog |
| R2 | Gebruik van prognoses voor beslissingen over individuele medewerkers (contractverlenging, beoordeling), waardoor sprake kan zijn van profilering en besluitvorming als bedoeld in artikel 22 AVG | Middel | Hoog | Hoog |
| R3 | Doorgifte van persoonsgegevens naar de VS via Dendra AI en toegang door Amerikaanse overheidsinstanties | Laag | Middel | Middel |
| R4 | Onvolledige pseudonimisering: namen of gezondheidsinformatie in prompts aan Dendra | Middel | Middel | Middel |
| R5 | Onjuiste of discriminerende prognoses, bijvoorbeeld systematisch hogere verwachte uitval bij teams met veel oudere of parttime medewerkers | Middel | Middel | Middel |
| R6 | Misleidende of verzonnen inhoud in AI-samenvattingen die planners voor feitelijk aannemen | Middel | Laag | Middel |
| R7 | Ongeautoriseerde toegang tot prognoses binnen de klantomgeving of tussen tenants | Laag | Hoog | Middel |
| R8 | Functieverschuiving: klant gebruikt Insights als instrument voor verzuimcontrole | Laag | Hoog | Middel |

### 4.1 Profilering en artikel 22 AVG

Insights voorspelt aspecten van werkprestaties en gezondheid van groepen werknemers. Zolang de uitvoer op teamniveau blijft, is er geen evaluatie van persoonlijke aspecten van een individu en daarmee geen profilering in de zin van artikel 4 punt 4 AVG van een specifieke werknemer. Wel ontstaat een profileringsrisico zodra een team klein is of wanneer een leidinggevende teamprognoses naast andere kennis legt.
Er is geen sprake van uitsluitend geautomatiseerde besluitvorming: Insights neemt geen besluiten en voert geen planningswijzigingen door. Een planner beoordeelt de prognose en beslist. Gelet op het SCHUFA-arrest van het Hof van Justitie (C-634/21, 7 december 2023) moet echter worden voorkomen dat een prognose in de praktijk doorslaggevend wordt voor een besluit over een individu. Contractueel is daarom vastgelegd dat klanten Insights niet gebruiken voor besluiten als bedoeld in artikel 22 AVG en dat beslissingen over individuele medewerkers altijd door een mens worden genomen.

## 5. Maatregelen

| Risico | Maatregel | Status 20 februari 2026 | Eigenaar |
|---|---|---|---|
| R1 | Minimale groepsgrootte acht; bandbreedte i.p.v. puntschatting; onderdrukking als teamsamenstelling binnen 4 weken meer dan 25 procent wijzigt | Gerealiseerd | M. Holtrop |
| R1 | Differential-privacy-ruis op verzuimaggregaten | Onderzoek, besluit Q2 2026 | M. Holtrop |
| R2, R8 | Contractuele gebruiksbeperking (addendum Insights); geen individuele scores in UI of API; duidelijke waarschuwingstekst in de module | Gerealiseerd | L. Dorrestein |
| R2, R8 | Verzuimprognose standaard uit; inschakelen alleen door klantbeheerder met bevestiging van eigen DPIA en OR-instemming | Gerealiseerd | S. Loonstra |
| R3 | TIA uitgevoerd; DPF-certificering Dendra gecontroleerd; SCC module 3 als terugval; verwerking primair in Ierland | Gerealiseerd | L. Dorrestein |
| R4 | PII-filter op namen, e-mailadressen, telefoonnummers en gezondheidstermen; vrije notities uitgesloten; logging van prompts in NL gedurende 30 dagen voor controle | Gerealiseerd; incident 27 januari 2026 leidde tot uitbreiding van de woordenlijst | M. Holtrop |
| R4 | Maandelijkse steekproef van 200 prompts op restanten van persoonsgegevens | Gerealiseerd | B. Hoekwater |
| R5 | Biastoets per hertraining op leeftijdscohort en deeltijdfactor (voor zover klant die vastlegt); afwijkingen boven 10 procent leiden tot handmatige review | Gedeeltelijk; volledige toets Q2 2026 | M. Holtrop |
| R6 | Samenvattingen gemarkeerd als AI-tekst; cijfers in de samenvatting worden automatisch vergeleken met de onderliggende prognose | Gerealiseerd | M. Holtrop |
| R7 | Tenantscheiding, rolgebaseerde toegang (alleen rol "planner" en hoger), hertest exportfunctie na pentestbevinding | Gerealiseerd na hertest Schildwacht | B. Hoekwater |

## 6. Classificatie onder de AI-verordening

### 6.1 Is Insights een AI-systeem en wie is aanbieder?

Insights is een AI-systeem in de zin van artikel 3 punt 1 van Verordening (EU) 2024/1689: het leidt uit invoer af hoe voorspellingen en teksten worden gegenereerd die beslissingen kunnen beïnvloeden. Noviqo brengt het systeem onder eigen naam in de handel en is daarmee aanbieder (artikel 3 punt 3). Klanten zijn gebruiksverantwoordelijken. Dendra AI is aanbieder van een AI-model voor algemene doeleinden; Noviqo is ten opzichte van Dendra een aanbieder verderop in de AI-waardeketen.

### 6.2 Hoog risico op grond van bijlage III, punt 4?

Bijlage III, punt 4, onder b, merkt als hoog risico aan AI-systemen die bedoeld zijn om te worden gebruikt voor het nemen van besluiten die van invloed zijn op de voorwaarden van arbeidsrelaties, promotie of beëindiging, voor het toewijzen van taken op basis van individueel gedrag of persoonlijke eigenschappen of kenmerken, of voor het monitoren en evalueren van prestaties en gedrag van personen in dergelijke relaties.
Noviqo beoordeelt Insights in de huidige vorm als niet hoog-risico, op grond van de volgende argumenten:
- Het beoogde doel is capaciteitsplanning op team- en projectniveau. Insights wijst geen taken toe aan individuen; de planner doet dat.
- De uitvoer betreft groepen van minimaal acht personen en bevat geen beoordeling van individueel gedrag, prestaties of persoonlijke eigenschappen.
- Insights wordt niet gebruikt voor besluiten over arbeidsvoorwaarden, promotie of ontslag; dat is contractueel uitgesloten.
Subsidiair beroept Noviqo zich op artikel 6 lid 3 AI-verordening: het systeem verricht een voorbereidende taak voor een beoordeling door een mens (sub d) en vormt geen wezenlijk risico. Deze uitzondering is niet beschikbaar als het systeem profilering van natuurlijke personen verricht. Daarom is het ontbreken van individuele uitvoer de dragende ontwerpkeuze. Wordt in de toekomst een functie toegevoegd die per medewerker voorspellingen doet (bijvoorbeeld een individuele "uitvalkans" of automatische roostertoewijzing op basis van persoonlijke kenmerken), dan is Insights wel hoog-risico en gelden de verplichtingen van hoofdstuk III, afdeling 2, waaronder risicobeheer, datagovernance, technische documentatie, menselijk toezicht en conformiteitsbeoordeling.
Op grond van artikel 6 lid 4 documenteert Noviqo deze beoordeling (dit hoofdstuk) en registreert zij het systeem in de EU-databank als bedoeld in artikel 49 lid 2, zodra die registratie openstaat. De verplichtingen voor hoog-risicosystemen uit bijlage III gelden volgens de oorspronkelijke tekst vanaf 2 augustus 2026; de Europese Commissie heeft in het Digital Omnibus-voorstel uitstel voorgesteld. Noviqo plant ongeacht de uitkomst daarvan een herbeoordeling vóór 1 juli 2026.

### 6.3 Overige verplichtingen

- AI-geletterdheid (artikel 4, van toepassing sinds 2 februari 2025): training voor ontwikkelaars, customer success en sales afgerond op 12 december 2025; klanten ontvangen een gebruikershandleiding met uitleg over beperkingen.
- Transparantie (artikel 50 lid 2): samenvattingen worden in de interface en in de API-uitvoer gemarkeerd als door AI gegenereerd.
- Verbod op emotieherkenning op de werkplek (artikel 5 lid 1 sub f): niet van toepassing; Insights verwerkt geen biometrische gegevens.

## 7. Restrisico

| Nr | Restrisico na maatregelen | Beoordeling |
|---|---|---|
| R1 | Heridentificatie is bij teams vanaf acht personen en met bandbreedtes beperkt, maar niet uitgesloten | Middel |
| R2 | Afhankelijk van naleving door klant; Noviqo kan feitelijk gebruik niet volledig controleren | Middel |
| R3 | Beperkt door pseudonimisering en DPF; juridische onzekerheid over het DPF blijft | Laag |
| R4 | Filter is niet volledig waterdicht, zoals incident januari 2026 liet zien | Laag |
| R5 | Biastoets nog niet volledig | Middel |
| R6, R7, R8 | Voldoende beheerst | Laag |

Er resteert geen hoog risico. Voorafgaande raadpleging van de Autoriteit Persoonsgegevens (artikel 36 AVG) is daarom niet vereist. Dit geldt voor de verwerking zoals Noviqo die heeft ontworpen; een klant die Insights anders inzet, moet dit zelf beoordelen.

## 8. Advies en besluit

De legal & privacy officer adviseert Insights voort te zetten onder de volgende voorwaarden:
- de verzuimprognose blijft standaard uitgeschakeld en wordt alleen ingeschakeld na bevestiging door de klant van een eigen DPIA en OR-instemming;
- de biastoets wordt uiterlijk 30 juni 2026 volledig ingevoerd;
- het besluit over differential privacy wordt uiterlijk 30 juni 2026 genomen;
- klanten die Insights in een proefperiode gebruiken, ontvangen deze DPIA en de modeltekst voor medewerkers;
- iedere functionele uitbreiding die individuele uitvoer oplevert, wordt vooraf aan deze DPIA en aan hoofdstuk 6 getoetst;
- deze DPIA wordt jaarlijks herzien, voor het eerst uiterlijk februari 2027.
De CTO neemt het advies over en stelt deze DPIA vast.

## Versiehistorie

| Versie | Datum | Wijziging | Auteur |
|---|---|---|---|
| 0.1 | 9 december 2025 | Eerste opzet, systematische beschrijving | L. Dorrestein |
| 0.2 | 23 januari 2026 | Risicoanalyse en AI-verordening toegevoegd | L. Dorrestein, M. Holtrop |
| 0.3 | 11 februari 2026 | Verwerking pentestbevinding en incident 27 januari 2026 | L. Dorrestein, B. Hoekwater |
| 1.0 | 20 februari 2026 | Vastgesteld | R.J. Okkersen |

Amsterdam, 20 februari 2026

___
Lieke Dorrestein, legal & privacy officer

___
Ruben Okkersen, bestuurder (CTO)
