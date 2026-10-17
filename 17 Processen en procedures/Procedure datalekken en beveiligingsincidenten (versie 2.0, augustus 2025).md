# PROCEDURE DATALEKKEN EN BEVEILIGINGSINCIDENTEN
_kenmerk NOV-PRC-2025-005 – versie 2.0 – augustus 2025_
## Documentgegevens
| Onderdeel | Gegevens |
|---|---|
| Documenteigenaar | Bas Hoekwater, DevOps lead & security officer (eigenaar ISMS) |
| Inhoudelijk mede-eigenaar | Lieke Dorrestein, Legal & privacy officer |
| Vastgesteld door | Bestuur (F.A. van Dalsem en R.J. Okkersen) |
| Versie | 2.0 |
| Datum vaststelling | 25 augustus 2025 |
| Ingangsdatum | 1 september 2025 |
| Volgende review | augustus 2026, en in ieder geval na elk incident met prioriteit Hoog of Kritiek |
| Classificatie | Intern |
| Vervangt | Procedure datalekken versie 1.1 (april 2025) |
## 1. Doel
Deze procedure beschrijft hoe Noviqo B.V. (hierna: Noviqo) beveiligingsincidenten en inbreuken in verband met persoonsgegevens (datalekken) herkent, intern meldt, beoordeelt, beperkt, registreert en waar nodig meldt aan klanten, de Autoriteit Persoonsgegevens (AP) en betrokkenen. Doel is dat iedere medewerker weet wat hij moet doen, dat de wettelijke termijn van 72 uur (artikel 33 AVG) en de contractuele meldtermijnen jegens klanten worden gehaald, en dat Noviqo van ieder incident leert.
## 2. Reikwijdte
Deze procedure geldt voor alle medewerkers, stagiairs en ingehuurde krachten (waaronder freelance developers) van Noviqo, en voor alle informatie en systemen die Noviqo beheert of gebruikt, waaronder:
- het platform PlanGrip (webapp en mobiele app PlanGrip Veld) en de onderliggende hostingomgeving bij Wolkenrand Hosting B.V.;
- interne systemen zoals Klantloep CRM, het supportsysteem, de salarisadministratie bij Salariswijs B.V., e-mail en gedeelde opslag;
- laptops, telefoons en papieren dossiers.
De procedure onderscheidt twee rollen, omdat de meldplichten verschillen:
- **Noviqo als verwerker**: voor alle gegevens die klanten in PlanGrip invoeren (planningsgegevens, namen, beschikbaarheid, accountgegevens van medewerkers van de klant). De klant is verwerkingsverantwoordelijke en beslist over melding aan de AP en betrokkenen (zie artikel 7 van de standaard verwerkersovereenkomst, bijvoorbeeld de Verwerkersovereenkomst PlanGrip – Bouwgroep Hazelaar van 2 september 2024).
- **Noviqo als verwerkingsverantwoordelijke**: voor eigen gegevens, zoals personeelsgegevens, sollicitanten, contactpersonen bij klanten en leveranciers, nieuwsbriefabonnees en websitebezoekers (zie Privacyverklaring Noviqo B.V., versie 3.0).
## 3. Definities
- **Beveiligingsincident**: iedere gebeurtenis die de beschikbaarheid, integriteit of vertrouwelijkheid van informatie of systemen van Noviqo (mogelijk) aantast, ongeacht of persoonsgegevens betrokken zijn. Voorbeelden: phishingmail waarop is geklikt, malware, verloren laptop, onbereikbaarheid van PlanGrip.
- **Datalek**: een inbreuk op de beveiliging die per ongeluk of op onrechtmatige wijze leidt tot vernietiging, verlies, wijziging of ongeoorloofde verstrekking van of toegang tot persoonsgegevens (artikel 4 onder 12 AVG).
- **Moment van ontdekking**: het moment waarop een medewerker van Noviqo een redelijke mate van zekerheid heeft dat een incident heeft plaatsgevonden waarbij persoonsgegevens zijn betrokken. Vanaf dit moment loopt de 72-uurstermijn (als Noviqo verwerkingsverantwoordelijke is) respectievelijk de contractuele termijn jegens de klant.
- **Incidentteam**: het team dat het incident behandelt (zie paragraaf 4).
## 4. Rollen en verantwoordelijkheden
Het incidentteam bestaat standaard uit Bas Hoekwater (incidentcoördinator), Lieke Dorrestein (privacybeoordeling en meldingen) en Ruben Okkersen (bestuurlijk eindverantwoordelijk). Bij afwezigheid van Bas Hoekwater neemt Marit Holtrop (senior developer) de coördinatie waar; bij afwezigheid van Lieke Dorrestein neemt Femke van Dalsem de privacybeoordeling waar, zo nodig met ondersteuning van een externe privacyjurist. Sem Loonstra (Customer Success lead) verzorgt de communicatie met klanten.
| Activiteit | Medewerker die ontdekt | Bas Hoekwater | Lieke Dorrestein | Ruben Okkersen | Femke van Dalsem | Sem Loonstra |
|---|---|---|---|---|---|---|
| Interne melding binnen 1 uur | R | I | I | – | – | – |
| Registratie in incidentregister | C | A/R | C | I | – | – |
| Technische analyse en inperking | C | A/R | I | C | – | – |
| Beoordeling datalek en risico (matrix) | – | C | A/R | C | I | – |
| Besluit melding AP (Noviqo als verantwoordelijke) | – | C | R | A | C | – |
| Melding aan klant (Noviqo als verwerker) | – | C | A/R | I | I | R |
| Communicatie met betrokkenen en pers | – | – | C | A | R | C |
| Evaluatie en verbetermaatregelen | C | A/R | R | I | I | C |
R = uitvoerend, A = eindverantwoordelijk, C = geraadpleegd, I = geïnformeerd.
## 5. Stappen en termijnen
### Stap 1 – Melden (binnen 1 uur)
Iedere medewerker die een (mogelijk) beveiligingsincident of datalek opmerkt, meldt dit direct en uiterlijk binnen één uur via securitymeldpunt@noviqo.example én telefonisch of via Slack-kanaal #security-incident bij Bas Hoekwater. Twijfel is geen reden om te wachten: liever tien onterechte meldingen dan één gemiste. Meldingen van klanten via het supportportaal of van leveranciers (Wolkenrand Hosting meldt binnen 24 uur, Klantloep CRM streeft naar 48 uur) worden door de ontvanger op dezelfde wijze doorgezet. Leg vast: wie, wat, wanneer ontdekt, welke systemen en welke klanten mogelijk geraakt zijn. Verwijder geen bestanden of logbestanden en voer geen eigen onderzoek uit buiten wat nodig is om verdere schade te voorkomen.
### Stap 2 – Registreren en classificeren (binnen 4 uur)
De incidentcoördinator registreert het incident in het incidentregister (ISMS-omgeving, tabblad Incidenten) met een uniek nummer in de vorm INC-JJJJ-nnn en stelt een eerste prioriteit vast (Laag, Midden, Hoog, Kritiek). Hij beoordeelt of persoonsgegevens betrokken (kunnen) zijn. Zo ja, dan wordt Lieke Dorrestein direct ingeschakeld en wordt het tijdstip van ontdekking vastgelegd. Vanaf dat moment houdt de incidentcoördinator een tijdlijn bij.
### Stap 3 – Inperken en herstellen (direct, doorlopend)
De incidentcoördinator neemt maatregelen om het lek te dichten en verdere schade te beperken, bijvoorbeeld: intrekken van gedeelde links en tokens, blokkeren van accounts, wijzigen van wachtwoorden, op afstand wissen van een verloren apparaat, terugzetten van een back-up of het tijdelijk uitschakelen van een functie. Alle handelingen worden met tijdstip in het incidentregister vastgelegd. Bewijs (logbestanden, schermafbeeldingen) wordt veiliggesteld en minimaal twaalf maanden bewaard.
### Stap 4 – Beoordelen (binnen 24 uur na ontdekking)
Lieke Dorrestein beoordeelt aan de hand van de beoordelingsmatrix (paragraaf 6) of sprake is van een datalek, welk risico het oplevert voor de rechten en vrijheden van betrokkenen, en welke rol Noviqo heeft (verwerker of verwerkingsverantwoordelijke). De uitkomst en motivering worden vastgelegd in het beoordelingsformulier (paragraaf 8), ook als wordt besloten níet te melden.
### Stap 5a – Noviqo als verwerker: melden aan de klant (uiterlijk binnen 36 uur)
Raakt het datalek gegevens die klanten in PlanGrip hebben ingevoerd, dan informeert Noviqo iedere getroffen klant zonder onredelijke vertraging en uiterlijk binnen de termijn uit de verwerkersovereenkomst met die klant. In de standaard verwerkersovereenkomst is dat 36 uur na ontdekking; afwijkende termijnen zijn vastgelegd in het contractregister in Klantloep CRM en gaan voor. Werkwijze:
- Sem Loonstra stelt vast wie bij de klant de contactpersoon voor datalekken is (Bijlage 1 bij de verwerkersovereenkomst) en belt deze persoon eerst telefonisch;
- Lieke Dorrestein stuurt direct daarna een schriftelijke melding met ten minste de gegevens uit artikel 33 lid 3 AVG: aard van de inbreuk, categorieën en (geschatte) aantallen betrokkenen en registers, waarschijnlijke gevolgen, genomen en voorgestelde maatregelen en een contactpersoon bij Noviqo;
- is nog niet alle informatie beschikbaar, dan wordt toch tijdig gemeld en volgt aanvulling in fasen (artikel 33 lid 4 AVG);
- Noviqo meldt het datalek niet zelfstandig aan de AP of aan betrokkenen. Wil de klant dat Noviqo namens hem meldt of betrokkenen informeert, dan legt Lieke Dorrestein die opdracht schriftelijk (per e-mail) vast vóórdat Noviqo handelt;
- Noviqo verleent de klant bijstand bij diens melding, zoals bedoeld in artikel 6.2 van de verwerkersovereenkomst, en houdt de klant op de hoogte tot het incident is afgesloten.
Zijn meerdere klanten geraakt, dan wordt iedere klant afzonderlijk geïnformeerd, zonder vertrouwelijke gegevens van de andere klanten te delen. Gegevens over de klant bij wie het lek zichtbaar werd, worden alleen gedeeld voor zover nodig.
### Stap 5b – Noviqo als verwerkingsverantwoordelijke: melden aan de AP (binnen 72 uur)
Leidt het datalek waarschijnlijk tot een risico voor de rechten en vrijheden van betrokkenen, dan meldt Lieke Dorrestein het namens Noviqo via het meldloket datalekken van de AP, uiterlijk 72 uur na ontdekking (artikel 33 lid 1 AVG). Het besluit wordt genomen door Ruben Okkersen na advies van Lieke Dorrestein. Het meldnummer van de AP wordt in het incidentregister opgenomen. Een melding na 72 uur bevat een motivering van de vertraging.
### Stap 6 – Informeren van betrokkenen (zo snel mogelijk)
Leidt het datalek waarschijnlijk tot een hoog risico, dan informeert de verwerkingsverantwoordelijke ook de betrokkenen zelf, in duidelijke en eenvoudige taal (artikel 34 AVG). Is Noviqo verantwoordelijke, dan stelt Lieke Dorrestein de tekst op en verstuurt Femke van Dalsem deze. Is Noviqo verwerker, dan doet de klant dit; Noviqo levert op verzoek een concepttekst en de benodigde gegevens. Communicatie met de pers loopt uitsluitend via Femke van Dalsem.
### Stap 7 – Afsluiten en evalueren (binnen 10 werkdagen na herstel)
Na herstel organiseert Bas Hoekwater een evaluatie (blameless post-mortem) met het incidentteam en betrokken medewerkers. Uitkomsten: oorzaakanalyse, verbetermaatregelen met eigenaar en deadline, en zo nodig een aanpassing van deze procedure. De evaluatie wordt gedeeld met de getroffen klanten als die daarom vragen, en ieder kwartaal geagendeerd in het bestuursoverleg.
## 6. Beoordelingsmatrix
De beoordeling vindt plaats op drie factoren. Iedere factor krijgt een score van 1 tot 3; de scores worden opgeteld.
| Factor | Score 1 | Score 2 | Score 3 |
|---|---|---|---|
| A. Aard van de gegevens | Zakelijke contactgegevens, functie, planninggegevens zonder gevoelige toevoegingen | Beschikbaarheid, verlofgegevens, locatiegegevens buitendienst, inloggegevens (gehasht) | Gezondheidsgegevens (verzuimnotities), BSN, financiële gegevens, wachtwoorden in leesbare vorm |
| B. Omvang | Minder dan 10 betrokkenen | 10 tot 250 betrokkenen | Meer dan 250 betrokkenen of meerdere klanten |
| C. Toegankelijkheid en gevolg | Gegevens versleuteld of aantoonbaar niet ingezien; ontvanger betrouwbaar en heeft verwijdering bevestigd | Gegevens ingezien door onbevoegde, maar beperkte verspreiding | Gegevens openbaar, gekopieerd, door kwaadwillende verkregen of niet terug te halen |
Op basis van de totaalscore geldt het volgende.
| Totaalscore | Risico | Melding AP (als verantwoordelijke) | Informeren betrokkenen |
|---|---|---|---|
| 3 – 4 | Geen of laag risico | Niet melden; vastleggen in register (artikel 33 lid 5 AVG) | Nee |
| 5 – 6 | Risico | Melden binnen 72 uur | In beginsel niet; per geval beoordelen |
| 7 – 9 | Hoog risico | Melden binnen 72 uur | Ja, zo snel mogelijk |
Bijzondere regels: is factor A score 3 (bijvoorbeeld een verzuimnotitie "ziek", wat een gezondheidsgegeven is), dan is de uitkomst altijd minimaal "Risico", ongeacht de totaalscore. De matrix ondersteunt het oordeel maar vervangt het niet; Lieke Dorrestein kan gemotiveerd afwijken. Als Noviqo verwerker is, deelt zij de uitkomst als advies met de klant.
## 7. Specifieke maatregelen na het datalek van juni 2025
Naar aanleiding van het datalek van 11 juni 2025 (INC-2025-014), waarbij een gedeelde exportlink zonder verloopdatum planningsgegevens van 63 medewerkers van Bouwgroep Hazelaar B.V., waaronder in vier gevallen een verzuimnotitie, zichtbaar maakte voor een gebruiker van een andere klant, gelden aanvullend:
- exportlinks in PlanGrip hebben standaard een verloopdatum van 7 dagen en zijn alleen toegankelijk voor ingelogde gebruikers van de eigen organisatie (doorgevoerd met hotfix 25.5.3);
- het vrije notitieveld bij afwezigheid toont een waarschuwing dat geen medische informatie mag worden vastgelegd;
- iedere wijziging in deel-, export- of autorisatiefunctionaliteit van PlanGrip doorloopt een verplichte privacy- en securityreview (zie Change- en releasemanagementproces PlanGrip);
- de rolverdeling bij melden is verduidelijkt: Noviqo meldt als verwerker alleen aan de AP na schriftelijke opdracht van de klant. Bij het incident van juni 2025 was dit niet vooraf vastgelegd; de melding aan de AP (meldnummer M-2025-0614-117, gedaan op 14 juni 2025) is na telefonische afstemming met Bouwgroep Hazelaar gedaan;
- alle medewerkers volgen jaarlijks een korte e-learning over deze procedure; nieuwe medewerkers in hun eerste maand (zie Proces in- en uitdiensttreding medewerkers).
## 8. Checklist beoordelingsformulier
Het beoordelingsformulier in het incidentregister bevat ten minste:
- incidentnummer, tijdstip melding en tijdstip ontdekking;
- korte beschrijving van wat er is gebeurd en de oorzaak (voor zover bekend);
- getroffen systemen, klanten en (sub)verwerkers;
- rol van Noviqo: verwerker, verwerkingsverantwoordelijke of beide;
- categorieën persoonsgegevens en betrokkenen, en het (geschatte) aantal;
- scores A, B en C uit de matrix, de totaalscore en de motivering;
- genomen en geplande maatregelen;
- besluit over melding aan klant(en), AP en betrokkenen, met datum, tijdstip en naam van de beslisser;
- meldnummer AP en verzonden berichten (als bijlage);
- datum evaluatie en verbetermaatregelen.
## 9. Termijnenoverzicht
| Handeling | Termijn | Bron |
|---|---|---|
| Interne melding door medewerker | Binnen 1 uur | Deze procedure |
| Registratie en eerste classificatie | Binnen 4 uur | Deze procedure |
| Risicobeoordeling | Binnen 24 uur na ontdekking | Deze procedure |
| Melding aan klant (Noviqo als verwerker) | Uiterlijk 36 uur, tenzij verwerkersovereenkomst korter | Artikel 33 lid 2 AVG; artikel 7.1 standaard verwerkersovereenkomst |
| Melding aan AP (Noviqo als verantwoordelijke) | Uiterlijk 72 uur na ontdekking | Artikel 33 lid 1 AVG |
| Informeren betrokkenen bij hoog risico | Zonder onredelijke vertraging | Artikel 34 AVG |
| Melding door Wolkenrand Hosting aan Noviqo | Uiterlijk 24 uur | Verwerkersovereenkomst Wolkenrand, artikel 7.1 |
| Evaluatie | Binnen 10 werkdagen na herstel | Deze procedure |
## 10. Samenhangende documenten
- Verwerkersovereenkomst PlanGrip – Bouwgroep Hazelaar (2 september 2024) en de standaard verwerkersovereenkomst voor klanten;
- Verwerkersovereenkomst Noviqo – Wolkenrand Hosting (8 mei 2023) en Verwerkersovereenkomst Klantloep CRM – Noviqo (19 februari 2024);
- Privacyverklaring Noviqo B.V. (versie 3.0, januari 2025);
- Procedure verzoeken van betrokkenen (versie 1.1, mei 2025);
- Change- en releasemanagementproces PlanGrip.
## Versiehistorie
| Versie | Datum | Auteur | Wijzigingen |
|---|---|---|---|
| 1.0 | september 2024 | Bas Hoekwater | Eerste versie, gericht op technische incidentafhandeling |
| 1.1 | april 2025 | Lieke Dorrestein | Rol Legal & privacy officer toegevoegd; verwijzing naar privacyverklaring 3.0 |
| 2.0 | augustus 2025 | Bas Hoekwater, Lieke Dorrestein | Volledige herziening naar aanleiding van het datalek van juni 2025 (exportlink, INC-2025-014): onderscheid verwerker/verwerkingsverantwoordelijke, meldflow richting klanten met 36-uurstermijn, beoordelingsmatrix, RACI, specifieke maatregelen exportlinks, vastlegging van opdracht bij melding namens klant |
