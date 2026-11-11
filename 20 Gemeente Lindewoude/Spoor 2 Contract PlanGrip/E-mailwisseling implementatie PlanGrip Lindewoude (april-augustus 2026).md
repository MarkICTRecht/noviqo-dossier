# E-mailwisseling implementatie PlanGrip

*Export uit de mailbox van W.F. Siebenga, contractmanager Gemeente Lindewoude, map "PlanGrip implementatie". Volgorde: nieuwste bericht bovenaan. Aangeleverd door Inkoop en Contractmanagement aan Juridische Zaken op 8 september 2026.*

---

**Van:** Bas Hoekwater &lt;b.hoekwater@noviqo.example&gt;
**Aan:** informatiebeveiliging@lindewoude.example
**CC:** Sem Loonstra; Lieke Dorrestein; W.F. Siebenga
**Datum:** donderdag 20 augustus 2026 11:20
**Onderwerp:** Melding beveiligingsincident PlanGrip, art. 6.4 overeenkomst, ref. INC-2026-017

Geacht meldpunt,

Hierbij melden wij conform artikel 6.4 van de overeenkomst een beveiligingsincident.

Wat: bij de inrichting van de SSO-rolkoppeling voor de livegang zijn op maandag 17 augustus 2026 de rollen van drie gebruikers van team Wijkbeheer onjuist gekoppeld. Daardoor hadden zij leesrechten op de planning van team Handhaving (circa 45 medewerkers; naam, beschikbaarheid en afwezigheidstype, geen reden van afwezigheid).

Ontdekking: naar aanleiding van supportticket #48213, door een gebruiker van de gemeente ingediend op dinsdag 18 augustus 2026 om 16:32 ("ik zie ineens de roosters van Handhaving, klopt dat?"), heeft ons securityteam de toegangslogs op woensdag 19 augustus om 08:50 geanalyseerd en het incident bevestigd.

Maatregelen: rolkoppeling hersteld op 19 augustus om 11:05. De logs tonen dat de drie gebruikers de planning van Handhaving in totaal 7 keer hebben geopend. Er zijn geen gegevens geëxporteerd. Wij hebben een validatiestap aan de SSO-onboarding toegevoegd.

De heer Loonstra heeft de heer Siebenga gisteren al telefonisch geïnformeerd.

Met vriendelijke groet,
Bas Hoekwater
DevOps lead & security officer, Noviqo B.V.

---

**Van:** W.F. Siebenga
**Aan:** E. Nijboer
**Datum:** woensdag 19 augustus 2026 14:20
**Onderwerp:** telefoonnotitie Noviqo rolkoppeling

Erik,

Sem Loonstra belde om 14:05. Bij de SSO-inrichting zijn rollen verkeerd gekoppeld, drie mensen van Wijkbeheer konden de roosters van Handhaving zien. Is vanochtend hersteld volgens hem. Ik heb gezegd dat ik dit niet kan beoordelen en dat hij het formeel via het meldpunt informatiebeveiliging moet melden, zoals in het contract staat. Hij zou dat "vandaag nog" laten doen.

Kun jij het meldpunt vast een seintje geven?

Wim

---

**Van:** E. Nijboer
**Aan:** Sem Loonstra
**CC:** W.F. Siebenga
**Datum:** donderdag 30 juli 2026 09:47
**Onderwerp:** RE: B-07 in productie

Hoi Sem,

Dank, productie draait stabiel. Zoals gepland gaan we per 1 september live met alle teams. Handhaving draait door als pilot.

Wel voor de goede orde: Handhaving heeft vanaf 15 juni ruim 600 werkorders met de hand aan zaken moeten koppelen, omdat de zaakkoppeling er niet was. Onze teamleider schat dat op zo'n 120 uur extra werk. Dat nemen we mee naar het contractoverleg.

Groet,
Erik Nijboer
projectleider I&A, Gemeente Lindewoude

---

**Van:** W.F. Siebenga
**Aan:** Sem Loonstra
**CC:** E. Nijboer
**Datum:** maandag 27 juli 2026 10:12
**Onderwerp:** RE: B-07 in productie

Sem,

Bevestigd: sinds vrijdag 24 juli werken alle koppelingen in productie. Daarmee beschouwen wij de bevindingen B-03 en B-07 als afgesloten.

Groet, Wim

---

**Van:** Sem Loonstra &lt;s.loonstra@noviqo.example&gt;
**Aan:** E. Nijboer; W.F. Siebenga
**Datum:** vrijdag 24 juli 2026 16:58
**Onderwerp:** B-07 in productie

Beste Erik, Wim,

Vandaag om 15:30 is release 3.15.1 met de herstelde zaakkoppeling in productie genomen, na jullie CAB-akkoord van dinsdag. Smoketest geslaagd. Fijn weekend!

Sem

---

**Van:** E. Nijboer
**Aan:** Sem Loonstra
**Datum:** dinsdag 21 juli 2026 15:40
**Onderwerp:** RE: B-07 werkt in acceptatie

CAB is akkoord, jullie mogen vrijdag 24/7 deployen tussen 15:00 en 17:00.

---

**Van:** E. Nijboer
**Aan:** Sem Loonstra
**CC:** W.F. Siebenga
**Datum:** vrijdag 10 juli 2026 11:03
**Onderwerp:** RE: B-07 werkt in acceptatie

Hoi Sem,

