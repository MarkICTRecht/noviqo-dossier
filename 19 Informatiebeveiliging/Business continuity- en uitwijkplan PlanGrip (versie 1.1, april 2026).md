# BUSINESS CONTINUITY- EN UITWIJKPLAN PLANGRIP
_kenmerk NOV-SEC-2026-004 – versie 1.1 – april 2026_

## Documentgegevens

| Onderdeel | Gegevens |
|---|---|
| Eigenaar | Bas Hoekwater, DevOps lead & security officer |
| Bestuurlijk verantwoordelijk | R.J. Okkersen, bestuurder (CTO) |
| Vastgesteld | 21 april 2026 door het bestuur |
| Classificatie | Vertrouwelijk |
| Geldt voor | PlanGrip webapplicatie, API, PlanGrip Veld, PlanGrip Insights en de ondersteunende processen |
| Samenhang | Informatiebeveiligingsbeleid NOV-SEC-2026-001; change- en releasemanagementproces versie 3.0; procedure datalekken en beveiligingsincidenten versie 2.0; SLA's Teams (2 september 2024) en Enterprise (versie 2.0) |
| Herziening | Jaarlijks en na iedere calamiteit |
| Vervangt | Versie 1.0 (september 2024) |

## 1. Doel

Dit plan beschrijft hoe Noviqo de beschikbaarheid van PlanGrip bewaakt en herstelt bij een ernstige verstoring. Het legt hersteldoelen vast, beschrijft de belangrijkste scenario's, regelt wie beslist en hoe klanten worden geïnformeerd.
Versie 1.1 is opgesteld na de storing van 3 en 4 maart 2026 (incident INC-2026-006). PlanGrip was toen circa 19 uur onbereikbaar voor alle klanten. Die storing liet zien dat versie 1.0 te veel uitging van uitval van infrastructuur en te weinig van fouten bij eigen wijzigingen, en dat de hersteltijd van een volledige databaserestore nooit op productieomvang was getest.

## 2. Hersteldoelen (RTO en RPO)

De Recovery Time Objective (RTO) is de maximale tijd tot herstel van de dienst. De Recovery Point Objective (RPO) is het maximale gegevensverlies, uitgedrukt in tijd.

| Tier | Component | Contractuele RTO / RPO | Interne doelstelling RTO / RPO | Toelichting |
|---|---|---|---|---|
| 1 | PlanGrip webapp, API v2, PlanGrip Veld, authenticatie en SSO | Teams/Start: 12 uur / 24 uur. Enterprise: 8 uur / 4 uur | 4 uur / 15 minuten | Kernproces van klanten; buitendienst en bouwplaatsen starten vanaf 06:30 |
| 1 | Noodexport planning (zie paragraaf 5) | – | Beschikbaar binnen 1 uur na begin calamiteit | Workaround bij uitval tier 1 |
| 2 | PlanGrip Insights (prognoses en samenvattingen) | Geen afzonderlijke afspraak | 48 uur / 24 uur | Niet bedrijfskritisch voor klanten; samenvattingen afhankelijk van Dendra AI |
| 2 | API v1 (legacy koppelingen) | Volgt tier 1 | 24 uur / 15 minuten | Wordt uitgefaseerd |
| 3 | Supportportaal (Ticketvlinder), CRM (Klantloep), website | – | 3 werkdagen / 24 uur | Leverancier verantwoordelijk; telefoon en e-mail als terugval |
| 3 | Interne kantoorautomatisering | – | 1 werkdag / 24 uur | Werken op afstand mogelijk |

De interne doelstellingen zijn scherper dan de contractuele, zodat er marge is. De RPO van 15 minuten wordt bereikt met continue archivering van databasetransacties (WAL-archivering) naar gescheiden objectopslag bij Wolkenrand, naast de dagelijkse volledige back-up die 30 dagen wordt bewaard.

## 3. Lessen uit de storing van 3 en 4 maart 2026

### 3.1 Wat er gebeurde

