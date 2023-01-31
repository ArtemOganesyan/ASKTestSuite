import json

jsonfile = open('../test-data/sample.json')
data = json.load(jsonfile)

for val in data['test_data']:
    print(val)

print(data['test_data']['name'])
jsonfile.close()