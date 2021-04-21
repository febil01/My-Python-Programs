#Initializing a 2D list
list = [[10,2,34,56],[122,34,45,67],[23,2232,12]]

#Prints all the lists present inside a list 
print(list)

#prints the second element in the first list
print(list[0][1])

#Prints the fourth element in the second list
print(list[1][3])

#prints the last element in the third list
print(list[2][2])

#Appends data in the third list
list[2].append(100)

#Modifying the value in the third list
list[2][0] = 500

#Prints the modified list after appending and modify the contents in the list 
print("Modified list:",list)

#List iteration for 2D lists 
print()
#Method 1
def method1_2D(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j],end=" ") #Ends with a space instead of a newline 
        print()

#Method 2
def method2_2D(list):
    for inner in list:
        for item in inner:
            print(item,end=" ")
        print()

print("2D List iteration using method 1:")
method1_2D(list)
print("\n2D List iteration using method 2")
method2_2D(list)