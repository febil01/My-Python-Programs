def checkClose():
    if file.closed:
        return True
    else:
        return False

file=open("input1","w")
file.write("write the file for the first time")
file.write("\nWriting the file the second time")
file.write("\nWriting the file the third time")
file=open("input2","a")
file.write("\nhello")
file.write("\nbye")

file=open("input1","r")

data=file.read().split('\n') #Splits the file based on newline else prints the entire text the way it is
print("The contents of the file \"input1:\"\n",data)

file=open("input2","r")
data=file.read().split('\n')
print('The contents of the file input2:',data)

print(checkClose())
file.close()
print(checkClose())

with open("input1") as file:
    print(checkClose())
    data=file.read().split(" ")
    print(data)
print(checkClose())
