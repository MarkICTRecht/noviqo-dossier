# OPEN SOURCE-BELEID EN SOFTWARECOMPOSITIE PLANGRIP
_kenmerk NOV-IE-2026-003 – versie 1.0, vastgesteld door het bestuur op 16 maart 2026_

**Eigenaar beleid:** R.J. Okkersen (CTO)

**Uitvoering en SBOM:** B. Hoekwater (DevOps lead & security officer)

**Juridische toetsing:** L. Dorrestein (legal & privacy officer)

**Herziening:** jaarlijks, of eerder bij een wezenlijke wijziging van de architectuur of de wet- en regelgeving

## 1. Doel en reikwijdte

1.1 PlanGrip bestaat voor een groot deel uit open source-componenten. Dat is efficiënt, maar brengt verplichtingen mee: licentievoorwaarden moeten worden nageleefd, kwetsbaarheden moeten tijdig worden verholpen en Noviqo moet tegenover klanten, investeerders en certificerende instellingen kunnen aantonen welke componenten zij gebruikt. Dit beleid legt vast welke licenties zijn toegestaan, hoe nieuwe componenten worden beoordeeld en hoe de softwarecompositie wordt bijgehouden.
1.2 Het beleid is van toepassing op alle software die Noviqo ontwikkelt, aanbiedt of verspreidt: de webapplicatie en API van PlanGrip, de mobiele app PlanGrip Veld, de module PlanGrip Insights, interne tools, scripts en infrastructuurcode. Het geldt voor medewerkers, stagiairs en ingehuurde ontwikkelaars, waaronder de freelance ontwikkelaar Duysak Development.
1.3 Aanleiding voor dit beleid zijn (i) de garanties over intellectuele eigendom die Noviqo in het kader van de Series A-financiering heeft verstrekt, (ii) de eisen van het ISMS in het kader van de ISO 27001-certificering, (iii) de aanbestedingseisen van publieke klanten, en (iv) de bevinding uit de eerste volledige softwarecompositieanalyse van 2 maart 2026 (paragraaf 7).

## 2. Uitgangspunten

2.1 Noviqo levert PlanGrip als SaaS-dienst. De webapplicatie en de API worden niet aan klanten verspreid, maar via het netwerk ter beschikking gesteld. De mobiele app PlanGrip Veld wordt wél verspreid, via de app-winkels van Apple en Google. Die twee situaties hebben verschillende gevolgen voor copyleft-licenties:
- bij klassieke copyleft-licenties (GPL) ontstaan verplichtingen tot het openbaar maken van broncode in beginsel pas bij verspreiding;
- bij netwerk-copyleft-licenties (AGPL, SSPL) ontstaan die verplichtingen al bij het via een netwerk beschikbaar stellen van gewijzigde software aan gebruikers.
2.2 Noviqo wenst de broncode van PlanGrip niet openbaar te maken. Componenten waarvan de licentie dat zou kunnen afdwingen, zijn daarom niet toegestaan in de productcode.
2.3 De beoordeling wordt gedaan per component en per versie. Een licentiewijziging bij een nieuwe versie, zoals die zich de afgelopen jaren bij diverse infrastructuurprojecten heeft voorgedaan, wordt behandeld als een nieuwe component.

## 3. Licentiecategorieën

| Categorie | Voorbeelden (SPDX) | Status | Voorwaarden |
|---|---|---|---|
| A – permissief | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, PostgreSQL, Zlib, 0BSD | toegestaan | copyright- en licentievermelding opnemen in de third-party notices; bij Apache-2.0 tevens het NOTICE-bestand |
| B – zwakke copyleft | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-2.0 | toegestaan onder voorwaarden | alleen ongewijzigd en als afzonderlijke bibliotheek (dynamisch gekoppeld); wijzigingen aan de component zelf vooraf voorleggen aan legal; MPL-2.0: gewijzigde bestanden onder MPL-2.0 beschikbaar stellen |
| C – sterke copyleft | GPL-2.0, GPL-3.0 | alleen na schriftelijke goedkeuring CTO en legal | nooit in PlanGrip Veld; in de backend uitsluitend als zelfstandig programma dat niet met eigen code wordt gecombineerd (bijvoorbeeld systeemtools in containers) |
| D – netwerk-copyleft en beperkende licenties | AGPL-3.0, SSPL-1.0, BUSL-1.1, Commons Clause, RSAL, Elastic License 2.0 | verboden in productcode en in de door klanten gebruikte infrastructuur | uitzondering alleen voor intern gebruik zonder toegang voor klanten, na schriftelijke goedkeuring CTO en legal |
| E – niet-commercieel of onduidelijk | CC-BY-NC, "no license", eigen licenties zonder SPDX-identificatie | verboden | component zonder licentie geldt als "alle rechten voorbehouden" |
| F – content en fonts | CC-BY-4.0, CC0-1.0, OFL-1.1 | toegestaan | naamsvermelding volgens licentie; fonts uit het designsysteem van Studio Pixelheuvel conform bijlage 2 bij NOV-IE-2023-002 |

