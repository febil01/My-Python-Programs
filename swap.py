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