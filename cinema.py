def checkSeats(seatingDict):
    countvacant=0
    for key in seatingDict:
        if seatingDict[key] == "vacant":
            countvacant=countvacant+1
    return countvacant

def bookTickets(seatingDict):
    tickets=int(input("Enter the number of tickets:"))
    countvacant=checkSeats(seatingDict)   
    if tickets>countvacant:
        print(tickets,"tickets are not available......")
        return seatingDict
    print(tickets,"tickets have been booked...")
    for key,elem in seatingDict.items():
        if elem == "vacant" and tickets>0:
            seatingDict[key]="booked"
            tickets=tickets-1
    return seatingDict

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