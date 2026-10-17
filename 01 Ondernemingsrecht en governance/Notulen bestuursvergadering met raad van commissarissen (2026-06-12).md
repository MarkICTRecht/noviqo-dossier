# NOTULEN GECOMBINEERDE VERGADERING BESTUUR EN RAAD VAN COMMISSARISSEN
_kenmerk NOV-RVC-2026-003 – vergadering van 12 juni 2026_

**Datum en plaats:** vrijdag 12 juni 2026, 09:30–13:00 uur, vergaderruimte "Kade", De Spilhoek, Verzonnelkade 88, Amsterdam.

**Raad van commissarissen:** mevrouw dr. A.L. Venhuizen (voorzitter), de heer M.O. Tjallingii (commissaris op voordracht van Kroonvaart Capital B.V.).

**Bestuur:** mevrouw F.A. van Dalsem (CEO, namens Van Dalsem Holding B.V.), de heer R.J. Okkersen (CTO, namens Okkersen Beheer B.V.).

**Waarnemer:** de heer T.M. Quistgaard (Sterrelink Ventures B.V.), zonder stemrecht, conform de aandeelhoudersovereenkomst NOV-AHO-2025-002.

**Tevens aanwezig (bij de genoemde punten):** mevrouw I. Wapperom, finance controller (2 en 8); de heer B. Hoekwater, DevOps lead & security officer (3, 5 en 6); de heer D. Achterberg, Head of Sales (4); mevrouw L. Dorrestein, legal & privacy officer (3 en 7).

**Notulist:** mevrouw Y. Mollinga.

## 1. Opening, agenda en notulen

1.1 De voorzitter opent de vergadering om 09:30 uur. Alle leden van de raad en het bestuur zijn aanwezig. De agenda wordt vastgesteld.
1.2 De notulen van de vergadering van 18 maart 2026 worden ongewijzigd vastgesteld. Uit de actielijst: de oorzaakanalyse van de storing is op 20 maart 2026 aan Hazelaar verstrekt (gereed); de gewijzigde migratieprocedure is vastgesteld (gereed, zie punt 3); het ISO-traject is aanbesteed (gereed, zie punt 5).

## 2. Kwartaalcijfers Q1 2026 en stand per mei

2.1 Mevrouw Wapperom presenteert de kwartaalrapportage over Q1 2026, die op 24 april 2026 aan de aandeelhouders is verzonden.

| Kerncijfer | Q1 2026 realisatie | Q1 2026 budget | Afwijking |
|---|---|---|---|
| Netto-omzet | EUR 438.200 | EUR 455.000 | -EUR 16.800 |
| waarvan abonnementen (incl. Insights) | EUR 401.900 | EUR 409.000 | -EUR 7.100 |
| waarvan implementatie | EUR 36.300 | EUR 46.000 | -EUR 9.700 |
| Bedrijfskosten | EUR 625.600 | EUR 615.000 | +EUR 10.600 |
| Nettoresultaat | -EUR 187.400 | -EUR 160.000 | -EUR 27.400 |
| MRR per 31 maart 2026 | EUR 149.200 | EUR 151.500 | -EUR 2.300 |
| Liquide middelen per 31 maart 2026 | EUR 2.212.000 | EUR 2.260.000 | -EUR 48.000 |

2.2 De ARR per 31 maart 2026 bedraagt EUR 1,79 miljoen. Het aantal betalende klanten bedroeg 221. In Q1 hebben 4 klanten opgezegd, met in totaal EUR 2.140 MRR. Het aantal medewerkers bedroeg 30 per 31 maart 2026; de heer T. Gravemaker is per die datum uit dienst getreden op grond van de vaststellingsovereenkomst van 20 februari 2026.
2.3 De achterstand op implementatieomzet hangt samen met het verschuiven van twee Enterprise-implementaties naar Q2. De kostenoverschrijding wordt voor EUR 5.800 verklaard door hogere kosten voor Dendra AI (punt 8) en voor het overige door eenmalige advieskosten in verband met de aanbesteding van Lindewoude en de storing in maart.
2.4 Stand per 31 mei 2026: MRR EUR 153.400, ARR EUR 1,84 miljoen, liquide middelen EUR 2.071.000. De runway bij de huidige netto-burn van circa EUR 65.000 per maand bedraagt ruim 30 maanden. Met de start van Lindewoude (punt 4) wordt de ARR per eind september 2026 verwacht op circa EUR 2,1 miljoen.
2.5 De heer Tjallingii vraagt de churn voortaan ook per abonnementsvorm te rapporteren en de netto-omzetretentie op te nemen. Mevrouw Wapperom zegt dit toe voor de rapportage over Q2.

