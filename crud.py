def main_menu():
    print("Menu:")
    while True:
        try:
            print("\nwelcome you can create new email entries, change email addresses, delete entries, or display entries.")

            print("1. create a new entry")

            print("2. display an entry by last name")

            print("3. update an existing entry")

            print("4. remove an entry")

            print("5. quit")

            choice = int(input("enter the number of your selection: "))

            if 1 <= choice <= 5:

                return choice
            
            else:

                print("that is not a valid number. try again.")

        except ValueError:

            print("that is not a valid number. try again.")


def check():
    try:

        file = open("customer_list.txt", 'r')

        lines = file.readlines()

        file.close()

        return lines
    
    except FileNotFoundError:

        print("customer list does not exist. creating a new file...")

        return []


def create():

    customer = check()

    fname = input("enter the customer's first name: ")

    lname = input("enter the customer's last name: ")

    phone = input("enter the customer's phone: ")

    email = input("enter the customer's email: ")

    entry = (fname + ", " + lname + ", " + phone + ", "  + email + "\n")

    customer.append(entry)

    save(customer)


def read():

    lname = input("enter the customer's last name to display: ")

    customer = check()

    found = False

    for entry in customer:

        if lname in entry:

            print(entry.strip())

            found = True

    if not found:

        print("entry not found.")


def update():

    lname = input("enter the customer's last name to update: ")

    customer = check()

    updated_customer = []

    found = False

    for entry in customer:

        if lname in entry:

            fname = input("enter the customer's first name: ")

            phone = input("enter the customer's phone: ")

            email = input("enter the customer's email: ")

            entry = (fname + ", " + lname + ", " + phone + ", "  + email + "\n")

            updated_customer.append(entry)

            found = True
        else:
            updated_customer.append(entry)
    if not found:
        print("entry not found.")

    else:
        save(updated_customer)

def delete():

    lname = input("enter the customer's last name to delete: ")

    customer = check()

    updated_customer = []

    found = False

    for entry in customer:

        if lname in entry:

            found = True


        else:
            updated_customer.append(entry)

    if not found:
        print("entry not found.")

    else:
        save(updated_customer)

def save(output):

    file = open("customer_list.txt", 'w')

    for line in output:

        file.write(line)

    file.close()

    print("file updated.")

def run_menu():

    while True:
        choice = main_menu()

        if choice == 1:
            create()

        elif choice == 2:
            read()

        elif choice == 3:
            update()

        elif choice == 4:
            delete()

        elif choice == 5:
            print("exiting program.")

            break


run_menu()