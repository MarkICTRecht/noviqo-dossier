# TRANSFER IMPACT ASSESSMENT DENDRA AI INC.
_kenmerk NOV-PRV-2025-011 – versie 1.0 – 28 oktober 2025_

## Documentgegevens

| Onderdeel | Gegevens |
|---|---|
| Onderwerp | Doorgifte van persoonsgegevens aan Dendra AI Inc. voor de taalmodelfunctie van PlanGrip Insights |
| Exporteur | Noviqo B.V., Amsterdam (verwerker namens klanten) |
| Importeur | Dendra AI Inc., Wilmington, Delaware, Verenigde Staten (subverwerker) |
| Opsteller | Lieke Dorrestein, legal & privacy officer |
| Technische input | Bas Hoekwater (security officer), Marit Holtrop (senior developer) |
| Goedgekeurd door | R.J. Okkersen, bestuurder (CTO) |
| Methode | EDPB-aanbevelingen 01/2020 over aanvullende maatregelen (versie 2.0, 18 juni 2021), zes stappen |
| Status | Definitief, voorafgaand aan ondertekening Enterprise Services Agreement |

## 1. Aanleiding

Noviqo ontwikkelt de module PlanGrip Insights, met een geplande lancering op 15 januari 2026. Insights genereert wekelijkse tekstuele samenvattingen van capaciteits- en verzuimprognoses. Daarvoor gebruikt Noviqo de API van Dendra AI Inc., een aanbieder van grote taalmodellen. Dendra verwerkt API-verzoeken op servers in Ierland en de Verenigde Staten.
Omdat Noviqo voor de gegevens in PlanGrip verwerker is, is Dendra een subverwerker. Klanten moeten voor de inschakeling van Dendra toestemming geven onder hun verwerkersovereenkomst; doorgifte buiten de EER vereist bovendien een geldig doorgifte-instrument op grond van hoofdstuk V AVG.
Deze TIA beoordeelt of de doorgifte een beschermingsniveau biedt dat in wezen gelijkwaardig is aan dat in de EER, en welke aanvullende maatregelen nodig zijn. Zij dient tevens als onderbouwing voor klanten bij hun eigen beoordeling.

## 2. Stap 1 – In kaart brengen van de doorgifte

| Element | Beschrijving |
|---|---|
| Doel | Genereren van een tekstuele samenvatting (circa 150 woorden) bij prognoses voor planners |
| Gegevens | Gestructureerde prompt met geaggregeerde uren, teamcodes, projectcodes, prognosebandbreedtes, en in uitzonderingsgevallen pseudoniemen van medewerkers (bijvoorbeeld bij "medewerker P-4821 heeft 3 projecten tegelijk") |
| Gegevens die niet worden doorgegeven | Namen, personeelsnummers, contactgegevens, vrije notities, afwezigheidstype per individu |
| Betrokkenen | Medewerkers, inhuurkrachten en onderaannemers van PlanGrip-klanten |
| Bijzondere categorieën | Geen op individueel niveau. Verzuimcijfers worden alleen geaggregeerd per team van minimaal acht medewerkers meegestuurd |
| Volume | Geraamd 12.000 tot 18.000 API-verzoeken per maand in het eerste jaar |
| Frequentie | Continu, met een piek op maandagochtend (wekelijkse samenvatting) |
| Verwerkingslocatie | Standaard: Dendra-regio Dublin (Ierland). Failover bij capaciteitsproblemen naar regio Virginia (VS). Misbruikmonitoring en support door Dendra-personeel in de VS |
| Bewaring bij Dendra | Invoer en uitvoer maximaal 30 dagen voor misbruikmonitoring; geen gebruik voor training |
| Doorgifte verder | Dendra maakt gebruik van een Amerikaanse cloudinfrastructuurleverancier als subverwerker (in de onderhandelde DPA vermeld) |

Ook als de verwerking standaard in Ierland plaatsvindt, is sprake van doorgifte: Amerikaans personeel van Dendra kan voor misbruikmonitoring en support toegang krijgen, en bij failover vindt verwerking in de VS plaats. Bovendien is Dendra als Amerikaanse onderneming onderworpen aan Amerikaanse wetgeving die verstrekking van gegevens kan verlangen, ongeacht de opslaglocatie.

### 2.1 Persoonsgegevens ondanks pseudonimisering

Noviqo vervangt identificerende gegevens vóór verzending door pseudoniemen; de sleuteltabel blijft bij Noviqo in Nederland. Voor Noviqo blijven de gegevens persoonsgegevens. Of zij dat ook voor Dendra zijn, hangt af van de middelen waarover Dendra redelijkerwijs beschikt om betrokkenen te identificeren (overweging 26 AVG). Gelet op de kleine teams en de combinatie met projectcodes gaat deze TIA er voorzichtigheidshalve van uit dat de gegevens ook bij Dendra persoonsgegevens zijn.