## 3. Storing 3–4 maart 2026 en claim Bouwgroep Hazelaar

3.1 De heer Hoekwater vat de oorzaakanalyse samen. De databasemigratie op 3 maart 2026 leidde onder productiebelasting tot een inconsistentie in de replicatie; het terugvalscenario kon niet worden voltooid. Na restore van de back-up van 21:45 uur was PlanGrip op 4 maart 2026 om 16:58 uur hersteld. De onbeschikbaarheid bedroeg 19 uur, waarvan 4 uur binnen het aangekondigde onderhoudsvenster. Er is geen data verloren gegaan.
3.2 Maatregelen: migraties van de productiedatabase vinden voortaan uitsluitend plaats in het zaterdagvenster, met een parallelle omgeving waarnaar binnen 30 minuten kan worden teruggeschakeld (blue-green), een go/no-go-moment om 00:30 uur en aankondiging ten minste tien werkdagen vooraf. Voor alle klanten wordt een automatische nachtelijke export van de dagplanning van de volgende dag als PDF beschikbaar gesteld aan beheerders ("noodplanning"), live sinds 1 juni 2026.
3.3 Mevrouw Dorrestein meldt de stand van de claim. Bij brief van 18 maart 2026 heeft Hazelaar, via Lindeboom & Vos Advocaten, EUR 38.400 aan gevolgschade gevorderd. Ravelijn Advocaten heeft op 1 april 2026 namens Noviqo aansprakelijkheid afgewezen, met een beroep op artikel 7.3 SLA (servicecredits als enige financiële remedie), artikel 6.2 van de SaaS-overeenkomst en artikel 8.2 van de algemene voorwaarden (uitsluiting van stagnatieschade). Zonder erkenning van aansprakelijkheid is een regeling aangeboden van in totaal EUR 4.793,75 (servicecredit 25% van EUR 368,75 en een creditnota van drie maandvergoedingen van EUR 4.425).
3.4 Bij brief van 4 mei 2026 heeft de advocaat van Hazelaar het aanbod afgewezen en een tegenvoorstel gedaan van EUR 12.500, met finale kwijting. De verzekeraar van Noviqo, Polderzeker Verzekeringen N.V., heeft op 21 mei 2026 laten weten dat de claim onder de beroeps- en bedrijfsaansprakelijkheidsverzekering valt voor zover sprake is van een aansprakelijkheid van Noviqo, maar dat zij het verweer van Noviqo onderschrijft; het eigen risico bedraagt EUR 5.000 per aanspraak.
3.5 De heer Achterberg merkt op dat de overeenkomst met Hazelaar per 1 oktober 2026 stilzwijgend wordt verlengd, tenzij Hazelaar uiterlijk 31 juli 2026 opzegt. Hazelaar heeft laten weten de verlenging mede te laten afhangen van de afhandeling van de claim. Het verlies van Hazelaar betekent EUR 17.700 ARR.
3.6 De raad bespreekt de procesrisico's. De heer Tjallingii acht de juridische positie van Noviqo sterk, maar wijst op de reputatierisico's richting de publieke sector, nu Lindewoude bij de aanbesteding naar incidenten heeft gevraagd.

**Besluit RvC 2026-11:** De raad van commissarissen verleent het bestuur mandaat de claim van Hazelaar te schikken tot een totaalbedrag van ten hoogste EUR 9.000, inclusief de reeds aangeboden servicecredit en creditnota, met finale kwijting, bij voorkeur in de vorm van creditering op de jaarfactuur per 1 oktober 2026 en gekoppeld aan verlenging van de overeenkomst. Het bestuur stelt eerst een bedrag van EUR 7.500 voor. Een eventuele procedure wordt niet gestart zonder voorafgaand overleg met de raad.

## 4. Gemeente Lindewoude

