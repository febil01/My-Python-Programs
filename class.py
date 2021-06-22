class Car():
    ValueForMoney=[]

    def __init__(self, Brand, Model, price):
        self.Brand=Brand
        self.Model=Model
        self.price=price
    
    def expensive(self):
        if self.price > 30000:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.Brand} {self.Model} costs around ${self.price} and is very budget friendly"
    
    def __eq__(self, next):
        if self.Brand == next.Brand and self.Model == next.Model:
            return True
        return False 

    #__hash__= None #For Mutable data types
    def __hash__(self):
       return hash(self.Brand) ^ (self.price) #Hashes should not changes and should be the same throughout the program

car1=Car("Tesla","Model S",131100) #New car object
car2=Car("Toyota","Prius",25000)    #Second car object
car3=Car("Tesla","Model S",131100)
#car3=Car("Ford","Focus",20000)

print("Brand Name:",car1.Brand)
print("Model:",car1.Model)
if car1.expensive():
    print("The car is on the expensive side")
else:
    print("The car is not expensive")

Car.ValueForMoney.append(car2)
Car.ValueForMoney.append(car3)
print("Budget friendly car:")
for car in Car.ValueForMoney:
    print(car)
print(car1==car3) #Compares both objects by data by overriding __eq__ method in class
print(hash(car1)==hash(car3))
print(hash(car1))

print(id(car1)) #prints unique ID of the object (objects in memory)
print(id(car2))
car1=car2 #Both objects has the same ID now
print(id(car1) == id(car2))
car1=Car("Toyota","Prius",25000)
car2=Car("Toyota","Prius",25000)  
print(id(car1)==id(car2)) #Both objects have the same data but the IDs are not considered equal
