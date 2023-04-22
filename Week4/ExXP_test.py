import json

# def delete():
#         a = all()
#         print(a)
#         b = input("Type the item'd to delete: ")
#         if b == a:
#             query = f"delete from cafe_menu where name = '{b}';"
#             with connection.cursor() as cursor:
#                 cursor.execute(query)
#                 connection.commit()
#                 connection.close()
#                 print(f'{b} has been successfully deleted!')
#         else:
#             print('There is no such item!')


# list_of_items = []

# response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population")
# countries = list(response)
# print(len(countries), countries[10])
# list_of_countries = []

# for i in range(0, 10):
#     list_of_countries.append(countries[i])

# print(list_of_countries[0])


filename = '/Users/sergeiboiko/Study/DI-Bootcamp-Stage1/Week4/Day5/EX_DC_F/mysite/people/people_data.json'

with open(filename, 'r') as f:
    data = json.load(f)


# for i in range(len(data)):

# print(data)
# data_2 = dict(data)
# data_3 = list(data_2.items())
# print(data_3)



data_1 = sorted(data, key=lambda i: i['age'])
# data_2 = []
# for i in 
print(data_1)