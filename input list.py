try:
    list=[]
    n=0;
    n=input("Enter the number of elements in a list:")
    n=int(n)
    print("Enter",n,"item(s) in the list:")
    for i in range(n):
        list.append(input())
    print("Printing all the items in the list...")
    print(list)
except Exception as e:
    print(e)