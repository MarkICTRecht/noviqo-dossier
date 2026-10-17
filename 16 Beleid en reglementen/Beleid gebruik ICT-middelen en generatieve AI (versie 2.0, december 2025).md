# BELEID GEBRUIK ICT-MIDDELEN EN GENERATIEVE AI
_kenmerk NOV-POL-2025-007 – versie 2.0, december 2025_

| Documentgegevens | |
|---|---|
| Kenmerk | NOV-POL-2025-007 |
| Eigenaar | Bas Hoekwater, DevOps lead & security officer (eigenaar ISMS) |
| Medeauteur | Lieke Dorrestein, Legal & privacy officer |
| Vastgesteld door | Bestuur (F.A. van Dalsem en R.J. Okkersen) |
| Datum vaststelling | 8 december 2025 |
| Ingangsdatum | 1 januari 2026 |
| Versie | 2.0 (vervangt versie 1.0 van oktober 2024) |
| Volgende review | december 2026, of eerder bij wijziging van wetgeving of van goedgekeurde AI-tools |
| Geldt voor | Werknemers, stagiairs en freelancers met een Noviqo-account |

## 1. Waarom dit beleid
1.1 Noviqo is een softwarebedrijf: onze laptops, accounts en code zijn het fundament van wat we leveren. Tegelijk verwerken we in PlanGrip gegevens van ongeveer tweehonderd klanten en tienduizenden van hun medewerkers. Dit beleid regelt hoe je ICT-middelen gebruikt, welke AI-tools je mag inzetten en hoe Noviqo toezicht houdt.
1.2 Nieuw in versie 2.0: een volledig hoofdstuk over generatieve AI (hoofdstuk 4), de verplichte AI-geletterdheid (hoofdstuk 5) en een herzien hoofdstuk over controle en monitoring (hoofdstuk 6). Aanleiding is het groeiend gebruik van AI-tools in ons team, de inwerkingtreding van artikel 4 van de AI-verordening per 2 februari 2025 en de ontwikkeling van PlanGrip Insights.
1.3 Dit beleid geeft invulling aan het instructierecht van Noviqo (artikel 7:660 BW), aan de beveiligingsplicht van artikel 32 AVG en aan de afspraken in onze verwerkersovereenkomsten met klanten.

## 2. Algemene regels voor ICT-middelen
2.1 Je krijgt een Noviqo-laptop, een account voor e-mail en kantoorsoftware, Slack, de wachtwoordmanager en, afhankelijk van je functie, toegang tot de code-repository, het ticketsysteem van Ticketvlinder, het CRM van Klantloep en de beheeromgeving bij Wolkenrand Hosting.
2.2 Accounts zijn persoonlijk. Je deelt nooit je wachtwoord of MFA-code, ook niet met een collega of met "de helpdesk" die je belt. Noviqo vraagt je nooit om je wachtwoord.
2.3 Wachtwoorden: minimaal 14 tekens, uniek per dienst, opgeslagen in de wachtwoordmanager van Noviqo. Multifactorauthenticatie is verplicht op alle diensten die het ondersteunen.
2.4 Software installeer je alleen uit de goedgekeurde catalogus in de beheerapp. Browserextensies vallen hier ook onder: veel extensies kunnen alles lezen wat je in je browser ziet, inclusief klantdata in PlanGrip.
2.5 Updates installeer je binnen vijf werkdagen nadat de beheerapp erom vraagt. Kritieke beveiligingsupdates worden automatisch geforceerd.
2.6 USB-sticks en externe schijven gebruik je niet voor klantdata of broncode. Bestanden delen gaat via de gedeelde schijf of de repository.
2.7 Privégebruik van de laptop, e-mail en internet is in beperkte mate toegestaan (zie Personeelshandboek, hoofdstuk 8). Niet toegestaan zijn in elk geval: het downloaden of verspreiden van illegale of aanstootgevende inhoud, cryptomining, het omzeilen van beveiligingsmaatregelen en het gebruik van je Noviqo-account voor privéaccounts bij webdiensten.
2.8 Productiedata blijft in productie. Voor ontwikkel- en testwerk gebruik je synthetische of geanonimiseerde testdata. Een kopie van productiedata naar een ontwikkelomgeving of je laptop is verboden, tenzij Bas Hoekwater daarvoor vooraf schriftelijk toestemming geeft voor een specifiek incident.

