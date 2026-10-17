# INCIDENTRAPPORT EN DATALEKREGISTER 2025-2026
_kenmerk NOV-PRV-2026-006 – deel A: incidentrapport datalek 11 juni 2025 – deel B: register van inbreuken (artikel 33 lid 5 AVG)_

## Documentgegevens

| Onderdeel | Gegevens |
|---|---|
| Eigenaar | Lieke Dorrestein, legal & privacy officer |
| Technisch verantwoordelijk | Bas Hoekwater, DevOps lead & security officer |
| Bestuurlijk verantwoordelijk | R.J. Okkersen, bestuurder (CTO) |
| Periode register | 1 januari 2025 tot en met 30 september 2026 |
| Laatste bijwerking | 2 oktober 2026 |
| Vertrouwelijkheid | Vertrouwelijk; deel A is in afgeschermde vorm gedeeld met Bouwgroep Hazelaar B.V. |
| Procedure | Procedure datalekken en beveiligingsincidenten (versie 2.0, augustus 2025); informatiebeveiligingsbeleid NOV-SEC-2026-001 |

## Deel A – Incidentrapport datalek exportlink PlanGrip (11 juni 2025)

### A1. Samenvatting

Op woensdag 11 juni 2025 heeft een gebruiker van Schildersbedrijf Gaasterhof v.o.f. via een gedeelde exportlink planningsgegevens kunnen inzien van 63 medewerkers van Bouwgroep Hazelaar B.V. De link was door een werkvoorbereider van Hazelaar aangemaakt om de projectplanning van één bouwproject met Gaasterhof als onderaannemer te delen. Door een fout in PlanGrip-release 25.5.2 toonde de link niet alleen dat project, maar het volledige medewerkersoverzicht van Hazelaar voor juni en juli 2025. De link had geen verloopdatum.
De inzage betrof naam, functie, beschikbaarheid en geplande inzet, en bij vier medewerkers de afwezigheidsnotitie "ziek". Noviqo ontdekte het incident op donderdag 12 juni 2025 om 09:40 uur, sloot de link om 10:20 uur en informeerde Hazelaar om 14:15 uur. Hazelaar heeft als verwerkingsverantwoordelijke op zaterdag 14 juni 2025 melding gedaan bij de Autoriteit Persoonsgegevens (meldnummer M-2025-0614-117) en de betrokken medewerkers geïnformeerd.

### A2. Rollen

| Partij | Rol | Contactpersoon |
|---|---|---|
| Bouwgroep Hazelaar B.V. | Verwerkingsverantwoordelijke | K.E. Hazelaar, directeur |
| Noviqo B.V. | Verwerker (VOK 2 september 2024, bijlage 2 bij NOV-VRK-2024-031) | Bas Hoekwater (incidentcoördinator), Lieke Dorrestein (privacy) |
| Wolkenrand Hosting B.V. | Subverwerker hosting; niet betrokken bij de oorzaak | S.B. Kraaijenbrink |
| Schildersbedrijf Gaasterhof v.o.f. | Ontvanger, onbevoegde inzage | Gebruiker met accountrol "extern" |

Op grond van artikel 7.3 van de verwerkersovereenkomst meldt Noviqo een inbreuk niet zelf aan de Autoriteit Persoonsgegevens; de beoordeling en melding liggen bij Hazelaar. Noviqo heeft bijstand verleend bij de beoordeling en een conceptmelding aangeleverd (artikel 6.2 VOK).

### A3. Tijdlijn

