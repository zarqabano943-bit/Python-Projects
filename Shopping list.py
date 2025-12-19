shopping_list=[]

while True:
    print('\nOptions:')
    print('1. Add item')
    print('2. View all items')
    print('3. Remove item ')
    print('4. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        item = input('Enter a new item: ')
        shopping_list.append({'item':item,})
        print("Item added!")

    elif choice == '2':
        if not shopping_list:
            print("No item added yet.")
        else:
            print(shopping_list)


    elif choice == '3':
        item =input('Enter item to remove: ')
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "item removed",)
        else:
            print("item not found")

    elif choice == '4':
        print("Exited")
        break

    else:
        print("Invalid option! Please choose again.")


