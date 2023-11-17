import os.path
import random
import re
from datetime import datetime

#Class of available car
class Car:
    def __init__(self, plate, name, model, properties, rented_price):
        self.plate = plate;
        self.name = name;
        self.model = model;
        self.properties = properties;
        self.rented_price = rented_price

    def getNameCar (self):
        return self.name

    def getPlate (self):
        return self.plate

    def getModel (self):
        return self.model

    def getProperties (self):
        return self.properties

    def getRentedPrice (self):
        return self.rented_price


#Class of rented car
class RentedCar:
    def __init__(self, plate, birth_date_customer, start_date, time_to_rent):
        self.plate = plate
        self.birth_date_customer = birth_date_customer
        self.start_date = start_date
        self.time_to_rent = time_to_rent

    def getPlate (self):
        return self.plate

    def getBirthDate (self):
        return self.birth_date_customer

    def getStartDate (self):
        return self.start_date

    def getTimeToRent(self):
        return self.time_to_rent

#Class to store list of available cars
class Cars:
    def __init__(self):
        self.list_of_cars = []

    def addCarToList (self, car):
        self.list_of_cars.append(car)

    def getCars (self):
        return self.list_of_cars;

#Class to store list of rented cars
class RentedCars:
    def __init__(self):
        self.rented_cars = []

    def addRentedCarToList(self, rented_car):
        self.rented_cars.append(rented_car)

    def getRentedCars (self):
        return self.rented_cars

#Class of customer
class Customer:
    def __init__(self, birth_date, first_name, last_name, email):
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def getBirthDate (self):
        return self.birth_date

    def getFirstName (self):
        return self.first_name

#Class to store list of customers
class Customers:
    def __init__(self):
        self.customers = []

    def addCustomerToList(self, customer):
        self.customers.append(customer)

    def getCustomerList(self):
        return self.customers

#Class to store transaction
class Transaction:
    def __init__(self, plate, birth_date, start_date, return_date, days, price):
        self.plate = plate
        self.birth_date = birth_date
        self.start_date = start_date
        self.return_date = return_date
        self.days = days
        self.price = price

    def getPlate (self):
        return self.plate

    def getBirthDate (self):
        return self.birth_date

    def getStartDate (self):
        return self.start_date

    def getReturnDate (self):
        return self.return_date

    def getDays (self):
        return self.days

    def getPrice (self):
        return self.price

#Class to store list of transactions
class Transactions:
    def __init__(self):
        self.transactions = []

    def getTransactionList (self):
        return self.transactions

    def addTransactionToList (self, transaction):
        self.transactions.append(transaction)

#Main function to run the program
def main():

    #List of cars
    list_of_cars = []

    #Read the path file for Vehicles.txt
    file_path_for_list_of_available_cars = "sources/Vehicles.txt"

    with open(file_path_for_list_of_available_cars, 'r') as file:
        content = file.read();

        if (len(content) > 0):
            splittedLinesToArray = content.split("\n");
            list_of_cars = saveToObjectForCars(splittedLinesToArray)

    #List of rented cars
    list_of_rented_cars = []

    # Read the path file for RentedVehicles.txt
    file_path_for_list_of_rented_cars = "sources/RentedVehicles.txt"

    with open(file_path_for_list_of_rented_cars, 'r') as file_second:
        content = file_second.read()

        if (len(content) > 0):
            splittedLinesToArray = content.split("\n")
            list_of_rented_cars = saveToObjectForRentedCars(splittedLinesToArray)

    #List of customers
    list_of_customers = []

    #Read the path file for Customers.txt
    file_path_for_list_of_customers = "sources/Customers.txt"
    with open(file_path_for_list_of_customers, 'r') as file_third:
        content = file_third.read()

        if (len(content) != 0):
            splittedLinesToArray = content.split("\n")
            list_of_customers = saveToObjectForCustomers(splittedLinesToArray)

    #Transaction list
    file_path_for_transactions = "sources/Transaction.txt"
    list_of_transactions = []
    with open(file_path_for_transactions, "r") as file_fourth:
        content = file_fourth.read()
        if (len(content) > 0):
            splittedLinesToArray = content.split("\n")
            list_of_transactions = saveToObjectForTransactions(splittedLinesToArray)

    #Program options

    program()

    #Run logic with selected options
    try:
        value = int(input())

        if (value == 1):
            listOfAvailableCars(list_of_cars)
            main()
        elif (value == 2):
            plate_number = rentACar(list_of_cars, list_of_rented_cars, main)
            birth_date_customer = checkBirthDateFunction(list_of_customers, main)
            first_name = saveCustomerToCustomerTxtFile(list_of_customers, birth_date_customer, main)
            saveToRentedVehiclesTxtFile(plate_number, birth_date_customer, first_name)
            main()
        elif (value == 3):
            returnRentedCar(list_of_cars, list_of_rented_cars, main)
            main()
        elif (value == 4):
            printTransaction(list_of_transactions)
            main()
        elif (value == 0):
            print("You chose exit. Welcome again!")
        else:
            print("There are no options with this number")
            main()
    except ValueError:
        print("Not a number but a string. Please provide it again as below\n")
        main()
    except KeyboardInterrupt:
        print("You interrupted the program.")