| Datum en tijd | Gebeurtenis |
|---|---|
| di 20 mei 2025, 22:30 | Uitrol release 25.5.2 met een nieuwe filtercomponent voor exports. Bij gedeelde links wordt het projectfilter niet meer toegepast. De fout wordt niet gedetecteerd: de geautomatiseerde test dekt alleen exports binnen de eigen omgeving. |
| wo 11 juni 2025, 15:58 | Werkvoorbereider van Hazelaar maakt een exportlink aan voor project "Nieuwbouw Kerkdijk" (onderaannemersplanning schilderwerk) en mailt die naar de contactpersoon van Gaasterhof. De link krijgt geen verloopdatum; dat was destijds optioneel. |
| wo 11 juni 2025, 16:35 | Eerste opening van de link vanaf een IP-adres van Gaasterhof. |
| wo 11 juni 2025, 16:41 | Download van de export als CSV-bestand (63 regels, 9 kolommen). |
| wo 11 juni 2025, 17:48 | Tweede opening van de link vanaf hetzelfde IP-adres. |
| wo 11 juni 2025, 17:52 | Gebruiker van Gaasterhof meldt via het supportportaal dat hij "de hele personeelsplanning van Hazelaar inclusief zieken" kan zien. Melding valt buiten supporttijden (tot 17:30) en is niet als Prioriteit 1 aangemerkt. |
| do 12 juni 2025, 09:40 | Supportmedewerker leest de melding en herkent een mogelijk datalek. **Moment van ontdekking.** |
| do 12 juni 2025, 09:55 | Escalatie naar Bas Hoekwater; incidentnummer INC-2025-007 aangemaakt. |
| do 12 juni 2025, 10:20 | Link gedeactiveerd. Uit voorzorg worden alle exportlinks zonder verloopdatum van Hazelaar ingetrokken (17 links). |
| do 12 juni 2025, 10:45 | Incidentteam bijeen: B. Hoekwater, L. Dorrestein, R.J. Okkersen, S. Loonstra. |
| do 12 juni 2025, 11:30 | Loganalyse afgerond: de link is drie keer geopend, uitsluitend vanaf het IP-adres van Gaasterhof; één download. |
| do 12 juni 2025, 13:10 | Oorzaak vastgesteld: regressie in release 25.5.2. |
| do 12 juni 2025, 14:15 | Telefonische melding aan de heer K.E. Hazelaar (binnen de termijn van 36 uur uit artikel 7.1 VOK). |
| do 12 juni 2025, 15:30 | Schriftelijke melding aan Hazelaar met de gegevens uit artikel 33 lid 3 AVG voor zover bekend. |
| do 12 juni 2025, 16:00 | Scan van alle 214 exportlinks die sinds 20 mei 2025 bij 37 klanten zijn aangemaakt. Geen andere links geopend door een partij buiten de klantorganisatie. |
| do 12 juni 2025, 17:30 | Hotfix 25.5.3 uitgerold: projectfilter afgedwongen op serverniveau, verloopdatum verplicht (maximaal 7 dagen), tenantcontrole bij openen. |
| vr 13 juni 2025, 10:05 | Gaasterhof bevestigt schriftelijk dat het CSV-bestand en de e-mail met de link zijn verwijderd en dat de gegevens niet verder zijn gedeeld. |
| vr 13 juni 2025, 15:00 | Overleg Noviqo en Hazelaar over risicobeoordeling; Noviqo levert conceptmelding aan. |
| za 14 juni 2025, 11:05 | Hazelaar meldt de inbreuk bij de Autoriteit Persoonsgegevens; meldnummer M-2025-0614-117. |
| ma 16 juni 2025 | Hazelaar informeert de 63 medewerkers schriftelijk; de vier medewerkers met de notitie "ziek" worden daarnaast persoonlijk gesproken door hun leidinggevende en de HR-adviseur van Hazelaar. |
| vr 20 juni 2025 | Evaluatie incidentteam Noviqo. |
| ma 30 juni 2025 | Eindrapport aan Hazelaar verstrekt. |
| wo 9 juli 2025 | Autoriteit Persoonsgegevens bevestigt registratie van de melding; geen nadere vragen. |

### A4. Oorzaakanalyse

De directe oorzaak was een regressie in de exportfunctie: release 25.5.2 verving de filtercomponent, waarbij de parameter die het projectfilter vastlegt bij gedeelde links niet werd doorgegeven. De link toonde daardoor de standaardweergave van de gehele omgeving.
Bijdragende oorzaken:
- exportlinks konden zonder verloopdatum worden aangemaakt;
- er was geen controle of de ontvanger van een link tot de eigen organisatie behoorde;
- de testset bevatte geen scenario voor gedeelde links met externe ontvangers;
- afwezigheidsnotities werden standaard in exports meegenomen, terwijl onderaannemers die niet nodig hebben;
- supportmeldingen buiten kantoortijd werden niet gescreend op beveiligingstrefwoorden.

### A5. Risicobeoordeling

| Factor | Beoordeling |
|---|---|
| Aard inbreuk | Inbreuk op vertrouwelijkheid |
| Aantal betrokkenen | 63 medewerkers van Hazelaar |
| Gegevens | Naam, functie, beschikbaarheid, geplande inzet, projectlocaties; bij 4 personen afwezigheidsnotitie "ziek" (gezondheidsgegeven, artikel 9 AVG) |
| Ontvanger | Eén bekende, zakelijke ontvanger (onderaannemer) die de gegevens aantoonbaar heeft verwijderd |
| Duur blootstelling | Circa 18 uur feitelijke toegang (11 juni 15:58 tot 12 juni 10:20) |
| Gevolgen | Mogelijk ongemak en reputatieschade voor de vier medewerkers in de lokale bouwsector; geen financiële gegevens, BSN of wachtwoorden |
| Conclusie | Risico voor de rechten en vrijheden van betrokkenen niet uit te sluiten vanwege gezondheidsgegevens: meldplicht AP (artikel 33 AVG). Hoog risico voor de vier medewerkers met de notitie "ziek" niet uitgesloten; Hazelaar heeft alle 63 medewerkers geïnformeerd (artikel 34 AVG). |

