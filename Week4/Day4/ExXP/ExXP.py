import psycopg2
from datetime import date

HOSTNAME = 'localhost'
USERNAME = 'postgres' 
PASSWORD = ''
DATABASE = 'ExXP_Week4_Day4'

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)

query = 'select * from actors'

# First method
# cursor = connection.cursor()
# cursor.execute(query)
# result = cursor.fetchall()
# print(result)
# connection.close()

def select_column(column_name: str, table_name: str) -> str:
    query = f'select {column_name} from {table_name}'
    return query


def run_query(query: str):
    with connection.cursor() as cursor:
        # cursor - query runner
        cursor.execute(query)
        # cursor.fetchall returns all data from the cursor
        result = cursor.fetchall()
    return result




# select first_name, last_name, number_oscars from actors;

def select_columns(columns: list[str], table_name: str) -> str:
    start = 'select '

    columns_str = ''
    for idx, column in enumerate(columns):
        columns_str += column 
        if idx < len(columns) - 1:
            columns_str += ', '

    end = f' from {table_name}'
    
    query = start + columns_str + end
    return query
    


query1 = select_column('first_name', 'actors')
query2 = select_column('last_name', 'actors')

columns = ['first_name', 'last_name', 'number_oscars', 'birthday']
q = select_columns(columns, 'actors')
print(q)

result1 = run_query(query1)
result2 = run_query(query2)

# print("First names:", result1)
# print("Last names:", result2)


result3 = run_query(q)
print(result3)





#-------------changing data--------------

f_name = 'Brad'
l_name = 'Pitt'
birthday = date(1970, 1, 1)
num_oscars = 2

q1 = f"insert into actors (first_name, last_name, birthday, number_oscars) values ('{f_name}', '{l_name}', '{birthday}', {num_oscars});"

def insert_query(columns_values: dict, table_name: str) -> str:
    ...

def run_change_query(query: str):

    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

run_change_query(q1)