#Function to run the program
def program():
    print("You may select one of the following:")
    print("1) List available cars")
    print("2) Rent a car")
    print("3) Return a car")
    print("4) Count the money")
    print("0) Exit")
    print("What is your selection?\n")

#Save car into car list from Vehicles.txt
def saveToObjectForCars (splittedLinesToArray):

    cars = Cars()

    for i in range(len(splittedLinesToArray)):
        single_string = splittedLinesToArray[i].split(",")

        if (len(single_string) != 1):
            single_car = Car(single_string[0], single_string[1], single_string[2], single_string[3:len(single_string)], random.randint(10, 52))
            cars.addCarToList(single_car)

    return cars.getCars()

#Save rented car into list from RentedVehicles.txt
def saveToObjectForRentedCars (splittedLinesToArray):
    rented_cars = RentedCars()
    splittedLinesToArray = [line for line in splittedLinesToArray if len(line) > 0]

    if (len(splittedLinesToArray) > 0):
        for i in range(len(splittedLinesToArray)):
            splitString = splittedLinesToArray[i].split(",")
            plate_number = splitString[0]
            birth_date_customer = splitString[1]
            start_date = datetime.strptime(splitString[2].split(" ")[0], "%m/%d/%Y")
            converted_start_date = start_date.strftime("%d/%m/%Y")
            time_to_rent = splitString[2].split(" ")[1]
            rented_car = RentedCar(plate_number, birth_date_customer, converted_start_date, time_to_rent)
            rented_cars.addRentedCarToList(rented_car)

    return rented_cars.getRentedCars()

#Save customers into list from Customers.txt
def saveToObjectForCustomers (splittedLinesToArray):

    customers = Customers()
    splittedLinesToArray = [line for line in splittedLinesToArray if len(line) > 0]
    for i in range(len(splittedLinesToArray)):
        splitString = splittedLinesToArray[i].split(",")
        birth_date = splitString[0]
        first_name = splitString[1]
        last_name = splitString[2]
        email = splitString[3]
        customer = Customer(birth_date, first_name, last_name, email)
        customers.addCustomerToList(customer)

    return customers.getCustomerList()

#Save transaction into list from Transaction.txt
def saveToObjectForTransactions (splittedLinesToArray):

    transactions = Transactions()
    splittedLinesToArray = [line for line in splittedLinesToArray if len(line) > 0]

    for i in range(len(splittedLinesToArray)):
        splitString = splittedLinesToArray[i].split(",")
        transaction_plate = splitString[0]
        transaction_birth_date = splitString[1]
        transaction_start_date = splitString[2]
        transaction_end_date = splitString[3]
        transaction_days = splitString[4]
        transaction_price = float(splitString[5])
        transaction = Transaction(transaction_plate, transaction_birth_date, transaction_start_date,
                                  transaction_end_date, transaction_days, transaction_price)

        transactions.addTransactionToList(transaction)

    return transactions.getTransactionList()

#Function to display a list of available cars
def listOfAvailableCars (list_of_cars):

    print("The following cars are available:\n")
    for i in range(len(list_of_cars)):
        print(f"* Reg. nr: " + list_of_cars[i].getPlate() + ", Model" + list_of_cars[i].getModel() + ", Price per day: " + str(list_of_cars[i].getRentedPrice()))
        properties = ""
        for f in range(len(list_of_cars[i].getProperties())):
            properties += list_of_cars[i].getProperties()[f]

        print("Properties: " + properties)
    print("\nYou selected to see the list of available cars. We return you to the main list as below.\n")

#Function to check whether customer can rent a car
def rentACar (list_of_cars, list_of_rented_cars, main):

    plate_number = str(input("Enter the correct registered number or you want to go back to the main menu, click x to exit: ")).strip().upper()

    if (plate_number == "X"):
        main()
        return

    if (isPlateNumberExists(list_of_cars, plate_number) == False or isPlateNumberExistsInRentedVehicles(list_of_rented_cars, plate_number) == False):
        print("You gave an incorrect plate number or this car is already rented. Please enter again. Or you want to go back to the main menu, click x to exit: ")
        plate_number = rentACar(list_of_cars, list_of_rented_cars, main)
        return plate_number

    return plate_number


