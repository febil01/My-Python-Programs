try:
    fact=input("Enter a number:")
    num=fact 
    fact=int(fact)
    factorial=1
    for x in range(fact):
        if(fact>=1):
            factorial=factorial*fact
            fact=fact-1
    print("The factorial of",num,"is",factorial)
except: 
    print("Invalid number")