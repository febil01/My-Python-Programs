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
print("The last 3 items in the list is",languages[-1:-4])
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
backpack[:]=[item for item in backpack if item in healthy]
print(backpack)