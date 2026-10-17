# OPDRACHTOVEREENKOMST PENETRATIETEST
_kenmerk NOV-INK-2026-001 (inkoop) – offertenummer Schildwacht SW-2025-1147_

**DE ONDERGETEKENDEN:**
1. de besloten vennootschap met beperkte aansprakelijkheid **Noviqo B.V.**, statutair gevestigd te Amsterdam en kantoorhoudende aan de Verzonnelkade 88, 1099 ZZ Amsterdam, ingeschreven in het handelsregister onder nummer 91234567, te dezen rechtsgeldig vertegenwoordigd door mevrouw F.A. van Dalsem en de heer R.J. Okkersen, beiden bestuurder, hierna te noemen: "Noviqo" of "Opdrachtgever";
2. de besloten vennootschap met beperkte aansprakelijkheid **Schildwacht Security B.V.**, statutair gevestigd te 's-Hertogenbosch en kantoorhoudende aan de Vestingwal 31, 5211 ZZ 's-Hertogenbosch (fictief), ingeschreven in het handelsregister onder nummer 95123468, te dezen rechtsgeldig vertegenwoordigd door de heer L.T. Wijnbergen, directeur, hierna te noemen: "Schildwacht" of "Opdrachtnemer",

hierna gezamenlijk te noemen: "Partijen" en ieder afzonderlijk: "Partij";

**IN AANMERKING NEMENDE DAT:**
(a) Opdrachtgever het SaaS-platform PlanGrip exploiteert, bestaande uit een webapplicatie, een API, de mobiele app PlanGrip Veld en de per 15 januari 2026 te lanceren AI-module PlanGrip Insights;
(b) Opdrachtgever zich in haar verwerkersovereenkomsten met klanten heeft verplicht tot periodieke penetratietesten en de beveiliging van PlanGrip, mede naar aanleiding van het beveiligingsincident van juni 2025, onafhankelijk wil laten toetsen;
(c) Opdrachtnemer een gespecialiseerd bureau is op het gebied van offensieve beveiligingstesten, waarvan de testers beschikken over erkende certificeringen;
(d) het zonder toestemming binnendringen in een geautomatiseerd werk strafbaar is op grond van artikel 138ab van het Wetboek van Strafrecht en Partijen daarom de reikwijdte van de toestemming en de spelregels van de test uitdrukkelijk en schriftelijk wensen vast te leggen;
(e) Opdrachtnemer op 15 december 2025 een offerte heeft uitgebracht met nummer SW-2025-1147, die Opdrachtgever met inachtneming van deze overeenkomst aanvaardt.

**KOMEN OVEREEN ALS VOLGT:**

## Artikel 1 – Opdracht
1.1 Opdrachtgever verleent Opdrachtnemer opdracht tot het uitvoeren van een penetratietest op de in artikel 2 omschreven systemen (de "Test") en het opstellen van een rapport met bevindingen en aanbevelingen (het "Rapport").
1.2 De Test wordt uitgevoerd volgens een grey-boxbenadering: Opdrachtnemer ontvangt testaccounts met verschillende rollen (beheerder, planner, medewerker) in twee afzonderlijke testomgevingen ("tenants"), alsmede de API-documentatie en een architectuuroverzicht, maar geen toegang tot de broncode.
1.3 De Test wordt uitgevoerd aan de hand van de OWASP Web Security Testing Guide, de OWASP Mobile Application Security Testing Guide en de OWASP Top 10 voor LLM-toepassingen. Bevindingen worden geclassificeerd volgens CVSS versie 4.0 in de categorieën kritiek, hoog, midden, laag en informatief.
1.4 Opdrachtnemer voert de opdracht uit als zelfstandig opdrachtnemer in de zin van artikel 7:400 BW. Op Opdrachtnemer rust een inspanningsverplichting; zij staat er niet voor in dat alle kwetsbaarheden worden gevonden.