Goed nieuws dat B-07 in acceptatie werkt, we hebben het vanochtend getest en het ziet er goed uit.

Productie-deploy kan helaas pas na onze CAB. Die vergadert elke dinsdag. Wijzigingsverzoeken moeten uiterlijk een week van tevoren, op de dinsdag ervoor, binnen zijn. Jullie verzoek kwam donderdag 9 juli binnen, dus dat haalt de CAB van 14 juli niet meer en schuift door naar 21 juli. Sorry, regels zijn regels.

Erik

---

**Van:** Sem Loonstra &lt;s.loonstra@noviqo.example&gt;
**Aan:** E. Nijboer; W.F. Siebenga
**Datum:** vrijdag 3 juli 2026 14:15
**Onderwerp:** B-03 opgelost

Beste Erik, Wim,

B-03 (BAG buitengebied) is opgelost met hotfix 3.14.2, vandaag in productie. Alle adressen in de buitengebieden zijn nu vindbaar. Aan B-07 werken we hard, verwachting volgende week in acceptatie.

Sem

---

**Van:** Sem Loonstra &lt;s.loonstra@noviqo.example&gt;
**Aan:** E. Nijboer
**Datum:** vrijdag 26 juni 2026 17:44
**Onderwerp:** FW: stand B-03 / B-07

Erik, ter info zie hieronder de stand van zaken van onze devs. Volgende week meer.

Sem

> **Van:** Marit Holtrop
> **Aan:** Sem Loonstra; Ruben Okkersen
> **Datum:** vrijdag 26 juni 2026 16:20
> **Onderwerp:** stand B-03 / B-07
>
> Sem, Ruben,
>
> B-03 heeft niks met de sleutels van het zaaksysteem te maken. Onze BAG-import filterde op de woonplaatscode van de kern. De buitengebieden hebben eigen woonplaatscodes, die vielen eruit. Fix is klein, kan volgende week mee. Niet naar de klant: dit hadden we in de test van eind mei al kunnen zien, de testset van de gemeente bevatte alleen adressen in de kern.
>
> B-07 is wel lastig. Hun zaaksysteem geeft in productie andere zaaktype-id's terug dan in de testomgeving. Dat stond niet in de koppelvlakspecificatie die we op 4 juni kregen. Mapping moet opnieuw, schatting twee weken.
>
> Marit

---

**Van:** W.F. Siebenga
**Aan:** Sem Loonstra
**CC:** E. Nijboer; R. Haaksma
**Datum:** maandag 15 juni 2026 16:30
**Onderwerp:** Acceptatie PlanGrip onder voorbehoud

Beste Sem,

Na overleg met Erik en het team Handhaving accepteren wij PlanGrip met ingang van vandaag, **onder voorbehoud van herstel van de blokkerende bevindingen B-03 (BAG buitengebied) en B-07 (zaakkoppeling)**. Wij verwachten herstel binnen 10 werkdagen, conform artikel 3.3 van de overeenkomst. Daarna volgt een hertest.

Wij doen dit zodat Handhaving vast met de pilot kan starten. Wij behouden ons uitdrukkelijk alle rechten uit de overeenkomst voor, waaronder artikel 9.

Met vriendelijke groet,
Wim Siebenga
contractmanager, Gemeente Lindewoude

---

**Van:** E. Nijboer
**Aan:** Sem Loonstra
**CC:** W.F. Siebenga
**Datum:** donderdag 4 juni 2026 09:15
**Onderwerp:** RE: sleutels zaaksysteem

Hoi Sem,

Excuses voor het lange wachten. In de bijlage de API-sleutels voor de testomgeving van het zaaksysteem en de koppelvlakspecificatie (versie 1.4). Onze leverancier ZaakVaart had vertraging met het inrichten van de testomgeving. Ik weet dat dit was toegezegd voor 1 mei.

Erik

---

**Van:** Sem Loonstra &lt;s.loonstra@noviqo.example&gt;
**Aan:** E. Nijboer; W.F. Siebenga
**Datum:** woensdag 27 mei 2026 12:01
**Onderwerp:** Acceptatieomgeving PlanGrip opgeleverd

Beste Erik, Wim,

Goed nieuws: de acceptatieomgeving staat klaar, inclusief SSO-koppeling. De BAG-koppeling werkt in test op basis van de testset die jullie hebben aangeleverd. De koppeling met het zaaksysteem kunnen we pas bouwen zodra we de sleutels en de specificatie hebben. Zoals eerder gemeld komt 1 juni daarmee voor dat onderdeel in gevaar.

Groet,
Sem Loonstra
Customer Success lead, Noviqo B.V.

---

**Van:** Sem Loonstra &lt;s.loonstra@noviqo.example&gt;
**Aan:** E. Nijboer
**Datum:** dinsdag 12 mei 2026 10:20
**Onderwerp:** sleutels zaaksysteem

Hoi Erik,

Hebben jullie al zicht op de sleutels voor de testomgeving van het zaaksysteem? Die waren toegezegd voor 1 mei. Zonder sleutels komt de opleverdatum van 1 juni in gevaar.

Sem

---

**Van:** E. Nijboer
**Aan:** Sem Loonstra
**Datum:** dinsdag 28 april 2026 16:05
**Onderwerp:** RE: planning koppelingen

Sem, de sleutels voor de testomgeving volgen deze week, ZaakVaart is ermee bezig.

Erik
