# SERVICE LEVEL AGREEMENT PLANGRIP ENTERPRISE
_kenmerk NOV-SLA-2025-002 – versie 2.0, januari 2025 – standaarddocument_

| Documentgegevens | |
|---|---|
| Versie | 2.0 (vervangt versie 1.1 van mei 2024) |
| Vastgesteld | 13 januari 2025 door het bestuur van Noviqo B.V. |
| Eigenaar | R.J. Okkersen (CTO); operationeel: B. Hoekwater (DevOps lead) |
| Toepassing | Alle overeenkomsten voor PlanGrip Enterprise gesloten vanaf 1 februari 2025 |
| Wijzigingen ten opzichte van 1.1 | beschikbaarheid verhoogd van 99,7% naar 99,8%; Prioriteit 1 24/7; nieuwe servicecreditstaffel; RPO/RTO aangescherpt |

## Artikel 1 – Toepassing en definities
1.1 Deze Service Level Agreement ("SLA") is van toepassing op de dienstverlening van Noviqo B.V. ("Leverancier") aan klanten die het abonnement PlanGrip Enterprise afnemen ("Klant"), voor zover de overeenkomst tussen Leverancier en Klant ("Overeenkomst") naar deze SLA verwijst. De SLA maakt integraal deel uit van de Overeenkomst. Afwijkingen gelden alleen indien zij in de Overeenkomst zijn opgenomen.
1.2 In deze SLA wordt verstaan onder: "Dienst": het platform PlanGrip in de Enterprise-uitvoering, inclusief de webapplicatie, de API en de mobiele applicatie PlanGrip Veld; "Incident": een niet-geplande onderbreking of vermindering van de kwaliteit van de Dienst; "Kantooruren": werkdagen van 08:30 tot 17:30 uur, met uitzondering van nationale feestdagen; "Responstijd": de tijd tussen de melding van een Incident en de eerste inhoudelijke reactie van een supportmedewerker; "Hersteltijd": de tijd tussen de melding en het herstel van de Dienst of het beschikbaar stellen van een werkbare workaround.

## Artikel 2 – Beschikbaarheid
2.1 Leverancier garandeert een beschikbaarheid van de Dienst van **99,8% per kalendermaand**. Dit komt neer op een maximale ongeplande onbeschikbaarheid van circa 1 uur en 27 minuten per maand.
2.2 Beschikbaarheid wordt berekend als: (totaal aantal minuten in de maand minus minuten onbeschikbaarheid) gedeeld door het totaal aantal minuten in de maand, maal 100%. De Dienst geldt als onbeschikbaar wanneer de webapplicatie of de API gedurende ten minste vijf aaneengesloten minuten vanaf twee onafhankelijke meetpunten niet bereikbaar is of foutmeldingen geeft.
2.3 Leverancier meet de beschikbaarheid met een externe monitoringdienst op de applicatielaag. Een publieke statuspagina is beschikbaar via status.plangrip.example.
2.4 Niet als onbeschikbaarheid gelden:
a. gepland onderhoud overeenkomstig artikel 6;
b. storingen in apparatuur, netwerken, software of identity provider van Klant;
c. onbeschikbaarheid als gevolg van handelen of nalaten van Klant of haar Gebruikers in strijd met de Overeenkomst;
d. overmacht als bedoeld in de algemene voorwaarden van Leverancier, met dien verstande dat storingen bij Wolkenrand Hosting B.V. of andere toeleveranciers van Leverancier niet als overmacht gelden voor zover Leverancier redelijkerwijs voorzorgsmaatregelen had kunnen treffen;
e. opschorting van de Dienst op grond van de Overeenkomst.
2.5 De beschikbaarheid van de mobiele applicatie PlanGrip Veld is afhankelijk van mobiele netwerken en app-stores van derden. Voor PlanGrip Veld geldt de beschikbaarheidsgarantie uitsluitend voor de onderliggende server-diensten; de offlinemodus van PlanGrip Veld synchroniseert automatisch na herstel van de verbinding.

