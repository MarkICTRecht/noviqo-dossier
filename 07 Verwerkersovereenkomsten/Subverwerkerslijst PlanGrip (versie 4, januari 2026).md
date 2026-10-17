# SUBVERWERKERSLIJST PLANGRIP
_kenmerk NOV-PRV-2026-001 – versie 4, januari 2026 – geldig vanaf 15 januari 2026_

## 1. Doel en reikwijdte
1.1 Noviqo B.V. ("Noviqo") verwerkt bij het leveren van PlanGrip, PlanGrip Veld en PlanGrip Insights persoonsgegevens als verwerker ten behoeve van haar klanten. Voor bepaalde onderdelen van de dienstverlening schakelt Noviqo andere verwerkers in. Deze subverwerkers worden in dit document vermeld.
1.2 Deze lijst hoort bij de verwerkersovereenkomsten die Noviqo met haar klanten heeft gesloten en vervangt per 15 januari 2026 versie 3 van juni 2025. Waar in een verwerkersovereenkomst wordt verwezen naar "het overzicht van goedgekeurde subverwerkers" of de bijlage met subverwerkers, wordt de lijst bedoeld die op grond van die verwerkersovereenkomst voor de betreffende klant geldt.
1.3 Deze lijst betreft uitsluitend subverwerkers die persoonsgegevens verwerken die klanten in PlanGrip invoeren of laten genereren ("Klantdata"). Leveranciers die uitsluitend voor Noviqo's eigen bedrijfsvoering persoonsgegevens verwerken, zijn geen subverwerkers en staan in paragraaf 4 ter informatie vermeld.
1.4 Eigenaar van dit document is de legal & privacy officer van Noviqo, mevrouw L. Dorrestein. Technische gegevens zijn aangeleverd door de heer B. Hoekwater, DevOps lead & security officer en eigenaar van het ISMS. Vragen kunnen worden gericht aan privacy@noviqo.example.

## 2. Overzicht subverwerkers
| Subverwerker | Vestiging | Dienst | Categorieën Klantdata | Locatie verwerking | Doorgiftegrondslag | Sinds |
|---|---|---|---|---|---|---|
| Wolkenrand Hosting B.V. | Eindhoven, Nederland | hosting van productie- en uitwijkomgeving, objectopslag, back-ups | alle Klantdata | Nederland (twee datacenters) | n.v.t. (EER) | mei 2023 |
| Postbaken B.V. | Utrecht, Nederland | verzending van systeem-e-mails (uitnodigingen, wachtwoordherstel, planningsnotificaties) | naam, e-mailadres, inhoud van notificaties | Nederland en Duitsland | n.v.t. (EER) | mei 2023 |
| Ticketvlinder B.V. | Leeuwarden, Nederland | supportsoftware en ticketing | contactgegevens van melders, inhoud van supportverzoeken, bijlagen en schermafdrukken die klanten meesturen | Nederland | n.v.t. (EER) | september 2024 |
| Spoorlicht Monitoring GmbH | Berlijn, Duitsland | foutmonitoring en applicatieprestaties (error tracking, logregistratie) | gebruikers-ID, IP-adres, technische loggegevens; inhoud van planningen wordt gemaskeerd | Duitsland | n.v.t. (EER) | juni 2025 |
| Dendra AI Inc. | Wilmington (Delaware), Verenigde Staten | taalmodel voor het genereren van samenvattingen in PlanGrip Insights | gepseudonimiseerde planningsgegevens (pseudoniem, functie, team, projecttoewijzing, beschikbaarheid, geaggregeerde verzuimindicatoren) | Verenigde Staten en Ierland | EU-US Data Privacy Framework; standaardcontractbepalingen (module 3) als terugvaloptie | 15 januari 2026 |

## 3. Toelichting per subverwerker
### 3.1 Wolkenrand Hosting B.V.
Wolkenrand is de hostingpartij van het volledige PlanGrip-platform. Alle productiegegevens en back-ups worden uitsluitend opgeslagen in twee datacenters in Nederland. Op de verwerking is de verwerkersovereenkomst van 8 mei 2023 (Bijlage 3 bij NOV-INK-2023-004) van toepassing. Wolkenrand schakelt geen eigen subverwerkers in zonder voorafgaande specifieke schriftelijke toestemming van Noviqo.

### 3.2 Postbaken B.V.
Postbaken verzorgt de technische verzending van e-mails die PlanGrip automatisch verstuurt. Berichten worden na verzending maximaal 30 dagen bewaard voor het afhandelen van bounces en afleverproblemen. Postbaken maakt voor redundantie gebruik van een tweede datacenter in Frankfurt am Main.

### 3.3 Ticketvlinder B.V.
Ticketvlinder levert het systeem waarmee het Customer Success-team van Noviqo supportverzoeken afhandelt. Klantdata komt in Ticketvlinder terecht wanneer een klant die zelf in een supportverzoek opneemt, bijvoorbeeld in een schermafdruk. Supporttickets worden twee jaar na sluiting verwijderd. Noviqo adviseert klanten in supportverzoeken geen persoonsgegevens van medewerkers op te nemen die niet nodig zijn voor de afhandeling.

### 3.4 Spoorlicht Monitoring GmbH
Spoorlicht is in juni 2025 ingeschakeld om fouten en afwijkend gedrag in PlanGrip sneller te detecteren, mede als verbetermaatregel na het beveiligingsincident met een gedeelde exportlink in juni 2025. Velden met planninginhoud, namen en vrije tekst worden vóór verzending in de applicatie gemaskeerd. Loggegevens worden 90 dagen bewaard.

