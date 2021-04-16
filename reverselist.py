data1=[1,2,3,4,5,6]
print("The value of list 1:",data1)
data1.reverse()
print("The value of list 1 in reverse:",data1)
#Method 2
data2=["Chrome","firefox","safari","opera","brave"]
print("The value of list 2:",data2)
for item in range(len(data2)//2):
    data2[item],data2[-item-1] = data2[-item-1], data2[item]
print("The value of list 2 in reverse:",data2)