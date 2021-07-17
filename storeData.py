def searchProcessor():
    file=open("Processors.txt","r")
    processor=file.read().split('\n')
    search=input("Enter the processor to be search for:")
    for value in processor:
        if value.lower() == search.lower():
            print(search,"has been found")
            return
    print(search,"IS NOT FOUND!!!!!!!!!!")

while True:
    print("##### READING AND DISPLAYING A FILE")
    print("1. Input processor data into a file")
    print("2. Display the processor data from a file")
    print("3. Search for a processor")
    print("4. Exit the program")
    choice=int(input("Enter your choice (1-3):"))
    if choice==1:
        file=open("Processors.txt","a")
        print("Enter the name of the processor to be added to the file:")
        value=input()
        file.write(value)
        file.write("\n")
        print(value,"has been written to Processors.txt")
    elif choice==2:
        file=open("Processors.txt","r")
        print('Contents of the file Processors.txt:')
        with file:
            for value in file:
                print(value,end='')
    elif choice==3:
        searchProcessor()
    elif choice==4:
        exit()
    else:
        print("Wrong choice entered :(")
         