4.1 De heer Achterberg meldt dat de opdracht na de Europese aanbesteding op 16 maart 2026 aan Noviqo is gegund. Er is geen bezwaar ingediend binnen de opschortende termijn, en de overeenkomst, met toepasselijkheid van de GIBIT, is getekend. Het gaat om een Enterprise-abonnement voor 400 gebruikers in de buitendienst tegen EUR 9.800 per maand (EUR 117.600 per jaar), voor drie jaar met twee opties tot verlenging van telkens één jaar.
4.2 De implementatie loopt volgens planning. De koppeling met het identiteitsbeheer (SSO) van de gemeente is getest; de livegang staat gepland op 1 september 2026. Contractmanager is de heer W.F. Siebenga.
4.3 Bijzondere verplichtingen uit de overeenkomst: (i) certificering naar ISO/IEC 27001 binnen 12 maanden na ingangsdatum; (ii) een jaarlijkse onafhankelijke pentest met deling van de managementsamenvatting; (iii) opslag van gegevens uitsluitend binnen de EER; (iv) melding van beveiligingsincidenten binnen 24 uur.
4.4 Mevrouw Dorrestein licht toe dat Lindewoude heeft verzocht de module PlanGrip Insights voorlopig niet te activeren, totdat de gemeente een eigen DPIA heeft afgerond, in verband met de verwerking door Dendra AI in de Verenigde Staten. Insights is voor Lindewoude technisch uitgeschakeld. Dit is in lijn met eis (iii).

## 5. Informatiebeveiliging: ISO 27001

5.1 De heer Hoekwater, eigenaar van het ISMS, meldt dat het ISMS sinds januari 2026 in opbouw is. De interne audit is gepland in augustus 2026, de fase 1-audit door Certivaart B.V. op 22 september 2026 en de fase 2-audit in de week van 23 november 2026.
5.2 Het budget voor het traject bedraagt EUR 42.000 in 2026 (externe begeleiding EUR 24.500, certificatie-audit EUR 11.000, tooling EUR 6.500), binnen het goedgekeurde budget 2026.
5.3 De heer Tjallingii vraagt of de capaciteit voldoende is, nu de heer Hoekwater ook DevOps lead is. Het bestuur zegt toe vóór 1 september 2026 te besluiten over een extra medewerker security en compliance.

## 6. Pentest Schildwacht Security

6.1 De heer Hoekwater geeft de stand van de opvolging van het pentestrapport van Schildwacht Security B.V. van 9 februari 2026:

| Ernst | Aantal | Opgelost | Open | Toelichting |
|---|---|---|---|---|
| Hoog | 1 | 1 | 0 | Toegang tot exportbestanden van een andere klant via voorspelbaar export-ID in de API; opgelost 30 januari 2026, hertest geslaagd 11 maart 2026 |
| Midden | 3 | 2 | 1 | Open: sessieduur mobiele app PlanGrip Veld (30 dagen); oplossing gepland in release van 30 juni 2026 |
| Laag | 6 | 4 | 0 | 2 bevindingen bewust als risico geaccepteerd (informatieve headers, versienummer in foutpagina van testomgeving) |

6.2 De raad vraagt of de bevinding met de hoge ernst samenhangt met het datalek van juni 2025. De heer Hoekwater bevestigt dat het om dezelfde functionaliteit gaat, maar om een ander gebrek: in 2025 ging het om links zonder verloopdatum, in 2026 om voorspelbare ID's. Uit de logbestanden blijkt geen misbruik.

## 7. DPIA PlanGrip Insights

7.1 Mevrouw Dorrestein meldt dat de DPIA voor PlanGrip Insights is gedateerd 20 februari 2026, terwijl de module op 15 januari 2026 is gelanceerd. De DPIA is dus achteraf uitgevoerd. De conclusie is dat de verwerking, met de genomen maatregelen, een aanvaardbaar restrisico kent: pseudonimisering van medewerkersnamen vóór verzending naar Dendra AI, geen verwerking van vrije-tekstvelden over verzuim, activering per klant (opt-in) en een bewaartermijn van 30 dagen bij Dendra.
7.2 Mevrouw Venhuizen spreekt haar zorg uit dat de DPIA niet vóór de lancering is uitgevoerd, nu de module voorspellingen doet over ziekteverzuimpieken. Zij vraagt hoe dit is gebeurd. De heer Okkersen geeft aan dat de lancering naar voren is gehaald voor een beurs in januari en dat de privacybeoordeling ten onrechte als formaliteit is behandeld.
7.3 De raad verzoekt het bestuur een vaste "privacy- en securitytoets" in te voeren als voorwaarde voor iedere release van nieuwe functionaliteit met persoonsgegevens, met aftekening door de legal & privacy officer en de security officer. Mevrouw Dorrestein bereidt een procedurevoorstel voor.

## 8. Budget AI-kosten Dendra AI

