Computer=["Monitor","Keyboard","CPU","SSD","HDD","GPU","RAM"] #Initialize list with elements
print("The contents of the list:",Computer)
print("The contents of the list in reverse order:",Computer[::-1])
print()
print("The first two elements in the list:",Computer[0:2:1])
print("Printing all the even elements in the list:",Computer[1::2])
print("Printing all the odd elements in the list:",Computer[::2])
print("Printing all the even elements in the list in reverse order:",Computer[-2::-2])
print("Printing all the odd elements in the list in reverse order:",Computer[::-2])
print("Printing the first 3 elements in the list:",Computer[:3:1])
print("Printing the last 3 elements in the list:",Computer[:-4:-1])
print(Computer[-1:-4:]) #list will be empty since Index jump by default is positive 
print(Computer[::4])
