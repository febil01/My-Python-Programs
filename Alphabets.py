def getResult(Words,Bucket):
    found=0
    for i in range(len(Words)):
        for j in range(len(Bucket)):
            if Bucket[j] == Words[i]:
                found=found+1
                Bucket.pop(j)
                break
    if found == len(Words):
        print("YES")
    else:
        print("NO")

Bucket=[] #An empty list to store the Alphabets
Words=[] #A list that stores the words 
Bucket=input("Enter all the Alphabets in the Bucket seperated by a comma:").split(', ') #Inputs all the words in the Bucket list
n=int(input("Enter the number of words:")) #Stores the number of lines
print("Input all the words:") 
for i in range(n):
    Words.append(input())  #Stores all the words in the list
print("Results:")
for i in range(n):
    getResult(Words[i],Bucket)

