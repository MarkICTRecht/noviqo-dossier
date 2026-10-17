# CHANGE- EN RELEASEMANAGEMENTPROCES PLANGRIP
_kenmerk NOV-PRC-2026-004 – versie 3.0 – april 2026_
## Documentgegevens
| Onderdeel | Gegevens |
|---|---|
| Documenteigenaar | Ruben Okkersen, CTO |
| Procesbeheerder | Bas Hoekwater, DevOps lead & security officer |
| Vastgesteld door | Bestuur (F.A. van Dalsem en R.J. Okkersen) |
| Versie | 3.0 |
| Datum vaststelling | 14 april 2026 |
| Ingangsdatum | 20 april 2026 |
| Volgende review | oktober 2026 (verkorte cyclus van zes maanden na herziening) |
| Classificatie | Intern |
## 1. Aanleiding en doel
Op 3 en 4 maart 2026 was PlanGrip circa 19 uur onbereikbaar voor alle klanten (incident INC-2026-006). De oorzaak was een fout bij een databasemigratie op de productieomgeving. De evaluatie liet zien dat de migratie niet vooraf op een productiekopie met representatief datavolume was getest, dat er geen uitgewerkt en getest rollbackplan was, dat de wijziging door één developer was voorbereid en uitgevoerd zonder inhoudelijke tweede beoordeling, en dat de herstelpoging de onbereikbaarheid verlengde. De storing leidde tot het overschrijden van de beschikbaarheidsnorm en de hersteltijd voor Prioriteit 1 uit de SLA's met klanten, en tot een aansprakelijkstelling door Bouwgroep Hazelaar B.V. van 18 maart 2026.
Dit proces is daarom volledig herzien. Doel: wijzigingen in PlanGrip beheerst, controleerbaar en omkeerbaar doorvoeren, zodat de afgesproken beschikbaarheid (99,5% voor Start en Teams, 99,8% voor Enterprise) wordt gehaald, en aantoonbaar kunnen maken richting klanten, auditors en de raad van commissarissen dat wijzigingen zorgvuldig gebeuren.
## 2. Reikwijdte
Het proces geldt voor iedere wijziging in de productieomgeving van PlanGrip, PlanGrip Veld en PlanGrip Insights, waaronder: applicatiecode, databaseschema en -migraties, infrastructuur en configuratie bij Wolkenrand Hosting, rechten- en autorisatiemodellen, koppelingen met subverwerkers (zoals Dendra AI) en certificaten. Het geldt voor alle developers, inclusief freelancers, en voor werkzaamheden van leveranciers die invloed hebben op de productieomgeving.
## 3. Soorten changes
| Type | Omschrijving | Voorbeelden | Goedkeuring | Uitvoermoment |
|---|---|---|---|---|
| Standaard | Vooraf goedgekeurde, laag-risico wijziging met vaste werkwijze | Tekstwijzigingen, feature flags aan of uit, afhankelijkheden met patch-versie | Code review (four-eyes) | Doordeweeks 09:00–16:00, niet op vrijdag |
| Normaal | Iedere wijziging die geen standaard- of spoedchange is | Nieuwe functionaliteit, wijzigingen in rechten of exportfuncties, API-wijzigingen | Code review plus Change Advisory | Volgens releasekalender |
| Hoog risico | Normale change met grote impact of beperkte omkeerbaarheid | Databasemigraties met schemawijziging of datatransformatie, infrastructuurwijzigingen, wijzigingen in authenticatie of SSO | Code review, Change Advisory en akkoord CTO | Uitsluitend in het onderhoudsvenster zaterdag 22:00–06:00, na aankondiging |
| Spoed | Wijziging die direct nodig is om een incident op te lossen of een kritiek beveiligingslek te dichten | Hotfix bij P1-incident, patch van een actief misbruikte kwetsbaarheid | Akkoord CTO of security officer (mondeling, achteraf vastgelegd) plus review door tweede developer | Direct |
## 4. Rollen
| Activiteit | Developer (indiener) | Reviewer (tweede developer) | Bas Hoekwater | Ruben Okkersen | Sem Loonstra | Lieke Dorrestein |
|---|---|---|---|---|---|---|
| Change request opstellen | R | – | C | I | – | – |
| Code review en review migratiescript | C | R | C | – | – | – |
| Privacy- en securityreview (indien van toepassing) | C | – | R | – | – | R |
| Change Advisory-bespreking | R | C | A/R | C | C | C |
| Akkoord hoog-risico-change | – | – | R | A | I | – |
| Aankondiging aan klanten | – | – | C | – | A/R | – |
| Uitvoering en monitoring | R | R (meekijken) | A | I | I | – |
| Rollbackbesluit | C | C | A/R | I | I | – |
| Post-implementatiereview | R | C | A | I | – | – |
R = uitvoerend, A = eindverantwoordelijk, C = geraadpleegd, I = geïnformeerd.
## 5. Processtappen
### Stap 1 – Change request
De indiener maakt in het ticketsysteem van het developmentteam een change request aan, gekoppeld aan de pull request. Verplichte velden: omschrijving en reden, type change, getroffen componenten en klanten, risico-inschatting (hoog, midden, laag), testbewijs, rollbackplan, verwachte duur en eventuele downtime, en of persoonsgegevens, rechten, export- of deelfuncties of subverwerkers worden geraakt.
### Stap 2 – Four-eyes review
Geen enkele wijziging gaat naar productie zonder goedkeuring van ten minste één andere developer dan de indiener. De main-branch is technisch afgeschermd: mergen zonder goedgekeurde review is niet mogelijk, ook niet voor beheerders. Bij databasemigraties beoordeelt de reviewer naast de code ook het migratiescript, het rollbackscript en de testresultaten op de productiekopie. Voor migraties is de reviewer bij voorkeur Marit Holtrop of Bas Hoekwater. Werk van freelance developers wordt altijd beoordeeld door een developer in loondienst.
### Stap 3 – Privacy- en securityreview
Raakt de wijziging persoonsgegevens, autorisatie, export- of deelfuncties, logging, SSO of een subverwerker, dan beoordelen Bas Hoekwater en Lieke Dorrestein de change vóór de Change Advisory. Zij toetsen onder meer privacy by default (artikel 25 AVG), de noodzaak van een DPIA of aanpassing ervan, en de gevolgen voor de subverwerkerslijst en verwerkersovereenkomsten. Deze stap is ingevoerd na het datalek van juni 2025 en blijft ongewijzigd.
### Stap 4 – Change Advisory
De Change Advisory komt iedere dinsdag om 11:00 uur bijeen (30 minuten), voorgezeten door Bas Hoekwater, met Ruben Okkersen of diens vervanger, de indieners, een vertegenwoordiger van Customer Success (Sem Loonstra) en, voor changes met privacy-impact, Lieke Dorrestein. De Change Advisory beoordeelt alle normale en hoog-risico-changes voor de komende release en besluit tot goedkeuring, aanhouden of afwijzen. Besluiten worden vastgelegd in het change request. Hoog-risico-changes vereisen daarnaast expliciet akkoord van Ruben Okkersen.
### Stap 5 – Testen en acceptatie
Iedere change doorloopt de geautomatiseerde testsuite en wordt gedeployed op de acceptatieomgeving. Aanvullend voor databasemigraties:
- uitvoering op een geanonimiseerde kopie van de productiedatabase met volledig datavolume, met gemeten doorlooptijd;
- uitvoering van het rollbackscript op dezelfde kopie, met controle dat de applicatie daarna correct werkt;
- migraties die langer dan 10 minuten duren of tabellen vergrendelen, worden opgeknipt of als online migratie uitgevoerd;
- schemawijzigingen worden in principe "expand and contract" uitgevoerd: eerst toevoegen, dan code aanpassen, pas in een latere release oude kolommen of tabellen verwijderen.
### Stap 6 – Rollbackplan
Iedere normale en hoog-risico-change heeft een rollbackplan met: de concrete rollbackstappen, de maximale tijd tot rollback, het beslismoment (go/no-go-criteria) en wie beslist. Hoofdregel: is een hoog-risico-change 30 minuten na de geplande eindtijd niet succesvol afgerond of zijn de controles na livegang niet groen, dan wordt teruggedraaid. Vóór iedere hoog-risico-change wordt een verse, geverifieerde back-up of snapshot gemaakt, en wordt vastgesteld hoe lang een volledige restore duurt. "Vooruit fixen" in plaats van terugdraaien mag alleen na expliciet akkoord van Bas Hoekwater en binnen het tijdvenster.
### Stap 7 – Aankondiging
Gepland onderhoud met mogelijke onbeschikbaarheid wordt ten minste vijf werkdagen vooraf via het supportportaal en per e-mail aan klantbeheerders aangekondigd (artikel 1.2 sub a en artikel 5 van de standaard-SLA). Merkbare functionele wijzigingen worden in de release notes opgenomen; wezenlijke wijzigingen in functionaliteit worden 30 dagen vooraf aangekondigd (artikel 1.3 SaaS-overeenkomst). Sem Loonstra is verantwoordelijk voor de communicatie.
### Stap 8 – Uitvoering
Hoog-risico-changes worden uitgevoerd door twee personen tegelijk (uitvoerder en meekijker), volgens een vooraf vastgelegd draaiboek, met een open verbinding naar de dienstdoende van Wolkenrand Hosting als infrastructuur wordt geraakt. Tijdens de uitvoering wordt een tijdlijn bijgehouden. Na afronding voeren beiden de afgesproken controles uit (smoke tests, monitoring, foutpercentages).
### Stap 9 – Post-implementatiereview
Binnen vijf werkdagen na iedere hoog-risico-change, iedere spoedchange en iedere change die tot een incident leidde, vindt een korte review plaats. Bevindingen gaan naar de verbeterlijst van het ISMS.
## 6. Releasekalender en freeze
- Reguliere releases: tweewekelijks op dinsdag, deployment tussen 10:00 en 12:00 uur, zodat het hele team beschikbaar is.
- Hoog-risico-changes: uitsluitend in het onderhoudsvenster op zaterdag 22:00–06:00 uur, met twee developers en Bas Hoekwater of Ruben Okkersen bereikbaar.
- Geen releases op vrijdag, op de dag vóór een feestdag of in de laatste twee weken van december (change freeze, behoudens spoedchanges).
- Bij een go-live van een Enterprise-klant geldt in de betreffende week geen hoog-risico-change zonder overleg met Customer Success.
## 7. Checklist hoog-risico-change
- change request volledig en gekoppeld aan pull request;
- review door tweede developer, inclusief migratie- en rollbackscript;
- test op geanonimiseerde productiekopie met volledig datavolume uitgevoerd, doorlooptijd bekend;
- rollback getest en gedocumenteerd, go/no-go-criteria vastgelegd;
- verse back-up of snapshot gemaakt en restoretijd bekend;
- akkoord Change Advisory en CTO vastgelegd;
- klanten ten minste vijf werkdagen vooraf geïnformeerd;
- uitvoerder en meekijker ingeroosterd, Wolkenrand op de hoogte;
- statuspagina klaargezet;
- post-implementatiereview ingepland.
## 8. Maatregelen uit de evaluatie van de storing van maart 2026
| Maatregel | Eigenaar | Status april 2026 |
|---|---|---|
| Afgeschermde main-branch, merge alleen na review | Bas Hoekwater | Gereed |
| Verplichte test op productiekopie voor migraties | Marit Holtrop | Gereed |
| Rollbackplan als verplicht veld in change request | Bas Hoekwater | Gereed |
| Hoog-risico-changes alleen in onderhoudsvenster | Ruben Okkersen | Gereed |
| Publieke statuspagina voor klanten | Sem Loonstra | Gereed |
| Restoretest volledige productiedatabase per kwartaal | Bas Hoekwater | Eerste test gepland mei 2026 |
| Herziening calamiteitenplan en bereikbaarheidsdienst | Bas Hoekwater | In uitvoering |
## 9. Samenhangende documenten
- Service Level Agreement PlanGrip – Bouwgroep Hazelaar (2 september 2024), artikelen 1, 3, 4 en 5;
- Inkoopovereenkomst hostingdiensten Wolkenrand Hosting (8 mei 2023), kenmerk NOV-INK-2023-004;
- Procedure datalekken en beveiligingsincidenten (versie 2.0, augustus 2025);
- Pentestrapport Schildwacht Security B.V. (9 februari 2026);
- Aansprakelijkstelling Bouwgroep Hazelaar B.V. (18 maart 2026).
## Versiehistorie
| Versie | Datum | Auteur | Wijzigingen |
|---|---|---|---|
| 1.0 | juni 2024 | Ruben Okkersen | Eerste beschrijving releaseproces |
| 2.0 | september 2025 | Bas Hoekwater | Privacy- en securityreview toegevoegd na het datalek van juni 2025; four-eyes voor wijzigingen in rechten en exportfuncties |
| 3.0 | april 2026 | Bas Hoekwater, Ruben Okkersen | Volledige herziening na de storing van 3–4 maart 2026 (databasemigratie): four-eyes voor alle changes, Change Advisory, categorie hoog risico, verplicht en getest rollbackplan, test op productiekopie, releasekalender en freeze |
