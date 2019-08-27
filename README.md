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

While whole output filenames are named in function to the path used, these can also be defined with `--out` option.

#### Examples

When we use either `country`, `institute` or `area` paths, `--of` option is coupled in order to match requested strings:

```Shell
obis.py country --of Peru Colombia
```
```
id      country code
169     Peru    PE
48      Colombia        CO
```

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


