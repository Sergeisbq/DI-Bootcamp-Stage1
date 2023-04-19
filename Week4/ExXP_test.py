def delete():
        a = all()
        print(a)
        b = input("Type the item'd to delete: ")
        if b == a:
            query = f"delete from cafe_menu where name = '{b}';"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                connection.close()
                print(f'{b} has been successfully deleted!')
        else:
            print('There is no such item!')


list_of_items = []


