import sqlite3

def category(type):
    switcher = {
        1: "CPU",
        2: "Motherboard",
        3: "Graphics card",
        4: "SSD",
        5: "HDD",
        6: "Monitor",
        7: "Keyboard",
        8: "Mouse"
    }
    return switcher.get(type,"Invalid")

conn = sqlite3.connect(":PC.db:")
c=conn.cursor()
print("-------------------PC STORE DATABASE-------------------")
print("1. Store a new product into the database")
print("2. Display all the records from the database")
print("3. Delete a record from the database")
choice=int(input("Enter your choice:"))
if choice==1:
    print("------Enter the type of the product------")
    print("1 .CPU")
    print("2. Motherboard")
    print("3. Graphics card")
    print("4. SSD")
    print("5. HDD")
    print("6. Monitor")
    print("7. Keyboard")
    print("8. Mouse")
    type=int(input("Enter your choice:"))
    ctgry=category(type)
    if ctgry != "Invalid":
        print("Enter the brand of the Product:")
        name=input()
        print("Enter the model:")
        model=input()
        print("MSRP:")
        price=input()
        print("Year of manufacture:")
        year=int(input())
        c.execute("CREATE TABLE IF NOT EXISTS PCrecords (brand TEXT, model TEXT, msrp TEXT, year INTEGER)")
        conn.commit()
        value=[name,model,price,year]
        c.execute("INSERT INTO PCrecords VALUES(?,?,?,?)",value)
        conn.commit()

elif choice==2:
    try:
        c.execute("SELECT * FROM PCrecords")
        conn.commit()
        data=c.fetchall()
        print(data)
    except Exception as e:
        print("Database does not exist. Insert records into the database first")

elif choice==3:
    model=input("Enter the model number of the product to be deleted:")
    mysql='SELECT * FROM PCrecords WHERE model="' + model + "\""
    c.execute(mysql)
    if c.rowcount == 0:
        print(True)
        print(model,"not found in the database")
    else:
        deletesql='DELETE FROM PCrecords WHERE model="' + model + "\""
        c.execute(deletesql)
        conn.commit()
        print("Delete sucessfully")
conn.close()
