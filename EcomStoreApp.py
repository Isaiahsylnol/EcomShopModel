import sqlite3

from EcomShop.User import User
from EcomShop.logging_module import write_log

# Code below is for user menu and system functionality
user = User(123, 'James', 'Dooley', 'james@email.com', 1)
global num, total

def list_products():
    conn = sqlite3.connect('ecomApp.db')
    cur = conn.cursor()
    display_dept()
    choice = ""
    # Loop request of department selection if choice
    # is not given a value between 1 - 5
    while choice not in (1, 2, 3, 4, 5):
        try:
            choice = int(input("Select department: "))
        except:
            pass
        print
        '\nIncorrect input, please try again'
    if choice == 1:
        choice = "Seasonal"
    if choice == 2:
        choice = "Housewares"
    if choice == 3:
        choice = "Automotive"
    if choice == 4:
        choice = "Sports"
    if choice == 5:
        print('bye')
    cur.execute("SELECT * FROM products WHERE department = ?", (choice,))
    rows = cur.fetchall()
    print('\n' + choice + ' Inventory')
    print('--' * 15 + '\n')
    for i in rows:
        # Formatting of the database query returned
        print(str(i[0]) + '\n' +
              'Stock: ' + str(i[1]) + '\n' +
              'Aisle: ' + str(i[3]) + '\n' +
              'Price: $' + str(i[6]) + '\n' +
              'Sku: ' + i[4])
        print('--' * 15 + '\n')
        conn.commit()
        conn.close()
    val = input('Enter any value to see menu: ')
    print()
    if val:
        write_log("View Products", "Ecom Store", 0)
        display_menu()

def buy_product():
    conn = sqlite3.connect('ecomApp.db')
    cur = conn.cursor()
    sku = str(input("\nPlease enter product sku: "))
    # This snippet of code allows two variables of user
    # input providing they forget the "dash" between a product's sku
    if len(sku) < 7:
        sku = sku[:2] + '-' + sku[2:]
    cur.execute("SELECT * FROM products WHERE sku = ?", (sku,))
    rows = cur.fetchall()
    if rows:
        name = rows[0][0]
        descrip = rows[0][2]
        aisle = rows[0][3]
        print('\n' + name)
        print(descrip)
        print('--'*15)
        print('Price: $' + str(rows[0][6]) + '\n' +
              'Aisle: ' + str(aisle) + '\n' +
              'Stock: ' + str(rows[0][1]) + '\n' +
              'Dept: ' + rows[0][7])
        print('--'*15+'\n')
        print("Y -  Add to cart")
        print("N -  Back to menu\n")
        item = rows
        choice = str(input('(Y/N)'))
        add_toCart(choice, item, total=0, num=0)
        conn.commit()
        conn.close()
    else:
        print("No product matched with sku")

def view_cart(num, total):
    print('\nShopping cart: ')
    print('--' * 15)
    for items in user.cart:
        num += 1
        print(items[0][0])
    print('\n' + str(num) + ' item(s) in cart\n' )
    for i in user.cart:
        total += i[0][6]
    print('Subtotal: $' + str(total) + '\n')
    display_menu()

def add_toCart(choice, item, total, num):
    total = 0.0
    # Evaluate the user's choice of input Y/N
    if choice.lower() == 'y':
        user.cart.append(item)
        # Calculate current total
        for i in user.cart:
            total += i[0][6]
            print('\n' + '"' + item[0][0] + '"' + ' Added to cart\n')
            display_menu()
    else:
        display_menu()

#----------------------------------        Menu Display Functions      ---------------------------------------------------------

def display_index_menu():
    print("\nIndex Module")
    print()
    print("SELECT FROM [1-3]")
    print("1 -  Everyday Store")
    print("2 -  Admin Module")
    print("3 -  Exit")
    print()

    while True:
        command = input("Index Command menu: ")
        if command == "1":
            display_menu()
        elif command == "2":
            from EcomShop.user_module import display_admin_menu
            display_admin_menu()
        elif command == "3":
            print('Bye')
            break
        else:
            print("Not a valid command. Please try again.")

def display_menu():
    print("The EveryDay Shop\n")
    print("COMMAND MENU")
    print("1 -  View products")
    print("2 -  Buy product")
    print("3 -  View Cart")
    print("4 -  Exit shop\n")

    while True:
        command = input("Command: ")
        if command == "1":
            list_products()
        elif command == "2":
            buy_product()
        elif command == "3":
            view_cart(num=0, total=0.0)
        elif command == "4":
            display_index_menu()
            break
        else:
            print("Not a valid command. Please try again.")

def display_dept():
    print("\nThe EveryDay Shop Departments")
    print()
    print("SELECT FROM [1-4]")
    print("1 -  Seasonal")
    print("2 -  Housewares")
    print("3 -  Automotive")
    print("4 -  Sports")
    print("5 -  Back to menu")
    print()

def main():
    display_index_menu()


if __name__ == "__main__":
    main()
