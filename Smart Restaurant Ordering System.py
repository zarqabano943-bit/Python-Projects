print("------WELCOME TO ZARQA'S RESTAURANT------")
print("    Smart Restaurant Ordering System  ")
print("                                                       ")

menu = {"Fast Food": {"Burger": 150, "Pizza": 300},"BBQ": {"Tikka": 200, "Boti": 250},"Chinese": {"Chowmein": 180, "Fried Rice": 220}}

while True:
    print("Select Food Category")
    print("1 - Fast Food")
    print("2 - BBQ")
    print("3 - Chinese")

    choice = input("Which type of Food Category you want to order : ")
    
#1--
    while True:
        if choice == "1":
            print("1 - Burger")
            print("2 - Pizza ")

            item = input("choose item of Fast Food: ")

            if item == "1":
                item_price = 150
                item_name = "Burger"
                break
            elif item == "2":
                item_price = 300
                item_name = "Pizza"
                break
            else:
                print("invalid item, choose again")
            

        elif choice == "2":
            print("1 - Tikka")
            print("2 - Boti ")

            item = input("choose item of BBQs: ")
            
            if item == "1":
                item_price = 200
                item_name = "Tikka"
                break
            elif item == "2":
                item_price = 250
                item_name = "Boti"
                break
            else:
                print("invalid item, choose again")


        elif choice == "3":
            print("1 - Chowmein")
            print("2 - Fried Rice")

            item = input("choose item of Chinese: ")
            
            if item == "1":
                item_price = 180
                item_name = "Chowmein"
                break
            elif item == "2":
                item_price = 220
                item_name = "Fried Rice"
                break
            else:
                print("invalid item, choose again")
             
        else:
            print("invalid option, Select again")
            break

#2---
    while True:
        try:
            quantity = int(input("Enter the Quantity of items: "))
            if quantity > 0:
                break
            else:
                print("invalid quantity, must be greater than 0")
        except:
            print("Enter numeric value only")


    total_price = item_price * quantity            

#3--
    add_on_price = 0
    add_On_name = "None"
    
    add_Ons = input("Do you want add-ons? (yes/no): ")

    if add_Ons == "yes":
        print("Add-Ons Selection ")
        print("1 → Extra Cheese 50 ")
        print("2 → Drink 60 ")
        print("3 → Both 110 ")

        item1 = input("Select the option: ")

        if item1 == "1":
            add_on_price = 50
            add_On_name = "Extra Cheese"
        elif item1 == "2":
            add_on_price = 60
            add_On_name = "Drink"
        elif item1 == "3":
            add_on_price = 110
            add_On_name = "Extra Cheese + Drink"
        else:
            print("No add-ons selected")

    grand_total = total_price + add_on_price

#4---
    print("\n----- Order Summary -----")
    print("Item          :", item_name)
    print("Price         :", item_price)
    print("Quantity      :", quantity)
    print("Total         :", total_price)
    print("Add-Ons       :", add_On_name)
    print("Add-Ons-Price :", add_on_price)
    print("-----------------------")
    print("Grand Total   :", grand_total)
    print("Thank you for ordering!")

    break