# Function to check birthdate
def checkBirthDateFunction (list_of_customers, main):

    birth_date = str(input("Enter correct date of birth in the form DD/MM/YYYY: Or you want to go back to the main menu, click x to exit: ")).strip()

    if (birth_date.lower() == "x"):
        main()
        return

    if (isBirthDateValid(birth_date) == False):
        print("Wrong type of birth of date. Please enter again. Or you want to go back to the main menu, click x to exit: ")
        birth_date = checkBirthDateFunction(list_of_customers, main)
        return birth_date

    if (functionToCheckAge(birth_date) >= 100 or functionToCheckAge(birth_date) < 18):
        print("Your age is not valid to rent a car since you are too old/young to rent the car. You are redirected to the main menu as your age is not allowed to rent the car as below.")
        main()
        return

    return birth_date

#Function to save customer to a list of customers
def saveCustomerToCustomerTxtFile(list_of_customers, birth_date_customer, main):

    if (isBirthDateExists(list_of_customers, birth_date_customer) == True):
        first_name = ""

        for i in range(len(list_of_customers)):
            if (list_of_customers[i].getBirthDate() == birth_date_customer):
                first_name = list_of_customers[i].getFirstName()
                break

        return first_name

    first_name = str(input("Please enter your first name: ")).strip().lower()
    first_name = first_name[0].upper() + first_name[1:]
    last_name = str(input("Please enter your last name: ")).strip().lower()
    last_name = last_name[0].upper() + last_name[1:]
    email = addEmailFunction(main)

    file_path_for_list_of_customers = "sources/Customers.txt"

    with open(file_path_for_list_of_customers, "a") as file:
        complete_string = birth_date_customer + "," + first_name + "," + last_name + "," + email + "\n"
        file.write(complete_string)

    return first_name;

#Save information to RentedVehicles.txt file
def saveToRentedVehiclesTxtFile(plate_number, birth_date_customer, first_name):
    file_path_for_list_of_rented_cars = "sources/RentedVehicles.txt"
    current_date = datetime.now()
    current_date_string = datetime.strftime(current_date, "%m/%d/%Y %H:%M")

    with open(file_path_for_list_of_rented_cars, "a") as file:
        string_to_parse = plate_number + "," + birth_date_customer + "," + current_date_string + "\n"
        file.write(string_to_parse)

    print(f"Hello {first_name}\nYou rented the car {plate_number}");

#Function to return a car
def returnRentedCar(list_of_cars, list_of_rented_cars, main):

    if (len(list_of_rented_cars) == 0):
        print("There are no rented cars. So you cannot return!")
        main()
        return

    plate = str(input("Enter the correct registered number to be returned or you want to go back to the main menu, click x to exit: ")).strip().upper()

    if (plate.lower() == "x"):
        main()
        return

    if (isPlateNumberExists(list_of_cars, plate) == False):
        print("This car with this plate number does not exist in a list of available cars.")
        transaction = returnRentedCar(list_of_cars, list_of_rented_cars, main)
        return transaction

    if (checkPlateNumberExistsInRentedVehicles(list_of_rented_cars, plate) == False):
        print("This car with this plate number was not rented")
        transaction = returnRentedCar(list_of_cars, list_of_rented_cars, main)
        return transaction

    rented_car = ""
    price = ""
    for i in range(len(list_of_rented_cars)):
        if (list_of_rented_cars[i].getPlate().strip().lower() == plate.strip().lower()):
            rented_car = list_of_rented_cars[i]
            break

    for i in range (len(list_of_cars)):
        if (rented_car.getPlate().strip().lower() == list_of_cars[i].getPlate().strip().lower()):
            price = "{:.2f}".format(float(list_of_cars[i].getRentedPrice()))
            break

    file_path_for_transactions = "sources/Transaction.txt"
    file_path_for_rented_vehicles = "sources/RentedVehicles.txt"

    transaction_plate = plate
    transaction_birth_date = rented_car.getBirthDate()
    transaction_start_date = changeDateFormat(rented_car.getStartDate() + " " + rented_car.getTimeToRent())
    transaction_end_date = getCurrentDate()
    transaction_days = getDaysForTransaction(rented_car)
    transaction_price = float(getDaysForTransaction(rented_car)) * float(price)
    transaction = Transaction(transaction_plate, transaction_birth_date, transaction_start_date, transaction_end_date, transaction_days, transaction_price)

    list_of_rented_cars_when_removing_rented_car = [car for car in list_of_rented_cars if (car.getPlate() != plate)]

    with open(file_path_for_rented_vehicles, "w") as file:
        for i in range(len(list_of_rented_cars_when_removing_rented_car)):
            complete_string = list_of_rented_cars_when_removing_rented_car[i].getPlate() + "," + list_of_rented_cars_when_removing_rented_car[i].getBirthDate() + "," + changeDateFormat(list_of_rented_cars_when_removing_rented_car[i].getStartDate() + " " + list_of_rented_cars_when_removing_rented_car[i].getTimeToRent()) + "\n"
            file.write(complete_string)


    with open(file_path_for_transactions, "a") as file:
        complete_string_transaction = transaction.getPlate() + "," + transaction.getBirthDate() + "," + transaction.getStartDate() + "," + transaction.getReturnDate() + "," + str(transaction.getDays()) + "," + str(transaction.getPrice())
        file.write(complete_string_transaction + "\n")

    print(f"The rent lasted {transaction.getDays()} days and the cost is {transaction.getPrice()} euros")
    return;