### A6. Maatregelen

| Maatregel | Datum gereed | Eigenaar |
|---|---|---|
| Hotfix 25.5.3: projectfilter server-side, verplichte verloopdatum, tenantcontrole | 12 juni 2025 | M. Holtrop |
| Afwezigheidstypen standaard uitgesloten van externe exports | 27 juni 2025 | M. Holtrop |
| Regressietests voor gedeelde links en externe ontvangers toegevoegd aan de CI-pijplijn | 4 juli 2025 | J. Vendelbroek |
| Supportportaal: trefwoordsignalering ("datalek", "andermans gegevens", "kan zien") met sms-alert naar dienstdoende security officer | 18 juli 2025 | S. Loonstra |
| Foutmonitoring via Spoorlicht Monitoring GmbH ingericht, met alert op afwijkende exportpatronen | 30 juni 2025 | B. Hoekwater |
| Audit-log van exportlinks voor klantbeheerders zichtbaar gemaakt | 29 augustus 2025 | M. Holtrop |
| Evaluatie meldprocedure en bijlage contactpersonen in alle verwerkersovereenkomsten | 30 september 2025 | L. Dorrestein |
| Exportfunctie API meegenomen in scope pentest januari 2026 | januari 2026 | B. Hoekwater |

Noviqo heeft Hazelaar geen kosten in rekening gebracht voor de verleende bijstand.

## Deel B – Register van inbreuken en beveiligingsincidenten

Het register bevat alle beveiligingsincidenten uit het incidentregister van het ISMS waarbij persoonsgegevens betrokken waren of mogelijk betrokken waren, ongeacht of melding is gedaan. De nummering volgt het incidentregister (INC-JJJJ-nnn); incidenten zonder persoonsgegevens, zoals storingen in interne systemen, zijn hier niet opgenomen, waardoor de nummering niet doorlopend is. Bij incidenten in de verwerkersrol is vermeld wat de verwerkingsverantwoordelijke heeft besloten. De beoordeling volgt de EDPB-richtsnoeren 9/2022 inzake de melding van inbreuken.

