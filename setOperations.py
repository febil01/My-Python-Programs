#union Operation
print()
print("########## SET OPERATIONS ###############")
Animals1={"Lion","Cheetah","Leopard","Jaguar","Rhino","Zebra"}
Animals2={"Lion","Leopard","Bear","Beaver","Hyena","Tiger","Deer"}
print("Set 1:",Animals1)
print("Set 2:",Animals2)
print()
print("1.Union Operation:")
Animals= Animals1 | Animals2 #Union operation where both the sets are combined and duplicates are removed
print(Animals)

#Intersection (Common elements or shared elements)
print()
Animals=Animals1 & Animals2
print("Intersection operation:")
print(Animals)

#Difference
print()
Animals=Animals1 - Animals2
print("Difference operation:")
print(Animals)

#Symmetric Difference
Animals = Animals1 ^ Animals2
print("Symmetric Difference:")
print(Animals)