#Print transaction
def printTransaction(list_of_transactions):

    total_transaction = 0.00

    if (len(list_of_transactions) > 0):
        for i in range(len(list_of_transactions)):
            price = list_of_transactions[i].getPrice()
            total_transaction += price

    total_transaction = "{:.2f}".format(total_transaction)

    print(f"The total amount of money is {total_transaction} euros")

#Change date format
def changeDateFormat (string):

    date = datetime.strptime(string, "%d/%m/%Y %H:%M")

    return datetime.strftime(date, "%m/%d/%Y %H:%M")

#Function to get days for transaction
def getDaysForTransaction (rented_car):

    rented_date = rented_car.getStartDate() + " " + rented_car.getTimeToRent()

    parsed_rented_date = datetime.strptime(rented_date, "%d/%m/%Y %H:%M")

    current_date = datetime.now()

    diff = current_date - parsed_rented_date

    if diff.days == 0:
        return 1

    return diff.days

#Function to get current date with date format MM/DD/YYYY HH/MM
def getCurrentDate():
    current_date = datetime.now()

    return datetime.strftime(current_date, "%m/%d/%Y %H:%M")

#Function to add email
def addEmailFunction (main):

    email = str(input("Please enter your email: ")).strip()

    if (email.lower() == "x"):
        main()
        return

    if (validateEmail(email) == False):
        print("Email is invalid. Please enter again. Or you want to exit. Please click x to exit: ")
        email = addEmailFunction(main)
        return email

    return email

#Function to validate email
def validateEmail (email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if (re.match(email_pattern, email)):
        return True

    return False

# Function to check age of customer

def functionToCheckAge (birth_date):

    birth_date_type = datetime.strptime(birth_date, "%d/%m/%Y")

    current_date = datetime.now()

    diff = (current_date - birth_date_type)

    age = diff.days // 365

    return age

# Function to check birthdate is valid
def isBirthDateValid(birth_date):
    date_pattern = r'^\d{2}/\d{2}/\d{4}$'

    if (re.match(date_pattern, birth_date)):
        try:
            datetime.strptime(birth_date, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    else:
        return False

#Common function to check birth date exists
def isBirthDateExists (list_of_customers, birth_date):
    check_birth_date_exists = False;

    for i in range(len(list_of_customers)):
        if (list_of_customers[i].getBirthDate() == birth_date):
            check_birth_date_exists = True
            break

    return check_birth_date_exists;

#Common function to check plate number exists
def isPlateNumberExists (list_of_cars, plate_number):
    check_plate_number = False
    for i in range(len(list_of_cars)):
        if (list_of_cars[i].getPlate() == plate_number):
            check_plate_number = True
            break

    return check_plate_number;


#Common function to check plate number exists
def checkPlateNumberExistsInRentedVehicles (list_of_rented_cars, plate_number):
    check_plate_number = False
    for i in range(len(list_of_rented_cars)):
        if (list_of_rented_cars[i].getPlate() == plate_number):
            check_plate_number = True
            break

    return check_plate_number;

#Common function to check plate number exists in RentedVehicles.txt to rent
def isPlateNumberExistsInRentedVehicles (list_of_rented_cars, plate_number):
    available_for_rent = True

    for i in range(len(list_of_rented_cars)):
        if (list_of_rented_cars[i].getPlate() == plate_number):
            available_for_rent = False
            break

    return available_for_rent;

#Main function to run a program
main();