import requests
import json


# get a value from kwargs and if not there set a default
def k_get(key, default, **kwargs):
    if key in kwargs:
        return kwargs[key]
    else:
        return default


# we need to transform data or prepare a json for the request, there are some caveats when feeding the model some data
# for example the timestamps must be in iso format (check my jupyter notebook) and the json file must have
# 'timestamp' and 'value' arrays
# examples:
# t_format='%Y-%m-%d' -> '2019-12-30'
# t_format='%M %d, %Y' -> 'December 30, 2019'
def prepare_data(values, timestamps, t_format):
    return


# use azure anomaly detection for a data as an array of azure Points (live detect or batch)
# because azure needs timestamp in ISO format you can give a t_format string and I'll reformat time for you
# TODO: make functions to accept many types of data structures
def detect_anomaly(data, api=None, endpoint=None):

    headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': api}
    response = requests.post(endpoint, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        result = json.loads(response.content.decode("utf-8"))
    else:
        print(response.status_code)
        raise Exception(response.text)

    return result
