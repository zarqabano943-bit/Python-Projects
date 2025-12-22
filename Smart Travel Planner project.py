while True:
    print("CITY SELECTION")
    print('1. Karachi')
    print('2. Lahore')
    print('3. Islamabad')

    choice = input('Choose an City: ')

    if choice == "1":
        print("You selected Karachi")
    elif choice == "2":
        print("You selected Lahore")
    elif choice == "3":
        print("You selected Islamabad")
    else:
        print("Invalid city selection")
        continue
        
    print("\nTRANSPORT SELECTION")
    print('1. Bus')
    print('2. Taxi')
    print('3. Metro')

    transport = input("Choose any transport: ")
    timing = input("Choose time slot (morning / afternoon / evening): ")

    fare = 0

    if transport == "1":   
        if timing == "morning" or timing == "evening":
            print("Bus is available in", timing)

            budget = int(input("Enter your budget: "))
            fare = 50

            if budget >= fare:
                print("In budget Bus selected")
            else:
                print("Insufficient budget!")
                continue
        else:
            print("Bus is NOT available in", timing)
            continue

    elif transport == "2":   
        if timing == "morning" or timing == "afternoon" or timing == "evening":
            print("Taxi is available in", timing)

            budget = int(input("Enter your budget: "))
            fare = 100

            if budget >= fare:
                print("In budget Taxi selected")
            else:
                print("Insufficient budget!")
                continue
        else:
            print("Invalid time slot")
            continue

    elif transport == "3":   
        if timing == "afternoon" or timing == "evening":
            print("Metro is available in", timing)

            budget = int(input("Enter your budget: "))
            fare = 80

            if budget >= fare:
                print("In budget Metro selected")
            else:
                print("Insufficient budget!")
                continue
        else:
            print("Metro is NOT available in", timing)
            continue

    else:
        print("Invalid transport option")
        continue

    
    total = fare

    extra = input("Do you want extra services? (yes/no): ")

    if extra == "yes":
        print("\nExtra Services")
        print("1. Meal (20)")
        print("2. Guide (30)")
        print("3. Priority Boarding (40)")

        service = input("Choose service: ")

        if service == "1":
            total += 20
        elif service == "2":
            total += 30
        elif service == "3":
            total += 40
        else:
            print("Invalid service")

    print("\nTotal Bill:", total)
    print("THANK YOU FOR YOUR BOOKING")
    break
