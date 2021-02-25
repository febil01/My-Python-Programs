#printing a basic message
print("Hello world") #print a message on the console 

a=10 #Declaring a variable 
b=20 #Declaring a variable

#printing a value (Method 1: Using comma , character) 
print("The value of a is",a,"and the value of b is",b) #print values of variables 


#printing a value (Method 2: Using Format String)
print(f"{a} and {b} are even numbers")

#printing a value (Method 3: Using Format String with Positional Argument)
print("Both {} and {} is divisible by 5".format(a,b))
print("Both {1} and {0} is divisible by 2".format(a,b))

#printing a value (Method 4: Using plus + character)
print("The sum of "+str(a)+" and " +str(b)+" is",a+b)

