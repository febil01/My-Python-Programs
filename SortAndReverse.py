list=[]
n=int(input("Enter the number of elements in the list:"))
print("Enter all the items:")
for item in range(n):
    string=input()
    list.append(string)
print("Printing the original list:",list)
print("Printing the reversed sorted list:",sorted(list,reverse=True))
""" METHOD 2
list.sort()
list.reverse()
print(list)
"""