import requests
from random import choice
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres' 
PASSWORD = ''
DATABASE = 'ExDC_Week4_Day4'

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)


def get_data(url) -> list[dict]:
    response = requests.get("https://restcountries.com/v3.1/all") 
    data = response.json()
    return data


def get_random_instanse(data_list: list, n: int):
    instances = []
    for _ in range(n):
        random_list = choice(data_list)
        instances.append(random_list)
    return instances


def extract(instance: dict):

    try:
        name = instance['name']['common']
        capital = instance['capital'][0]
        flag = instance['flag']
        subregion = instance['subregion']
        population = instance['population']
        return name, capital, flag, subregion, population
    
    except KeyError:
        return None


def preprocess(instances: list[dict]):
    preprocessed = []

    for instance in instances:
        preprocessed_inst = extract(instance)
        if preprocessed_inst is None:
            continue
        preprocessed.append(preprocessed_inst)
    return preprocessed


url = "https://restcountries.com/v3.1/all"
data = get_data(url)
random_list = get_random_instanse(data, 10)
clean_list = preprocess(random_list)
print(clean_list)


def insert_query(columns_names: list[str], data: tuple, table_name: str) -> str:
    columns = ", ".join(columns_names)
    name, capital, flag, subregion, population = data
    query = f"insert into {table_name} ({columns}) values ('{name}', '{capital}', '{flag}', '{subregion}', '{population}')"
    return query


def run_change_query(query: str): 
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
        print("SUCCESS")


columns = ['name', 'capital', 'flag', 'subregion', 'population']
for inst in clean_list:
    q = insert_query(columns, inst, 'country')
    run_change_query(q)