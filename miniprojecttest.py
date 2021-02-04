
products = ["water", "apple juice", "orange Juice", "lemonade", "sprite", "coke", "tea", "americano", "expresso", "cappuccino"]

def view_products():
    for product in products:
        print(product)
        
def add_product(): 
    new_entry = str(input("Enter name of new product: "))
    products.append(new_entry)
    print("{} has been added to the list".format(new_entry)) 

def update_product():
    print(products)
    product_update = str(input("Enter the name of the product you want to update:\n"))
    for i, product in enumerate(products):
        if product == product_update:
            updated_name = str(input("Enter the updated name:\n"))
            products[i] = updated_name
            print("This is the new list:\n{}".format(products))

def delete_product():
    print(products)
    product_delete = input("Enter name of product you want to delete from the list:\n")
    for i, product in enumerate(products):
        if product == product_delete:
            products.remove(product_delete)
            print ("{} has been removed from the list".format(product_delete))
            print(products)
        
            
#NEED TO ADD ELSE STATEMENTS IF WRONG NUMBER IS ENTERED
#TRY EXCEPT BLOCKS?
#MAINMENU FUNCTION? DEF MAIN()?
#ALL LOWERCASE? .LOWER
        
    
while True:    
    print("-----------------------------------------------")
    print("           CAFE FOOD ORDERING SYSTEM           ")
    print("                  MAIN MENU                    ")
    print("-----------------------------------------------")
    first_input = int(input("Welcome!\nTo start, enter 1 to see our product menu or 0 to exit the app:")) 
    if first_input == 0:
        print("Thank you, goodbye!")
        exit()
    elif first_input == 1:
        print("-----------------------------------------------")
        print("                PRODUCT MENU                   ")
        print("-----------------------------------------------")
        second_input = int(input("Enter 0 to return to main menu \nEnter 1 to view existing products \nEnter 2 to create a new product \nEnter 3 to update an existing product \nEnter 4 to delete an existing product:\n"))
        if second_input == 0:
            break       
        elif second_input == 1:   
            print("-----------------------------------------------")
            print("                PRODUCT LIST                   ")
            print("-----------------------------------------------")
            view_products()
            menu_input = int(input("Enter 0 to return to main menu:"))
            if menu_input == 0:
                continue
        elif second_input == 2:
            print("-----------------------------------------------")
            print("                ADD NEW PRODUCT                ")
            print("-----------------------------------------------")
            add_product()
            menu_input2 = int(input("Enter 0 to return to main menu:"))
            if menu_input2 == 0:
                continue
        elif second_input == 3:
            print("-----------------------------------------------")
            print("           MODIFY EXISTING PRODUCT             ")
            print("-----------------------------------------------")
            update_product()
            menu_input3 = int(input("Enter 0 to return to main menu:"))
            if menu_input3 == 0:
                continue
        elif second_input == 4:
            print("-----------------------------------------------")
            print("                REMOVE A PRODUCT               ")
            print("-----------------------------------------------")
            delete_product()
            menu_input4 = int(input("Enter 0 to return to main menu:"))
            if menu_input4 == 0:
                continue      
    else:
        print("Sorry that entry was not recognised, please enter a different number")
                