import json


# jsonfile = open('../test-data/api_test_data.json')
# data = json.load(jsonfile)
#
# for val in data['test_data']:
#     print(val)
#
# print(data['test_data']['name'])
# jsonfile.close()

# this function will parse json file and return test data based on test suit and case name arguments
def get_test_data(test_type, test_suit, case_name):
    if test_type == 'api':
        jsonfile = open('./test-data/api_test_data.json')
    elif test_type == 'web':
        jsonfile = open('./test-data/web_test_data.json')

    elif test_type == 'responsive':
        jsonfile = open('./test-data/responsive_ui.json')

    data = json.load(jsonfile)
    return data[test_suit][case_name]
    jsonfile.close
