stack=[]
while True:
    print("==========STACK==========")
    print("1. Push items to the stack")
    print("2. Pop an item from the stack")
    print("3. Display the stack")
    print("4. Quit")
    choice=int(input("Enter your choice (1-4):"))
    
    if(choice==1):
        print("Enter items in the stack (Hit Enter after each item and type 'q' to quit):")
        while True:
            item=input()
            if item.lower() == 'q':
                break
    
            stack.append(item)
        print(stack,"has been added to the stack")
    
    elif(choice==2):
        if not stack:
           print("The stack is empty")
           continue 
        print(stack.pop(),"Has been popped") 
    
    elif(choice==3):
        print("Printing the items in your shopping cart:")
        print(stack)
    
    elif(choice==4):
        break
    
    else:
        print("Invalid choice entered. try again")