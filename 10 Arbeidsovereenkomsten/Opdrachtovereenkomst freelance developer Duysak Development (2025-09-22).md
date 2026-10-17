# OPDRACHTOVEREENKOMST FREELANCE SOFTWAREONTWIKKELING
_kenmerk NOV-HR-2025-021 (inhuur zelfstandige)_

**DE ONDERGETEKENDEN:**
1. de besloten vennootschap met beperkte aansprakelijkheid **Noviqo B.V.**, statutair gevestigd te Amsterdam en kantoorhoudende aan de Verzonnelkade 88, 1099 ZZ Amsterdam, ingeschreven in het handelsregister onder nummer 91234567, te dezen rechtsgeldig vertegenwoordigd door mevrouw F.A. van Dalsem en de heer R.J. Okkersen, beiden bestuurder, hierna te noemen: "Noviqo" of "Opdrachtgever";
2. de heer **K. (Kerem) Duysak**, handelend onder de naam **Duysak Development**, eenmanszaak, kantoorhoudende aan de Codekade 5, 2011 AB Haarlem (fictief), ingeschreven in het handelsregister onder nummer 96234781, btw-identificatienummer NL000000000B77 (fictief), hierna te noemen: "Opdrachtnemer",

hierna gezamenlijk te noemen: "Partijen" en ieder afzonderlijk: "Partij";

**IN AANMERKING NEMENDE DAT:**
(a) Opdrachtgever de AI-module PlanGrip Insights ontwikkelt, die per januari 2026 aan klanten beschikbaar wordt gesteld en voor tekstuele samenvattingen gebruikmaakt van een taalmodel van Dendra AI Inc.;
(b) Opdrachtgever voor de realisatie van de koppeling met Dendra AI Inc. en de daarvoor benodigde pseudonimiseringscomponent tijdelijk specialistische kennis nodig heeft die binnen haar ontwikkelteam niet voorhanden is;
(c) Opdrachtnemer een zelfstandig ondernemer is die sinds 2019 onder eigen naam en voor eigen rekening en risico softwareontwikkeling verricht voor meerdere opdrachtgevers, met specialisatie in het integreren van taalmodellen in bestaande applicaties;
(d) Partijen uitdrukkelijk geen arbeidsovereenkomst wensen aan te gaan maar een overeenkomst van opdracht in de zin van artikel 7:400 BW, en hun samenwerking ook feitelijk zo zullen inrichten dat geen sprake is van werkgeversgezag of van inbedding in de organisatie van Opdrachtgever;
(e) Partijen zich ervan bewust zijn dat de Belastingdienst met ingang van 1 januari 2025 de handhaving op schijnzelfstandigheid volledig heeft hervat, dat de feitelijke uitvoering doorslaggevend is en niet de benaming van de overeenkomst, en dat zij bij het opstellen van deze overeenkomst de criteria uit de rechtspraak (waaronder de criteria gezag, loon, persoonlijke arbeid en inbedding) en de door de Belastingdienst gepubliceerde algemene modelovereenkomsten als uitgangspunt hebben genomen.

**KOMEN OVEREEN ALS VOLGT:**

## Artikel 1 – Opdracht en resultaat
1.1 Opdrachtgever verleent Opdrachtnemer opdracht tot het ontwerpen, bouwen, testen en documenteren van de volgende onderdelen van PlanGrip Insights (de "Opdracht"):
a. een integratielaag tussen PlanGrip en de API van Dendra AI Inc., inclusief foutafhandeling, rate limiting en kostenbewaking per klant;
b. een pseudonimiseringscomponent die namen en contactgegevens van medewerkers van klanten vóór verzending aan Dendra AI Inc. vervangt door pseudoniemen en na ontvangst van de samenvatting weer terugvertaalt, waarbij de sleutel binnen de door Wolkenrand Hosting B.V. gehoste omgeving blijft;
c. een evaluatieset en geautomatiseerde tests waarmee de kwaliteit van de gegenereerde samenvattingen en de afscherming tussen klantomgevingen kunnen worden gecontroleerd;
d. technische documentatie en een overdrachtssessie aan het interne ontwikkelteam.
1.2 De functionele en technische eisen zijn beschreven in het opdrachtdocument "Insights – integratie en pseudonimisering" van 15 september 2025 (Bijlage 1). De Opdracht is in drie mijlpalen verdeeld; een mijlpaal is opgeleverd wanneer Opdrachtgever deze heeft geaccepteerd aan de hand van de acceptatiecriteria in Bijlage 1.

