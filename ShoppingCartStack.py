stack=[]
while True:
    print("==========ONLINE SHOP==========")
    print("1. Buy items")
    print("2. Delete items from carts")
    print("3. Buy items")
    print("4. Display shopping cart")
    print("5. Quit")
    choice=int(input("Enter your choice (1-5):"))
    if(choice==1):
        print("Enter a List of items in your shopping cart (Hit Enter after each item and type 'q' to quit):")
        while True:
            item=input()
            if item.lower() == 'q':
                break
            stack.append(item)
        print("The items you have entered has been added to your shopping cart")
    elif(choice==2):
        delete=input("Enter an item to delete from the shopping cart:")
        d=stack.index(delete)
        stack.pop(d)
        print(delete,"Has been popped") 
    elif(choice==3):
        print("The items in your cart have been ordered :)")
        stack.clear()
    elif(choice==4):
        print("Printing the items in your shopping cart:")
        print(stack)
    elif(choice==5):
        break
    else:
        print("Invalid choice entered. try again")