| Tijdstip | Gebeurtenis |
|---|---|
| di 24 februari 2026 | Aankondiging via het supportportaal: onderhoud op dinsdag 3 maart 2026 tussen 22:00 en 02:00 uur voor migratie van de database naar een nieuwe clusteromgeving; geen of slechts korte onbeschikbaarheid verwacht |
| di 3 maart, 22:00 | Onderhoudsmodus aan; start kopie van de productiedatabase (circa 1,2 TB) naar het nieuwe cluster |
| 22:40 | Kopie verloopt veel trager dan verwacht. Op de acceptatieomgeving, met ongeveer een achtste van het datavolume, duurde de stap 25 minuten |
| 23:50 | Kopie op circa 60 procent. De uitvoerende developer besluit de migratie af te breken en terug te gaan naar het oude cluster |
| wo 4 maart, 00:15 | Het oude cluster start niet correct: een deel van de schemawijzigingen was al doorgevoerd. Er is geen uitgewerkt rollbackscript |
| 00:30 | Handmatige herstelpoging door het migratiescript opnieuw te starten; dit leidt tot inconsistenties in twee planningstabellen |
| 01:10 | Escalatie naar de dienstdoende engineer (B. Hoekwater) |
| 01:45 | Prioriteit 1 vastgesteld; CTO geïnformeerd; storingsdienst Wolkenrand ingeschakeld |
| 02:30 | Besluit tot herstel uit de volledige back-up van 3 maart 02:00 uur, aangevuld met WAL-archief tot 22:00 uur |
| 03:00 – 11:40 | Restore van de back-up. De doorvoersnelheid uit objectopslag lag circa drie keer lager dan in versie 1.0 was aangenomen |
| 06:40 | Eerste e-mail aan alle klantbeheerders en update statuspagina |
| 11:40 – 14:30 | Toepassen WAL-archief tot het moment van de onderhoudsmodus |
| 14:30 – 16:15 | Integriteitscontroles, steekproef bij 40 tenants, controle Veld-synchronisatie |
| 16:15 – 17:00 | Gefaseerde openstelling; vanaf omstreeks 17:00 volledig beschikbaar |
| 17:30 | Herstelbericht aan klanten; incidentrapport aan klanten op 11 maart 2026 |

Er zijn geen gegevens verloren gegaan: schrijfacties waren vanaf 22:00 uur geblokkeerd en het WAL-archief was volledig. Van de 19 uur onbeschikbaarheid vielen er circa 10 binnen kantoortijd.

### 3.2 Oorzaken

- De migratie was niet getest op een productiekopie met representatief datavolume.
- Er was geen getest rollbackplan en geen pre-migratiesnapshot.
- De wijziging is door één developer voorbereid en uitgevoerd, zonder inhoudelijke tweede beoordeling en zonder tweede persoon aanwezig.
- Een databasemigratie met hoog risico werd uitgevoerd in de nacht vóór een werkdag, buiten het onderhoudsvenster op zaterdag.
- De escalatie naar de dienstdoende engineer volgde pas na ruim drie uur.
- De herstelpoging zonder draaiboek verlengde de onbereikbaarheid.
- De restoretijd van een volledige productiedatabase was nooit gemeten; versie 1.0 ging uit van een RTO van 6 uur die in de praktijk niet haalbaar was.
- De uitwijk naar het tweede datacenter bood geen uitkomst, omdat de replicatie de half doorgevoerde wijzigingen ook naar de uitwijkomgeving had gekopieerd.
- Klanten kregen pas om 06:40 uur bericht, en er was geen workaround om de planning van de dag in te zien. Buitendienstmedewerkers van onder meer Bouwgroep Hazelaar B.V. konden 's ochtends hun planning niet raadplegen.

### 3.3 Gevolgen

De beschikbaarheidsnormen en de hersteltijden voor Prioriteit 1 uit de SLA's zijn overschreden. Bouwgroep Hazelaar B.V. heeft Noviqo op 18 maart 2026 aansprakelijk gesteld. De storing is beoordeeld als beschikbaarheidsincident zonder risico voor betrokkenen en geregistreerd in het datalekregister.

### 3.4 Verbetermaatregelen

