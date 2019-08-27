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

Using `git`:

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
