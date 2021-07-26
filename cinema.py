def checkSeats(seatingDict):
    countvacant=0
    for key in seatingDict:
        if seatingDict[key] == "vacant":
            countvacant=countvacant+1
    return countvacant

def bookTickets(seatingDict):
    tickets=int(input("Enter the number of tickets:"))
    seatList=[]
    i=0
    seatList=assignSeats(seatingDict,tickets)
    countvacant=checkSeats(seatingDict)
    if(not validateSeat(seatList,seatingDict)):
        print("Invalid Seat(s) Entered. Please try adding it again with valid seat numbers....")
        return seatingDict
    if tickets>countvacant:
        print(tickets,"tickets are not available......")
        return seatingDict
    print(tickets,"tickets have been booked...")
    for i in range(len(seatList)):
            seatingDict[seatList[i]]="booked"
            i=i+1
    return seatingDict

def assignSeats(seatingDict,tickets):
    seatList=[]
    print("List of available seats:")
    i=1
    for key,elem in seatingDict.items():
        if elem == "vacant":
            print(key,"---->",elem)
    print("Enter the list of seats to be booked (Press Enter after every seat):")
    while (i<=tickets):
        seatList.append(input())
        i=i+1
    return seatList

def validateSeat(seatList,seatingDict):
    check=0
    for i in seatingDict:
        for j in seatList:
            if j == i:
                check=check+1
                break
    if check==len(seatList):
        return True
    return False    


def displayTickets(seatingDict):
    for key,value in seatingDict.items():
        print(key,":",value)

def cancelTicket(seatingDict,seatNo):
    if seatingDict.get(seatNo):
        seatingDict[seatNo]="vacant"
        print(seatNo,"seat has been cancelled...")
        return seatingDict
    print("Invalid seat entered..")
    return seatingDict

seatingDict={
    "s1":"vacant",
    "s2":"vacant",
    "s3":"vacant",
    "s4":"vacant",
    "s5":"vacant",
    "s6":"vacant",
    "s7":"vacant",
    "s8":"vacant",
    "s9":"vacant",
}
countbooked=0
countvacant=0
while True:
    print("++++++++++++MOVIE BOOKING++++++++++++")
    print("1. BOOK A TICKET")
    print("2. DISPLAY ALL SEATS")
    print("3. CANCEL A TICKET")
    print("4. EXIT THE PROGRAM")
    choice=int(input("Enter your choice(1-4):"))
    if choice==1:
        seatingDict=bookTickets(seatingDict)
    elif choice==2:
        displayTickets(seatingDict)
    elif choice==3:
        seatNo=input("Enter the seat number:")
        cancelTicket(seatingDict,seatNo)
    elif choice==4:
        exit()