## 3. Stap 2 – Doorgifte-instrument

| Instrument | Toepassing |
|---|---|
| Adequaatheidsbesluit EU-US Data Privacy Framework (10 juli 2023) | Primaire grondslag. Dendra AI Inc. is gecertificeerd onder het DPF; certificering gecontroleerd op de DPF-lijst op 27 oktober 2025, status "active", inclusief HR-gegevens (relevant omdat het om werknemersgegevens gaat) |
| Standaardcontractbepalingen (Uitvoeringsbesluit (EU) 2021/914), module 3 verwerker aan verwerker | Terugvaloptie, op te nemen in de DPA bij de Enterprise Services Agreement, van kracht zodra de DPF-certificering vervalt of het adequaatheidsbesluit ongeldig wordt |

Bij een geldig adequaatheidsbesluit is een TIA juridisch niet vereist. Noviqo voert de TIA toch volledig uit, omdat (a) de standaardcontractbepalingen als terugval een TIA vereisen (clausule 14), (b) de houdbaarheid van het DPF onzeker is en (c) klanten, waaronder overheidsklanten, om onderbouwing vragen.

## 4. Stap 3 – Beoordeling van wetgeving en praktijk in de VS

### 4.1 Relevante wetgeving

| Regeling | Relevantie voor Dendra |
|---|---|
| Section 702 FISA | Dendra kwalificeert als aanbieder van elektronische communicatiediensten of remote computing services en kan bevel krijgen tot medewerking aan gerichte inzameling over niet-Amerikaanse personen. De huidige machtiging (RISAA, april 2024) loopt tot april 2026 |
| Executive Order 12333 | Inlichtingenactiviteiten buiten de VS, onder meer onderschepping van communicatie in transit. Relevant voor gegevensverkeer tussen Ierland en de VS |
| Executive Order 14086 | Beperkt inlichtingenactiviteiten tot wat noodzakelijk en evenredig is en voorziet in een beroepsmechanisme via de Data Protection Review Court |
| CLOUD Act | Verstrekking van gegevens in handen van Amerikaanse bedrijven op bevel in strafrechtelijke onderzoeken, ook als gegevens buiten de VS zijn opgeslagen |

### 4.2 Ontwikkelingen

- Het Gerecht van de Europese Unie heeft op 3 september 2025 het beroep tot nietigverklaring van het DPF-adequaatheidsbesluit afgewezen (zaak T-553/23, Latombe). Hoger beroep bij het Hof van Justitie is mogelijk; de uitkomst van een eventuele procedure is onzeker.
- Het Privacy and Civil Liberties Oversight Board (PCLOB), een van de toezichtmechanismen waarop het adequaatheidsbesluit steunt, is sinds januari 2025 niet op volle sterkte nadat leden zijn ontslagen. De Europese Commissie volgt dit in haar periodieke evaluatie.
- De verlenging van Section 702 na april 2026 is onzeker en kan met gewijzigde waarborgen plaatsvinden.

### 4.3 Praktijk en ervaring van de importeur

Dendra publiceert een halfjaarlijks transparantierapport. Over 2024 en het eerste halfjaar van 2025 meldt Dendra nul verzoeken onder Section 702 voor zakelijke API-klanten in de EU (binnen de wettelijk toegestane bandbreedte van 0 tot 499) en geen CLOUD Act-bevelen die gegevens van EU-klanten betroffen. Dendra verklaart in de onderhandelde DPA dat zij geen achterdeurtoegang biedt en verzoeken van overheden zal aanvechten waar daar rechtsgronden voor zijn.
De gegevens die Noviqo doorgeeft, zijn bedrijfsmatige planningsgegevens van mkb-ondernemingen en gemeenten in Nederland. Op basis van het type gegevens en de betrokkenen (werknemers in bouw, installatie en zakelijke dienstverlening) acht Noviqo de kans dat deze gegevens voor Amerikaanse inlichtingendiensten van belang zijn zeer klein.

## 5. Stap 4 – Aanvullende maatregelen

