from collections import Counter
duplicates=["Mango","Grapes","Watermelon","Oranges","Pears","Strawberry","Kiwi","Mango","Pears","Oranges","Oranges","Strawberry"]
print("List before removing duplicates:",duplicates)
print(Counter(duplicates))
for item in duplicates:
    if duplicates.count(item) > 1:
        duplicates.remove(item)
print("List after removing duplicates:",duplicates)