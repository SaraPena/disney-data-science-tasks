# functions that will write objects to json files, and load json files. 

import json

def write_to_json(obj, file_name):
    with open(file_name, 'w') as fout:
        json.dump(obj, fout, ensure_ascii=False, indent=2)

def load_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        return json.load(f)