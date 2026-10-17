# REACTIE OP AANSPRAKELIJKSTELLING
_ons kenmerk RAV 26-0147/PCZ – dossier Noviqo NOV-GES-2026-002 – uw kenmerk LV 2026.0311/SAV_

**Ravelijn Advocaten** (fictief)
Prinsengracht 999, 1017 ZZ Amsterdam (fictief)
T 020-0000000 (fictief) – p.zandbergen@ravelijn.example

**Aan:** Lindeboom & Vos Advocaten, t.a.v. mr. S.A. Vos, Stationsplein-Oost 41, 7300 CC Apeldoorn

**Datum:** Amsterdam, 1 april 2026

**Betreft:** Bouwgroep Hazelaar B.V. / Noviqo B.V. – storing PlanGrip 3 en 4 maart 2026

**Per e-mail en per post**

Geachte confrère,

Ik schrijf u namens Noviqo B.V. ("Noviqo") in reactie op uw brief van 18 maart 2026, waarin u Noviqo namens uw cliënte, Bouwgroep Hazelaar B.V. ("Hazelaar"), aansprakelijk stelt voor de gevolgen van de storing van PlanGrip op 3 en 4 maart 2026 en een bedrag van EUR 38.400 vordert.

Vooropgesteld: Noviqo betreurt de storing en het ongemak dat Hazelaar daarvan heeft ondervonden. Zij hecht aan de relatie met Hazelaar, die sinds september 2024 klant is. Dat neemt niet weg dat Noviqo de aansprakelijkheid voor de gevorderde schade van de hand wijst. Ik licht dat hieronder toe en sluit af met een voorstel om de kwestie in der minne te regelen.

## 1. Aanvulling en correctie van de feiten

1.1 De databasemigratie is op 24 februari 2026, vijf werkdagen vooraf, via het supportportaal aangekondigd voor dinsdag 3 maart 2026 van 22:00 tot 02:00 uur, buiten kantooruren zoals gedefinieerd in artikel 1.2 sub a SLA (07:00–19:00 uur op werkdagen). De aankondiging vermeldde dat de dienst gedurende het onderhoudsvenster onbereikbaar kon zijn.
1.2 De migratie is voorafgaand drie keer volledig doorlopen op een productiegetrouwe acceptatieomgeving bij Wolkenrand Hosting, op 17, 19 en 23 februari 2026, inclusief het terugvalscenario. Bij de uitvoering op 3 maart 2026 bleek dat de replicatie tussen het oude en het nieuwe databasecluster onder productiebelasting een inconsistentie opleverde die in de testomgeving niet was opgetreden. Het terugvalscenario is om 01:30 uur gestart, maar kon niet worden voltooid, omdat ook de bronomgeving inmiddels gedeeltelijk was aangepast. Noviqo heeft vervolgens besloten tot een gecontroleerde restore van de back-up die om 21:45 uur, direct vóór de migratie, was gemaakt. Er is geen klantdata verloren gegaan.
1.3 Om 02:00 uur, bij het verstrijken van het onderhoudsvenster, heeft Noviqo het incident als Prioriteit 1 geregistreerd. De statuspagina is vanaf 23:15 uur ieder uur bijgewerkt. Om 06:40 uur is aan alle beheerders van klanten een e-mail verzonden met uitleg en een verwachte hersteltijd.
1.4 Anders dan u stelt, heeft Noviqo wel een workaround geboden. Om 07:30 uur is aan alle Teams- en Enterprise-klanten aangeboden een export van de dagplanning van 4 maart 2026, afkomstig uit de back-up van 21:45 uur, als CSV- en PDF-bestand per e-mail te leveren. De beheerder van Hazelaar heeft dat aanbod om 09:40 uur aanvaard; de export is om 10:15 uur aan hem verzonden. Andere klanten die het aanbod direct aanvaardden, hadden de export vóór 08:30 uur in handen.
1.5 De dienst was op 4 maart 2026 om 16:58 uur volledig hersteld. De oorzaakanalyse is op 20 maart 2026 aan de heer Hazelaar verzonden en is voor de volledigheid als bijlage 1 bijgevoegd.

