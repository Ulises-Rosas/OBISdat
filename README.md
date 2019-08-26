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
The structure is 

```Shell
./src/obis.py [path] [parameters]
```

This excutable uses paths that avilable for its 

* country
* area
* institute
* checklist
* checklist/redlist
* checklist/newest

Which can be 


Here are some examples:

#### Country

Example:

```Shell
./src/obis.py country --of Peru Colombia
```
```
id      country code
169     Peru    PE
48      Colombia        CO
```

#### Institute


Example:

```Shell
./src/obis.py institute --of 'Smithsonian Institution'
```
```
id	name	parent	children	records
7553	National Museum of Natural History, Smithsonian Institution	{'id': 17611, 'name': 'Smithsonian Institution'}	None	638317
19436	Tennenbaum Marine Observatories Network	{'id': 17611, 'name': 'Smithsonian Institution'}	None	1135
17611	Smithsonian Institution	None	[{'id': 19436, 'name': 'Tennenbaum Marine Observatories Network'}, {'id': 7553, 'name': 'National Museum of Natural History, Smithsonian Institution'}]	1056
```


#### Area

Example:
```Shell
./src/obis.py area --of Peru Colombia
```
```
id      name    type
190     Peru    obis
10198   Peru Upwelling Cores    ebsa
10199   PeruvianHCSUpwelling    ebsa
41      Colombia        obis
127     Joint Regime: Colombia - Jamaica        obis
```

#### Checklist