## 3. E-mail, Slack en bestanden
3.1 Zakelijke communicatie loopt via je Noviqo-mailbox en Slack, niet via privé-WhatsApp of privémail. Afspraken met klanten die je via een ander kanaal maakt, leg je vast in het CRM.
3.2 Stuur persoonsgegevens van klanten (zoals exports uit PlanGrip) niet als bijlage per e-mail. Gebruik de beveiligde deelfunctie met een verloopdatum van maximaal zeven dagen.
3.3 Kanalen in Slack met klantinformatie zijn privé. Deel geen inloggegevens of API-sleutels in Slack; daarvoor gebruik je de gedeelde kluis in de wachtwoordmanager.
3.4 Gegevens bewaar je niet langer dan nodig. Zie het Bewaarbeleid documenten en gegevens voor de termijnen.

## 4. Generatieve AI
### 4.1 Uitgangspunt
4.1.1 Generatieve AI kan ons werk sneller en beter maken: een eerste opzet van een e-mail, het uitleggen van een foutmelding, het schrijven van unittests. Tegelijk kunnen AI-tools gegevens bewaren, gebruiken voor training of opslaan buiten de EER, en geven ze soms met grote stelligheid onjuiste antwoorden. Daarom gelden de volgende regels.
### 4.2 Goedgekeurde AI-tools
4.2.1 Je mag uitsluitend de volgende AI-tools voor werk gebruiken, en alleen via je Noviqo-account:
| Tool | Toegestaan voor | Toegestane gegevens | Bijzonderheden |
|---|---|---|---|
| Noviqo Assistent (interne chatomgeving op basis van de API van Dendra AI) | Teksten, samenvattingen, analyse, vertalingen | Interne informatie, inclusief vertrouwelijke bedrijfsinformatie; zakelijke contactgegevens. Géén klantdata uit PlanGrip | Zakelijke API onder de Enterprise Services Agreement van 3 november 2025; geen training op invoer; logging 30 dagen |
| Code-assistent in de ontwikkelomgeving (Business-licentie, beheerd door Bas Hoekwater) | Code-suggesties, uitleg, tests | Broncode van PlanGrip | Training op onze code uitgeschakeld; geen productiedata of secrets in prompts |
| AI-functies in onze kantoorsoftware (zakelijke tenant) | Notulen, samenvatten van documenten | Interne documenten | Transcriptie van vergaderingen alleen met vooraf gemelde toestemming van alle deelnemers |
4.2.2 Wil je een andere AI-tool gebruiken, dan dien je een aanvraag in via het formulier "nieuwe tool" in Ticketvlinder. Bas Hoekwater beoordeelt de beveiliging, Lieke Dorrestein de privacy- en contractuele aspecten (verwerkersovereenkomst, doorgifte buiten de EER, gebruiksvoorwaarden). Een besluit volgt binnen tien werkdagen.
### 4.3 Verboden invoer
4.3.1 In publieke of niet-goedgekeurde AI-tools (zoals gratis consumentenversies van chatbots, AI-vertaalsites en browserextensies met AI-functies) voer je nooit in:
- **klantdata**: gegevens die klanten in PlanGrip hebben ingevoerd, exports, screenshots, supporttickets met namen van medewerkers van klanten;
- **broncode** van PlanGrip, configuratiebestanden, infrastructuurscripts en databaseschema's;
- **secrets**: wachtwoorden, API-sleutels, tokens, certificaten;
- **personeelsgegevens**: beoordelingen, verzuim, salarissen, sollicitatiegegevens;
- **strikt vertrouwelijke bedrijfsinformatie**: financiële cijfers, investeerdersdocumenten, contracten, pentestrapporten.
4.3.2 Ook in de goedgekeurde tools voer je geen bijzondere persoonsgegevens (zoals gezondheidsgegevens of verzuimnotities) in, en geen gegevens uit PlanGrip-klantomgevingen. Het verwerken van klantdata met AI gebeurt uitsluitend binnen het product PlanGrip Insights, onder de afspraken die we daarvoor met klanten maken.
4.3.3 Voorbeeld: je krijgt een supportticket van een klant met een foutmelding en een tabel met planningsregels van zijn medewerkers. Je mag de foutmelding (zonder namen) aan de code-assistent voorleggen. De tabel met medewerkers plak je nergens in.
### 4.4 Gebruik van AI-output
4.4.1 Jij blijft verantwoordelijk voor alles wat je met behulp van AI maakt. Controleer feiten, cijfers, juridische verwijzingen en code op juistheid voordat je die gebruikt.
4.4.2 AI-gegenereerde code doorloopt dezelfde code review als alle andere code. Let extra op beveiligingsfouten, verouderde libraries en code die opvallend veel lijkt op bestaande open-sourcecode met een beperkende licentie.
4.4.3 Teksten voor klanten (offertes, juridische correspondentie, release notes) die substantieel met AI zijn opgesteld, laat je door een collega meelezen. Juridische teksten leg je voor aan Lieke.
4.4.4 Je gebruikt AI niet om beslissingen over mensen te nemen of voor te bereiden, zoals het beoordelen van sollicitanten, het rangschikken van cv's of het beoordelen van functioneren.
### 4.5 PlanGrip Insights
4.5.1 Voor de ontwikkeling en het beheer van PlanGrip Insights, waarin wij zelf AI aanbieden aan klanten, gelden aanvullende eisen uit het productontwikkelingsproces, waaronder een gegevensbeschermingseffectbeoordeling, een beoordeling van de risicoklasse onder de AI-verordening en transparantie richting gebruikers. Die eisen vallen buiten dit beleid; eigenaar is de CTO.

