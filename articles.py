from clearModule import clear

clear()
articles={
    "a":0,
    "an":0,
    "the":0
}
string=input("Enter a paragraph:")

string=string.lower()
words=string.split()

for item in words:
    if item in articles:
        articles[item]+=1


print(articles)