## Artikel 3 – Support
3.1 Support is beschikbaar via het supportportaal (support.plangrip.example), per e-mail en telefonisch via 020-0000000 (fictief) tijdens Kantooruren.
3.2 Voor Incidenten met Prioriteit 1 is Leverancier 24 uur per dag, 7 dagen per week bereikbaar via het calamiteitennummer dat aan de geautoriseerde beheerders van Klant wordt verstrekt. Buiten Kantooruren is een engineer van dienst binnen 30 minuten inzetbaar.
3.3 Klant wijst maximaal vijf geautoriseerde beheerders aan die Incidenten met Prioriteit 1 en 2 kunnen melden. Meldingen door andere Gebruikers worden in behandeling genomen als Prioriteit 3 totdat een beheerder de prioriteit bevestigt.
3.4 Iedere Enterprise-klant heeft een vaste customer success manager, die het aanspreekpunt is voor niet-technische vragen, adoptie en escalaties.

## Artikel 4 – Prioriteiten, respons- en hersteltijden
4.1 Incidenten worden als volgt geclassificeerd en behandeld:

| Prioriteit | Omschrijving | Responstijd | Hersteltijd | Venster |
|---|---|---|---|---|
| P1 – Kritiek | Dienst geheel onbeschikbaar of ernstig beveiligingsincident, alle of nagenoeg alle Gebruikers geraakt | 30 minuten | 4 uur | 24/7 |
| P2 – Hoog | Kernfunctionaliteit (planning, Veld-synchronisatie, SSO) ernstig beperkt voor een groot deel van de Gebruikers, geen workaround | 2 uur | 1 werkdag | Kantooruren |
| P3 – Normaal | Beperkte verstoring, workaround beschikbaar of slechts enkele Gebruikers geraakt | 4 kantooruren | 5 werkdagen | Kantooruren |
| P4 – Laag | Cosmetisch gebrek, vraag of wens | 2 werkdagen | volgens releaseplanning | Kantooruren |

4.2 Klant stelt bij melding een prioriteit voor; Leverancier stelt de prioriteit in redelijkheid vast en motiveert een afwijking schriftelijk. Bij verschil van inzicht beslist de escalatiemanager van Leverancier, na overleg met Klant.
4.3 De hersteltijden voor P1 en P2 zijn resultaatsverplichtingen, behoudens de uitzonderingen in artikel 2.4. De hersteltijden voor P3 en P4 zijn inspanningsverplichtingen.
4.4 Na ieder P1-Incident levert Leverancier binnen vijf werkdagen een schriftelijke root cause analysis met de oorzaak, de getroffen maatregelen en de maatregelen ter voorkoming van herhaling.

## Artikel 5 – Escalatie
5.1 Indien een Incident niet binnen de hersteltijd is opgelost, kan Klant escaleren volgens het volgende schema:
- eerste niveau: teamlead support;
- tweede niveau: DevOps lead (thans de heer B. Hoekwater);
- derde niveau: CTO (thans de heer R.J. Okkersen).
5.2 Bij een P1-Incident informeert Leverancier Klant ten minste ieder uur over de voortgang, totdat de Dienst is hersteld.

## Artikel 6 – Onderhoud en releases
6.1 Gepland onderhoud vindt plaats in het onderhoudsvenster op zondag tussen 00:00 en 06:00 uur en wordt ten minste vijf werkdagen vooraf aangekondigd via het supportportaal en de statuspagina. Gepland onderhoud bedraagt maximaal vier uur per kalendermaand.
6.2 Spoedonderhoud ter oplossing van een ernstig beveiligingsrisico mag Leverancier met een kortere aankondigingstermijn uitvoeren; onbeschikbaarheid daardoor telt mee voor de beschikbaarheid, tenzij het onderhoud binnen het onderhoudsvenster plaatsvindt.
6.3 Leverancier brengt nieuwe releases uit volgens haar releasekalender. Enterprise-klanten krijgen ten minste tien werkdagen vóór een release met merkbare gevolgen voor de gebruikersinterface toegang tot de releasenotes en een acceptatieomgeving.

