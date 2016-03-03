BEGIN;
COPY kn_codes (nam, cod, val) FROM stdin;
CDE	1	Ťarcha
CDE	2	Iný údaj
CDE	3	Titul nadobudnutia
CDE	4	Poznámka
DNP	1	Zariadenie obchodu
DNP	2	Garáž
DNP	3	Zariadenie verejnej správy a administratívy
DNP	4	Zariadenie služieb (výrobné, nevýrobné, opravárenské)
DNP	5	Zariadenie školské a výchovné
DNP	6	Zariadenie kultúrne a osvetové
DNP	7	Zariadenie stravovacie
DNP	8	Skladový priestor
DNP	9	Zariadenie zdravotníckej a sociálnej starostlivosti
DNP	10	Telovýchovné a športové zariadenie
DNP	12	Iný nebytový priestor
DON	100	Chránená nehnuteľnosť
DON	101	Chránená krajinná oblasť
DON	102	Národný park
DON	103	Chránený areál
DON	104	Prírodná rezervácia (národná prírodná rezervácia)
DON	105	Prírodná pamiatka (národná prírodná pamiatka)
DON	106	Chránený krajinný prvok
DON	107	Ochranné pásmo chráneného územia (II. - IV. stupeň)
DON	108	Chránené vtáčie územie
DON	109	Chránený strom a jeho ochranné pásmo
DON	200	Chránená nehnuteľnosť
DON	201	Nehnuteľná kultúrna pamiatka (národná kultúrna pamiatka)
DON	202	Pamiatková rezervácia
DON	203	Pamiatková zóna
DON	204	Ochranné pásmo nehnuteľnej kultúrnej pamiatky, pamiatkovej rezervácie alebo pamiatkovej zóny
DON	300	Chránená nehnuteľnosť
DON	301	Kúpeľné územie
DON	302	Prírodný liečivý zdroj alebo prírodný zdroj minerálnej stolovej vody
DON	303	Ochranné pásmo kúpeľného územia
DON	304	Ochranné pásmo prírodného liečivého zdroja alebo prírodného zdroja minerálnej stolovej vody
DON	401	Chránené ložiskové územie
DON	500	Chránená nehnuteľnosť
DON	501	Chránená vodohospodárska oblasť
DON	502	Ochranné pásmo vodárenských zdrojov (I. - III. stupeň)
DON	503	Ochranné pásmo vodnej stavby
DON	601	Chránená značka geodetického bodu
DON	602	Ochranné pásmo geodetického bodu
DON	801	Iná ochrana
DRP	2	Orná pôda
DRP	3	Chmeľnica
DRP	4	Vinica
DRP	5	Záhrada
DRP	6	Ovocný sad
DRP	7	Trvalý trávny porast
DRP	10	Lesný pozemok
DRP	11	Vodná plocha
DRP	13	Zastavaná plocha a nádvorie
DRP	14	Ostatná plocha
DRF	1	informatívna
DRF	2	obmedzujúca
DRV	1	Oprávnená držba k pozemku
DRV	2	Nájom k pozemku
DRV	3	Spoluvlastníctvo k pozemku pod stavbou
DRV	4	Vlastník pozemku je vlastníkom stavby postavenej na tomto pozemku
DRV	5	Vlastník pozemku nie je vlastníkom stavby postavenej na tomto pozemku (pozemkoch)
DRV	7	Právny vzťah nie je evidovaný v súbore popisných informácií katastra nehnuteľností
DRV	9	Duplicitné alebo viacnásobné vlastníctvo k tej istej nehnuteľnosti alebo k jej časti
BNP	1	Byt
BNP	2	Nebytový priestor
BNP	3	Rozostavaný byt
BNP	4	Rozostavaný nebytový priestor
PRP	0	Pozemok nezaradený do pôdneho fondu
PRP	1	Pozemok patrí do poľnohospodárskeho pôdneho fondu
PRP	2	Pozemok patrí do lesného pôdneho fondu
SPN	1	Pozemok nie je spoločnou nehnuteľnosťou
SPN	2	Pozemok je spoločnou nehnuteľnosťou
TUC	1	Vlastník
TUC	2	Správca
TUC	3	Nájomca
TUC	4	Iná oprávnená osoba z práv k nehnuteľnosti
UMP	1	Pozemok je umiestnený v zastavanom území obce
UMP	2	Pozemok je umiestnený mimo zastavaného územia obce
UMS	1	Stavby postavané na zemskom povrchu
UMS	2	Podzemné stavby
UMS	3	Nadzemné stavby
PKK	1	Pozemok využívaný pre rastlinnú výrobu, na ktorom sa pestujú obilniny, okopaniny, krmoviny, technické plodiny, zelenina a iné poľnohospodárske plodiny alebo pozemok dočasne nevyužívaný pre rastlinnú výrobu
PKK	2	Pozemok vysadený chmeľom alebo pozemok vhodný na pestovanie chmeľu, na ktorom bol chmeľ dočasne odstránený
PKK	3	Pozemok, na ktorom sa pestuje vinič alebo pozemok vhodný na pestovanie viniča, na ktorom bol vinič dočasne odstránený
PKK	4	Pozemok prevažne v zastavanom území obce alebo v záhradkárskej osade, na ktorom sa pestuje zelenina, ovocie, okrasná nízka a vysoká zeleň a iné poľnohospodárske plodiny
PKK	5	Pozemok v rámci záhradného centra, na ktorom sa pestuje okrasná nízka a vysoká zeleň alebo pozemok dočasne využívaný na výrobu trávnikových kobercov, vianočných stromčekov a inej okrasnej zelene
PKK	6	Pozemok súvisle vysadený ovocnými stromami, ovocnými krami a ovocnými sadenicami na jednom mieste, jedným alebo viacerými druhmi
PKK	7	Pozemok lúky a pasienku trvalo porastený trávami alebo pozemok dočasne nevyužívaný pre trvalý trávny porast
PKK	8	Na pozemku je postavený skleník, japan, parenisko a iné
PKK	9	Na pozemku je škôlka pre chmeľové sadivo, viničová škôlka, škôlka pre ovocné, alebo okrasné dreviny, lesná škôlka alebo semenný sad a iné
PKK	10	Na pozemku je účelová ochranná poľnohospodárska a ekologická zeleň proti erozívnych opatrení a opatrení na zabezpečenie ekologickej stability územia
PKK	11	Vodný tok (prirodzený - rieka, potok; umelý - kanál, náhon a iné)
PKK	12	Vodná plocha (jazero, umelá vodná nádrž, odkryté podzemné vody - štrkovisko, bagrovisko a iné)
PKK	13	Rybník - umelá vodná nádrž určená na chov rýb vrátane stavieb
PKK	14	Močiar
PKK	15	Pozemok, na ktorom je postavená bytová budova označená súpisným číslom
PKK	16	Pozemok, na ktorom je postavená nebytová budova označená súpisným číslom
PKK	17	Pozemok, na ktorom je postavená budova bez označenia súpisným číslom
PKK	18	Pozemok, na ktorom je dvor
PKK	19	Pozemok, na ktorom je spoločný dvor
PKK	20	Pozemok, na ktorom je postavená inžinierska stavba - železničná, lanová a iná dráha a jej súčasti
PKK	21	Pozemok, na ktorom je postavená inžinierska stavba - diaľnica a rýchlostná komunikácia a jej súčasti
PKK	22	Pozemok, na ktorom je postavená inžinierska stavba - cestná, miestna a účelová komunikácia, lesná cesta, poľná cesta, chodník, nekryté parkovisko a ich súčasti
PKK	23	Pozemok, na ktorom je postavená inžinierska stavba - vzletová, pristávacia a rolovacia dráha letiska a jej súčasti
PKK	24	Pozemok, na ktorom je postavená inžinierska stavba - prístav, plavebný kanál a komora, priehrada a iná ochranná hrádza, závlahová a melioračná sústava a jej súčasti
PKK	25	Pozemok, na ktorom je postavená ostatná inžinierska stavba a jej súčasti
PKK	26	Pozemok, na ktorom je rozostavaná stavba
PKK	27	Pozemok, na ktorom je zrúcanina
PKK	28	Pozemok, na ktorom je postavený vstupný portál do podzemnej stavby alebo pivnice
PKK	29	Pozemok, na ktorom je okrasná záhrada, uličná a sídlisková zeleň, park a iná funkčná zeleň a lesný pozemok na rekreačné a poľovnícke využívanie
PKK	30	Pozemok, na ktorom je ihrisko, štadión, kúpalisko, športová dráha, autokemp, táborisko a iné
PKK	31	Pozemok, na ktorom je botanická a zoologická záhrada, skanzen, amfiteáter, pamätník a iné
PKK	32	Pozemok, na ktorom je cintorín alebo urnový háj
PKK	33	Pozemok, ktorý slúži na ťažbu nerastov a surovín
PKK	34	Pozemok, na ktorom je manipulačná a skladová plocha, objekt a stavba slúžiaca lesnému hospodárstvu
PKK	35	Pozemok, na ktorom je skládka odpadu
PKK	36	Pozemok, ktorý nie je využívaný žiadnym z uvedených spôsobov
PKK	37	Pozemok, na ktorom sú skaly, svahy, rokliny, výmole, vysoké medze krovím alebo kamením a iné plochy, ktoré neposkytujú trvalý úžitok
PKK	38	Pozemok s lesným porastom, dočasne bez lesného porastu na účely obnovy lesa alebo po vykonaní náhodnej ťažby
PKK	99	Pozemok využívaný podľa druhu pozemku
DRS	1	Priemyselná budova
DRS	2	Poľnohospodárska budova
DRS	3	Budova železníc a dráh
DRS	4	Budova pre správu a údržbu diaľnic a rýchlostných ciest
DRS	5	Budova letísk
DRS	6	Iná dopravná a telekomunikačná budova (budova prístavu, garáže, kryté parkovisko, budova na rádiové a televízne vysielanie a iné)
DRS	7	Samostatne stojaca garáž
DRS	8	Budova lesného hospodárstva (horáreň, technická prevádzková stavba a iné)
DRS	9	Bytový dom
DRS	10	Rodinný dom
DRS	11	Budova pre školstvo, na vzdelávanie a výskum
DRS	12	Budova zdravotníckeho a sociálneho zariadenia
DRS	13	Budova ubytovacieho zariadenia
DRS	14	Budova obchodu a služieb
DRS	15	Administratívna budova
DRS	16	Budova pre kultúru a na verejnú zábavu (múzeum, knižnica a galéria)
DRS	17	Budova na vykonávanie náboženských aktivít, krematóriá a domy smútku
DRS	18	Budova technickej vybavenosti sídla (výmenníková stanica, budova na rozvod energií, čerpacia a prečerpávacia stanica, úpravňa vody, transformačná stanica a rozvodňa, budova vodojemu alebo čistiarne odpadových vôd a iné)
DRS	19	Budova pre šport a na rekreačné účely
DRS	20	Iná budova
DRS	21	Rozostavaná budova
DRS	22	Polyfunkčná budova
DRS	23	Inžinierska stavba
TVL	0	Vlastník, ktorého miesto trvalého pobytu alebo sídlo sú známe
TVL	1	Správa majetku štátu, kde je vlastníkom Slovenská republika
TVL	2	Správa majetku obce, kde vlastníkom je obec
TVL	3	Vlastník je známy, ale miesto jeho trvalého pobytu alebo sídla nie je známe
TVL	4	Vlastník nie je známy
TVL	5	Evidovaný vlastník, ktorý nemôže do rozhodnutia správneho orgánu s pozemkom  nakladať podľa § 12 ods. 4 zákona Národnej rady Slovenskej republiky č. 180/1995 Z. z. o niektorých opatreniach na usporiadanie vlastníctva
TVL	6	Poručiteľ, po ktorom sa prihlásil domnelý dedič alebo dedičia (dedičské konanie zatiaľ nebolo začaté alebo skončené)
TVL	7	Poručiteľ, ktorého dedič nie je známy
TVL	8	Právnická osoba, ktorá zanikla a jej právny nástupca nie je známy
\.
END;