| Nr | Datum ontdekking | Omschrijving | Rol Noviqo | Betrokkenen en gegevens | Melding AP | Betrokkenen geïnformeerd | Motivering en maatregelen |
|---|---|---|---|---|---|---|---|
| INC-2025-002 | 18 februari 2025 | Offerte-e-mail met bijlage met contactpersonenoverzicht van een andere prospect naar verkeerde ontvanger gestuurd | Verantwoordelijke | 6 zakelijke contactpersonen; naam, functie, zakelijk e-mailadres en telefoonnummer | Nee | Nee | Zakelijke contactgegevens, ontvanger bekend en heeft verwijdering bevestigd; geen risico. Instructie e-mailbijlagen aan sales. |
| INC-2025-004 | 7 april 2025 | Laptop van een developer gestolen uit auto | Verantwoordelijke en verwerker | Mogelijk broncode en testdata; geen productiedata | Nee | Nee | Volledige schijfversleuteling en MFA; laptop binnen 2 uur op afstand gewist via MDM; testdata synthetisch. Geen inbreuk op persoonsgegevens vastgesteld. |
| INC-2025-007 | 12 juni 2025 | Exportlink zonder verloopdatum toonde planningsgegevens Hazelaar aan gebruiker Gaasterhof | Verwerker | 63 medewerkers Hazelaar; naam, functie, beschikbaarheid; 4 x notitie "ziek" | Ja, door Hazelaar op 14 juni 2025 (M-2025-0614-117) | Ja, door Hazelaar op 16 juni 2025 | Zie deel A. |
| INC-2025-009 | 22 juli 2025 | Phishingmail; medewerker vult wachtwoord in op valse inlogpagina | Verantwoordelijke | Mailbox van 1 medewerker | Nee | Nee | Inlogpoging vanuit buitenland geblokkeerd door MFA; wachtwoord direct gewijzigd; geen toegang tot gegevens. Geen inbreuk. Extra phishingtraining voor alle medewerkers in september 2025. |
| INC-2025-012 | 9 september 2025 | Supportmedewerker voegt per abuis CSV-export van klant A toe aan antwoord aan klant B | Verwerker | 12 medewerkers van klant A; naam, functie, mobiel nummer | Nee (besluit klant A) | Nee (besluit klant A) | Klant A binnen 6 uur geïnformeerd; klant B heeft verwijdering bevestigd; geen gevoelige gegevens. Klant A achtte het risico onwaarschijnlijk. Exports als bijlage in tickets niet langer toegestaan. |
| INC-2025-015 | 21 oktober 2025 | Melding Klantloep CRM over incident bij subverwerker Relayport Software Inc. | Verantwoordelijke | Geen gegevens van Noviqo geraakt volgens onderzoeksrapport Klantloep | Nee | Nee | Geen inbreuk bij Noviqo; rapport Klantloep ontvangen 4 november 2025. |
| INC-2026-002 | 21 januari 2026 | Pentest Schildwacht: IDOR in exportfunctie API (bevinding hoog) | Verwerker | Potentieel alle exports; feitelijk geen | Nee | Nee | Loganalyse over 12 maanden: geen misbruik buiten de testaccounts van Schildwacht. Kwetsbaarheid, geen inbreuk. Fix uitgerold 30 januari 2026, hertest geslaagd. |
| INC-2026-003 | 27 januari 2026 | PII-filter Insights liet achternaam van een medewerker in een prompt aan Dendra AI door (naam stond in een teamnaam) | Verwerker | 1 medewerker Installatiebedrijf Rietvelden; achternaam in combinatie met teamnaam | Nee (besluit Rietvelden) | Nee | Geen gevoelige gegevens; Dendra gebruikt invoer niet voor training en wist binnen 30 dagen. Rietvelden op 28 januari 2026 geïnformeerd. Filter uitgebreid met controle op teamnamen. |
| INC-2026-006 | 3 maart 2026 | Storing PlanGrip na mislukte databasemigratie; circa 19 uur onbereikbaar (3 maart vanaf 22:00 tot 4 maart omstreeks 17:00) | Verwerker | Alle klanten; tijdelijke onbeschikbaarheid planningsgegevens; geen verlies of onbevoegde toegang | Nee | Nee (alle klanten wel geïnformeerd over storing) | Beschikbaarheidsincident in de zin van de EDPB-richtsnoeren. Gegevens volledig hersteld zonder verlies; geen bekende gevolgen voor betrokkenen. Klanten op 4 maart 2026 en via incidentrapport van 11 maart 2026 geïnformeerd zodat zij zelf konden beoordelen; geen klant heeft gemeld voor zover bekend. Zie BCP versie 1.1. |
| INC-2026-009 | 6 april 2026 | Account van een per 31 maart 2026 uit dienst getreden salesmedewerker nog actief in Klantloep | Verantwoordelijke | Klant- en prospectgegevens in CRM | Nee | Nee | Loganalyse: geen inlog na 27 maart 2026. Geen inbreuk. Offboardingchecklist aangevuld met CRM en sluiting op laatste werkdag. |
| INC-2026-011 | 14 mei 2026 | Uitnodiging webinar handmatig verstuurd met 87 ontvangers in het CC-veld | Verantwoordelijke | 87 prospects en klanten; naam en zakelijk e-mailadres | Nee | Ja, excuusmail 15 mei 2026 | Zakelijke e-mailadressen in een zakelijke context; geen gevoelige gegevens of kwetsbare groep; risico onwaarschijnlijk. Verzending alleen nog via mailingmodule. |
| INC-2026-017 | 19 augustus 2026 | Onjuiste rolkoppeling bij SSO-inrichting gaf 3 gebruikers van Gemeente Lindewoude inzage in planning van een andere afdeling | Verwerker | Circa 45 buitendienstmedewerkers van de gemeente; naam, beschikbaarheid, afwezigheidstype | Nee (besluit Gemeente Lindewoude) | Nee (besluit gemeente) | Inzage binnen dezelfde organisatie door ambtenaren met geheimhoudingsplicht, 2 dagen; gemeente beoordeelde risico als onwaarschijnlijk en registreerde intern. Rolkoppeling hersteld; validatiestap toegevoegd aan SSO-onboarding. |

### B1. Kengetallen

| Kengetal | 2025 | 2026 (t/m september) |
|---|---|---|
| Geregistreerde incidenten | 6 | 6 |
| Waarvan inbreuk in verband met persoonsgegevens | 3 | 4 |
| Gemeld bij AP (door Noviqo of verwerkingsverantwoordelijke) | 1 | 0 |
| Gemiddelde tijd tot informeren klant (verwerkersrol) | 5,3 uur na ontdekking | 6,5 uur na ontdekking |

## Versiehistorie

| Versie | Datum | Wijziging | Auteur |
|---|---|---|---|
| 1.0 | 30 juni 2025 | Deel A eindrapport datalek | L. Dorrestein, B. Hoekwater |
| 1.4 | 15 januari 2026 | Register bijgewerkt 2025 | L. Dorrestein |
| 1.7 | 2 oktober 2026 | Register bijgewerkt t/m september 2026, kengetallen | L. Dorrestein |

___
L. Dorrestein, legal & privacy officer

___
B. Hoekwater, DevOps lead & security officer