## Artikel 7 – Back-up, recovery en continuïteit
7.1 Leverancier maakt continu transactielog-back-ups en dagelijks een volledige back-up van de Klantdata. Back-ups worden versleuteld opgeslagen in een tweede, fysiek gescheiden datacenter in Nederland en 35 dagen bewaard.
7.2 De Recovery Point Objective (RPO) bedraagt 4 uur; de Recovery Time Objective (RTO) bij een calamiteit bedraagt 8 uur.
7.3 Leverancier test haar herstelprocedure ten minste tweemaal per jaar en deelt op verzoek een samenvatting van de resultaten. Op verzoek van Klant voert Leverancier eenmaal per jaar kosteloos een restore-test van de omgeving van Klant uit naar een testomgeving.

## Artikel 8 – Beveiliging
8.1 Leverancier onderhoudt een informatiebeveiligingsmanagementsysteem dat is ingericht volgens ISO/IEC 27001. Eigenaar van het ISMS is de security officer van Leverancier.
8.2 Gegevens worden versleuteld in transit (TLS 1.2 of hoger) en at rest (AES-256). Beheertoegang verloopt uitsluitend via multifactorauthenticatie en wordt gelogd; logbestanden worden twaalf maanden bewaard.
8.3 Leverancier laat jaarlijks een penetratietest uitvoeren door een onafhankelijke partij en verstrekt Enterprise-klanten op verzoek een managementsamenvatting.

## Artikel 9 – Rapportage en serviceoverleg
9.1 Leverancier stelt maandelijks vóór de tiende werkdag een servicerapportage beschikbaar met de gerealiseerde beschikbaarheid, het aantal Incidenten per prioriteit, de gerealiseerde respons- en hersteltijden en eventuele servicecredits.
9.2 Ieder kwartaal vindt een serviceoverleg plaats tussen de customer success manager en de contactpersoon van Klant. Eenmaal per jaar sluit de CTO van Leverancier hierbij aan.

## Artikel 10 – Servicecredits
10.1 Indien de beschikbaarheid in een kalendermaand lager is dan 99,8%, heeft Klant recht op een servicecredit, berekend als percentage van de maandelijkse abonnementsvergoeding (bij jaarlijkse of kwartaalfacturatie omgerekend naar een maandbedrag):

| Gerealiseerde beschikbaarheid | Servicecredit |
|---|---|
| 99,5% tot 99,8% | 5% |
| 99,0% tot 99,5% | 10% |
| 98,0% tot 99,0% | 20% |
| lager dan 98,0% | 30% |

10.2 Voor iedere overschrijding van de hersteltijd van een P1-Incident met meer dan twee uur ontvangt Klant een aanvullende servicecredit van 5% van de maandvergoeding, met een maximum van 15% per maand.
10.3 Het totaal aan servicecredits bedraagt maximaal 50% van de maandvergoeding per kalendermaand.
10.4 Servicecredits worden automatisch berekend op basis van de servicerapportage en verrekend met de eerstvolgende factuur. Klant kan binnen 30 dagen na ontvangst van de rapportage gemotiveerd bezwaar maken tegen de berekening.
10.5 Servicecredits gelden als forfaitaire schadevergoeding voor het niet halen van de service levels en komen in mindering op iedere schadevergoeding die Leverancier wegens dezelfde tekortkoming verschuldigd is. Servicecredits laten het recht van Klant op nakoming en ontbinding onverlet.

## Artikel 11 – Bijzonder ontbindingsrecht
Indien de beschikbaarheid in drie opeenvolgende kalendermaanden, of in vier kalendermaanden binnen een periode van twaalf maanden, lager is dan 99,5%, mag Klant de Overeenkomst schriftelijk ontbinden met een opzegtermijn van één maand, zonder tot enige schadevergoeding gehouden te zijn. Vooruitbetaalde vergoedingen over de periode na beëindiging worden terugbetaald.

## Artikel 12 – Evaluatie en wijziging
12.1 Leverancier evalueert deze SLA jaarlijks. Een nieuwe versie geldt voor lopende Overeenkomsten slechts indien zij voor Klant niet nadeliger is, of indien Klant daarmee schriftelijk instemt.
12.2 Deze SLA volgt de looptijd van de Overeenkomst.

Vastgesteld door het bestuur van Noviqo B.V. te Amsterdam op 13 januari 2025.

___
Noviqo B.V.
F.A. van Dalsem
bestuurder

___
Noviqo B.V.
R.J. Okkersen
bestuurder
