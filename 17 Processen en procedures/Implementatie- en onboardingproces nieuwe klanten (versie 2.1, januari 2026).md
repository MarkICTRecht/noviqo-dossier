# IMPLEMENTATIE- EN ONBOARDINGPROCES NIEUWE KLANTEN
_kenmerk NOV-PRC-2026-001 – versie 2.1 – januari 2026_
## Documentgegevens
| Onderdeel | Gegevens |
|---|---|
| Documenteigenaar | Sem Loonstra, Customer Success lead |
| Betrokken afdelingen | Sales, Customer Success, Development/DevOps, Legal, Finance |
| Vastgesteld door | F.A. van Dalsem, CEO |
| Versie | 2.1 |
| Datum vaststelling | 12 januari 2026 |
| Volgende review | januari 2027 |
| Classificatie | Intern |
## 1. Doel
Dit proces beschrijft hoe Noviqo B.V. (hierna: Noviqo) een nieuwe klant van ondertekend contract naar zelfstandig gebruik van PlanGrip brengt. Doel is een voorspelbare implementatie, een snelle "time to value" en het voorkomen van fouten aan de voorkant die later tot supportdruk, ontevredenheid of privacyrisico's leiden. Belangrijke les uit 2025 is dat gegevens pas mogen worden geïmporteerd als de contractuele en privacyrandvoorwaarden rond zijn, en dat klantbeheerders bij de start goed worden geïnstrueerd over rechten, deelfuncties en het vastleggen van afwezigheid.
## 2. Reikwijdte
Het proces geldt voor alle nieuwe klanten op de abonnementen Teams en Enterprise en voor bestaande klanten die de module PlanGrip Insights gaan gebruiken. Start-klanten die via de webshop instromen, krijgen het geautomatiseerde onboardingtraject (paragraaf 7). Voor klanten van reseller Cijferkrans ICT B.V. voert de reseller de eerstelijns onboarding uit; Noviqo blijft verantwoordelijk voor technische inrichting, SSO en de verwerkersovereenkomst.
## 3. Implementatiepakketten
| Abonnement | Standaardpakket | Inbegrepen uren | Doorlooptijd richtlijn |
|---|---|---|---|
| Start | Zelfstandige onboarding met e-mailreeks en webinar | 0 | 1 week |
| Teams | Kick-off, inrichting, één beheerderstraining, één gebruikerstraining | 8 uur | 3 tot 4 weken |
| Enterprise | Projectplan, SSO-koppeling, datamigratie, trainingsprogramma, hypercare | Volgens offerte | 6 tot 12 weken |
| Insights-add-on | Datakwaliteitscheck, activatie, training planners | 4 uur | 2 weken |
Uren boven het pakket worden gefactureerd tegen € 145 per uur exclusief btw, na schriftelijk akkoord van de klant op een urenraming.
## 4. Rollen
| Activiteit | Account manager | Sem Loonstra (CS) | Implementatieconsultant CS | Bas Hoekwater | Lieke Dorrestein | Iris Wapperom |
|---|---|---|---|---|---|---|
| Overdrachtsnotitie Sales naar CS | R | A | I | – | I | I |
| Controle randvoorwaarden (fase 0) | C | A | R | C | R | R |
| Kick-off en projectplan | C | A | R | – | – | – |
| Technische inrichting en SSO | – | A | C | R | – | – |
| Datamigratie | – | A | R | C | C | – |
| Trainingen | – | A | R | – | – | – |
| Go-live-besluit | I | A/R | R | C | – | I |
| Hypercare en overdracht naar support | I | A | R | C | – | – |
| Facturatie implementatie-uren | – | C | C | – | – | A/R |
R = uitvoerend, A = eindverantwoordelijk, C = geraadpleegd, I = geïnformeerd.
## 5. Fasen en stappen
### Fase 0 – Randvoorwaarden (binnen 3 werkdagen na ondertekening)
Stap 0.1 – De account manager levert de overdrachtsnotitie in Klantloep CRM aan (zie Contractmanagementproces van offerte tot verlenging, stap 5).
Stap 0.2 – De implementatieconsultant controleert met de checklist in paragraaf 8 of aan alle randvoorwaarden is voldaan. Harde voorwaarden vóór het importeren van persoonsgegevens: de SaaS-overeenkomst en de verwerkersovereenkomst zijn door beide partijen getekend; de klant heeft de actuele subverwerkerslijst ontvangen; en de contactpersonen voor privacy en datalekken zijn bekend.
Stap 0.3 – Neemt de klant PlanGrip Insights af, dan bevestigt Lieke Dorrestein dat de klant is geïnformeerd over de inzet van Dendra AI Inc. als subverwerker (doorgifte naar de Verenigde Staten op basis van het EU-US Data Privacy Framework met standaardcontractbepalingen als terugval) en daarmee heeft ingestemd conform de verwerkersovereenkomst. Zonder die bevestiging wordt Insights niet geactiveerd.
Stap 0.4 – Iris Wapperom controleert of de eerste abonnementsfactuur is verstuurd.
### Fase 1 – Kick-off (week 1)
Stap 1.1 – De implementatieconsultant plant binnen vijf werkdagen na ondertekening een kick-off van 90 minuten (Enterprise: halve dag, bij voorkeur op locatie).
Stap 1.2 – Agenda: doelen van de klant, planningsprocessen en -ritme, organisatiestructuur (vestigingen, teams, rollen), bestaande planningstools en data, gewenste koppelingen, rechtenstructuur, trainingsbehoefte en de go-live-datum.
Stap 1.3 – Binnen twee werkdagen na de kick-off ontvangt de klant een projectplan met mijlpalen, verantwoordelijken aan beide kanten en een urenraming voor werk buiten het pakket.
### Fase 2 – Inrichting (week 1 tot 3)
Stap 2.1 – De implementatieconsultant maakt de omgeving aan, richt organisatie-eenheden, projecttypen, vaardigheden en capaciteitsregels in, en maakt de klantbeheerders aan.
Stap 2.2 – Rechtenstructuur: standaard krijgen alleen klantbeheerders exportrechten; deelfuncties worden niet geactiveerd voor externe partijen tenzij de klant daar schriftelijk om vraagt. Exportlinks hebben een verloopdatum van 7 dagen en werken alleen voor ingelogde gebruikers van de eigen organisatie.
Stap 2.3 – Enterprise met SSO: Bas Hoekwater of een door hem aangewezen developer configureert de SAML- of OIDC-koppeling met de identity provider van de klant, test met twee testaccounts van de klant en zet daarna lokale wachtwoordlogin uit voor alle gebruikers behalve één noodbeheerder.
Stap 2.4 – Afwezigheidsregistratie: de consultant adviseert de klant om in PlanGrip uitsluitend "afwezig" of een neutrale afwezigheidscategorie te gebruiken en géén medische informatie vast te leggen. De waarschuwing bij het notitieveld blijft aan.
### Fase 3 – Datamigratie (week 2 tot 4)
Stap 3.1 – De klant levert data aan via het importsjabloon (CSV) in de beveiligde uploadomgeving van PlanGrip. Data per e-mail of via externe deelplatforms wordt niet geaccepteerd; ontvangen bestanden worden verwijderd en de klant wordt gevraagd de upload opnieuw via de juiste route te doen.
Stap 3.2 – De consultant voert eerst een proefimport uit in de acceptatieomgeving. De klant controleert steekproefsgewijs en geeft schriftelijk akkoord.
Stap 3.3 – Na akkoord volgt de productie-import. Importbestanden worden binnen 14 dagen na de productie-import uit de uploadomgeving verwijderd.
Stap 3.4 – Voor Insights: de consultant controleert of minimaal zes maanden historische planningsdata beschikbaar is; anders wordt de klant geïnformeerd dat voorspellingen in de eerste maanden minder betrouwbaar zijn.
### Fase 4 – Training (week 3 tot 5)
| Training | Doelgroep | Duur | Vorm |
|---|---|---|---|
| Beheerderstraining | Klantbeheerders | 3 uur | Online of op locatie |
| Plannerstraining | Planners en teamleiders | 2 uur | Online |
| Veld-instructie | Buitendienstmedewerkers (PlanGrip Veld) | 30 minuten | Video en handleiding |
| Insights-training | Planners en management | 1,5 uur | Online |
In de beheerderstraining komen verplicht aan bod: gebruikersbeheer en het tijdig deactiveren van vertrokken medewerkers, rechten en exportfuncties, de afhandeling van verzoeken van betrokkenen (de klant is verwerkingsverantwoordelijke; zie Procedure verzoeken van betrokkenen) en hoe de klant een (vermoed) beveiligingsincident bij Noviqo meldt.
### Fase 5 – Go-live (week 4 tot 6)
Stap 5.1 – De implementatieconsultant en de klantbeheerder doorlopen samen de go-live-checklist. Sem Loonstra neemt het go-live-besluit.
Stap 5.2 – Go-live vindt plaats op een dinsdag, woensdag of donderdag, nooit op vrijdag of in de week van een geplande grote release.
Stap 5.3 – De klant ontvangt een go-live-bericht met supportkanalen, het calamiteitennummer voor Prioriteit 1-incidenten (Enterprise) en de link naar de statuspagina.
### Fase 6 – Hypercare en overdracht (30 dagen na go-live)
Stap 6.1 – Gedurende 30 dagen na go-live heeft de klant een vast aanspreekpunt bij Customer Success; vragen worden binnen één werkdag beantwoord.
Stap 6.2 – Na twee en na vier weken volgt een korte check-in. Na 30 dagen een evaluatie met tevredenheidsmeting (score 1 tot 10).
Stap 6.3 – Daarna gaat de klant over naar reguliere support conform de SLA. Enterprise-klanten krijgen een kwartaalreview met Sem Loonstra.
Stap 6.4 – De consultant sluit het project in Klantloep CRM af, met geregistreerde uren; Iris Wapperom factureert meerwerk.
## 6. Prestatie-indicatoren
| Indicator | Norm |
|---|---|
| Kick-off binnen 5 werkdagen na ondertekening | 90% van de klanten |
| Go-live binnen geplande doorlooptijd | 80% van de klanten |
| Tevredenheid na hypercare | Gemiddeld 8 of hoger |
| Actieve gebruikers na 60 dagen | Minimaal 75% van de gecontracteerde gebruikers |
| Imports via een niet-toegestane route | 0 |
## 7. Geautomatiseerde onboarding Start-klanten
Start-klanten ontvangen na aanmelding via de webshop een welkomstmail met verwijzing naar de algemene voorwaarden en de standaard verwerkersovereenkomst (online aanvaard bij aanmelding), een e-mailreeks van vijf berichten in drie weken en een uitnodiging voor het maandelijkse onboardingwebinar. Customer Success belt iedere Start-klant die na 14 dagen nog minder dan drie actieve gebruikers heeft.
## 8. Checklist randvoorwaarden en go-live
- SaaS-overeenkomst getekend en geregistreerd in het contractregister;
- verwerkersovereenkomst getekend, versie subverwerkerslijst vastgelegd;
- bij Insights: instemming klant met Dendra AI als subverwerker vastgelegd;
- contactpersonen privacy en datalekken bekend en in Klantloep CRM ingevoerd;
- eerste factuur verstuurd;
- omgeving ingericht, rechtenstructuur gecontroleerd, exportrechten beperkt tot beheerders;
- SSO getest en lokale login uitgeschakeld (Enterprise);
- proefimport goedgekeurd door klant;
- trainingen gegeven, inclusief verplichte onderdelen beheerderstraining;
- importbestanden ingepland voor verwijdering;
- supportkanalen en calamiteitennummer gecommuniceerd.
## 9. Samenhangende documenten
- Contractmanagementproces van offerte tot verlenging (versie 1.0, september 2025);
- Service Level Agreement PlanGrip (standaard), bijvoorbeeld de SLA met Bouwgroep Hazelaar van 2 september 2024;
- Procedure datalekken en beveiligingsincidenten (versie 2.0, augustus 2025);
- Procedure verzoeken van betrokkenen (versie 1.1, mei 2025);
- Procedure leveranciersbeoordeling en inkoop SaaS-diensten (versie 1.0, oktober 2025), voor de beoordeling van Dendra AI.
## Versiehistorie
| Versie | Datum | Auteur | Wijzigingen |
|---|---|---|---|
| 1.0 | februari 2025 | Sem Loonstra | Eerste versie, opgesteld bij start Customer Success-team |
| 2.0 | september 2025 | Sem Loonstra, Lieke Dorrestein | Fase 0 randvoorwaarden toegevoegd na het datalek van juni 2025; beperking exportrechten; importroute via beveiligde uploadomgeving; verplichte onderdelen beheerderstraining |
| 2.1 | januari 2026 | Sem Loonstra | Onboarding PlanGrip Insights toegevoegd (stap 0.3, stap 3.4, Insights-training) in verband met de lancering op 15 januari 2026; go-live-regels aangescherpt |
