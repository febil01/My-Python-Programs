list=["Welcome","to","Python"]

#Joins or Adds a space after every element in the list
string=" ".join(list) #Join only works with strings by default
#Prints the string after the join operation is performed 
print(string)
print("#".join(string)) #Adds a # after each character in the string 

data=[23,65,"Numbers"]
print(" ".join(str(item) for item in data)) #Using Generator expression so that join works with numbers

string_="hello"
print("#".join(string_))