3.1 **AGPL in een SaaS-omgeving.** De AGPL-3.0 verplicht tot het aanbieden van de volledige corresponderende broncode aan gebruikers die via een netwerk met een gewijzigde versie van het programma interacteren. Bij integratie in PlanGrip kan dit de broncode van (delen van) PlanGrip omvatten. Het risico is niet beheersbaar via configuratie of contractuele afspraken met klanten; daarom geldt een volledig verbod in categorie D. Dit geldt ook voor bibliotheken die alleen in een achtergrondproces worden gebruikt, zoals rapportgeneratie, wanneer de uitkomst aan klanten wordt getoond.
3.2 **Duale licenties.** Een component die zowel onder AGPL als onder een commerciële licentie beschikbaar is, mag alleen worden gebruikt indien Noviqo een commerciële licentie heeft gesloten. Het contract wordt opgenomen in het contractenregister.
3.3 **Licenties van leveranciers.** Gesloten software en API's van derden (zoals de API van Dendra AI Inc. en de SDK's van Wolkenrand Hosting) vallen niet onder dit beleid maar onder het inkoopproces. Het gebruik van hun SDK's wordt wel in de SBOM opgenomen.

## 4. Proces voor het toevoegen van componenten

4.1 Iedere nieuwe directe afhankelijkheid wordt via een pull request toegevoegd. De geautomatiseerde licentiecontrole in de CI-pijplijn blokkeert componenten uit categorie D en E, en markeert componenten uit categorie C en componenten waarvan de licentie niet kan worden vastgesteld.
4.2 Bij een markering beslist de reviewer niet zelf, maar legt de ontwikkelaar een aanvraag voor via het formulier "OSS-toets" met: naam en versie, licentie, doel, wijze van integratie, alternatieven en onderhoudsstatus (laatste release, aantal onderhouders, bekende kwetsbaarheden).
4.3 Beslistermijnen: categorie B binnen 3 werkdagen door de CTO; categorie C binnen 10 werkdagen door CTO en legal gezamenlijk.
4.4 Componenten die langer dan 24 maanden geen release hebben gehad of die één onderhouder hebben, worden alleen toegestaan als er geen redelijk alternatief is; zij krijgen in de SBOM de markering "onderhoudsrisico".

## 5. Bijdragen aan open source en gebruik van AI-assistenten

5.1 Medewerkers mogen tijdens werktijd bijdragen aan open source-projecten die Noviqo gebruikt, mits het gaat om het oplossen van fouten of kleine verbeteringen en er geen vertrouwelijke informatie of eigen bedrijfscode van Noviqo wordt gedeeld. Bijdragen aan projecten met een Contributor License Agreement worden vooraf voorgelegd aan legal. Het publiceren van eigen code van Noviqo als open source vereist een besluit van het bestuur.
5.2 De rechten van intellectuele eigendom op werk dat medewerkers in dienst verrichten, berusten bij Noviqo (artikel 7 Auteurswet en de IE-bepalingen in de arbeidsovereenkomsten). Bij freelancers is een schriftelijke overdracht van rechten vereist voordat hun code in de productcode wordt opgenomen.
5.3 Bij het gebruik van AI-programmeerassistenten geldt: (i) alleen door Noviqo goedgekeurde tools met een zakelijke licentie, waarbij de code van Noviqo niet wordt gebruikt voor training; (ii) de functie die suggesties blokkeert die overeenkomen met openbare code staat aan, voor zover beschikbaar; (iii) gegenereerde code wordt op dezelfde wijze gereviewd als handgeschreven code.

## 6. Softwarecompositie en SBOM

6.1 Bij iedere productierelease wordt automatisch een Software Bill of Materials (SBOM) gegenereerd in het CycloneDX-formaat, voor elk van de drie hoofdonderdelen. De SBOM's worden 5 jaar bewaard en zijn op verzoek, onder geheimhouding, beschikbaar voor Enterprise-klanten en auditors.
6.2 De SBOM wordt dagelijks vergeleken met openbare kwetsbaarhedendatabases. Kwetsbaarheden worden opgelost binnen: kritiek 72 uur, hoog 14 dagen, midden 60 dagen, laag bij de eerstvolgende reguliere update. Deze termijnen sluiten aan op het patchbeleid in het ISMS.
6.3 Met het oog op de Cyber Resilience Act, waarvan de meldplichten vanaf 11 september 2026 en de overige verplichtingen vanaf 11 december 2027 gelden, wordt beoordeeld in hoeverre PlanGrip Veld als product met digitale elementen kwalificeert. De SBOM-praktijk in dit beleid is erop gericht aan die eisen te kunnen voldoen.

### 6.4 Overzicht softwarecompositie per 2 maart 2026

