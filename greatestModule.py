def great(data):
    data.sort()
    return data[-1]

"""
#Another method:
def great(data):
    for item in data:
        count=0
        for j in data:
            if((item>j) and (item!=j)):
                count=count+1
        if(count==len(data) - 1):
            big=item
    return big
"""