## jSona

##### JSON Format handler with bulit-in json module

Error tolerances are added to bulit-in json module.

Because those kind of works are really annoying.
***

### Projects

jSona have two major functions

* loadJson : Loads data from json format file.

* saveJson : Saves to json format file.

* loads, dumps : Equals loads and dumps functions in json module.

Also supports useful function from exists.

* loads

* dumps

***

### Examples

* Script
```python
from jSona import jSona
from pprint import pprint as pp

jso = jSona()

sample_data = {'hello':['world', 'everyone~']}
jso.saveJson("sample.json", sample_data, cry=True) # Save data

load_data = jso.loadJson("sample.json", cry=True)  # Load data
pp(load_data)
```
* Outputs
```python
SAVE SUCCESS TO [ sample.json ]
LOAD SUCCESS FROM [ sample.json ]
{'hello': ['world', 'everyone~']}
```

***


### Notices

###### Unauthorized distribution and commercial use are strictly prohibited without the permission of the original author and the related module.