## Artikel 2 – Scope
2.1 Binnen de scope van de Test vallen uitsluitend:
a. de webapplicatie PlanGrip op app.plangrip.noviqo.example en de acceptatieomgeving op acc.plangrip.noviqo.example;
b. de REST-API op api.plangrip.noviqo.example, inclusief authenticatie, autorisatie en de exportfunctionaliteit;
c. de mobiele app PlanGrip Veld (Android en iOS), in de door Opdrachtgever via een testdistributie beschikbaar gestelde versie;
d. de module PlanGrip Insights, uitsluitend via de interface en de API van PlanGrip, met inbegrip van tests op promptinjectie, het uitlekken van gegevens tussen tenants via gegenereerde samenvattingen en de afscherming van gepseudonimiseerde gegevens;
e. de single-sign-on-koppeling (SAML/OIDC) zoals die voor Enterprise-klanten wordt aangeboden.
2.2 Buiten de scope vallen uitdrukkelijk:
a. de onderliggende infrastructuur van Wolkenrand Hosting B.V., voor zover het niet gaat om de door Opdrachtgever beheerde containers en applicatiecomponenten;
b. de systemen en API-endpoints van Dendra AI Inc. zelf; directe aanvallen op die systemen, pogingen tot het extraheren van modelgegevens en het omzeilen van rate limits van Dendra zijn niet toegestaan;
c. tenants en gegevens van klanten van Opdrachtgever;
d. de systemen van Ticketvlinder B.V., Klantloep CRM B.V. en andere leveranciers;
e. social engineering, phishing en fysieke toegangstesten;
f. denial-of-service-aanvallen en belastingtesten.
2.3 Stuit Opdrachtnemer tijdens de Test op een systeem of gegevens buiten de scope, dan staakt zij onmiddellijk de betreffende handeling, legt zij vast wat zij heeft waargenomen en meldt zij dit dezelfde werkdag aan de contactpersoon van Opdrachtgever.

## Artikel 3 – Toestemming en vrijwaring
3.1 Opdrachtgever verklaart dat zij rechthebbende is ten aanzien van de in artikel 2.1 genoemde systemen, dan wel bevoegd is daarover toestemming te verlenen, en verleent Opdrachtnemer hierbij uitdrukkelijk toestemming om binnen de scope en de testperiode, met de in Bijlage 1 omschreven methoden, toegang te verkrijgen tot deze systemen, beveiligingsmaatregelen te doorbreken en de daarbij aangetroffen gegevens in te zien voor zover dat voor de Test noodzakelijk is.
3.2 Opdrachtgever verklaart dat zij van Wolkenrand Hosting B.V. bij e-mail van 22 december 2025 schriftelijke toestemming heeft verkregen voor het uitvoeren van de Test op de bij Wolkenrand gehoste omgevingen, onder de voorwaarde dat de Test vooraf bij de storingsdienst van Wolkenrand wordt aangemeld met de IP-adressen van Opdrachtnemer. Opdrachtgever draagt zorg voor die aanmelding uiterlijk 16 januari 2026.
3.3 De Test op Insights is zo ingericht dat het verkeer naar Dendra AI Inc. binnen de gebruikelijke voorwaarden van Opdrachtgevers overeenkomst met Dendra AI Inc. blijft. Opdrachtnemer verstuurt via Insights niet meer dan 500 testverzoeken per dag en gebruikt uitsluitend synthetische gegevens.
3.4 Opdrachtgever vrijwaart Opdrachtnemer en de door haar ingezette testers tegen aanspraken van derden, waaronder Wolkenrand Hosting B.V., Dendra AI Inc. en klanten van Opdrachtgever, voor zover die aanspraken voortvloeien uit handelingen die Opdrachtnemer binnen de scope, binnen de testperiode en overeenkomstig deze overeenkomst heeft verricht.
3.5 De vrijwaring geldt niet voor schade die het gevolg is van handelingen buiten de scope, van het negeren van een stopverzoek als bedoeld in artikel 5.3, of van opzet of bewuste roekeloosheid van Opdrachtnemer of de door haar ingezette testers.
3.6 De toestemming in dit artikel geldt uitsluitend voor de in Bijlage 2 genoemde testers en IP-adressen en kan door Opdrachtgever te allen tijde met onmiddellijke ingang worden ingetrokken.