8.1 Mevrouw Wapperom licht toe dat de kosten van de LLM-API van Dendra AI Inc. (Enterprise Services Agreement van 3 november 2025) op gebruik zijn gebaseerd. In Q1 2026 bedroegen zij EUR 14.800, tegen EUR 9.000 begroot. Insights wordt per 31 mei 2026 gebruikt door 41 klanten met in totaal 1.460 gebruikers, wat EUR 8.760 per maand aan Insights-omzet oplevert (EUR 6 per gebruiker).
8.2 De prognose voor april tot en met december 2026 is EUR 63.000 (gemiddeld EUR 7.000 per maand), zodat de totale kosten 2026 uitkomen op EUR 77.800, tegen EUR 36.000 begroot. Het tekort bedraagt EUR 41.800. De brutomarge van Insights blijft positief, maar daalt van de begrote 60% naar circa 20%.
8.3 De heer Okkersen stelt maatregelen voor: caching van samenvattingen, het gebruik van een kleiner model voor eenvoudige taken en een maandelijks kostenplafond met automatische waarschuwing bij 80%. Daarmee verwacht hij de maandkosten vanaf september 2026 met circa 30% te verlagen. De heer Achterberg bereidt een voorstel voor om de Insights-prijs per 1 januari 2027 te verhogen.

**Besluit RvC 2026-12:** De raad van commissarissen keurt een verhoging van het budget 2026 voor AI-diensten goed met EUR 42.000, tot EUR 78.000, onder de voorwaarde dat (i) een maandelijks kostenplafond van EUR 9.500 wordt ingesteld en (ii) het bestuur in de vergadering van september 2026 rapporteert over het effect van de kostenmaatregelen. De verhoging valt binnen het door de raad goedgekeurde budget en behoeft geen afzonderlijke goedkeuring van de algemene vergadering.

## 9. Uitbreiding huisvesting

9.1 De allonge bij de huurovereenkomst De Spilhoek (MER-HUUR-2023-118/A1) is op 1 mei 2026 ondertekend. Per 1 juni 2026 huurt Noviqo aanvullend circa 165 m² op de tweede verdieping tegen EUR 2.900 per maand exclusief btw, met een huurvrije eerste maand (goedgekeurd door de raad op 22 april 2026 en door de algemene vergadering op 24 april 2026). De bankgarantie is op 22 mei 2026 met EUR 12.051,60 verhoogd.
9.2 De allonge bevat een break-optie voor uitsluitend de uitbreiding tegen 30 april 2027, uit te oefenen uiterlijk 31 oktober 2026. De raad verzoekt het bestuur in de vergadering van september 2026 een advies voor te leggen over het al dan niet uitoefenen daarvan, in samenhang met de personeelsplanning 2027.

## 10. Rondvraag en sluiting

10.1 De heer Quistgaard vraagt naar de stand van het optieplan. Het bestuur meldt dat tot op heden 4.180 opties zijn toegekend aan 9 medewerkers, na goedkeuring van de raad van commissarissen op 18 februari 2026; er resteren 5.744 opties in de pool van 9.924.
10.2 De voorzitter sluit de vergadering om 13:00 uur. De volgende vergadering is op 18 september 2026.

## Actielijst

| Nr. | Actie | Eigenaar | Termijn |
|---|---|---|---|
| 1 | Schikkingsvoorstel Hazelaar (EUR 7.500, mandaat tot EUR 9.000) via Ravelijn Advocaten | F.A. van Dalsem | 26 juni 2026 |
| 2 | Hazelaar benaderen over verlenging per 1 oktober 2026 | D. Achterberg | 15 juli 2026 |
| 3 | Churn per abonnementsvorm en netto-omzetretentie in kwartaalrapportage | I. Wapperom | rapportage Q2 |
| 4 | Maandelijkse voortgangsrapportage Lindewoude aan RvC | D. Achterberg | tot livegang |
| 5 | Besluit extra capaciteit security en compliance | R.J. Okkersen | 1 september 2026 |
| 6 | Oplossen openstaande pentestbevinding (sessieduur PlanGrip Veld) | B. Hoekwater | 30 juni 2026 |
| 7 | Procedurevoorstel privacy- en securitytoets voor releases | L. Dorrestein | 18 september 2026 |
| 8 | Kostenplafond Dendra AI instellen en effect kostenmaatregelen rapporteren | R.J. Okkersen / I. Wapperom | 1 juli 2026 / 18 september 2026 |
| 9 | Voorstel prijsverhoging Insights per 1 januari 2027 | D. Achterberg | 18 september 2026 |
| 10 | Advies over break-optie uitbreiding De Spilhoek | F.A. van Dalsem | 18 september 2026 |

Aldus vastgesteld in de vergadering van 18 september 2026.

___
dr. A.L. Venhuizen
voorzitter raad van commissarissen

___
F.A. van Dalsem
namens het bestuur
