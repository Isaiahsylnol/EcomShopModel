import sqlite3

from EcomShop.EcomStoreApp import display_index_menu, display_dept
from EcomShop.logging_module import write_log

def display_admin_menu():
    while True:
        print("\n** Admin Module **")
        print()
        print("SELECT FROM [1-7]")
        print("1 -  Add Product")
        print("2 -  Remove Product")
        print("3 -  View All Users")
        print("4 -  Add User")
        print("5 -  Remove User")
        print("6 -  Search User")
        print("7 -  Exit to Index")
        print()
        command = input("Admin Command menu: ")
        if command == "1":
            add_product()
        elif command == "2":
            delete_product()
        elif command == "3":
            list_users()
        elif command == "4":
            add_user()
        elif command == "5":
            delete_user()
        elif command == "6":
            search_users()
        elif command == "7":
            display_index_menu()
        else:
            print("Not a valid command. Please try again.")

def search_users():
    conn = sqlite3.connect('ecomApp.db')
    cur = conn.cursor()
    while(True):
        try:
            id = int(input("Please enter user ID to search for: "))
            cur.execute("SELECT * FROM users WHERE user_id = ?", (id,))
            rows = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            if rows:
                for i in rows:
                    print('\n' + '--' * 15)
                    print(
                        'ID: ' + str(i[0]) + '\n' +
                        'Name: ' + i[1] + ' ' + i[2] + '\n' +
                        'Email: ' + i[3] + '\n' +
                        'Account Type: ' + str(i[4]))
                    print('--' * 15 + '\n')
                    write_log("Searched user", "User Module", 1)
                    display_admin_menu()
            else:
                print('Failed to match ID to user\n')
                display_admin_menu()
        except:
            pass
        print
        '\nIncorrect input, please try again'

def add_product():
    conn = sqlite3.connect('ecomApp.db')
    cur = conn.cursor()
    name = str(input("Please enter product name: "))
    quantity = int(input("Please enter product quantity: "))
    description = str(input("Please enter product description: "))
    aisle = int(input("Please enter product location: "))
    rating = 0
    display_dept()
    choice = ""
    while choice not in (1, 2, 3, 4, 5):
        try:
            choice = int(input("Select department: "))
        except:
            pass
        print
        '\nIncorrect input, please try again'
    if choice == 1:
        choice = "Seasonal"
        sku_d = "84-"
    if choice == 2:
        choice = "Housewares"
        sku_d = "42-"
    if choice == 3:
        choice = "Automotive"
        sku_d = "23-"
    if choice == 4:
        choice = "Sports"
        sku_d = "33-"
    department = choice
    sku = str(input("Please enter product sku: "))
    while(len(sku) != 4):
        print('Error: 4 digits are required\n')
        sku = str(input("Please enter product sku: "))
    else:
        sku = sku_d + sku
        price = float(input("Please enter price: "))
        cur.execute("INSERT INTO products VALUES(?,?,?,?,?,?,?,?)",
                    (name, quantity, description, aisle, sku, rating, price, department))
        conn.commit()
        cur.close()
        conn.close()
        write_log("Created product", "User Module", 0)
        print(name + " was added.\n")

def delete_product():
    conn = sqlite3.connect('ecomApp.db')
    cur = conn.cursor()
    sku = str(input("\nPlease enter product sku: "))
    cur.execute("DELETE FROM products WHERE sku = ?", (sku,))
    conn.commit()
    conn.close()
    print(sku + " was deleted.\n")
    write_log("Deleted product", "User Module", 1)

def delete_user():
    conn = sqlite3.connect('ecomApp.db')
    cur = conn.cursor()
    id = int(input('Please enter user ID: '))
    cur.execute("DELETE FROM users WHERE user_id = ?", (id,))
    conn.commit()
    conn.close()
    write_log("Deleted user", "User Module", 1)
    print(str(id) + ' Deleted')

def list_users():
    conn = sqlite3.connect('ecomApp.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if rows:
        for i in rows:
            print('\n' + '--' * 15)
            print(
                  'ID: ' + str(i[0]) + '\n' +
                  'Name: ' + i[1] + ' ' + i[2] + '\n' +
                  'Email: ' + i[3] + '\n' +
                  'Account Type: ' + str(i[4]))
            print('--' * 15 + '\n')
    write_log("Viewed all users", "User Module", 1)
    display_admin_menu()

def add_user():
    conn = sqlite3.connect('ecomApp.db')
    cur = conn.cursor()
    first_name = str(input("Please enter first name: ")).strip()
    last_name = str(input("Please enter last name: ")).strip()
    email = str(input("Please enter user email: ")).strip()
    accType = int(input("Please enter account type: "))
    if accType != 1: accType = 0
    cur.execute("INSERT INTO users VALUES(NULL,?,?,?,?)",
                (first_name,last_name,email,accType))
    conn.commit()
    conn.close()
    accType = "Admin" if(accType == 1) else "User"
    print("\n" + first_name + " " + last_name + " was added as a " + accType + '\n')
    write_log("Created user", "User Module", 1)
    display_admin_menu()


