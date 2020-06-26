from jSona import jSona
from pprint import pprint as pp

jso = jSona()

sample_data = {'hello':['world', 'everyone~']}
jso.saveJson("sample.json", sample_data, cry=True)

load_data = jso.loadJson("sample.json", cry=True)
pp(load_data)