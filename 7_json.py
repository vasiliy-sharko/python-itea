import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

data_json = json.dumps(data)
print(f"Type is {type(data_json)}, data is {data_json}")
print(data_json[2:11])

test_json = json.loads(data_json)
print(f"Type is {type(test_json)}, data is {test_json}")
print(test_json["president"]["name"])
