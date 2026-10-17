# INFORMATIEBEVEILIGINGSBELEID NOVIQO B.V.
_kenmerk NOV-SEC-2026-001 – versie 2.0 – januari 2026_

## Documentgegevens

| Onderdeel | Gegevens |
|---|---|
| Eigenaar (ISMS-eigenaar) | Bas Hoekwater, DevOps lead & security officer |
| Bestuurlijk verantwoordelijk | R.J. Okkersen, bestuurder (CTO) |
| Vastgesteld door | Bestuur Noviqo B.V. op 19 januari 2026 |
| Geldig voor | Alle medewerkers, stagiairs, freelancers en leveranciers met toegang tot informatie of systemen van Noviqo |
| Classificatie | Intern |
| Normenkader | NEN-EN-ISO/IEC 27001:2023 (gelijk aan ISO/IEC 27001:2022), ISO/IEC 27002:2022; aansluiting op de Baseline Informatiebeveiliging Overheid (BIO) voor overheidsklanten |
| Herziening | Jaarlijks in januari, of eerder bij ingrijpende wijzigingen |
| Vervangt | Informatiebeveiligingsbeleid versie 1.2 (maart 2024) |

## 1. Inleiding en doel

Noviqo levert met PlanGrip een SaaS-dienst waarin ongeveer 240 klanten de planning van hun medewerkers vastleggen. Die klanten vertrouwen ons gegevens toe over de beschikbaarheid, inzet en afwezigheid van duizenden mensen. Betrouwbaarheid, vertrouwelijkheid en integriteit van die gegevens zijn de kern van ons product.
Dit beleid legt vast hoe Noviqo informatiebeveiliging organiseert. Het is het hoogste document in het managementsysteem voor informatiebeveiliging (ISMS). Onderliggende procedures en standaarden werken het beleid uit.
Versie 2.0 is een volledige herziening. Aanleidingen zijn het datalek van juni 2025, de lancering van PlanGrip Insights met een AI-subverwerker buiten de EER, de groei naar 31 medewerkers, de komst van een raad van commissarissen, en het besluit om het ISMS te laten certificeren volgens ISO 27001.

## 2. Ambitie: ISO 27001-certificering eind 2026

Noviqo streeft naar ISO/IEC 27001-certificering van het ISMS uiterlijk 31 december 2026. Directe aanleiding is de Europese aanbesteding van Gemeente Lindewoude voor een planningsoplossing voor de buitendienst. De aanbestedingsstukken eisen dat de leverancier uiterlijk 31 december 2026 beschikt over een geldig ISO 27001-certificaat en tot dat moment aantoonbaar werkt volgens de BIO. Ook andere Enterprise-klanten vragen steeds vaker om certificering.

| Mijlpaal | Planning |
|---|---|
| Vaststelling beleid en scope | januari 2026 |
| Risicoanalyse en Verklaring van Toepasselijkheid (VvT) | maart 2026 |
| Implementatie beheersmaatregelen | maart tot en met augustus 2026 |
| Interne audit (externe auditor, niet de certificerende instelling) | september 2026 |
| Directiebeoordeling | september 2026 |
| Fase 1-audit certificerende instelling Certivaart B.V. | oktober 2026 |
| Fase 2-audit | november-december 2026 |

### 2.1 Scope van het ISMS

De scope omvat de ontwikkeling, het beheer, de hosting (via Wolkenrand Hosting B.V.) en de ondersteuning van PlanGrip, PlanGrip Veld en PlanGrip Insights, inclusief de ondersteunende processen HR, inkoop en klantcontact, uitgevoerd vanuit het kantoor aan de Verzonnelkade 88 in Amsterdam en op afstand.

## 3. Beleidsuitgangspunten

- Informatiebeveiliging is een verantwoordelijkheid van iedereen, met eindverantwoordelijkheid bij het bestuur.
- Maatregelen zijn risicogestuurd: wij beschermen informatie in verhouding tot de waarde ervan en de dreigingen.
- Wij werken volgens het principe van minimale rechten (least privilege) en functiescheiding.
- Beveiliging is onderdeel van het ontwikkelproces (security by design) en van privacy by design.
- Klantdata wordt uitsluitend verwerkt binnen de EER, tenzij een klant uitdrukkelijk heeft ingestemd met een subverwerker buiten de EER en de doorgifte voldoet aan hoofdstuk V AVG.
- Wij leren van incidenten en meten de werking van maatregelen.