## Artikel 2 – Zelfstandige uitvoering
2.1 Opdrachtnemer bepaalt zelf de wijze waarop hij de Opdracht uitvoert, de volgorde van de werkzaamheden, zijn werktijden en zijn werkplek. Opdrachtgever geeft uitsluitend aanwijzingen over het gewenste resultaat en over de technische randvoorwaarden die voor alle leveranciers gelden, zoals de beveiligingseisen in artikel 7.
2.2 Opdrachtnemer neemt deel aan afstemmingsoverleggen met het ontwikkelteam voor zover dat voor de aansluiting van zijn resultaat op het platform nodig is, in de regel eenmaal per week. Opdrachtnemer neemt geen deel aan het storingsrooster, aan personeelsbijeenkomsten of aan de beoordelingscyclus van Opdrachtgever en heeft geen leidinggevende of ondergeschikten bij Opdrachtgever.
2.3 Opdrachtnemer gebruikt zijn eigen apparatuur en programmatuur. Opdrachtgever verstrekt uitsluitend de toegang tot haar ontwikkel- en testomgevingen en een e-mailadres onder het domein noviqo.example dat herkenbaar is als extern (k.duysak.extern@noviqo.example).
2.4 Opdrachtnemer is vrij om tijdens de looptijd werkzaamheden voor andere opdrachtgevers te verrichten, met uitzondering van werkzaamheden voor directe concurrenten van PlanGrip in de periode tot de oplevering van de laatste mijlpaal, voor zover daarbij een reëel risico bestaat dat vertrouwelijke informatie van Opdrachtgever wordt gebruikt.
2.5 Opdrachtnemer mag zich met voorafgaande toestemming van Opdrachtgever laten vervangen door een andere deskundige, die aan dezelfde eisen voldoet en eveneens schriftelijk geheimhouding aanvaardt. Opdrachtgever weigert die toestemming niet op onredelijke gronden. De kosten van vervanging, inclusief inwerken, komen voor rekening van Opdrachtnemer.
2.6 Opdrachtnemer staat in voor de kwaliteit van zijn werk en herstelt gebreken in opgeleverde mijlpalen die binnen drie maanden na acceptatie worden gemeld, voor eigen rekening.

## Artikel 3 – Looptijd en omvang
3.1 Deze overeenkomst gaat in op 1 oktober 2025 en eindigt op 31 maart 2026, dan wel eerder bij acceptatie van de laatste mijlpaal en de overdrachtssessie. Verlenging is slechts mogelijk bij schriftelijke overeenkomst, met een afzonderlijk omschreven vervolgopdracht.
3.2 Partijen verwachten dat de Opdracht gemiddeld circa 20 uur per week vergt. Opdrachtnemer is niet gehouden tot een vast aantal uren per week en Opdrachtgever is niet gehouden een minimum aantal uren af te nemen.
3.3 De totale vergoeding onder deze overeenkomst bedraagt ten hoogste € 45.000 exclusief btw (het "plafond"). Opdrachtnemer meldt tijdig, en in ieder geval zodra 80% van het plafond is bereikt, of het resultaat binnen het plafond kan worden opgeleverd. Overschrijding van het plafond is slechts toegestaan na voorafgaande schriftelijke toestemming van beide bestuurders van Opdrachtgever.

