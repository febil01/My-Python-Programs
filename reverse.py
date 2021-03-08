string=input("Enter a string:")
n=len(string) - 1
reverse=""
while (n >= 0):
    reverse = reverse + string[n]
    n=n-1
print("The reversed string is:",reverse)