## 4. Organisatie en rollen

| Rol | Invulling | Belangrijkste verantwoordelijkheden |
|---|---|---|
| Bestuur | F.A. van Dalsem, R.J. Okkersen | Eindverantwoordelijk; stelt beleid en risicobereidheid vast; jaarlijkse directiebeoordeling |
| Bestuurlijk portefeuillehouder | R.J. Okkersen | Aanspreekpunt bestuur voor ISMS, rapporteert aan de raad van commissarissen |
| ISMS-eigenaar en security officer | Bas Hoekwater | Onderhoud ISMS, risicoanalyse, VvT, incidentcoördinatie, beveiligingsmonitoring, certificeringstraject |
| Legal & privacy officer | Lieke Dorrestein | AVG-naleving, DPIA's, verwerkersovereenkomsten, datalekbeoordeling, leveranciersbeoordeling (juridisch) |
| Security forum | ISMS-eigenaar, privacy officer, CTO, Customer Success lead, Office & HR manager | Maandelijks overleg over risico's, incidenten, voortgang en uitzonderingen |
| Systeemeigenaren | Per systeem aangewezen (zie verwerkingsregister) | Toegangsbeheer en periodieke review van het eigen systeem |
| Medewerkers en freelancers | Allen | Naleving van dit beleid en de gedragscode, melden van incidenten |

De raad van commissarissen ontvangt elk kwartaal een rapportage over de stand van informatiebeveiliging, incidenten en het certificeringstraject.

## 5. Risicomanagement

De ISMS-eigenaar voert ten minste eenmaal per jaar en bij grote wijzigingen een risicoanalyse uit volgens ISO/IEC 27005. Risico's worden beoordeeld op kans en impact (schaal 1 tot 5). Risico's met een score van 12 of hoger worden door het bestuur geaccepteerd of behandeld. De Verklaring van Toepasselijkheid motiveert per beheersmaatregel uit bijlage A van ISO 27001 (93 maatregelen) of deze van toepassing is en hoe deze is geïmplementeerd.

## 6. Classificatie van informatie

| Niveau | Omschrijving | Voorbeelden | Basisregels |
|---|---|---|---|
| Openbaar | Bedoeld voor publicatie | Website, marketingmateriaal | Geen beperkingen |
| Intern | Voor medewerkers, beperkte schade bij openbaarmaking | Procesbeschrijvingen, dit beleid | Alleen in Noviqo-systemen; delen met derden na afweging |
| Vertrouwelijk | Schade voor Noviqo, klanten of betrokkenen bij openbaarmaking | Klantdata, contracten, personeelsgegevens, broncode, pentestrapporten | Toegang op need-to-know; versleuteld delen; niet op privé-apparaten |
| Strikt vertrouwelijk | Ernstige schade bij openbaarmaking | Verzuimdossiers, cryptografische sleutels, beheerwachtwoorden, investeringsdocumenten | Benoemde personen; versleutelde opslag; delen alleen met toestemming eigenaar |

Klantdata in PlanGrip geldt altijd minimaal als vertrouwelijk. Afwezigheidstypen en verzuimgegevens van klantmedewerkers worden behandeld als strikt vertrouwelijk.

## 7. Toegangsbeheer

- Toegang wordt verleend op basis van rol en noodzaak. Aanvragen lopen via de leidinggevende en worden vastgelegd in Ticketvlinder.
- Beheertoegang tot productie (Kubernetes, databases, cloudconsole Wolkenrand) is voorbehouden aan de DevOps lead, de senior developer en maximaal twee aangewezen developers. Freelancers krijgen geen permanente productietoegang.
- Productietoegang verloopt via een bastionhost met just-in-time-toegang van maximaal 8 uur, vastgelegd in de auditlog.
- Toegang tot klantdata voor support gebeurt alleen na een ticket en, bij Enterprise-klanten, na toestemming van de klantbeheerder ("support access" in de applicatie, maximaal 72 uur).
- Systeemeigenaren reviewen elk kwartaal alle accounts en rechten. Beheerrechten worden maandelijks gereviewd.
- Bij uitdiensttreding of einde opdracht worden alle accounts uiterlijk op de laatste werkdag om 17:00 uur geblokkeerd. HR meldt vertrek ten minste vijf werkdagen vooraf aan de security officer.

