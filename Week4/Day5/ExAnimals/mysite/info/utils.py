import json
# Create your views here.

def read_data(location: str, key: str):

    with open(location, 'r') as file:
        data = json.load(file)

    sub_data = data[key]
    return sub_data


def find_instance(data_list: list[dict], id: int) -> dict:
    for i in data_list:
        if i['id'] == id:
            return i
    return None