| Maatregel | Eigenaar | Status april 2026 |
|---|---|---|
| Hoog-risico-changes (waaronder databasemigraties) alleen in het onderhoudsvenster op zaterdag 22:00–06:00, met twee developers en een bereikbare beslisser | R.J. Okkersen | Gereed (change-proces 3.0) |
| Verplichte test op productiekopie en getest rollbackscript bij iedere migratie | M. Holtrop | Gereed |
| Pre-migratiesnapshot van de database als vaste stap; replicatie naar uitwijk wordt tijdens migraties gepauzeerd | B. Hoekwater | Gereed |
| Escalatieregel: bij overschrijding van het geplande venster met 30 minuten direct escalatie naar dienstdoende engineer en CTO | B. Hoekwater | Gereed |
| Noodexport planning voor klantbeheerders en offline cache in PlanGrip Veld (zie paragraaf 5) | M. Holtrop | Noodexport gereed; offline cache release 26.5 (juni 2026) |
| Publieke statuspagina bij een externe aanbieder met automatische monitoring, los van de PlanGrip-infrastructuur | S. Loonstra | Gereed |
| Restoretest van de volledige productiedatabase per kwartaal, met meting van de hersteltijd | B. Hoekwater | Eerste test gepland mei 2026 |
| Snellere restore door parallelle hersteltaken en een warme stand-by-database die vertraagd repliceert (4 uur) | B. Hoekwater, Wolkenrand | Offerte Wolkenrand ontvangen; besluit mei 2026 |
| Klantcommunicatie binnen 30 minuten na vaststelling Prioriteit 1 | S. Loonstra | Gereed |

## 4. Scenario's en uitwijkstrategieën

| Nr | Scenario | Strategie | Verwachte hersteltijd |
|---|---|---|---|
| S1 | Uitval primair datacenter Wolkenrand | Automatische failover van het Kubernetes-cluster en de database naar het tweede datacenter in Nederland | 1 tot 2 uur |
| S2 | Mislukte wijziging of logische corruptie van gegevens (zoals maart 2026) | Terugzetten pre-migratiesnapshot; anders point-in-time-herstel uit back-up en WAL-archief; vanaf besluit mei 2026 eventueel omschakelen naar vertraagde stand-by | Snapshot: 1 uur; volledige restore: nu circa 14 uur, doel 4 uur |
| S3 | Ransomware of compromittering van beheeraccounts | Isoleren van de omgeving; herstel uit onveranderbare back-ups (object lock, 30 dagen) in schone omgeving; rotatie van alle sleutels; procedure datalekken | 24 tot 48 uur |
| S4 | Uitval Dendra AI | Insights-samenvattingen automatisch uitgeschakeld; prognoses blijven beschikbaar; bij langdurige uitval exitplan naar alternatieve aanbieder in de EER | Samenvattingen: afhankelijk van Dendra; overige functies niet geraakt |
| S5 | Uitval sleutelpersoon (DevOps lead of senior developer) | Draaiboeken in de wiki; piketrooster van vier personen; minimaal twee personen met productietoegang per taak; noodaccount in kluis bij de CTO | Geen directe dienstonderbreking |
| S6 | Uitval kantoor De Spilhoek of internetverbinding | Volledig werken op afstand met beheerde laptops en VPN; telefonie via softphone | Binnen 1 uur |
| S7 | Faillissement of contractbreuk Wolkenrand | Exitregeling hostingovereenkomst (6 maanden migratieondersteuning); wekelijkse versleutelde export van back-ups naar gescheiden opslag in Nederland; infrastructuur als code maakt herinrichting bij andere aanbieder mogelijk | 2 tot 4 weken voor volledige migratie |
| S8 | Grootschalige DDoS-aanval | DDoS-mitigatie van Wolkenrand; tijdelijk beperken van API-toegang; Veld offline cache | Afhankelijk van aanval |

## 5. Workaround voor klanten: noodexport