### 7.1 Authenticatie en MFA

- Multifactorauthenticatie is verplicht voor alle medewerkersaccounts, alle beheertoegang en alle SaaS-diensten die Noviqo gebruikt. Bij voorkeur phishingbestendig (FIDO2-sleutel); de DevOps-afdeling gebruikt uitsluitend FIDO2-sleutels.
- Wachtwoorden hebben minimaal 14 tekens, worden niet hergebruikt en worden opgeslagen in de zakelijke wachtwoordmanager. Periodiek wijzigen is niet verplicht; wijzigen wel bij vermoeden van compromittering.
- In PlanGrip is MFA verplicht voor alle klantbeheerders. Enterprise-klanten kunnen SSO via SAML 2.0 of OpenID Connect inrichten.
- Servicesleutels en API-tokens worden beheerd in de secrets-vault en ten minste jaarlijks geroteerd.

## 8. Cryptografie

| Toepassing | Standaard |
|---|---|
| Data in transit | TLS 1.2 minimaal, TLS 1.3 voorkeur; HSTS op alle publieke domeinen |
| Data at rest (databases, objectopslag, back-ups) | AES-256, sleutels beheerd in de key-management-dienst van Wolkenrand |
| Wachtwoorden PlanGrip-gebruikers | Argon2id |
| Laptops | Volledige schijfversleuteling, afgedwongen via MDM |
| Pseudonimisering Insights | HMAC-SHA-256 met tenantgebonden sleutel; sleutels uitsluitend in NL |
| Sleutelbeheer | Rotatie data-encryptiesleutels jaarlijks; toegang tot sleutelbeheer alleen voor DevOps lead en CTO |

## 9. Logging en monitoring

- Alle productiesystemen loggen authenticatie, beheeracties, wijzigingen in rechten, exports en API-aanroepen naar centrale logopslag bij Wolkenrand.
- Logs zijn alleen-lezen. Audit- en toegangslogs worden 12 maanden bewaard, applicatielogs 90 dagen (conform het bewaarbeleid). Foutmonitoring verloopt via Spoorlicht Monitoring GmbH, waarbij planninginhoud vóór verzending wordt gemaskeerd.
- Geautomatiseerde alerts bestaan onder meer voor: herhaalde mislukte inlogpogingen, inloggen vanuit een ongebruikelijk land, bulkexports boven 5.000 records, nieuwe beheeraccounts en API-aanroepen naar andere tenants.
- Alerts met prioriteit hoog worden 24/7 doorgezet naar de dienstdoende engineer (piketrooster van vier personen).
- Logs worden niet gebruikt voor het beoordelen van prestaties van medewerkers.

## 10. Veilige ontwikkeling en wijzigingsbeheer

- Alle code wordt gereviewd door een tweede developer voordat deze wordt samengevoegd. Wijzigingen in authenticatie, autorisatie, export en cryptografie vereisen review door de senior developer of de security officer.
- De CI-pijplijn voert statische codeanalyse, afhankelijkheidsscans en geautomatiseerde tests uit, waaronder tests op tenantscheiding en gedeelde links.
- Wijzigingen in productie vinden plaats volgens het wijzigingsproces; databasemigraties en andere wijzigingen met hoog risico alleen in het onderhoudsvenster en na een geslaagde proef op een productiegetrouwe acceptatieomgeving.
- Eenmaal per jaar laat Noviqo een onafhankelijke penetratietest uitvoeren, en daarnaast bij ingrijpende nieuwe functionaliteit. Bevindingen met risico hoog worden binnen 14 dagen verholpen, midden binnen 60 dagen en laag binnen 180 dagen of gemotiveerd geaccepteerd.

## 11. Leveranciersbeheer

- Leveranciers die toegang hebben tot vertrouwelijke informatie, worden vooraf beoordeeld op beveiliging en privacy (vragenlijst, certificaten, assurancerapporten).
- Met iedere leverancier die persoonsgegevens verwerkt, sluit Noviqo een verwerkersovereenkomst. Subverwerkers voor klantdata staan op de subverwerkerslijst; wijzigingen worden aan klanten aangekondigd volgens hun verwerkersovereenkomst.
- Bij doorgifte buiten de EER voert de legal & privacy officer een transfer impact assessment uit.
- Kritieke leveranciers worden jaarlijks herbeoordeeld:

