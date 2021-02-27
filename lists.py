languages=["C++","Python","Java","C","Javascript","php"] # Assign a list with values
print('Printing the contents in the list "languages" ',languages) # Printing the list
print('The length of the list "languages" is ',len(languages)) # printing the length of the list
languages.append("ruby")
print("New list after adding an item using append:",languages)
languages.extend(["CSS","xml"])
print('New list after multiple items using extend:',languages)
print('The value of the first item in the list is',languages[0]) # printing a single item in the list using its index or position
print('The value of the last item in the list is',languages[-1]) # Prints the last element or item in the list 
print('The value of the second last item in the list is',languages[-2])
print("THE LAST 3 ITEMS IN THE LIST IS",languages[-1:])
print('The length of the string "languages" is',len(languages))
languages.append("Keyboard")
print("Current list:",languages)

if "Keyboard" in languages:
    languages.remove("Keyboard")
print("Updated list",languages)

if "C++" in languages:
    print('C++ is in the list "languages"')

if "C++" not in languages:
    print("C++ is not in the list")  

healthy=["kale chips","broccoli"]
backpack=["pizza","frozen custard","apple crisp","kale chips"]
backpack[:]=[item for item in backpack if item in healthy] #list comprehension 
power = [(square+1)**2 for square in range(10)]
print(backpack)
print("List of first 10 square numbers:",power)
separator=" "
print(separator.join(map(str,power)))
print(backpack)
Monitors=["Acer","Acer","Dell","BENQ","Samsung","LG","Sony","Sony"]
print("Printing the list Monitors:",Monitors)
print("Sony occurs",Monitors.count("Sony"),'times in the list "Monitors"')
print("Sony" in Monitors)
setMonitors=[str(Monitors.count(item)) + " " + item for item in set(Monitors)]
print(setMonitors)
lowerMonitors=[]
upperMonitors=[]
print(Monitors)
print("Printing List Monitors",Monitors)
for item in Monitors:
    lowerMonitors.append(item.lower())
    upperMonitors.append(item.upper())
print("List \"Monitors\" in lower case:",lowerMonitors)
print("List \"Monitors\" in UPPER CASE:",upperMonitors)
Monitors.insert(0,"LG") # To place items in a particular index
print(Monitors)