#All the elements in a set has to be unique
Brands={"Dell","Apple","Nvidia","Intel","Amd"}
Brands.add("Dell") #Does not add Dell to the set since its already present
print(Brands)

#Creating a set that takes value from the user
mySet=set() #Initialize empty set
print("Enter the number of elements in the set:")
n=int(input())
print("Enter all the item in the set:")
for i in range(n):
    mySet.add(input())
print("The set is",mySet)