| Leverancier | Dienst | Kritikaliteit | Zekerheid |
|---|---|---|---|
| Wolkenrand Hosting B.V. | Hosting PlanGrip | Kritiek | ISO 27001, NEN 7510, ISAE 3402 type II |
| Dendra AI Inc. | Taalmodel Insights | Hoog | SOC 2 type II, DPF-certificering, TIA 28 oktober 2025 |
| Klantloep CRM B.V. | CRM | Middel | ISO 27001, SOC 2 type II |
| Ticketvlinder B.V. | Support | Middel | ISO 27001 |
| Postbaken B.V. | Systeem-e-mails PlanGrip | Middel | ISO 27001 |
| Spoorlicht Monitoring GmbH | Foutmonitoring | Middel | ISO 27001 |
| Salariswijs B.V. | Salarisadministratie | Middel | ISAE 3402 type II |

## 12. Incidentbeheer

Iedere medewerker meldt een (vermoedelijk) beveiligingsincident of datalek direct via securitymeldpunt@noviqo.example of telefonisch bij de dienstdoende engineer. De security officer coördineert de afhandeling; de legal & privacy officer beoordeelt binnen 24 uur of sprake is van een inbreuk in verband met persoonsgegevens en of klanten moeten worden geïnformeerd (binnen de termijnen uit de verwerkersovereenkomsten, de kortste is 24 uur). Alle incidenten worden geregistreerd in het datalekregister. Na ieder incident met prioriteit hoog volgt binnen 10 werkdagen een evaluatie.

## 13. Bedrijfscontinuïteit

Het business continuity- en uitwijkplan PlanGrip legt de hersteldoelen (RTO en RPO), scenario's en verantwoordelijkheden vast. Het plan wordt jaarlijks getest met een restore-test en een tabletop-oefening.

## 14. Personeel en bewustzijn

- Nieuwe medewerkers en freelancers ondertekenen een geheimhoudingsverklaring en volgen binnen hun eerste maand de training beveiliging en privacy.
- Alle medewerkers volgen jaarlijks een opfristraining en nemen deel aan ten minste twee phishingsimulaties per jaar.
- Developers volgen jaarlijks een training veilige ontwikkeling (OWASP Top 10).
- Werken op afstand mag uitsluitend met een door Noviqo beheerde laptop; openbare wifi alleen met de bedrijfs-VPN.

## 15. Wet- en regelgeving

Dit beleid ondersteunt naleving van onder meer de AVG, de Uitvoeringswet AVG, de AI-verordening en contractuele verplichtingen jegens klanten (waaronder de GIBIT en de BIO voor overheidsklanten). Noviqo valt op basis van omvang naar verwachting niet zelf onder de Cyberbeveiligingswet (implementatie NIS2), maar verwacht dat klanten die daar wel onder vallen, ketenverplichtingen aan Noviqo opleggen. Het ISMS is daarop ingericht.

## 16. Uitzonderingen en handhaving

Afwijkingen van dit beleid zijn alleen toegestaan na schriftelijke goedkeuring door de security officer, met een vastgelegde termijn en motivering; afwijkingen met een risicoscore van 12 of hoger vereisen goedkeuring door het bestuur. Overtreding van dit beleid kan leiden tot arbeidsrechtelijke of contractuele maatregelen.

## Versiehistorie

| Versie | Datum | Wijziging | Auteur |
|---|---|---|---|
| 1.0 | september 2023 | Eerste beleid | R.J. Okkersen |
| 1.1 | november 2023 | MFA verplicht voor alle beheertoegang | R.J. Okkersen |
| 1.2 | maart 2024 | Rol security officer toegevoegd (in te vullen per 1 juli 2024) | R.J. Okkersen |
| 2.0 | januari 2026 | Volledige herziening: ISO 27001-scope en certificeringsambitie, classificatie, cryptografietabel, leveranciersbeheer incl. Dendra AI, logging, lessen datalek juni 2025 | B. Hoekwater, L. Dorrestein |

___
F.A. van Dalsem, bestuurder (CEO)

___
R.J. Okkersen, bestuurder (CTO)
