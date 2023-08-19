
# in python we have 3 types of variables:
# class variables(static variables), instance variable 

# note --> we create INSTANCE VARIABLE so it will be unique for every objects, If you want a COMMON VARIABLE for all object you can use CLASS VARIABLE/STATIC VARIABLE.
class Car:

    # defining class/static variable --> these variable are common for all object
    
    wheels=4
    
    def __init__(self):
       # defining the instance variable with value
       self.mileage=19
       self.company='BMW'

c1=Car()
c2=Car()

print('car-1 is ',c1.company,':',c1.mileage)
print('car-2 is ',c2.company,':',c2.mileage)

# let us update the value of car-1
c1.company='Honda'
print('After updating the car-1 is ',c1.company,':',c1.mileage)

# note --> we create INSTANCE VARIABLE so it will be unique for every objects, If you want a COMMON VARIABLE for all object you can use CLASS VARIABLE/STATIC VARIABLE.
print('Wheels for car 1 is',c1.wheels)
print('Wheels for car 2 is',c2.wheels)
# Suppose In future if the wheels changes to 5, then to make the changes in all object at once we use class/static variable which is shared among all objects.
# updating the wheels using class Name
Car.wheels=5
print('After Updating Wheels............. ')
print('Wheels for car 1 is',c1.wheels)
print('Wheels for car 2 is',c2.wheels)
#You can't change static variable with an instance , if you try to change it then it  will only create a new instance of that variable for the object. This will not affect the entire class.
c1.wheels=10
print('After Updating Wheels for car-1')
print('Wheels for car 1 is',c1.wheels)
print('Wheels for car 2 is',c2.wheels)

Car.wheels=99
# since you have changed the class static wheels's variable value therefore it has created a new object's instance variable inside obj car1 ... hence that;s why it is fetched the wheels values which is present inside object car-1 not the class  static wheels's variable. 
print('Wheels for car 1 is',c1.wheels)
print('Wheels for car 2 is',c2.wheels)
# accessing the class name
print(c1.__class__)