strings=["a","aAA","ABCD","FE","F"]
print("Printing the original list:",strings)
print("Sorted list based on ASCII",sorted(strings))
print("Sorted list with lower case priority:",sorted(strings,key=str.lower)) #or strings.sort(key=str.lower)
print("Sorted list based on length:",sorted(strings,key=len))