| Nr | Maatregel | Type | Effect |
|---|---|---|---|
| M1 | Pseudonimisering vóór verzending; sleuteltabel uitsluitend in NL | Technisch | Dendra en een eventuele overheidsinstantie kunnen gegevens niet zonder aanvullende informatie aan een persoon koppelen |
| M2 | PII-filter op namen, e-mailadressen, telefoonnummers, BSN-patronen en gezondheidstermen; vrije notities uitgesloten | Technisch | Minimaliseert directe identificatoren in prompts |
| M3 | Alleen geaggregeerde verzuimcijfers (teams vanaf acht medewerkers) | Technisch | Geen gezondheidsgegevens op individueel niveau |
| M4 | Verwerking standaard in regio Dublin; failover naar VS alleen bij capaciteitsproblemen en gelogd | Contractueel en technisch | Beperkt de omvang van verwerking in de VS |
| M5 | TLS 1.3 voor alle API-verkeer; versleuteling at rest door Dendra (AES-256) | Technisch | Beschermt tegen onderschepping in transit (EO 12333) |
| M6 | Contractueel verbod op training met klantdata; bewaring maximaal 30 dagen | Contractueel | Beperkt bewaarduur en hergebruik |
| M7 | Verplichting om Noviqo te informeren over overheidsverzoeken voor zover wettelijk toegestaan, en verzoeken aan te vechten; jaarlijks transparantierapport | Contractueel | Vergroot zicht en rechtsbescherming |
| M8 | Verplichting om binnen 5 werkdagen te melden als DPF-certificering vervalt, waarna SCC module 3 geldt | Contractueel | Continuïteit doorgiftegrondslag |
| M9 | Klant kan Insights-samenvattingen uitschakelen zonder de prognosefunctie te verliezen | Organisatorisch | Keuzevrijheid voor klanten die geen doorgifte willen |
| M10 | Kwartaalcontrole steekproef van prompts op restanten van persoonsgegevens | Organisatorisch | Toetst werking van M1 en M2 |

Noviqo heeft onderzocht of versleuteling met sleutels in de EU (zodat Dendra de gegevens niet in leesbare vorm verwerkt) mogelijk is. Dat is bij een taalmodel niet uitvoerbaar, omdat het model de inhoud moet lezen om een samenvatting te maken. Dit is een bekende beperking (EDPB-aanbevelingen 01/2020, use case 6). De maatregelen richten zich daarom op minimalisatie en pseudonimisering.

## 6. Stap 5 – Procedurele stappen

- Opnemen van M4 tot en met M8 in de DPA bij de Enterprise Services Agreement met Dendra, beoogde ondertekening 3 november 2025.
- Toevoeging van Dendra aan de subverwerkerslijst (versie 4) en aankondiging aan klanten ten minste 30 dagen vóór gebruik, conform hun verwerkersovereenkomsten. Voor klanten wier verwerkersovereenkomst specifieke toestemming of uitdrukkelijke toestemming voor doorgifte buiten de EER vereist, wordt die toestemming vooraf schriftelijk gevraagd voordat Insights wordt ingeschakeld.
- Aanvulling van de verwerkersdocumentatie en het verwerkingsregister.

## 7. Stap 6 – Herbeoordeling

Deze TIA wordt herzien:
- jaarlijks, voor het eerst uiterlijk oktober 2026;
- bij een uitspraak van het Hof van Justitie over het DPF;
- bij het verlopen of wijzigen van Section 702 FISA (april 2026);
- bij een wijziging van de verwerkingslocaties of subverwerkers van Dendra;
- bij uitbreiding van de gegevens die naar Dendra worden gestuurd.

## 8. Conclusie

| Aspect | Oordeel |
|---|---|
| Doorgifte-instrument | Geldig: DPF-adequaatheidsbesluit, met SCC module 3 als terugval |
| Risico op toegang door overheidsinstanties | Laag, gezien aard van gegevens, pseudonimisering en transparantiegegevens importeur |
| Juridische onzekerheid | Middel, gelet op PCLOB-situatie, mogelijke procedure bij het Hof van Justitie en onzekerheid over Section 702 |
| Eindoordeel | Doorgifte aanvaardbaar onder de voorwaarde dat M1 tot en met M10 vóór lancering zijn ingevoerd en contractueel geborgd |

Noviqo kan Dendra AI Inc. inschakelen als subverwerker voor PlanGrip Insights, mits aan de voorwaarden in paragraaf 6 en 8 is voldaan. Mocht het DPF komen te vervallen en de standaardcontractbepalingen op zichzelf ontoereikend blijken, dan schakelt Noviqo de samenvattingsfunctie uit of verplaatst zij die naar een aanbieder met uitsluitend verwerking binnen de EER. Een exitplan daarvoor is opgesteld door M. Holtrop (doorlooptijd geraamd op 6 weken).

## Versiehistorie

| Versie | Datum | Wijziging | Auteur |
|---|---|---|---|
| 0.1 | 29 september 2025 | Eerste concept op basis van conceptcontract Dendra | L. Dorrestein |
| 0.2 | 17 oktober 2025 | Technische maatregelen en transparantierapport verwerkt | L. Dorrestein, B. Hoekwater |
| 1.0 | 28 oktober 2025 | Definitief, goedgekeurd | R.J. Okkersen |

Amsterdam, 28 oktober 2025

___
L. Dorrestein, legal & privacy officer

___
R.J. Okkersen, bestuurder (CTO)
