
#products = ["water", "apple juice", "orange Juice", "lemonade", "sprite", "coke", "tea", "americano", "expresso", "cappuccino"]

import csv
products = []
couriers = []
orders_list = []


#------------------------------------------PRODUCT FILE CODE------------------------------------------

def load_products_file():
    try:
        with open("products.txt", "r") as file:
            for line in file:
                products.append(line.rstrip())
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    except Exception as e:
        print('An error occurred: ' + str(e))

def add_products_file():
    print("Current List:\n")
    for product in products:
        print(product)
    new_entry = str(input("\nEnter name of new product\nor 0 to go back:\n").lower())
    if new_entry == "":
        print("Please enter a valid item")
        add_products_file()
    elif new_entry == str(0):
        product_menu()
    else:
        products.append(new_entry)            
        try: 
            with open("products.txt", "w") as file:
                for product in products:
                    file.write(product + '\n')
        except FileNotFoundError as fnfe:
            print('Unable to open file: ' + str(fnfe))
        except Exception as e:
            print('An error occurred: ' + str(e))
        print("\n{} has been added to the list".format(new_entry.lower()))
        print("\nThis is the new list:\n")
        for product in products:
            print(product)

def update_products_file():
    print("Current List:\n")
    for product in products:
        print(product)
    product_update = str(input("\nEnter the name of the product you want to update or\nEnter 0 to go back:\n").lower())
    if product_update == str(0):
        product_menu()
    else:
        for i, product in enumerate(products):
            if product_update == product:
                updated_name = str(input("\nEnter the updated name:\n"))
                products[i] = updated_name
                try:
                    with open("products.txt","w") as file:
                        for product in products:
                            file.write(product + '\n')
                except:
                    print('\nFailed to open file')
                print("\nThis is the new list:\n")
                for product in products:
                    print(product)
                break
        else:
            incorrect_function()
            update_products_file()
    navigation()

def delete_product_file():
    print("Current List:\n")
    for product in products:
        print(product)

    product_delete = str(input("\nEnter name of product you want to delete from the list or\nEnter 0 to go back:\n").lower())
    if product_delete == str(0):
        product_menu()
    else:
        for i, product in enumerate(products):
            if product_delete == product:
                products.remove(product)
                try:
                    with open("products.txt","w") as file:
                        for product in products:
                            file.write(product + '\n')
                except:
                    print('\nFailed to open file')
                print ("\n{} has been removed from the list\n".format(product_delete))
                for product in products:
                    print(product)
                break
        else:
            incorrect_function()
            delete_product()    
    navigation()

#------------------------------------------COURIER FILE CODE------------------------------------------

def load_couriers_file():
    try:
        with open("courier.txt", "r") as file:
            for line in file:
                couriers.append(line.rstrip())
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    except Exception as e:
        print('An error occurred: ' + str(e))  

def add_courier_file():
    print("Current List:\n")
    for courier in couriers:
        print(courier)
    new_entry = str(input("\nEnter name of new courier\nor 0 to go back:\n").title())
    if new_entry == "":
        print("Please enter a valid name")
        add_courier_file()
    elif new_entry == str(0):
        courier_menu()
    else:
        couriers.append(new_entry)            
        try: 
            with open("courier.txt", "w") as file:
                for courier in couriers:
                    file.write(courier + '\n')
        except FileNotFoundError as fnfe:
            print('Unable to open file: ' + str(fnfe))
        except Exception as e:
            print('An error occurred: ' + str(e))
        print("{} has been added to the list".format(new_entry.title()))
        print("\nThis is the new list:\n")
        for courier in couriers:
            print(courier)

def update_courier_file():
    print("Current List:\n")
    for courier in couriers:
        print(courier)
    
    courier_update = str(input("\nEnter the name of the courier you want to update or\nEnter 0 to go back:\n").title())
    if courier_update == str(0):
        courier_menu()
    else:
        for i, courier in enumerate(couriers):
            if courier_update == courier:
                updated_name = str(input("\nEnter the updated name:\n").title())
                couriers[i] = updated_name
                try:
                    with open("courier.txt","w") as file:
                        for courier in couriers:
                            file.write(courier + '\n')
                except:
                    print('\nFailed to open file')
                print("\nThis is the new list:\n")
                for courier in couriers:
                    print(courier)
                break
        else:
            incorrect_function()
            update_courier_file()    
    navigation()