## Artikel 4 – Planning en oplevering
4.1 De Test wordt uitgevoerd in de periode van maandag 19 januari 2026 tot en met vrijdag 30 januari 2026, op werkdagen tussen 8.00 en 20.00 uur. Testactiviteiten buiten die tijden vinden uitsluitend plaats na voorafgaande schriftelijke afstemming.
4.2 Opdrachtnemer levert uiterlijk 5 februari 2026 een conceptrapport op. Partijen bespreken het concept in een sessie met de heer B. Hoekwater, waarna Opdrachtnemer het definitieve Rapport uiterlijk 9 februari 2026 oplevert.
4.3 Het Rapport bevat ten minste een managementsamenvatting, een beschrijving van de gevolgde methode, per bevinding een beschrijving, de CVSS-score, bewijs (zoals schermafdrukken of verzoeken), het risico voor Opdrachtgever en haar klanten en een concrete aanbeveling voor herstel.
4.4 Bevindingen met de classificatie kritiek meldt Opdrachtnemer direct telefonisch en uiterlijk binnen twee uur na vaststelling aan de contactpersoon van Opdrachtgever, zonder het Rapport af te wachten.
4.5 Opdrachtnemer voert binnen drie maanden na oplevering van het Rapport op verzoek van Opdrachtgever eenmalig kosteloos een hertest uit op de bevindingen met de classificatie kritiek, hoog en midden, en levert daarvan een hertestverklaring op.

## Artikel 5 – Uitvoering en communicatie
5.1 De Test wordt uitgevoerd door de in Bijlage 2 genoemde testers onder leiding van mevrouw M. Ekelschot (OSCP, OSWE). Vervanging van testers is uitsluitend toegestaan na voorafgaande schriftelijke goedkeuring van Opdrachtgever.
5.2 Contactpersoon van Opdrachtgever is de heer B. Hoekwater, DevOps lead & security officer; diens vervanger is mevrouw M. Holtrop, senior developer. Zij zijn tijdens de testperiode op werkdagen tussen 8.00 en 20.00 uur telefonisch bereikbaar.
5.3 Opdrachtgever mag de Test te allen tijde geheel of gedeeltelijk laten stoppen, bijvoorbeeld bij een verstoring van de productieomgeving. Opdrachtnemer geeft onmiddellijk gehoor aan een stopverzoek. De Test wordt slechts hervat na uitdrukkelijk akkoord van Opdrachtgever.
5.4 Opdrachtnemer voert de Test uit vanaf de in Bijlage 2 vermelde vaste IP-adressen en houdt een logboek bij van alle uitgevoerde activiteiten, dat zij op verzoek aan Opdrachtgever verstrekt.
5.5 Opdrachtnemer installeert geen persistente software, backdoors of webshells op de systemen van Opdrachtgever. Tijdens de Test aangemaakte bestanden, accounts en gegevens worden na afloop door Opdrachtnemer verwijderd of in het Rapport opgesomd zodat Opdrachtgever die kan verwijderen.

## Artikel 6 – Vergoeding
6.1 De Test wordt uitgevoerd tegen een vaste prijs van € 16.800 exclusief btw, gebaseerd op veertien testdagen à € 1.200, inclusief het opstellen van het Rapport, de bespreeksessie en de hertest als bedoeld in artikel 4.5.
6.2 Opdrachtnemer factureert 50% bij aanvang van de Test en 50% na oplevering van het definitieve Rapport. Betaling geschiedt binnen 30 dagen na factuurdatum.
6.3 Indien de Test door oorzaken die aan Opdrachtgever zijn toe te rekenen, zoals het niet tijdig beschikbaar stellen van testaccounts, niet binnen de testperiode kan worden voltooid, mag Opdrachtnemer de daardoor ontstane extra testdagen tegen het dagtarief in rekening brengen, na voorafgaand overleg.