## 2. De SLA: beschikbaarheid, hersteltijd en servicecredits

2.1 **Beschikbaarheid.** Op grond van artikel 1.2 sub a SLA valt gepland onderhoud dat ten minste vijf werkdagen vooraf is aangekondigd en buiten kantooruren plaatsvindt, tot maximaal vier uur per maand, buiten de beschikbaarheidsmeting. De eerste vier uur (22:00 tot 02:00 uur) vallen daaronder. De SLA koppelt deze uitzondering aan het tijdstip en de aankondiging, niet aan het al dan niet slagen van het onderhoud. De meetbare onbeschikbaarheid bedraagt daarmee 15 uur (02:00 tot circa 17:00 uur). De beschikbaarheid over maart 2026 bedraagt (744 – 15) / 744 = 97,98%. Op grond van artikel 7.1 sub b SLA hoort daarbij een servicecredit van 10%, ofwel EUR 147,50.
2.2 **Hersteltijd.** Noviqo erkent dat de hersteltijd voor een Prioriteit 1-incident van 8 klokuren, gerekend vanaf 02:00 uur, niet volledig is gehaald voor zover het gaat om herstel van de dienst. De workaround als bedoeld in artikel 3.1 sub a SLA was om 07:30 uur beschikbaar en is aan Hazelaar om 10:15 uur geleverd, 15 minuten na het verstrijken van die termijn, en dat als gevolg van de late reactie van Hazelaar zelf.
2.3 **Exclusieve remedie.** Artikel 7.3 SLA bepaalt dat servicecredits "de enige financiële remedie" zijn voor het niet halen van service levels. Service levels zijn alle in de SLA vastgelegde normen, waaronder de beschikbaarheid (artikel 1) en de respons- en hersteltijden (artikel 3). De SLA maakt geen onderscheid tussen "gedeeltelijke" en "totale" uitval; uitval van 19 uur is precies het scenario waarvoor de hoogste staffel van 25% en de ontbindingsmogelijkheid van artikel 7.3 zijn opgenomen. De kwalificatie van de hersteltijd als resultaatsverplichting in artikel 3.3 SLA heeft betekenis voor de vraag óf er een tekortkoming is; zij doet niet af aan de door partijen afgesproken gevolgen daarvan. Hazelaar is een professionele partij met ruim 60 medewerkers, die de SLA bij het aangaan van de overeenkomst heeft kunnen beoordelen.

## 3. Aansprakelijkheidsbeperking en uitsluiting van gevolgschade