## Artikel 4 – Vergoeding en facturering
4.1 Opdrachtnemer ontvangt een vergoeding van € 85 per uur exclusief btw. Reistijd en reiskosten zijn in het uurtarief begrepen.
4.2 Opdrachtnemer factureert maandelijks achteraf, onder vermelding van de bestede uren per mijlpaal en een korte omschrijving van de werkzaamheden. Opdrachtgever betaalt binnen 30 dagen na ontvangst van de factuur.
4.3 Opdrachtnemer is zelf verantwoordelijk voor de afdracht van omzetbelasting, inkomstenbelasting en eventuele sociale premies. Opdrachtgever houdt geen loonheffingen in. Opdrachtnemer heeft geen recht op doorbetaling bij ziekte, vakantietoeslag, vakantiedagen of andere arbeidsvoorwaarden die voor werknemers van Opdrachtgever gelden.
4.4 Indien de Belastingdienst of het UWV onherroepelijk vaststelt dat de arbeidsrelatie als dienstbetrekking moet worden aangemerkt en Opdrachtgever daardoor naheffingen moet voldoen, treden Partijen in overleg. Partijen zijn zich ervan bewust dat een regresrecht op Opdrachtnemer ter zake van loonheffingen wettelijk beperkt is.

## Artikel 5 – Intellectuele eigendom
5.1 Alle rechten van intellectuele eigendom op de in het kader van de Opdracht tot stand gebrachte resultaten, waaronder broncode, objectcode, ontwerpen, testsets en documentatie, worden hierbij bij voorbaat door Opdrachtnemer aan Opdrachtgever overgedragen, die deze overdracht aanvaardt. Deze overeenkomst geldt als akte als bedoeld in artikel 2 lid 2 Auteurswet. Voor zover een nadere akte nodig is, werkt Opdrachtnemer daaraan op eerste verzoek mee.
5.2 Opdrachtnemer doet, voor zover rechtens toegestaan, afstand van zijn persoonlijkheidsrechten als bedoeld in artikel 25 lid 1 sub a tot en met c Auteurswet.
5.3 Opdrachtnemer mag algemene kennis, ervaring en vooraf bestaande eigen hulpprogrammatuur blijven gebruiken. Voor zover dergelijke hulpprogrammatuur in de resultaten is verwerkt, verleent Opdrachtnemer Opdrachtgever een eeuwigdurende, niet-exclusieve, overdraagbare en kosteloze licentie om deze als onderdeel van PlanGrip te gebruiken, te wijzigen en te sublicentiëren. Opdrachtnemer vermeldt zulke hulpprogrammatuur in de documentatie.
5.4 Opdrachtnemer verwerkt geen opensourcecomponenten met een copyleft-licentie in de resultaten zonder voorafgaande schriftelijke toestemming van Opdrachtgever, en garandeert dat de resultaten geen inbreuk maken op rechten van derden.
5.5 De vergoeding voor de overdracht is in het uurtarief begrepen.

## Artikel 6 – Geheimhouding
6.1 Opdrachtnemer houdt alle informatie die hij in het kader van de Opdracht verkrijgt geheim, waaronder broncode, architectuur en beveiligingsmaatregelen van PlanGrip, de voorwaarden van de overeenkomst met Dendra AI Inc. en gegevens van klanten, ook na het einde van deze overeenkomst.
6.2 Bij overtreding van artikel 6.1 verbeurt Opdrachtnemer een direct opeisbare boete van € 10.000 per overtreding, onverminderd het recht van Opdrachtgever op volledige schadevergoeding.

## Artikel 7 – Beveiliging en persoonsgegevens
7.1 Opdrachtnemer werkt uitsluitend in de ontwikkel- en testomgevingen van Opdrachtgever, die gevuld zijn met synthetische gegevens. Toegang tot de productieomgeving wordt niet verleend.
7.2 Opdrachtnemer houdt zich aan de leveranciersbeveiligingseisen van Opdrachtgever (Bijlage 2), waaronder het gebruik van multifactorauthenticatie, volledige schijfversleuteling op de gebruikte apparatuur, actuele beveiligingsupdates en het niet opslaan van broncode buiten de repository van Opdrachtgever.
7.3 Voor zover Opdrachtnemer onverhoopt toch persoonsgegevens verwerkt waarvoor Opdrachtgever verwerkingsverantwoordelijke of verwerker is, doet hij dat uitsluitend op instructie van Opdrachtgever en gelden de verwerkersbepalingen in Bijlage 3, die voldoen aan artikel 28 lid 3 AVG. Opdrachtnemer meldt een (vermoedelijke) inbreuk in verband met persoonsgegevens binnen 24 uur aan de heer B. Hoekwater, DevOps lead & security officer.
7.4 Opdrachtnemer gebruikt voor de Opdracht geen eigen accounts bij Dendra AI Inc. of andere AI-aanbieders en voert geen gegevens of broncode van Opdrachtgever in externe AI-diensten in, anders dan via de door Opdrachtgever beschikbaar gestelde omgeving.