## 5. AI-geletterdheid
5.1 Sinds 2 februari 2025 moeten aanbieders en gebruiksverantwoordelijken van AI-systemen op grond van artikel 4 van de AI-verordening (Verordening (EU) 2024/1689) maatregelen nemen om, zoveel als mogelijk, te zorgen voor een toereikend niveau van AI-geletterdheid bij hun personeel en anderen die namens hen AI-systemen gebruiken. Noviqo is beide: we gebruiken AI-tools intern en bieden met PlanGrip Insights zelf een AI-systeem aan.
5.2 Daarom geldt:
- iedere medewerker volgt vóór 1 maart 2026 de interne e-learning "AI bij Noviqo" (circa 90 minuten): werking en beperkingen van taalmodellen, hallucinaties, bias, privacy en dit beleid;
- developers, de DevOps lead, Customer Success en Sales volgen daarnaast een workshop van een halve dag over PlanGrip Insights: hoe het model werkt, wat het wel en niet kan voorspellen, en hoe je klanten daarover eerlijk informeert;
- nieuwe medewerkers volgen de e-learning binnen vier weken na indiensttreding; freelancers met toegang tot onze code of AI-tools ook;
- Yara Mollinga registreert de deelname; de registratie dient als onderbouwing richting klanten, auditors en toezichthouders.
5.3 De e-learning en workshop worden jaarlijks geactualiseerd door Lieke Dorrestein en Ruben Okkersen en tellen niet mee voor je persoonlijke opleidingsbudget.