3.1 Voor zover Hazelaar, naast de servicecredits, aanspraak zou kunnen maken op schadevergoeding op grond van artikel 6:74 BW, wordt die aanspraak beheerst door artikel 6.2 van de SaaS-overeenkomst NOV-VRK-2024-031: de aansprakelijkheid is beperkt tot directe schade en tot maximaal de in het betreffende kalenderjaar door Hazelaar betaalde vergoedingen, en aansprakelijkheid voor indirecte schade is uitgesloten.
3.2 **Indirecte schade.** Artikel 8.1 van de SaaS-overeenkomst verklaart de algemene voorwaarden van Noviqo (versie 2.1) van toepassing; de overeenkomst gaat alleen voor "bij strijdigheid". Er is geen strijdigheid: artikel 6.2 van de SaaS-overeenkomst sluit indirecte schade uit, en artikel 8.2 van de algemene voorwaarden vult dat begrip in, met uitdrukkelijke vermelding van "schade door bedrijfsstagnatie". De door Hazelaar gevorderde posten zijn bij uitstek stagnatieschade: kosten van medewerkers en materieel die door het stilvallen van de bedrijfsvoering onproductief zijn geweest. De contra proferentem-regel vindt hier geen toepassing; de bepalingen zijn helder en tussen professionele partijen gesloten.
3.3 **Maximum.** In het kalenderjaar 2026 heeft Hazelaar tot op heden geen vergoeding aan Noviqo betaald; de jaarvergoeding over de periode oktober 2025 tot en met september 2026 is in oktober 2025 voldaan. Een letterlijke toepassing van artikel 6.2 brengt de aansprakelijkheid voor 2026 op nihil. Ook als men, zoals u ten overvloede doet, de jaarvergoeding van EUR 17.700 als maximum neemt, ligt de vordering daar ruim boven. Het algemene maximum van EUR 50.000 in artikel 8.1 van de algemene voorwaarden is, als hoger bedrag, ten opzichte van de SaaS-overeenkomst niet van toepassing.
3.4 **Geen bewuste roekeloosheid.** De beperkingen gelden niet bij opzet of bewuste roekeloosheid van de bedrijfsleiding (artikel 6.3 SaaS-overeenkomst). Volgens vaste rechtspraak vereist bewuste roekeloosheid dat de bedrijfsleiding zich daadwerkelijk bewust was van het aanmerkelijke risico dat de schade zou ontstaan en zich daardoor niet heeft laten weerhouden. Daarvan is geen sprake. Noviqo heeft de migratie drie maal getest, inclusief het terugvalscenario, haar tijdig aangekondigd en uitgevoerd op een tijdstip dat de SLA uitdrukkelijk toestaat. Artikel 5.1 SLA, dat het venster op zaterdag noemt, bepaalt dat onderhoud daar "zoveel mogelijk" plaatsvindt; het is geen verplichting. Dat een getest scenario onder productiebelasting anders verloopt, kan Noviqo worden aangerekend als tekortkoming, maar niet als bewuste roekeloosheid.
3.5 **Redelijkheid en billijkheid.** Voor het buiten toepassing laten van een exoneratie tussen professionele partijen op grond van artikel 6:248 lid 2 BW is plaats bij uitzondering. Bij de afweging zijn onder meer van belang de aard en ernst van het verwijt, de verhouding tussen de vergoeding (EUR 1.475 per maand) en het gevorderde bedrag, de professionaliteit van partijen en de mogelijkheid voor Hazelaar om zich tegen dit risico te verzekeren of een terugvaloptie te organiseren. Die afweging valt niet uit in het voordeel van Hazelaar.
3.6 **Datalek juni 2025.** Het incident van juni 2025 betrof een fout in een exportfunctie die op 12 juni 2025 binnen een half uur na ontdekking is verholpen en is afgehandeld volgens de verwerkersovereenkomst. Het heeft geen verband met de storing van maart 2026 en speelt geen rol bij de beoordeling daarvan.

## 4. De schade

4.1 Ten overvloede betwist Noviqo de omvang van de gestelde schade:
- a. Loonkosten van medewerkers in vaste dienst zijn ook zonder storing verschuldigd. Schade bestaat alleen voor zover productie daadwerkelijk verloren is gegaan en niet is ingehaald. Daarover vermeldt uw brief niets.
- b. De gemiddelde vertraging van zes uur per vakman is niet onderbouwd. De urenregistratie die u bijvoegt, toont de aanvangstijden per ploeg, maar niet de vertraging ten opzichte van de planning.
- c. Hazelaar beschikt binnen PlanGrip over 50 gebruikersaccounts, terwijl zij stelt dat 64 vakmensen uitsluitend via PlanGrip Veld hun planning ontvingen.
- d. Hazelaar heeft de om 07:30 uur aangeboden workaround pas om 09:40 uur aanvaard. Voor zover schade na 07:30 uur is ontstaan, komt die op grond van artikel 6:101 BW voor rekening van Hazelaar, die de schade had kunnen beperken.
4.2 Buitengerechtelijke incassokosten zijn niet verschuldigd. Nog afgezien van het ontbreken van een verbintenis tot betaling, ziet het Besluit vergoeding voor buitengerechtelijke incassokosten op vorderingen tot betaling van een geldsom die na een aanmaning onbetaald blijven, en niet op een betwiste vordering tot schadevergoeding.
4.3 Uw cliënte stelt dat uw brief geldt als in rechte aanhangig maken in de zin van artikel 8.4 van de algemene voorwaarden. Dat is onjuist. Die bepaling vereist een procedure bij de rechter; een brief volstaat niet. Noviqo houdt Hazelaar aan die termijn.