### 3.5 Dendra AI Inc.
3.5.1 Dendra AI Inc. wordt uitsluitend ingeschakeld voor klanten die de module PlanGrip Insights hebben geactiveerd. Voor klanten zonder Insights worden geen gegevens aan Dendra doorgegeven.
3.5.2 Voordat gegevens aan Dendra worden verstuurd, vervangt PlanGrip namen en contactgegevens van medewerkers door pseudoniemen. De sleutel waarmee pseudoniemen aan personen kunnen worden gekoppeld, blijft binnen de door Wolkenrand gehoste omgeving in Nederland. Vrije-tekstnotities bij verzuim worden niet doorgegeven.
3.5.3 Op de verwerking is de Enterprise Services Agreement van 3 november 2025 (NOV-INK-2025-014) met de daarbij behorende Data Processing Addendum van toepassing. Dendra gebruikt de gegevens contractueel niet voor het trainen of verbeteren van haar modellen. Dendra bewaart invoer en uitvoer maximaal 30 dagen voor misbruikmonitoring; de optie om dit tot nul te beperken (zero data retention) is beschikbaar maar per de datum van deze lijst niet geactiveerd.
3.5.4 Dendra verwerkt de gegevens in de Verenigde Staten en Ierland. De doorgifte naar de Verenigde Staten is gebaseerd op de certificering van Dendra onder het EU-US Data Privacy Framework (adequaatheidsbesluit van de Europese Commissie van 10 juli 2023). Indien dat besluit vervalt of de certificering eindigt, gelden de standaardcontractbepalingen van de Europese Commissie (Uitvoeringsbesluit (EU) 2021/914, module 3, verwerker aan verwerker), die in de Data Processing Addendum zijn opgenomen.
3.5.5 Dendra heeft een algemene toestemming voor het inschakelen van eigen subverwerkers, met name de aanbieders van de cloudinfrastructuur waarop haar platform draait. Een actuele lijst daarvan is op verzoek bij Noviqo verkrijgbaar.

## 4. Leveranciers die geen subverwerker zijn
De volgende leveranciers verwerken persoonsgegevens uitsluitend voor Noviqo's eigen bedrijfsvoering, waarvoor Noviqo zelf verwerkingsverantwoordelijke is. Zij verwerken geen Klantdata en zijn daarom geen subverwerker:
- Klantloep CRM B.V. (Groningen): het CRM-systeem van Noviqo voor gegevens van contactpersonen bij klanten en prospects;
- Salariswijs B.V. (Utrecht): salarisadministratie van Noviqo's eigen medewerkers;
- Boekhof & Partners Accountants (Utrecht): accountant van Noviqo;
- ArboVlak B.V.: arbodienst voor Noviqo's eigen medewerkers.

## 5. Wijzigingsprocedure
5.1 Noviqo kondigt het toevoegen of vervangen van een subverwerker aan overeenkomstig de verwerkersovereenkomst met de betreffende klant, in de regel ten minste 30 dagen voor de ingangsdatum, per e-mail aan de contactpersoon van de klant en via de release notes in PlanGrip.
5.2 Een klant kan binnen de in de verwerkersovereenkomst genoemde termijn gemotiveerd bezwaar maken. Partijen treden dan in overleg. Bij een subverwerker die alleen voor een optionele module wordt ingezet, zoals Dendra AI Inc. voor Insights, kan een klant ook volstaan met het niet activeren van die module.
5.3 Waar een verwerkersovereenkomst voor doorgifte buiten de Europese Economische Ruimte voorafgaande schriftelijke toestemming van de klant vereist, wordt een subverwerker buiten de EER voor die klant pas ingeschakeld nadat die toestemming is verkregen.
5.4 De aankondiging van versie 4 van deze lijst is op 12 december 2025 verzonden aan de contactpersonen van alle klanten met een Teams- of Enterprise-abonnement.

## 6. Versiehistorie
| Versie | Datum | Wijziging | Vastgesteld door |
|---|---|---|---|
| 1 | mei 2023 | eerste versie: Wolkenrand Hosting B.V. en Postbaken B.V. | R.J. Okkersen |
| 2 | september 2024 | toegevoegd: Ticketvlinder B.V. (supportsoftware) | R.J. Okkersen |
| 3 | juni 2025 | toegevoegd: Spoorlicht Monitoring GmbH (foutmonitoring); toelichting toegevoegd over bewaartermijnen en over leveranciers die geen subverwerker zijn; geen subverwerkers buiten de EER | L. Dorrestein en B. Hoekwater |
| 4 | januari 2026 | toegevoegd: Dendra AI Inc. (Verenigde Staten), uitsluitend voor PlanGrip Insights; paragraaf 3.5 en 5.3 toegevoegd | L. Dorrestein en B. Hoekwater, goedgekeurd door R.J. Okkersen op 10 december 2025 |

## 7. Vaststelling
Deze versie is vastgesteld door de CTO van Noviqo op 10 december 2025 en geldt vanaf 15 januari 2026, de lanceringsdatum van PlanGrip Insights. De volgende reguliere herziening is gepland voor juli 2026, of eerder bij een wijziging van subverwerkers.

___
Noviqo B.V.
R.J. Okkersen
bestuurder (CTO)