Iedere ochtend om 05:00 uur genereert PlanGrip voor klanten die dit hebben ingeschakeld een versleutelde PDF- en CSV-export van de planning voor de komende twee werkdagen. Deze wordt afgeleverd bij de klantbeheerder via een door de klant opgegeven e-mailadres of SFTP-locatie. De export bevat geen afwezigheidstypen en geen vrije notities. Daarnaast bewaart PlanGrip Veld vanaf release 26.5 de eigen planning van de medewerker voor 48 uur in versleutelde vorm op het toestel, zodat medewerkers bij uitval hun planning nog kunnen zien. De noodexport wordt opgenomen in de verwerkersdocumentatie van PlanGrip.

## 6. Calamiteitenorganisatie

| Rol | Persoon | Vervanger | Taken |
|---|---|---|---|
| Leider crisisteam | Ruben Okkersen (CTO) | Femke van Dalsem | Besluiten over herstelstrategie, inzet middelen, contact met leveranciers op directieniveau |
| Technisch coördinator | Bas Hoekwater | Marit Holtrop | Analyse, herstel, contact storingsdienst Wolkenrand, logboek |
| Communicatie klanten | Sem Loonstra | Daan Achterberg | Statuspagina, berichten klantbeheerders, telefonische opvang Enterprise-klanten |
| Bestuur en externe communicatie | Femke van Dalsem (CEO) | Ruben Okkersen | Contact met grote klanten, raad van commissarissen, pers |
| Juridisch en privacy | Lieke Dorrestein | – | Beoordeling datalek, contractuele gevolgen, meldingen |

Het crisisteam wordt bijeengeroepen bij ieder Prioriteit 1-incident dat naar verwachting langer dan 1 uur duurt. De technisch coördinator houdt een logboek bij met tijdstippen van waarnemingen, besluiten en handelingen.

### 6.1 Communicatie

| Moment | Kanaal | Inhoud |
|---|---|---|
| Binnen 30 minuten na vaststelling P1 | Statuspagina en e-mail klantbeheerders | Melding storing, eerste inschatting, verwijzing naar noodexport |
| Elk uur (tussen 06:00 en 22:00) | Statuspagina | Voortgang en verwachte hersteltijd |
| Bij Enterprise-klanten | Telefonisch, binnen 1 uur | Persoonlijk contact met contactpersoon uit het contract (onder meer Gemeente Lindewoude en Installatiebedrijf Rietvelden) |
| Na herstel | E-mail | Herstelbericht |
| Binnen 5 werkdagen | Incidentrapport | Oorzaak, gevolgen, maatregelen |

## 7. Testen en onderhoud

| Test | Frequentie | Eerstvolgende | Verantwoordelijk |
|---|---|---|---|
| Restoretest volledige productiedatabase op gescheiden omgeving, met tijdmeting | Per kwartaal | mei 2026 | B. Hoekwater |
| Failovertest tweede datacenter (S1) | Jaarlijks, in onderhoudsvenster | september 2026 | B. Hoekwater, Wolkenrand |
| Tabletop-oefening crisisteam (wisselend scenario) | Halfjaarlijks | juni 2026 (scenario S3) | R.J. Okkersen |
| Controle noodexport bij steekproef van klanten | Maandelijks | mei 2026 | S. Loonstra |
| Restore-test op verzoek klant (artikel 4.3 SLA Teams) | Maximaal tweemaal per jaar per klant | Op verzoek | B. Hoekwater |

De resultaten van tests worden besproken in het security forum en meegenomen in de directiebeoordeling van het ISMS. Dit plan dient tevens als invulling van de beheersmaatregelen voor bedrijfscontinuïteit uit ISO 27001 (bijlage A, 5.29 en 5.30, en 8.13 en 8.14).

## Versiehistorie

| Versie | Datum | Wijziging | Auteur |
|---|---|---|---|
| 1.0 | september 2024 | Eerste versie, opgesteld bij de SLA voor Teams-klanten | B. Hoekwater |
| 1.1 | april 2026 | Herziening na storing 3 en 4 maart 2026: tiers en interne hersteldoelen, scenario S2 en S8, noodexport, calamiteitenorganisatie, communicatieschema, testregime | B. Hoekwater, R.J. Okkersen |

___
R.J. Okkersen, bestuurder (CTO)

___
B. Hoekwater, DevOps lead & security officer