## 6. Controle en monitoring
6.1 Noviqo heeft een gerechtvaardigd belang (artikel 6 lid 1 onder f AVG) bij het beveiligen van systemen en klantdata, en houdt daarom beperkt toezicht. Monitoring moet noodzakelijk en proportioneel zijn en mag niet verder gaan dan voor dat doel nodig is. We houden ons aan de AVG, de rechtspraak over privacy op de werkvloer (waaronder het Bărbulescu-arrest van het EHRM) en de richtsnoeren van de Autoriteit Persoonsgegevens.
6.2 Wat we standaard loggen:
- inlogpogingen, toegang tot productieomgevingen en beheerhandelingen (auditlogs), bewaartermijn twaalf maanden;
- toegang van medewerkers tot klantomgevingen in PlanGrip (wie, wanneer, welke klant, met welk ticketnummer), bewaartermijn twaalf maanden;
- de beveiligingsstatus van laptops via de beheerapp (versleuteling, updates, antivirus), niet de inhoud van je bestanden of je browsegeschiedenis;
- verbindingen naar bekende kwaadaardige domeinen;
- in de Noviqo Assistent: prompts en antwoorden gedurende 30 dagen, uitsluitend toegankelijk voor Bas Hoekwater bij een beveiligingsincident.
6.3 Wat we niet doen: toetsaanslagen registreren, schermafbeeldingen maken, webcams of microfoons gebruiken voor toezicht, de locatie van je laptop of telefoon volgen (behalve op jouw verzoek bij verlies of diefstal), of de inhoud van je e-mail en Slack-berichten structureel meelezen.
6.4 Gericht onderzoek. Alleen bij een concreet vermoeden van ernstig misbruik, een beveiligingsincident of een strafbaar feit kan Noviqo gericht onderzoek doen naar het gebruik van ICT-middelen door een individuele medewerker, inclusief inzage in zakelijke e-mail of logs. Daarvoor geldt:
- het besluit wordt genomen door de CEO samen met Lieke Dorrestein, en schriftelijk vastgelegd met de reden, de reikwijdte en de duur;
- we kiezen het minst ingrijpende middel en beperken ons tot zakelijke communicatie; berichten in een als privé herkenbare map of met een duidelijk privékarakter worden niet ingezien;
- de betrokken medewerker wordt geïnformeerd zodra dat het onderzoek niet meer schaadt, en krijgt de gelegenheid te reageren;
- onderzoeksgegevens worden niet langer bewaard dan nodig, en uiterlijk vier weken na afronding van het onderzoek vernietigd, tenzij ze nodig zijn voor een maatregel of procedure.
6.5 Medezeggenschap. Noviqo heeft geen ondernemingsraad of personeelsvertegenwoordiging; daartoe is zij met minder dan vijftig werknemers niet verplicht. Dit beleid, en in het bijzonder hoofdstuk 6, is als concept op 18 november 2025 besproken in de personeelsvergadering (artikel 35b WOR). Opmerkingen daaruit zijn verwerkt, onder meer de beperking van de logging van de Noviqo Assistent tot 30 dagen. Bij een toekomstige ondernemingsraad worden wijzigingen in dit hoofdstuk ter instemming voorgelegd (artikel 27 lid 1 onder l WOR).
6.6 Voor de logging en het onderzoek is een gegevensbeschermingseffectbeoordeling uitgevoerd op hoofdlijnen (vastgelegd door Lieke Dorrestein, november 2025). De verwerkingen zijn opgenomen in het verwerkingsregister.

## 7. Incidenten en verlies
7.1 Elk vermoeden van een beveiligingsincident meld je direct in #security-incidenten of telefonisch bij Bas Hoekwater: een verloren laptop, een phishingmail waarop je hebt geklikt, klantdata die per ongeluk in een AI-tool is beland, een deellink naar de verkeerde ontvanger. Een snelle melding is altijd beter dan een perfecte melding.
7.2 Een melding van een eigen fout wordt niet bestraft. Wie een incident verzwijgt, handelt in strijd met de Gedragscode medewerkers.

## 8. Einde dienstverband
8.1 Op je laatste werkdag lever je alle ICT-middelen in en worden je accounts geblokkeerd. Je zakelijke mailbox wordt na uitdiensttreding één maand doorgestuurd naar je leidinggevende, met een automatisch antwoord, en daarna verwijderd conform het Bewaarbeleid documenten en gegevens. Privébestanden kopieer je vóór je laatste werkdag zelf naar een eigen medium, in aanwezigheid van Bas of Yara.

## 9. Naleving
9.1 Overtreding van dit beleid kan leiden tot maatregelen volgens de Gedragscode medewerkers, waaronder intrekking van toegangsrechten en, in ernstige gevallen, ontslag. Het invoeren van klantdata of broncode in een publieke AI-tool beschouwen wij als een ernstige overtreding.
9.2 Vragen over dit beleid stel je in #security of aan Bas Hoekwater en Lieke Dorrestein.

## 10. Versiehistorie
| Versie | Datum | Wijziging | Door |
|---|---|---|---|
| 1.0 | oktober 2024 | Eerste versie: gebruik laptop, e-mail, internet, wachtwoorden | B. Hoekwater |
| 1.1 | juli 2025 | Regels voor deellinks en exports aangescherpt (paragraaf 3.2) | B. Hoekwater, L. Dorrestein |
| 2.0 | december 2025 | Nieuwe hoofdstukken generatieve AI en AI-geletterdheid; hoofdstuk monitoring herzien na bespreking personeelsvergadering 18 november 2025; titel gewijzigd | B. Hoekwater, L. Dorrestein |
