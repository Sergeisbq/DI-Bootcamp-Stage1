import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres' 
PASSWORD = ''
DATABASE = 'ExXP_Week4_Day4'

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)

class MenuItem():
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


    def save(self):
        query = f"insert into cafe_menu (name, price) values ('{self.name}',{self.price})"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
# connection.close()
            print(f'{self.name} has been successfully added!')


    def delete():
        a = MenuItem.all()
        print(a)
        b = input("Type the item you'd like to delete: ")
        for i in range(len(a)):
            c = a[i][1]
            if str(b) == str(c):
                query = f"delete from cafe_menu where name = '{str(b)}';"
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    connection.commit()
# connection.close()
                    print(f'{b} has been successfully deleted!')
            else:
                pass # print('There is no such item!')

# connection.close()

    def update(self, name_1, price_1):
        query = (f"update cafe_menu set name = '{name_1}', price = '{price_1}' where name = '{self.name}'")
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            connection.close()
            print(f'Information about {self.name} has been successfully changed!')


    def all():
        query = f"select * from cafe_menu"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
# connection.close()
        return result
    

    def get_by_name(name):
            query = f"select * from cafe_menu where name = '{name}'"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                result = cursor.fetchall()
                connection.close()
            return result


# item = MenuItem('Bowl', 59)
# item.save()

# MenuItem.delete()


# item2 = MenuItem.delete('Chips')
# print(item2)
# item3 = MenuItem('Burger', 50)
# item3.update('Burger', 70)


# item4 = MenuItem.all()
# print(item4)
# a = input("Type the item you'd like to delete: ")
# print(a)
# for i in range(len(item4)):
#     b = item4[i][1]
#     print(b)
#     print(str(b) == str(a))


# item5 = MenuItem.get_by_name('Burger')
# print(item5)







