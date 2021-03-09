string=input("Enter a string:")
#Method 1
n=len(string) - 1
reverse=""
while (n >= 0):
    reverse = reverse + string[n]
    n=n-1
print("The reversed string is:",reverse)
#Method 2 (Easier way)
print("The reversed string is",string[::-1])