## Artikel 7 – Geheimhouding en Rapport
7.1 Opdrachtnemer houdt alle informatie die zij in het kader van de opdracht verkrijgt, waaronder de aangetroffen kwetsbaarheden, het Rapport en de werkwijze van PlanGrip, strikt geheim. Deze verplichting blijft ook na het einde van de overeenkomst van kracht.
7.2 Opdrachtnemer maakt aangetroffen kwetsbaarheden niet openbaar en meldt deze niet aan derden, ook niet in geanonimiseerde vorm, tenzij Opdrachtgever daarvoor schriftelijk toestemming geeft. Indien een kwetsbaarheid in standaardsoftware van een derde wordt aangetroffen, stemmen Partijen een gecoördineerde melding aan de leverancier af.
7.3 Het Rapport wordt uitsluitend versleuteld verzonden. Opdrachtgever mag het Rapport, of een samenvatting daarvan, onder geheimhouding verstrekken aan haar raad van commissarissen, investeerders, auditors, klanten en toezichthouders.
7.4 Opdrachtnemer bewaart het Rapport, het logboek en de bij de Test verkregen gegevens niet langer dan drie maanden na de hertest of, indien geen hertest plaatsvindt, na oplevering van het Rapport, en vernietigt deze daarna aantoonbaar.

## Artikel 8 – Persoonsgegevens
8.1 De testomgevingen bevatten uitsluitend synthetische gegevens. Opdrachtgever draagt er zorg voor dat in de testtenants geen persoonsgegevens van klanten of hun medewerkers aanwezig zijn.
8.2 Voor zover Opdrachtnemer tijdens de Test desondanks persoonsgegevens verwerkt waarvoor Opdrachtgever verwerkingsverantwoordelijke of verwerker is, handelt zij als (sub)verwerker van Opdrachtgever en gelden de verwerkersbepalingen in Bijlage 3, die voldoen aan artikel 28 lid 3 AVG. Opdrachtnemer maakt van zulke gegevens geen kopieën, behoudens het minimale bewijs dat noodzakelijk is voor het Rapport, dat zij zoveel mogelijk maskeert.
8.3 Opdrachtnemer meldt een vermoedelijke inbreuk in verband met persoonsgegevens binnen 24 uur aan Opdrachtgever.

## Artikel 9 – Aansprakelijkheid
9.1 Opdrachtgever is zich ervan bewust dat een penetratietest, ook bij zorgvuldige uitvoering, kan leiden tot verstoringen, prestatieverlies of het onbedoeld wijzigen van gegevens in de testomgevingen. Opdrachtgever draagt zorg voor actuele back-ups voorafgaand aan de Test.
9.2 De aansprakelijkheid van Opdrachtnemer voor directe schade als gevolg van een toerekenbare tekortkoming is beperkt tot tweemaal het bedrag van de vergoeding als bedoeld in artikel 6.1. Aansprakelijkheid voor indirecte schade is uitgesloten.
9.3 De beperking van artikel 9.2 geldt niet in geval van opzet of bewuste roekeloosheid van Opdrachtnemer of haar leidinggevenden, bij handelingen buiten de scope en bij schending van artikel 7 of artikel 8.
9.4 Opdrachtnemer beschikt over een beroeps- en bedrijfsaansprakelijkheidsverzekering met een dekking van ten minste € 2.500.000 per aanspraak die uitdrukkelijk ook beveiligingstesten dekt.

## Artikel 10 – Duur en slotbepalingen
10.1 Deze overeenkomst eindigt na de uitvoering van de hertest of, indien Opdrachtgever binnen drie maanden na oplevering van het Rapport geen hertest verzoekt, na verloop van die termijn. Artikel 3.4, 7, 8 en 9 blijven daarna van kracht.
10.2 De algemene voorwaarden van Opdrachtnemer zijn niet van toepassing.
10.3 Op deze overeenkomst is Nederlands recht van toepassing. Geschillen worden voorgelegd aan de bevoegde rechter te Amsterdam.

Aldus overeengekomen en ondertekend op 5 januari 2026.

___
Noviqo B.V.
F.A. van Dalsem
bestuurder

___
Noviqo B.V.
R.J. Okkersen
bestuurder

___
Schildwacht Security B.V.
L.T. Wijnbergen
directeur

**Bijlagen**
- Bijlage 1: Rules of engagement en testmethoden
- Bijlage 2: Testers, IP-adressen en contactgegevens (vertrouwelijk)
- Bijlage 3: Verwerkersbepalingen ex artikel 28 AVG
