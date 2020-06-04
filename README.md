## jSona

##### JSON Format handler with bulit-in json module

Error tolerances are added to bulit-in json module.

Because those kind of works are really annoying.
***

### Projects

jSona have two major functions

* loadJson : Loads data from json format file.

* saveJson : Saves to json format file.

Also supports useful function from exists.

* loads

* dumps

***

### Examples

* Script
```python
from jSona import jSona

jso = jSona()
table = jso.loadJson("json path", cry=True)
jso.saveJson("json path", table, cry=True)
```
* Outputs
```python
LOAD SUCCESS FROM [json path]
SAVE SUCCESS TO [json path]
```

***


### Notices

###### Unauthorized distribution and commercial use are strictly prohibited without the permission of the original author and the related module.