| Onderdeel | Technologie | Directe afhankelijkheden | Totaal (incl. transitief) |
|---|---|---|---|
| Backend en API | Python, Django, Celery, PostgreSQL-client | 64 | 214 |
| Webfrontend | TypeScript, React | 58 | 1.142 |
| PlanGrip Veld | React Native (iOS en Android) | 47 | 731 |
| PlanGrip Insights (dienst) | Python | 21 | 96 |
| Infrastructuur (containers) | Linux-basisimages, PostgreSQL 15, Redis 7.2, Nginx | 12 | 12 images |
| **Totaal** | | **202** | **2.183 pakketten + 12 images** |

### 6.5 Verdeling naar licentie (alle pakketten, per 2 maart 2026)

| Licentie | Aantal | Aandeel | Categorie |
|---|---|---|---|
| MIT | 1.512 | 69,3% | A |
| Apache-2.0 | 241 | 11,0% | A |
| ISC | 168 | 7,7% | A |
| BSD-3-Clause en BSD-2-Clause | 173 | 7,9% | A |
| Overige permissief (PostgreSQL, Zlib, 0BSD, Python-2.0) | 31 | 1,4% | A |
| LGPL-2.1 / LGPL-3.0 | 9 | 0,4% | B |
| MPL-2.0 | 14 | 0,6% | B |
| CC-BY-4.0 / CC0-1.0 / OFL-1.1 | 22 | 1,0% | F |
| GPL (alleen systeemtools in containers) | 6 | 0,3% | C |
| AGPL-3.0 | 1 | 0,05% | D |
| Onbekend of niet vastgesteld | 6 | 0,3% | E |
| **Totaal** | **2.183** | **100%** | |

## 7. Bevindingen van de eerste analyse en opvolging

7.1 **AGPL-component in Insights.** Bij de analyse van 2 maart 2026 bleek dat de dienst PlanGrip Insights voor het genereren van PDF-rapporten de bibliotheek PyMuPDF gebruikte, die onder AGPL-3.0 is gelicentieerd (met een commerciële licentie als alternatief). Een commerciële licentie was niet gesloten. De component was op 8 december 2025 toegevoegd en is met de lancering van Insights op 15 januari 2026 in productie genomen. Het gebruik was niet gewijzigd, maar de rapporten werden aan klanten getoond.
7.2 **Maatregel.** De component is op 11 maart 2026 verwijderd en vervangen door WeasyPrint (BSD-3-Clause). Juridisch is beoordeeld dat het risico van een verplichting tot openbaarmaking beperkt is geweest, nu de bibliotheek ongewijzigd en in een afzonderlijke dienst werd gebruikt, maar dat dit niet met zekerheid kan worden uitgesloten. Het incident is vastgelegd in het register van bevindingen van het ISMS. Er zijn geen verzoeken om broncode ontvangen.
7.3 **Onbekende licenties.** Van de zes pakketten zonder vastgestelde licentie zijn er vier transitieve afhankelijkheden in de webfrontend waarvoor de licentie alsnog is achterhaald (alle MIT). Twee pakketten in PlanGrip Veld, beide kleine hulpbibliotheken voor datumweergave, zijn vervangen.
7.4 **Redis.** Redis wordt gebruikt in versie 7.2, die onder de BSD-3-Clause valt. Latere versies zijn onder andere licentievoorwaarden uitgebracht (RSALv2, SSPLv1 en, vanaf versie 8, tevens AGPLv3). Een upgrade vereist voorafgaande toetsing; als alternatief wordt een fork onder een permissieve licentie onderzocht. Het beheer van de Redis-instanties ligt bij Noviqo; Wolkenrand Hosting levert alleen de onderliggende infrastructuur.
7.5 **GPL-componenten.** De zes GPL-componenten zijn systeemtools in de Linux-basisimages (onder meer shell-hulpprogramma's). Zij worden niet met code van Noviqo gecombineerd en de images worden niet aan klanten verspreid. Er is geen actie nodig.
7.6 **Third-party notices.** In PlanGrip Veld ontbrak een volledig overzicht van licentievermeldingen. Vanaf release 3.8 (april 2026) staat dit overzicht onder "Instellingen – Over deze app – Licenties". De webapplicatie toont het overzicht op app.plangrip.example/licenses.

## 8. Naleving en rapportage

8.1 Overtreding van dit beleid kan leiden tot maatregelen volgens het personeelshandboek; bij freelancers tot een tekortkoming onder de opdrachtovereenkomst.
8.2 De security officer rapporteert per kwartaal aan het bestuur over: het aantal nieuwe componenten, aanvragen in categorie B en C, openstaande kwetsbaarheden per ernst en eventuele licentiebevindingen. Het bestuur informeert de raad van commissarissen halfjaarlijks.
8.3 Bij iedere due diligence, aanbesteding of auditvraag over open source wordt dit beleid samen met de laatste SBOM-samenvatting verstrekt, na goedkeuring van legal.

Vastgesteld door het bestuur op 16 maart 2026.

___
R.J. Okkersen
namens Okkersen Beheer B.V., bestuurder (CTO)

___
F.A. van Dalsem
namens Van Dalsem Holding B.V., bestuurder (CEO)
