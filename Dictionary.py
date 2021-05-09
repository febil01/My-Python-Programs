from clearModule import clear

clear()

#dictionary can store strings, intergers, tuples (immutable data types)
#All the keys are hashable 
pc={
    "Processor": "Amd Ryzen",
    "Ram": "16gb",
    "HDD": "1TB",
} 
print("Printing the dictionary:",pc)
print(pc["Ram"])

print(pc.get("HDD"))
print(pc.get("Monitor")) #Prints none since key is not found

pc["Monitor"] = "Dell"
pc.update({"Keyboard": "Corsair", "Mouse": "Logitech"}) #Adding multiple values else remove curly braces to add a single key:pair

print("Dictionary after adding more values:",pc)
del pc["Mouse"] #Deletes
print("Dictionary after deleting a key:pair",pc)

#iterating through a dictionary
for key,elem in pc.items():
    print(key,elem)