Example:
```Shell
./src/obis.py checklist --areaid 190 --taxa Reptilia Mammalia
```
```
scientificName	scientificNameAuthorship	taxonID	taxonRank	taxonomicStatus	acceptedNameUsage	acceptedNameUsageID	is_marine	kingdom	phylum	subphylum	superclass	class	order	suborder	superfamily	family	genus	species	kingdomid	phylumid	subphylumid	superclassid	classid	orderid	suborderid	superfamilyid	familyid	genusid	speciesid	category	records
Dermochelys coriacea	(Vandelli, 1761)	137209	Species	accepted	Dermochelys coriacea	137209	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Dermochelyidae	Dermochelys	Dermochelys coriacea	2	1821	146419	1831	1838	2689	148741	987094	137000	137070	137209	VU	48
Caretta caretta	(Linnaeus, 1758)	137205	Species	accepted	Caretta caretta	137205	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	Caretta	Caretta caretta	2	1821	146419	1831	1838	2689	148741	987094	136999	137066	137205	VU	31
Cheloniidae	Oppel, 1811	136999	Family	accepted	Cheloniidae	136999	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	2	1821	146419	1831	1838	2689	148741	987094	136999	18
Lepidochelys olivacea	(Eschscholtz, 1829)	220293	Species	accepted	Lepidochelys olivacea	220293	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	Lepidochelys	Lepidochelys olivacea	2	1821	146419	1831	1838	2689	148741	987094	136999	137069	220293	VU	13
Chelonia	Brongniart, 1800	137067	Genus	accepted	Chelonia	137067	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	Chelonia	2	1821	146419	1831	1838	2689	148741	987094	136999	137067	1
Chelonia mydas	(Linnaeus, 1758)	137206	Species	accepted	Chelonia mydas	137206	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	Chelonia	Chelonia mydas	2	1821	146419	1831	1838	2689	148741	987094	136999	137067	137206	EN	1
Eretmochelys imbricata	(Linnaeus, 1766)	137207	Species	accepted	Eretmochelys imbricata	137207	True	Animalia	Chordata	Vertebrata	Tetrapoda	Reptilia	Testudines	Cryptodira	Chelonioidea	Cheloniidae	Eretmochelys	Eretmochelys imbricata	2	1821	146419	1831	1838	2689	148741	987094	136999	137068	137207	CR	1
Physeter macrocephalus	Linnaeus, 1758	137119	Species	accepted	Physeter macrocephalus	137119	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Physeteridae	Physeter	Physeter macrocephalus	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136985	137032	137119	VU	372
Delphinus delphis	Linnaeus, 1758	137094	Species	accepted	Delphinus delphis	137094	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Delphinidae	Delphinus	Delphinus delphis	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136980	137015	137094	61
Megaptera novaeangliae	(Borowski, 1781)	137092	Species	accepted	Megaptera novaeangliae	137092	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Mysticeti	Balaenopteridae	Megaptera	Megaptera novaeangliae	2	1821	146419	1831	1837	380416	370511	370545	2688	148724	136979	137014	137092	60
Tursiops truncatus	(Montagu, 1821)	137111	Species	accepted	Tursiops truncatus	137111	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Delphinidae	Tursiops	Tursiops truncatus	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136980	137026	137111	56
Cetacea	Brisson, 1762	2688	Infraorder	accepted	Cetacea	2688	True	True	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	2	1821	146419	1831	1837	380416	370511	370545	2688	54
Otaria flavescens	Shaw, 1800	231425	Species	accepted	Otaria flavescens	231425	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Carnivora	Caniformia	Pinnipedia	Otariidae	Otaria	Otaria flavescens	2	1821	146419	1831	1837	380416	2687	254957	148736	231386	231397	231425	47
Lagenorhynchus obscurus	(Gray, 1828)	231434	Species	accepted	Lagenorhynchus obscurus	231434	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Delphinidae	Lagenorhynchus	Lagenorhynchus obscurus	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136980	137020	231434	36
Balaenoptera	Lacépède, 1804	137013	Genus	accepted	Balaenoptera	137013	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Mysticeti	Balaenopteridae	Balaenoptera	2	1821	146419	1831	1837	380416	370511	370545	2688	148724	136979	137013	22
Grampus griseus	(G. Cuvier, 1812)	137098	Species	accepted	Grampus griseus	137098	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Delphinidae	Grampus	Grampus griseus	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136980	137018	137098	21
Orcinus orca	(Linnaeus, 1758)	137102	Species	accepted	Orcinus orca	137102	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Delphinidae	Orcinus	Orcinus orca	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136980	137021	137102	19
Caniformia	254957	Suborder	accepted	Caniformia	254957	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Carnivora	Caniformia	2	1821	146419	1831	1837	380416	2687	254957	13
Globicephala	Lesson, 1828	137017	Genus	accepted	Globicephala	137017	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Delphinidae	Globicephala	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136980	137017	11
Balaenoptera musculus	(Linnaeus, 1758)	137090	Species	accepted	Balaenoptera musculus	137090	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Mysticeti	Balaenopteridae	Balaenoptera	Balaenoptera musculus	2	1821	146419	1831	1837	380416	370511	370545	2688	148724	136979	137013	137090	EN	10
Balaenoptera edeni	Anderson, 1878	137089	Species	accepted	Balaenoptera edeni	137089	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Mysticeti	Balaenopteridae	Balaenoptera	Balaenoptera edeni	2	1821	146419	1831	1837	380416	370511	370545	2688	148724	136979	137013	137089	9
Mesoplodon	Gervais, 1850	137034	Genus	accepted	Mesoplodon	137034	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Ziphiidae	Mesoplodon	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136986	137034	8
Ziphius cavirostris	Cuvier, 1823	137127	Species	accepted	Ziphius cavirostris	137127	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Ziphiidae	Ziphius	Ziphius cavirostris	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136986	137035	137127	7
Arctocephalus australis	(Zimmermann, 1783)	231435	Species	accepted	Arctocephalus australis	231435	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Carnivora	Caniformia	Pinnipedia	Otariidae	Arctocephalus	Arctocephalus australis	2	1821	146419	1831	1837	380416	2687	254957	148736	231386	231390	231435	6
Ziphius	Cuvier, 1823	137035	Genus	accepted	Ziphius	137035	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Ziphiidae	Ziphius	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136986	137035	5
Delphinus	Linnaeus, 1758	137015	Genus	accepted	Delphinus	137015	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Delphinidae	Delphinus	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136980	137015	3
Mesoplodon peruvianus	Reyes, Mead & Van Waerebeek, 1991	231409	Species	accepted	Mesoplodon peruvianus	231409	True	False	False	False	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Ziphiidae	Mesoplodon	Mesoplodon peruvianus	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136986	137034	231409	3
Delphinidae	Gray, 1821	136980	Family	accepted	Delphinidae	136980	True	True	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Delphinidae	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136980	2
Mirounga leonina	(Linnaeus, 1758)	231413	Species	accepted	Mirounga leonina	231413	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Carnivora	Caniformia	Pinnipedia	Phocidae	Mirounga	Mirounga leonina	2	1821	146419	1831	1837	380416	2687	254957	148736	136976	231398	231413	2
Balaenoptera acutorostrata	Lacépède, 1804	137087	Species	accepted	Balaenoptera acutorostrata	137087	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Mysticeti	Balaenopteridae	Balaenoptera	Balaenoptera acutorostrata	2	1821	146419	1831	1837	380416	370511	370545	2688	148724	136979	137013	137087	1
Phocoena spinipinnis	(Burmeister, 1865)	343898	Species	accepted	Phocoena spinipinnis	343898	True	Animalia	Chordata	Vertebrata	Tetrapoda	Mammalia	Theria	Cetartiodactyla	Cetancodonta	Cetacea	Odontoceti	Phocoenidae	Phocoena	Phocoena spinipinnis	2	1821	146419	1831	1837	380416	370511	370545	2688	148723	136984	137031	343898	1
```


