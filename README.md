[![DOI](https://zenodo.org/badge/204370467.svg)](https://zenodo.org/badge/latestdoi/204370467)

# OBISdat

Features:

- [x] get up-to-date information from [OBIS database](https://obis.org)
- [x] Terminal-based scripts

Software requierements:
* Python 3

#### Installation

Upon downloading this repository, unzip it and move into `OBISdat` directory, then run the following to install excutables:

```Shell
python3 setup.py install
```

Using `git` (optional):

```Shell
git clone https://github.com/Ulises-Rosas/OBISdat.git
cd OBISdat
python3 setup.py install
```

### Usage

The way this executable is used match up with this structure:

```Shell
obis.py [path] [parameters]
```

Paths that [OBIS API](https://api.obis.org) accepts are stated at `[path]` position. It has been tested the following paths so far:

* `country`
* `area`
* `institute`
* `checklist`
* `checklist/redlist`
* `checklist/newest`
* `occurrence`

Each outcome from paths can be modified by adding constraining parameters at `[parameters]` position. Paramenters available are:

* `--taxa` (e.g. `Elasmobranchii Reptilia`)
* `--of` (e.g. `Peru Colombia`)
* `--areaid` 
* `--datasetid`
* `--instituteid`
* `--nodeid`
* `--startdate`
* `--enddate`
* `--startdepth`
* `--enddepth`
* `--geometry`

Only both `--taxa` and `--of` options accept more than one value. While whole output filenames are named in function to the path used, these can also be defined with `--out` option. 

#### Examples

When we use either `country`, `institute` or `area` paths, `--of` option is coupled in order to match requested strings:

```Shell
obis.py institute --of 'Smithsonian Institution'
```
```
id	name	parent	children	records
7553	National Museum of Natural History, Smithsonian Institution	{'id': 17611, 'name': 'Smithsonian Institution'}	None	638317
19436	Tennenbaum Marine Observatories Network	{'id': 17611, 'name': 'Smithsonian Institution'}	None	1135
17611	Smithsonian Institution	None	[{'id': 19436, 'name': 'Tennenbaum Marine Observatories Network'}, {'id': 7553, 'name': 'National Museum of Natural History, Smithsonian Institution'}]	1056
```
```Shell
obis.py area --of Peru Colombia
```
```
id	name	type
190	Peru	obis
10198	Peru Upwelling Cores	ebsa
10199	PeruvianHCSUpwelling	ebsa
41	Colombia	obis
127	Joint Regime: Colombia - Jamaica	obis
```

Above examples output were named **obis_institute.tsv** and **obis_area.tsv** correspondingly. We can also retrieve data by using any geographical id from above results. On the following example, the Peruvian areaid (i.e. 190) is used to look for taxa within both `checklist/redlist` and `occurrence` paths:

```Shell
obis.py checklist/redlist --areaid 190 --taxa Reptilia Mammalia
```
```
scientificName	scientificNameAuthorship	taxonID	taxonRank	taxonomicStatus	acceptedNameUsage	acceptedNameUsageID	is_marine	kingdom	phylum	subphylum	superclass	class	order	suborder	superfamily	family	genus	species	kingdomid	phylumid	subphylumid	superclassid	classid	orderid	suborderid	superfamilyid	familyid	genusid	speciesid	category	records
Dermochelys coriacea	(Vandelli, 1761)	137209	Species	accepted	Dermochelys coriacea	137209	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Dermochelyidae	Dermochelys	Dermochelys coriacea	2	1821	146419	1831	1838	2689	148741	987094	137000	137070	137209	VU	48
Caretta caretta	(Linnaeus, 1758)	137205	Species	accepted	Caretta caretta	137205	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	Caretta	Caretta caretta	2	1821	146419	1831	1838	2689	148741	987094	136999	137066	137205	VU	31
Lepidochelys olivacea	(Eschscholtz, 1829)	220293	Species	accepted	Lepidochelys olivacea	220293	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	Lepidochelys	Lepidochelys olivacea	2	1821	146419	1831	1838	2689	148741	987094	136999	137069	220293	VU	13
Chelonia mydas	(Linnaeus, 1758)	137206	Species	accepted	Chelonia mydas	137206	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	Chelonia	Chelonia mydas	2	1821	146419	1831	1838	2689	148741	987094	136999	137067	137206	EN	1
Eretmochelys imbricata	(Linnaeus, 1766)	137207	Species	accepted	Eretmochelys imbricata	137207	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	Eretmochelys	Eretmochelys imbricata	2	1821	146419	1831	1838	2689	148741	987094	136999	137068	137207	CR	1
Physeter macrocephalus	Linnaeus, 1758	137119	Species	accepted	Physeter macrocephalus	137119	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Physeteridae	Physeter	Physeter macrocephalus	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136985	137032	137119	VU	372
Balaenoptera musculus	(Linnaeus, 1758)	137090	Species	accepted	Balaenoptera musculus	137090	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Mysticeti	Balaenopteridae	Balaenoptera	Balaenoptera musculus	2	1821	146419	1831	1837	380416	370511	370545	2688	148724	136979	137013	137090	EN	10
```

```Shell
obis.py occurrence --areaid 190 --taxa 'Anchoa nasus' 
```
```
brackish	scientificNameID	scientificName	absence	dropped	aphiaID	genusid	decimalLatitude	originalScientificName	marine	minimumDepthInMeters	familyid	phylumid	subphylumid	terrestrial	basisOfRecord	superclass	maximumDepthInMeters	id	class	order	superclassid	orderid	dataset_id	decimalLongitude	speciesid	kingdom	classid	phylum	species	genus	subphylum	family	kingdomid	node_id
True	urn:lsid:marinespecies.org:taxname:275528	Anchoa nasus	False	False	275528	158697	-9.06999969482	Anchoa nasus	True	None	125465	1821	146419	False	HumanObservation	Pisces	None	5fc5547b-f0b1-43e1-a8b2-bf90f19c9a4f	Actinopterygii	Clupeiformes	11676	10297	0e1d55f3-c7dc-4355-a81f-e48a96795329	-78.5999984741	275528	Animalia	10194	Chordata	Anchoa nasus	Anchoa	Vertebrata	Engraulidae	2	['310922b4-9d0c-4de1-92d7-9b442d34765b']
True	urn:lsid:marinespecies.org:taxname:275528	Anchoa nasus	False	False	275528	158697	-3.63000011444	Anchoa nasus	True	None	125465	1821	146419	False	HumanObservation	Pisces	None	86decef7-ecc8-4afc-855d-846ffd74f528	Actinopterygii	Clupeiformes	11676	10297	0e1d55f3-c7dc-4355-a81f-e48a96795329	-80.5999984741	275528	Animalia	10194	Chordata	Anchoa nasus	Anchoa	Vertebrata	Engraulidae	2	['310922b4-9d0c-4de1-92d7-9b442d34765b']
True	PǸrou	urn:lsid:marinespecies.org:taxname:275528	Anchoa nasus	kner ,steindachner	False	False	275528	158697	-13.0260000229	Anchoa nasus	True	None	125465	1821	146419	2006-1641	False	PreservedSpecimen	MNHN	Pisces	None	a34ef4db-101f-4fba-8872-cf054c2eb7e6	bearez	Actinopterygii	Clupeiformes	11676	10297	705770e5-3474-4e69-be8b-3107a0c5610a	-76.4779968262	IC	275528	pacifique	Animalia	10194	bǸarez	Chordata	Anchoa nasus	Anchoa	Vertebrata	Engraulidae	2	['310922b4-9d0c-4de1-92d7-9b442d34765b']
Peru	1986	urn:lsid:marinespecies.org:taxname:308324	1986	Anchoa nasus	observedindividualcount=1;	False	275528	-6.838116	125465	1821	55397	False	HumanObservation	Pisces	None	c154a9d2-7da8-41be-a936-c3791099dbaa	9	Clupeiformes	RC86-43	11676	b8617377-eb1c-4db2-baa6-8788a632e810	Off Pimentel (Station 30), Pacific Ocean	Lambayeque	-79.937686	521251200000	Fishes	275528	521251200000	07	Anchoa	1986-07-09T12:00:00Z	True	False	158697	Anchoa naso	True	None	146419	ROM	521251200000	Holm, E.	Actinopterygii	10297	Animalia	10194	Reed Horse Fishermen	Chordata	Anchoa nasus	Vertebrata	Engraulidae	2	['310922b4-9d0c-4de1-92d7-9b442d34765b']
True	urn:lsid:marinespecies.org:taxname:275528	Anchoa nasus	False	False	275528	158697	-5.07999992371	Anchoa nasus	True	None	125465	1821	146419	False	HumanObservation	Pisces	None	f5d642a5-5a30-4d26-8921-01dd0bc229ef	Actinopterygii	Clupeiformes	11676	10297	0e1d55f3-c7dc-4355-a81f-e48a96795329	-81.1200027466	275528	Animalia	10194	Chordata	Anchoa nasus	Anchoa	Vertebrata	Engraulidae	2	['310922b4-9d0c-4de1-92d7-9b442d34765b']
True	urn:lsid:marinespecies.org:taxname:275528	Anchoa nasus	False	False	275528	158697	-3.65000009537	Anchoa nasus	True	None	125465	1821	146419	False	HumanObservation	Pisces	None	f8e2bccc-d19e-436f-9f8e-223a6e95de57	Actinopterygii	Clupeiformes	11676	10297	0e1d55f3-c7dc-4355-a81f-e48a96795329	-80.9499969482	275528	Animalia	10194	Chordata	Anchoa nasus	Anchoa	Vertebrata	Engraulidae	2	['310922b4-9d0c-4de1-92d7-9b442d34765b']
```

From above examples both would be named equal (i.e. **obis_area.tsv**). For that reason, `--out` option might be handy on these cases. Specific geographic area can be introduced in WKT format by using `--geometry` option. In the following example, we will use coordenates obtained from the [OBIS Mapper](https://mapper.obis.org/?geometry=POLYGON%20((9.6034%201.5839,%209.3501%201.1679,%209.1873%201.4555,%209.3027%201.6134,%209.6034%201.5839))) online app in order to get species occurrence from a tiny area of Equatorial Guinea and Gabon:


```Shell
obis.py occurrence --geometry 'POLYGON ((9.6034 1.5839, 9.3501 1.1679, 9.1873 1.4555, 9.3027 1.6134, 9.6034 1.5839))'
```
```
date_year	scientificNameID	scientificName	dynamicProperties	superfamilyid	individualCount	dropped	associatedReferences	aphiaID	decimalLatitude	type	taxonRemarks	phylumid	familyid	catalogNumber	occurrenceStatus	basisOfRecord	superclass	maximumDepthInMeters	modified	id	order	recordNumber	georeferencedDate	superclassid	verbatimEventDate	dataset_id	decimalLongitude	date_end	collectionCode	speciesid	occurrenceID	superfamily	suborderid	license	date_start	organismID	dateIdentified	genus	bibliographicCitation	eventDate	scientificNameAuthorship	absence	taxonRank	genusid	originalScientificName	marine	minimumDepthInMeters	subphylumid	vernacularName	institutionCode	date_mid	identificationRemarks	class	suborder	nomenclaturalCode	orderid	sex	datasetName	taxonomicStatus	geodeticDatum	kingdom	specificEpithet	classid	phylum	lifeStage	species	coordinatePrecision	organismRemarks	subphylum	datasetID	occurrenceRemarks	family	category	kingdomid	node_id
2009	urn:lsid:marinespecies.org:taxname:137209	Dermochelys coriacea	MachineObservation	987094	4	False	[{"crossref":{"citeinfo":{"origin":"Coyne, M. S., and B. J. Godley","pubdate":"2005","title_html":"Satellite Tracking and Analysis Tool (STAT): an integrated sy [...]	137209	1.5	Event	Taxon recorded as "Leatherback" by the provider	1821	137000	1454_1238197	present	MachineObservation	Tetrapoda	None	2018-06-13 14:36:11	13fe7b7d-eb09-4aea-adfb-9b845b0783c8	Testudines	1454_1238197	2008-12-11T02:19:58/2009-02-19T08:34:54	1831	2008-12-11 02:19:58/2009-02-19 08:34:54	5783eb41-8787-415f-beb8-178fa05684ef	9.5	1235001600000	1454	137209	1454_1238197	Chelonioidea	148741	http://creativecommons.org/licenses/by-nc/4.0/	1228953600000	89071a;89072a;89075a;89076a	2008-12-11T02:19:58/2009-02-19T08:34:54	Dermochelys	[{"crossref":{"citeinfo":{"origin":"Coyne, M. S., and B. J. Godley","pubdate":"2005","title_html":"Satellite Tracking and Analysis Tool (STAT): an integrated sy [...]	2008-12-11T02:19:58/2009-02-19T08:34:54	(Vandelli, 1761)	False	Species	137070	Dermochelys coriacea	True	None	146419	Leatherback	MTRG / Seaturtle.org	1231977600000	Identification Type:Telemetry	Reptilia	Cryptodira	WoRMS LSID	2689	Female	Gabon 2008-09: Mayumba & Pongara, Leatherback Turtles	valid	EPSG:4326 WGS84	Animalia	coriacea	1838	Chordata	Adult	Dermochelys coriacea	0.001	Tagged animal. organismID may refer to the ID of the telemetry device.	Vertebrata	1454	Telemetry locations aggregated per species per 1-degree cell	Dermochelyidae	VU	2	573654c1-4ce7-4ea2-b2f1-e4d42f8f9c31
2014	urn:lsid:marinespecies.org:taxname:137206	Chelonia mydas	MachineObservation	987094	3	False	;http://www.seaturtle.org/tracking/index.shtml?project_id=1001	137206	1.5	Event	Taxon recorded as "Green Turtle" by the provider	1821	136999	1840_585748	present	MachineObservation	Tetrapoda	None	2018-06-13 14:36:11	30390ec2-924e-47c5-9b82-b42320d4f11c	Testudines	1840_585748	2014-06-17T16:59:14/2014-10-10T22:10:39	1831	2014-06-17 16:59:14/2014-10-10 22:10:39	4a06a415-2954-4597-baf3-7934b07355ea	9.5	1412899200000	1840	137206	1840_585748	Chelonioidea	148741	http://creativecommons.org/licenses/by-nc/4.0/	1402963200000	138424;138426;138427	2014-06-17T16:59:14/2014-10-10T22:10:39	Chelonia	Halpin, P.N., A.J. Read, E. Fujioka, B.D. Best, B. Donnelly, L.J. Hazen, C. Kot, K. Urian, E. LaBrecque, A. Dimatteo, J. Cleary, C. Good, L.B. Crowder, and K.D. [...]	2014-06-17T16:59:14/2014-10-10T22:10:39	(Linnaeus, 1758)	False	Species	137067	Chelonia mydas	True	None	146419	Green Sea Turtle	Wildlife Conservation Society	1407888000000	Identification Type:Telemetry	Reptilia	Cryptodira	WoRMS LSID	2689	Male;Unknown	Equatorial Guinea 2014: Foraging Green Sea Turtles	valid	EPSG:4326 WGS84	Animalia	mydas	1838	Chordata	Juvenile;Subadult	Chelonia mydas	0.001	Tagged animal. organismID may refer to the ID of the telemetry device.	Vertebrata	1840	Telemetry locations aggregated per species per 1-degree cell	Cheloniidae	EN	2	573654c1-4ce7-4ea2-b2f1-e4d42f8f9c31
2009	urn:lsid:marinespecies.org:taxname:137209	Dermochelys coriacea	MachineObservation	987094	1	False	[{"crossref":{"citeinfo":{"origin":"Coyne, M. S., and B. J. Godley","pubdate":"2005","title_html":"Satellite Tracking and Analysis Tool (STAT): an integrated sy [...]	137209	1.5	Event	Taxon recorded as "Leatherback" by the provider	1821	137000	1456_1057383	present	MachineObservation	Tetrapoda	None	2016-12-27 06:05:08	35f94c5c-e83e-40b5-9092-562fa2fbb460	Testudines	1456_1057383	2009-12-28T07:30:36/2009-12-28T07:30:36	1831	2009-12-28 07:30:36/2009-12-28 07:30:36	961a2b3e-d2f1-4fff-b5f4-af9f01d4565a	9.5	1261958400000	1456	137209	1456_1057383	Chelonioidea	148741	http://creativecommons.org/licenses/by-nc/4.0/	1261958400000	92581a	2009-12-28T07:30:36/2009-12-28T07:30:36	Dermochelys	[{"crossref":{"citeinfo":{"origin":"Coyne, M. S., and B. J. Godley","pubdate":"2005","title_html":"Satellite Tracking and Analysis Tool (STAT): an integrated sy [...]	2009-12-28T07:30:36/2009-12-28T07:30:36	(Vandelli, 1761)	False	Species	137070	Dermochelys coriacea	True	None	146419	Leatherback	Marine Turtle Research Group / Seaturtle.org	1261958400000	Identification Type:Telemetry	Reptilia	Cryptodira	WoRMS LSID	2689	Female	Gabon 2009-10: Pongara, Leatherback Turtles	valid	EPSG:4326 WGS84	Animalia	coriacea	1838	Chordata	Adult	Dermochelys coriacea	0.001	Tagged animal. organismID may refer to the ID of the telemetry device.	Vertebrata	1456	Telemetry locations aggregated per species per 1-degree cell	Dermochelyidae	VU	2	573654c1-4ce7-4ea2-b2f1-e4d42f8f9c31
2011	urn:lsid:marinespecies.org:taxname:137206	Chelonia mydas	MachineObservation	987094	2	False	[{"crossref":{"citeinfo":{"origin":"Coyne, M. S., and B. J. Godley","pubdate":"2005","title_html":"Satellite Tracking and Analysis Tool (STAT): an integrated sy [...]	137206	1.5	Event	Taxon recorded as "Green Turtle" by the provider	1821	136999	718_980354	present	MachineObservation	Tetrapoda	None	2017-07-18 06:02:22	468f3da1-7a1e-46e8-946e-e272b8bf4034	Testudines	718_980354	2010-12-29T07:17:52/2011-05-31T14:46:06	1831	2010-12-29 07:17:52/2011-05-31 14:46:06	ce258d5f-3097-412a-a969-112f34f9169e	9.5	1306800000000	718	137206	718_980354	Chelonioidea	148741	http://creativecommons.org/licenses/by-nc/4.0/	1293580800000	68395;68395a	2010-12-29T07:17:52/2011-05-31T14:46:06	Chelonia	Marine Turtle Research Group	[{"crossref":{"citeinfo":{"origin":"Coyne, M. S., and B. J. Godley","pubdate":"2005","title_html":"Satellite Tracking and Analysis Tool (STAT): an integrated sy [...]	2010-12-29T07:17:52/2011-05-31T14:46:06	(Linnaeus, 1758)	False	Species	137067	Chelonia mydas	True	None	146419	Green Sea Turtle	Marine Turtle Research Group	1300147200000	Identification Type:Telemetry	Reptilia	Cryptodira	WoRMS LSID	2689	Unknown	Equatorial Guinea 2011: Green Turtles	valid	EPSG:4326 WGS84	Animalia	mydas	1838	Chordata	Juvenile	Chelonia mydas	0.001	Tagged animal. organismID may refer to the ID of the telemetry device.	Vertebrata	718	Telemetry locations aggregated per species per 1-degree cell	Cheloniidae	EN	2	573654c1-4ce7-4ea2-b2f1-e4d42f8f9c31
2015	urn:lsid:marinespecies.org:taxname:220293	Lepidochelys olivacea	MachineObservation	987094	1	False	[{"crossref":{"citeinfo":{"origin":"Coyne, M. S., and B. J. Godley","pubdate":"2005","title_html":"Satellite Tracking and Analysis Tool (STAT): an integrated sy [...]	220293	1.5	Event	Taxon recorded as "Olive Ridley" by the provider	1821	136999	1328_627560	present	MachineObservation	Tetrapoda	None	2016-09-20 05:56:52	b65e791e-4f51-4d69-8e25-58569844e2af	Testudines	1328_627560	2015-11-26T05:10:58/2015-11-29T14:28:43	1831	2015-11-26 05:10:58/2015-11-29 14:28:43	f282147d-5689-4da7-a8aa-6aa54c5bb5be	9.5	1448755200000	1328	220293	1328_627560	Chelonioidea	148741	http://creativecommons.org/licenses/by-nc/4.0/	1448496000000	152857	2015-11-26T05:10:58/2015-11-29T14:28:43	Lepidochelys	[{"crossref":{"citeinfo":{"origin":"Coyne, M. S., and B. J. Godley","pubdate":"2005","title_html":"Satellite Tracking and Analysis Tool (STAT): an integrated sy [...]	2015-11-26T05:10:58/2015-11-29T14:28:43	(Eschscholtz, 1829)	False	Species	137069	Lepidochelys olivacea	True	None	146419	Olive Ridley	Old Dominion Univ/Univ of Exeter/Wildlife Conservation Society	1448582400000	Identification Type:Telemetry	Reptilia	Cryptodira	WoRMS LSID	2689	Female	Gabon Olive Ridley Tracking Project: Pongara National Park 2015	valid	EPSG:4326 WGS84	Animalia	olivacea	1838	Chordata	Adult	Lepidochelys olivacea	0.001	Tagged animal. organismID may refer to the ID of the telemetry device.	Vertebrata	1328	Telemetry locations aggregated per species per 1-degree cell	Cheloniidae	VU	2	573654c1-4ce7-4ea2-b2f1-e4d42f8f9c31
2007	urn:lsid:marinespecies.org:taxname:137165	Sterna paradisaea	MachineObservation	2	False	[{"crossref":{"citeinfo":{"origin":"Egevang, C., I.J. Stenhouse, R.A. Phillips, A. Petersen, J.W. Fox and J.R.D. Silk","pubdate":"2010","title_html":"Tracking o [...]	137165	1.5	Event	Taxon recorded as "Arctic tern" by the provider	148764	1821	705_2186	present	MachineObservation	Tetrapoda	None	2011-02-24 13:46:04	d9405451-f8cf-4ee4-9e08-13b84cca5962	Charadriiformes	705_2186	2007-10-11T00:10:00/2007-10-13T12:07:00	1831	2007-10-11 00:10:00/2007-10-13 12:07:00	b7939ba9-6d4c-4359-b92b-136cf591e072	9.5	1192233600000	705	137165	705_2186	http://creativecommons.org/licenses/by-nc/4.0/	1192060800000	ARTE_376;ARTE_395	2007-10-11T00:10:00/2007-10-13T12:07:00	Sterna	Greenland Institute of Natural Resources	[{"crossref":{"citeinfo":{"origin":"Egevang, C., I.J. Stenhouse, R.A. Phillips, A. Petersen, J.W. Fox and J.R.D. Silk","pubdate":"2010","title_html":"Tracking o [...]	2007-10-11T00:10:00/2007-10-13T12:07:00	Pontoppidan, 1763	False	Species	137047	Sterna paradisaea	True	None	146419	Arctic Tern	Greenland Institute of Natural Resources	1192147200000	Identification Type:Telemetry	Aves	WoRMS LSID	2682	Tracking of Arctic tern migrations 2007-2008	valid	EPSG:4326 WGS84	Greenland,high-Arctic,Antarctica,Weddell Sea	Animalia	paradisaea	1836	Chordata	Sterna paradisaea	0.000001	Tagged animal. organismID may refer to the ID of the telemetry device.	Vertebrata	705	Telemetry locations aggregated per species per 1-degree cell	Sternidae	2	573654c1-4ce7-4ea2-b2f1-e4d42f8f9c31
2012	urn:lsid:marinespecies.org:taxname:137209	Dermochelys coriacea	MachineObservation	987094	4	False	;http://www.seaturtle.org/tracking/index.shtml?project_id=776	137209	1.5	Event	Taxon recorded as "Leatherback" by the provider	1821	137000	1836_393151	present	MachineObservation	Tetrapoda	None	2018-06-13 14:36:11	f3ee062e-2671-4d32-a813-acd517c8dcc8	Testudines	1836_393151	2012-11-03T08:40:01/2012-12-25T18:02:31	1831	2012-11-03 08:40:01/2012-12-25 18:02:31	768d9e0b-a4d8-4e02-8c50-74f0adf4cf52	9.5	1356393600000	1836	137209	1836_393151	Chelonioidea	148741	http://creativecommons.org/licenses/by-nc/4.0/	1351900800000	122426a;122428a;122433a;122434a	2012-11-03T08:40:01/2012-12-25T18:02:31	Dermochelys	Halpin, P.N., A.J. Read, E. Fujioka, B.D. Best, B. Donnelly, L.J. Hazen, C. Kot, K. Urian, E. LaBrecque, A. Dimatteo, J. Cleary, C. Good, L.B. Crowder, and K.D. [...]	2012-11-03T08:40:01/2012-12-25T18:02:31	(Vandelli, 1761)	False	Species	137070	Dermochelys coriacea	True	None	146419	Leatherback	University of Exeter	1354147200000	Identification Type:Telemetry	Reptilia	Cryptodira	WoRMS LSID	2689	Female	Gabon 2012: Pongara, Leatherback Turtles	valid	EPSG:4326 WGS84	Animalia	coriacea	1838	Chordata	Adult	Dermochelys coriacea	0.001	Tagged animal. organismID may refer to the ID of the telemetry device.	Vertebrata	1836	Telemetry locations aggregated per species per 1-degree cell	Dermochelyidae	VU	2	573654c1-4ce7-4ea2-b2f1-e4d42f8f9c31
```