## Artikel 8 – Aansprakelijkheid en verzekering
8.1 Opdrachtnemer is aansprakelijk voor schade die Opdrachtgever lijdt als gevolg van een toerekenbare tekortkoming, tot ten hoogste het bedrag dat in het betreffende geval onder zijn beroepsaansprakelijkheidsverzekering wordt uitgekeerd en, bij gebreke daarvan, tot ten hoogste € 25.000. Deze beperking geldt niet bij opzet of bewuste roekeloosheid en niet bij schending van artikel 6 of 7.
8.2 Opdrachtnemer beschikt gedurende de looptijd over een beroeps- en bedrijfsaansprakelijkheidsverzekering met een dekking van ten minste € 500.000 per aanspraak en overlegt op verzoek een polisblad.
8.3 Opdrachtnemer draagt zelf het risico van ziekte en arbeidsongeschiktheid en is zelf verantwoordelijk voor zijn oudedagsvoorziening.

## Artikel 9 – Beëindiging
9.1 Iedere Partij kan deze overeenkomst tussentijds schriftelijk opzeggen met inachtneming van een termijn van één maand. Opdrachtgever vergoedt in dat geval de tot de einddatum verrichte en gedeclareerde werkzaamheden. Artikel 7:408 lid 2 BW is voor het overige uitgesloten, voor zover rechtens mogelijk.
9.2 Iedere Partij kan de overeenkomst met onmiddellijke ingang beëindigen indien de andere Partij in staat van faillissement wordt verklaard, of indien de andere Partij een wezenlijke verplichting niet nakomt en de tekortkoming niet binnen tien werkdagen na schriftelijke ingebrekestelling heeft hersteld. Een schending van artikel 6 of 7 geldt als wezenlijke tekortkoming die geen ingebrekestelling vereist.
9.3 Bij het einde van de overeenkomst draagt Opdrachtnemer alle resultaten, ook niet-afgeronde, en alle documentatie over aan Opdrachtgever, retourneert hij eventuele toegangsmiddelen en verwijdert hij alle informatie van Opdrachtgever van zijn eigen apparatuur. Hij bevestigt dit schriftelijk.

## Artikel 10 – Slotbepalingen
10.1 Opdrachtnemer verklaart dat hij is ingeschreven in het handelsregister, voor eigen rekening en risico werkt, meerdere opdrachtgevers heeft en zelf zorg draagt voor zijn acquisitie.
10.2 Partijen evalueren halverwege de looptijd, uiterlijk op 31 december 2025, of de feitelijke uitvoering nog overeenkomt met deze overeenkomst, in het bijzonder met artikel 2. Afwijkingen worden schriftelijk vastgelegd en zo nodig gecorrigeerd.
10.3 Op deze overeenkomst is Nederlands recht van toepassing. Geschillen worden voorgelegd aan de bevoegde rechter te Amsterdam.

Aldus overeengekomen en in tweevoud ondertekend te Amsterdam op 22 september 2025.

___
Noviqo B.V.
F.A. van Dalsem
bestuurder

___
Noviqo B.V.
R.J. Okkersen
bestuurder

___
Duysak Development
K. Duysak
eigenaar

**Bijlagen**
- Bijlage 1: Opdrachtdocument "Insights – integratie en pseudonimisering" d.d. 15 september 2025, met mijlpalen en acceptatiecriteria
- Bijlage 2: Beveiligingseisen voor externe ontwikkelaars
- Bijlage 3: Verwerkersbepalingen ex artikel 28 AVG
