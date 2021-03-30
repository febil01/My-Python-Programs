swap1="hi"
swap2="bye"
print("Values before swapping:",swap1,swap2)
swap1,swap2=swap2,swap1
print("Values after swapping:",swap1,swap2)

#method 2 
a=10
b=20
print("Values before swapping:",a,b)
temp=a
a=b
b=temp
print("Values after swapping:",a,b)

#Swapping in list
fruits=["Strawberry","Mango","kiwi","Apple","Orange","Watermelon"]
index=0
print("List before swapping",fruits)
for index in range(len(fruits) // 2):
    fruits[index],fruits[-index-1] = fruits[-index-1],fruits[index]
print("List after swapping",fruits)