def delete_courier_file():
    print("Current List:\n")
    for courier in couriers:
        print(courier)

    courier_delete = str(input("\nEnter name of courier you want to delete from the list or\nEnter 0 to go back:\n").title())
    if courier_delete == str(0):
        courier_menu()
    else:
        for i, courier in enumerate(couriers):
            if courier_delete == courier:
                couriers.remove(courier)
                try:
                    with open("courier.txt","w") as file:
                        for courier in couriers:
                            file.write(courier + '\n')
                except:
                    print('\nFailed to open file')
                print ("\n{} has been removed from the list\n".format(courier_delete))
                for courier in couriers:
                    print(courier)
                break
        else:
            incorrect_function()
            delete_courier()    
    navigation()

#---------------------------------------------ORDERS FILE CODE----------------------------------------
#NEED TO ADD TRY EXCEPT STATEMNTS TO ALL HERE 
def load_orders_file():
    with open("orders.csv", "r") as file:
        csv_file = csv.DictReader(file)  
        for row in csv_file:
                orders_list.append(row)
#NEED TO ADD UNIT TESTS TO ALL THESE, AND RETURN/CANCEL OPTIONS
def view_orders_file():
    with open("orders.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            print("\n")
            for key, value in row.items():
                print("{}: {}".format(key, value).title())

def add_order_file():
    def courier_order_choice():
        for courier in couriers:
            print(courier)
        courier_choice = str(input("\nChoose a courier from the list above:").title())
        for i, courier in enumerate(couriers):
            if courier_choice == courier:
                print("\n{} has been added as the courier for your order\n".format(courier_choice))
                with open('orders.csv', mode='a') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow([firstname_input, surname_input, address_input, postcode_input, phone_input, order_status, courier_choice])
                
                load_orders_file()
                print("This is the new order:\n")
                last_order = orders_list[-1]        
                for key, value in last_order.items():
                    print("{}: {}".format(key, value).title())  
                navigation()
        else:
            print("Sorry, please choose a courier from the list")
            courier_order_choice()
    
    firstname_input = str(input("Enter your first name:\n").title())
    surname_input = str(input("Enter your surname:\n").title())
    address_input = str(input("Enter the first line of your address:\n").title())
    postcode_input = str(input("Enter your postcode:\n").upper())
    phone_input = int(input("Enter your contact number:\n"))
    order_status = "Preparing"
    print("\n")
    courier_order_choice()

def update_order_status_file():
    
    #steps:
    #print out the list of orders, with order number?
    #obtain the correct item from list
    #update the order status
    #rewrite the csv file with the updated dictionary values

    print("\nOrder list:")
    for i, order in enumerate(orders_list):
        print("\n")
        print(i)
        for key, value in order.items():
            print("{}: {}".format(key, value).title())
    
    order_status_to_update = int(input("\nEnter the number of the order you want to update\n:"))
    for i, order in enumerate(orders_list):
        if i == order_status_to_update:
            print("This is the order to be updated:\n")
            selected_order = orders_list[order_status_to_update]        
            for key, value in selected_order.items():
                print("{}: {}".format(key, value).title()) 
            confirmation = int(input("\nEnter 1 to confirm\nEnter 2 to restart\nEnter 0 to return to the Order Menu:\n"))
            if confirmation == 2:
                update_order_status_file()
            elif confirmation == 0:
                order_menu()
            elif confirmation == 1:
                status_list = ["Cancelled","Preparing","Out for Delivery", "Delivered"]
                print("\nOrder Statuses:\n")
                for i, stat in enumerate(status_list):
                    print(i,stat)
                updated_status = int(input("\nSelect the number corresponding to the new status:\n"))
                if updated_status == 0:
                    d1 = {"Status":"Cancelled"}
                    print("This is the updated order:\n")
                    orders_list[order_status_to_update].update(d1)
                    for order in orders_list[order_status_to_update]:
                        for key, value in order.items():
                            print("{}: {}".format(key, value).title())
                            navigation()
                            break
                elif updated_status == 1:
                    d1 = {"Status":"Preparing"}
                    print("This is the updated order:\n")
                    for order in orders_list[order_status_to_update]:
                        order[order_status_to_update].update(d1)
                        for key, value in order.items():
                            print("{}: {}".format(key, value).title())
                            navigation()
                            break
                elif updated_status == 2:
                    d1 = {"Status":"Out for Delivery"}
                    print("This is the updated order:\n")
                    for i, order in orders_list[order_status_to_update]:
                        order[order_status_to_update].update(d1)
                        for key, value in order.items():
                            print("{}: {}".format(key, value).title())
                            navigation()
                            break
                elif updated_status == 3:
                    d1 = {"Status":"Delivered"}
                    print("This is the updated order:\n")
                    for order in orders_list[order_status_to_update]:
                        order[order_status_to_update].update(d1)
                        for key, value in order.items():
                            print("{}: {}".format(key, value).title())
                            navigation()
                            break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#def update_order_file():

#def cancel_order_file():

#---------------------------------------------MENU CODE-----------------------------------------------

def main_menu():
    print("-----------------------------------------------")
    print("         DEL'S DINER ORDERING SYSTEM           ")
    print("                  MAIN MENU                    ")
    print("-----------------------------------------------")
    try:
        first_input = int(input("Welcome! To start:\nEnter 1 to see our Product Menu\nEnter 2 to see our Courier Menu\nEnter 3 to see our Order Menu or\nEnter 0 to Exit the App:\n"))
        if first_input == 0:
            close_app()
        elif first_input == 1:
            product_menu()
        elif first_input == 2:
            courier_menu()
        elif first_input == 3:
            order_menu()
        else:
            incorrect_function()
            main_menu()
    except ValueError:
        incorrect_function()
        main_menu()

def navigation():
    try:
        navigation_input = int(input("\nEnter 0 to return to Main Menu\nEnter 1 to return to Product Menu\nEnter 2 to return to return to Courier Menu\nEnter 3 to Return to Order Menu:\n"))
        if navigation_input == 0:
            main_menu()
        elif navigation_input == 1:
            product_menu()
        elif navigation_input == 2:
            courier_menu()
        elif navigation_input == 3:
            order_menu()        
        else:
            incorrect_function()
            main_menu()
    except ValueError:
        incorrect_function()
        main_menu()

#------------------------------------------PRODUCT MENU CODE------------------------------------------

def product_menu():
    print("-----------------------------------------------")
    print("                PRODUCT MENU                   ")
    print("-----------------------------------------------")
    try:
        second_input = int(input("Enter 0 to Return to Main Menu\nEnter 1 to View Existing Products\nEnter 2 to Add a New Product\nEnter 3 to Update an Existing Product\nEnter 4 to Delete a Product:\n"))
        if second_input == 0:
            main_menu()
        elif second_input == 1:  
            view_products()
        elif second_input == 2:
            add_product()
        elif second_input == 3:
            update_product()
        elif second_input == 4:
            delete_product()     
        else:
            incorrect_function()
            product_menu()
    except ValueError:
        incorrect_function()
        product_menu()

def view_products():
    print("-----------------------------------------------")
    print("                PRODUCT LIST                   ")
    print("-----------------------------------------------")
    for product in products:
        print(product)
    navigation()

def add_product():
    print("-----------------------------------------------")            
    print("                ADD NEW PRODUCT                ")            
    print("-----------------------------------------------") 
    add_products_file()
    navigation()

def update_product():
    print("-----------------------------------------------")
    print("           MODIFY EXISTING PRODUCT             ")
    print("-----------------------------------------------")
    update_products_file()    

def delete_product():
    print("-----------------------------------------------")
    print("                REMOVE A PRODUCT               ")
    print("-----------------------------------------------")
    delete_product_file()

#------------------------------------------COURIER MENU CODE------------------------------------------

def courier_menu():
    print("-----------------------------------------------")
    print("                COURIER MENU                   ")
    print("-----------------------------------------------")
    try:
        second_input = int(input("Enter 0 to Return to Main Menu\nEnter 1 to View Existing Couriers\nEnter 2 to Add a New Courier\nEnter 3 to Update an Existing Courier\nEnter 4 to Delete a Courier:\n"))
        if second_input == 0:
            main_menu()
        elif second_input == 1:  
            view_couriers()
        elif second_input == 2:
            add_courier()
        elif second_input == 3:
            update_courier()
        elif second_input == 4:
            delete_courier()     
        else:
            incorrect_function()
            courier_menu()
    except ValueError:
        incorrect_function()
        courier_menu()

def view_couriers():
    print("-----------------------------------------------")
    print("                COURIER LIST                   ")
    print("-----------------------------------------------")
    for courier in couriers:
        print(courier)
    navigation()

def add_courier():
    print("-----------------------------------------------")            
    print("                ADD NEW COURIER                ")            
    print("-----------------------------------------------") 
    add_courier_file()
    navigation()

def update_courier():
    print("-----------------------------------------------")
    print("           MODIFY EXISTING COURIER             ")
    print("-----------------------------------------------")
    update_courier_file()

def delete_courier():
    print("-----------------------------------------------")
    print("                REMOVE A COURIER               ")
    print("-----------------------------------------------")
    delete_courier_file()

#--------------------------------------------ORDER MENU CODE-------------------------------------------

def order_menu():
    print("-----------------------------------------------")
    print("                 ORDER MENU                    ")
    print("-----------------------------------------------")
    try:
        second_input = int(input("Enter 0 to Return to Main Menu\nEnter 1 to View Existing Orders\nEnter 2 to Add a New Order\nEnter 3 to Update the Status of an Order\nEnter 4 to Update an Order\nEnter 5 to Delete an Order:\n"))
        if second_input == 0:
            main_menu()
        elif second_input == 1:  
            view_orders()
        elif second_input == 2:
            add_order()
        elif second_input == 3:
            update_order_status()
        elif second_input == 4:
            update_order()
        elif second_input == 5:
            delete_order()     
        else:
            incorrect_function()
            order_menu()
    except ValueError:
        incorrect_function()
        order_menu()

def view_orders():
    print("-----------------------------------------------")
    print("                 ORDER LIST                    ")
    print("-----------------------------------------------")
    for i, order in enumerate(orders_list):
        print("\n")
        print(i)
        for key, value in order.items():
            print("{}: {}".format(key, value).title())
    #view_orders_file()
    navigation()

def add_order():
    print("-----------------------------------------------")            
    print("                 ADD NEW ORDER                 ")            
    print("-----------------------------------------------")
    add_order_file()
    navigation()

def update_order_status():
    print("-----------------------------------------------")
    print("             MODIFY ORDER STATUS               ")
    print("-----------------------------------------------")
    update_order_status_file()
    navigation()

def update_order():
    print("-----------------------------------------------")
    print("            MODIFY EXISTING ORDER              ")
    print("-----------------------------------------------")
    #def update_order_file():
    navigation()

def delete_order():
    print("-----------------------------------------------")
    print("               REMOVE AN ORDER                 ")
    print("-----------------------------------------------")
    #def cancel_order_file():
    navigation()

#----------------------------------------------OTHER CODE-----------------------------------------------

def incorrect_function():
    print("\nSorry that entry was not recognised, please try again")

def close_app():
    exit("Thank you, goodbye!")

load_products_file()
load_couriers_file()
load_orders_file()
main_menu()

#TO DO:
#LOOK AT VE, LIBRARIS AND DIRECTORY LAYOUT AND MINIPRO SLIDES
# do you need to add the entire file path to open(.txt, 'r)???
#scrub up on unit testing, rewatch missed part of lecture - pytest, mnkeycapture
#SSAVE ON EXIT OF APP - HOW TO DO
#ADD UNIT TESTING


# write a dictionary and save to csv file to add:
# customer's name, address and phone number, as well as the status of the order, the courier etc
#write unit test to cover update order status test  function
#headings = [["Firstname", "Surname", "Address", "Postcode", "Phone no.", "Order Status", "Courier"]]