#Seperates the string based on spaces
string1="Hello how are you"
split1 = string1.split() #Splits the string
print(split1)

#Split the string based on newline
string2 = """Python is a high level programming\
 language
You can do a lot with python\
 like machine learning
Python is really cool"""
split2=string2.split("\n")
print(split2)

#Seperates the string based on a certain character
string3="HELLO#HOW#ARE YOU?"
split3=string3.split('#')
print(split3)
