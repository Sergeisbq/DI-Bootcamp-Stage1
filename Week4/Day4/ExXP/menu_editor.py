from menu import MenuItem

input_list = ['a','d','v','x']

def load_manager():
    ...


def show_user_menu():
    print('''
         MENU:
    (a) Add an item
    (d) Delete an item
    (v) View the menu
    (x) Exit
    ''')


def add_item_to_menu():
    item_name = input("Enter item's name:  ")
    item_price = int(input("Enter item's price:  "))
    item = MenuItem(item_name, item_price)
    item.save() 


def remove_item_from_menu():
    MenuItem.delete()


def show_restaurant_menu():
    print(MenuItem.all()) 
    

def main():
    choice = ''
    while choice != 'x':
        show_user_menu()
        choice = str()
        while choice not in input_list:
            choice = input('Your choice: ')
            if choice == 'a':
                add_item_to_menu()
            elif choice == 'd':
                remove_item_from_menu()
            elif choice == 'v':
                show_restaurant_menu()
            else:
                break

main()