from deepdiff import DeepDiff
import json

def open_json_file(name):
    with open(name, 'rb') as f:
        return json.load(f)

new_json = open_json_file("list1.json")
downloaded_json = open_json_file( "list2.json")
ddiff = list(set(new_json) - set(downloaded_json))

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(ddiff, f, ensure_ascii=False, indent=4)

    
ddiff = DeepDiff(new_json, downloaded_json, ignore_order=True)
