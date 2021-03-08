# Assign a list with values
languages=["C++","Python","Java","C","Javascript","php"] 
 # Printing the list
print('Printing the contents in the list "languages" ',languages)
 # printing the length of the list
print('The length of the list "languages" is ',len(languages))
# Adding A single item into the list
languages.append("ruby")
# Printing the list after appending it 
print("New list after adding an item using append:",languages)
# Appending multiple items in the list using extend
languages.extend(["CSS","xml"])
# Printing the list after extending it 

#Printing the index and the item in a list
for item in languages:
    print(f"languages[{languages.index(item)}]:",item)

print('New list after multiple items using extend:',languages)
print('The value of the first item in the list is',languages[0]) # printing a single item in the list using its index or position
print('The value of the last item in the list is',languages[-1]) # Prints the last element or item in the list 
print('The value of the second last item in the list is',languages[-2]) # Prints the second last item in the list 
print('The length of the string "languages" is',len(languages))
languages.append("Keyboard")
print("Current list:",languages)

# using conditional statement to check for a certain condition
if "Keyboard" in languages: #Checks if keyboard is in the list languages 
    languages.remove("Keyboard") #Removes the item if it is present 
print("Updated list",languages)

if "C++" in languages:
    print('C++ is in the list "languages"')

if "C++" not in languages:
    print("C++ is not in the list")  

healthy=["kale chips","broccoli"]
backpack=["pizza","frozen custard","apple crisp","kale chips"]
# LIST COMPREHENSION
# Traverse throught backpack and checks if that item is present in another list healthy and stores in backpack
backpack[:]=[item for item in backpack if item in healthy] 
print(backpack)

power = [(square+1)**2 for square in range(10)] #Stores the squares of numbers from 1 to 10
print("List of first 10 square numbers:",power) 

separator=" "
print(separator.join(map(str,power))) #Removes the square brackets when printing a list
print(backpack)

Monitors=["Acer","Acer","Dell","BENQ","Samsung","LG","Sony","Sony"]
print("Printing the list Monitors:",Monitors)

print("Sony occurs",Monitors.count("Sony"),'times in the list "Monitors"') #Finds the occurence of an item in the list

print("Sony" in Monitors) #Prints the number of times an item occurs in the list

setMonitors=[str(Monitors.count(item)) + " " + item for item in set(Monitors)] #Prints the occurence of an item and the display the item in the list
print(setMonitors)

lowerMonitors=[] #Assigns an empty list
upperMonitors=[]
print(Monitors)
print("Printing List Monitors",Monitors)
for item in Monitors:
    lowerMonitors.append(item.lower()) #Converting the items in the list to lowercase 
    upperMonitors.append(item.upper()) #Converting the items in the list to uppercase 

print("List \"Monitors\" in lower case:",lowerMonitors)
print("List \"Monitors\" in UPPER CASE:",upperMonitors)

Monitors.insert(0,"LG") # To place items in a particular index
print(Monitors)
Monitors.remove("Sony")
print(Monitors)

del Monitors[0] # To delete an item in the list in a particular index
print(Monitors)
Monitors.pop(3)
print(Monitors)

del Monitors[Monitors.index("Acer"):Monitors.index("Acer")+2] # To delete items from a range of index
del Monitors[0:2]
print(Monitors)

MonitorsCopy = Monitors[:] #Saving a copy of list using slicing 
print("The id of the list \"Monitors\" is",id(Monitors),"and the id of the list \"MonitorsCopy\" is",id(MonitorsCopy)) #Prints the id of both the list

MonitorsCopy[:]=["1","2","3"] #Retains the ID of the list
print(id(MonitorsCopy))
MonitorsCopy = ["1","2","3"] #Does not retain the ID of the list and creates a brand new list 
print(id(Monitors))