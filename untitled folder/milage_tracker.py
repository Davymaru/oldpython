'''
    Track mileage for work
    Calculate reimbursement based on mileage_rate
    store in external file

'''


milage_rate = .52


def open_file():
    try:
        # Open the file in read mode
        directory = open('mileage.txt', 'r')
        # we can read and write (append)
        content = directory.read()
        print(content)
        directory.close()  # Always close the file
        return (content)
    except FileNotFoundError:
        print("File not found.")

    except IOError:
        print("We created this file for you, it did not exist or was empty.")

    except Exception as e:
        print("An error occurred:", e)


def add_values(my_values):
    date = input("What is today's date: ")
    destination = input("Where did you go? ")
    total_miles = input("What were the total miles for this trip? ")
    entry = date + ", " + destination + ", " + total_miles + "\n"
    record = open('mileage.txt', 'a')
    record.write(entry)
    record.close()


def main():
    # Trying to open a file and handle exceptions
    values = open_file()
    print(f"The contents of the file are: {values}")
    add_values(values)


main()
