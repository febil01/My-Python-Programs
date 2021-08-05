def getBlock(apartmentBlock,reqs):
    schoolSet=set()
    gymSet=set()
    storeSet=set()
    for index,apartment in enumerate(apartmentBlock):
        if apartment.get(reqs[0]) == True:
            schoolSet.add(index+1)
        if apartment.get(reqs[1]) == True:
            gymSet.add(index+1)
        if apartment.get(reqs[2]) == True:
            storeSet.add(index+1)
    i1=schoolSet & gymSet
    i2=schoolSet & storeSet
    i3=gymSet & storeSet
    i4=schoolSet & gymSet & storeSet
   
    if i4:
         return f"Apartment {i4} is the right one for you. Has all the requirements"
    if i1 and i2:
        return f"Apartment {i1} is the right one for you. It has both a school and a gym and a store is present at apartment {i2}"
    if i2 and i3:
        return f"Apartment {i2} is the right one for you. It has both a school and a gym and a store is present at apartment {i3}"
    if i1:
        return f"Apartment {i1} is the right one for you. It has both a school and a gym and a store is present at apartment {storeSet}"
    if i2:
        return f"Apartment {i2} is the right one for you. It has both a school and a gym and a store is present at apartment {gymSet}"
    if i3:
        return f"Apartment {i3} is the right one for you. It has both a school and a gym and a store is present at apartment {schoolSet}"
    return f"All the apartments are bad. Better luck next time"


apartmentBlock=[
    {
        "School" : True,
        "Gym": False,
        "Store": False
    },
    {
        "School" : True,
        "Gym": True,
        "Store": False
    },
    {
        "School" : False,
        "Gym": True,
        "Store": False
    },
    {
        "School" : False,
        "Gym": False,
        "Store": False
    },
    {
        "School" : True,
        "Gym": False,
        "Store": False
    },
    {
        "School" : False,
        "Gym": True,
        "Store": True
    }
]
reqs=["School","Gym","Store"]
print(getBlock(apartmentBlock,reqs))