## 5. Voorstel tot minnelijke regeling

5.1 Zonder erkenning van enige aansprakelijkheid en uitsluitend uit coulance, in het belang van de klantrelatie, stelt Noviqo het volgende voor:
- a. Noviqo kent Hazelaar de servicecredit toe van de hoogste staffel van 25% (artikel 7.1 sub c SLA), alsof alle 19 uren hebben meegeteld: **EUR 368,75**;
- b. Noviqo verstrekt daarnaast een creditnota ter grootte van drie maandvergoedingen, 3 x EUR 1.475 = **EUR 4.425,00**;
- c. het totaal van **EUR 4.793,75** (exclusief btw) wordt naar keuze van Hazelaar binnen 14 dagen na aanvaarding uitbetaald, of verrekend met de jaarfactuur voor de periode vanaf 1 oktober 2026;
- d. Noviqo voert in 2026 kosteloos een restore-test uit voor de omgeving van Hazelaar (aanvullend op artikel 4.3 SLA) en deelt de resultaten;
- e. Noviqo bevestigt dat zij toekomstige migraties van de productiedatabase uitvoert in het onderhoudsvenster op zaterdag (artikel 5.1 SLA), met een parallelle omgeving waarnaar binnen 30 minuten kan worden teruggeschakeld, en die migraties ten minste tien werkdagen vooraf aankondigt.
5.2 Dit voorstel geldt onder de voorwaarde dat Hazelaar Noviqo finale kwijting verleent ter zake van alle vorderingen in verband met de storing van 3 en 4 maart 2026. Het voorstel blijft van kracht tot en met 22 april 2026 en wordt na aanvaarding vastgelegd in een korte vaststellingsovereenkomst.
5.3 Indien Hazelaar het voorstel niet aanvaardt, kent Noviqo in elk geval de servicecredit van 10% (EUR 147,50) toe die volgens haar uit de SLA voortvloeit, en houdt zij zich het recht voor alle hierboven genoemde verweren te voeren.

## 6. Tot slot

6.1 Noviqo heeft de kwestie gemeld bij haar aansprakelijkheidsverzekeraar. Dat houdt geen erkenning van aansprakelijkheid in.
6.2 Deze brief is geschreven met behoud van alle rechten en weren. Niets in deze brief houdt een erkenning in van aansprakelijkheid of van de gestelde schade.
6.3 Noviqo stelt een gesprek op prijs tussen de heer Hazelaar, mevrouw Van Dalsem en de heer Okkersen, met of zonder advocaten, om de maatregelen na de storing toe te lichten. Ik verneem graag of uw cliënte daarvoor openstaat.

Met collegiale groet,

___
mr. P.C. Zandbergen
advocaat, Ravelijn Advocaten

**Afschrift:** Noviqo B.V., t.a.v. mevrouw F.A. van Dalsem

**Bijlagen:**
- 1. Oorzaakanalyse storing 3 en 4 maart 2026 (versie 1.0, 20 maart 2026), opgesteld door B. Hoekwater
- 2. Aankondiging onderhoud supportportaal d.d. 24 februari 2026
- 3. Logboek statuspagina 3 en 4 maart 2026
- 4. E-mail van Noviqo aan beheerders d.d. 4 maart 2026, 07:30 uur (aanbod export dagplanning)
