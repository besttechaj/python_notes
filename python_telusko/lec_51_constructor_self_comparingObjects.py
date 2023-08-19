
# case 1:
"""class Computer:
    def __init__(self):
        # self-> it stores the current object
        # storing the local variables inside current object 
        self.name='Ajay'
        self.age=26

#creating the objects for class Computer
c1=Computer() # here the constructor will automatically call the init method internally whenever a new object is created
c2=Computer() # here the constructor will automatically call the init method internally whenever a new object is created
# Accessing the address of object c1 memory stored inside heap Memory
print('The address of current object is ',id(c1))
print('The address of current object is ',id(c2))

# Checking the variables assigned to both the objects
print('Name variable passed in c1 object is ',c1.name)
print('Age variable passed in c1 object is ',c1.age)
print('Name variable passed in c2 object is ',c2.name)
print('Age variable passed in c2 object is ',c2.age)

# overriding the existing name and age in object c2
print('Updating value')
c2.name='Prashant'
c2.age=24
print('Name variable passed in c2 object is ',c2.name)
print('Age variable passed in c2 object is ',c2.age)"""

# case 2:
class Computer:
    def __init__(self):
        # self-> it stores the current object
        # storing the local variables inside current object 
        self.name='Ajay Sharma'
        self.age=26

    # creating a method to update value
    def update(self):
        # Note: whichever object called this update method  self store that object as a parameter 
        # self contains the current object hence to change the variable inside object we need to do it by calling self
        self.age=30
    
    #creating a function to compare two objects
    def compare(self,otherFunction):
        # here self contains the object who is calling compare method
        # otherFunction contains another method which is passed as an argument
        if self.age == otherFunction.age:
            return True
        else:
            return False

#creating the objects for class Computer
c1=Computer() 
c2=Computer()  

# to compare two objects we need to create method for it
# with the help of one object we are calling the compare object and passing the send obj as a parameter inside compare method. hence self store the calling obj and other variable stores the other object
if c1.compare(c2):
    print('Both the Objects  are same')
else:
    print('Both the Objects are Different')
print('Data from object c1 name is ',c1.name)
print('Data from object c1 age is ',c1.age)
print('Data from object c2 age is ',c2.age)
print('Data from object c2 name is ',c2.name)

c1.update()
print('Data from object c1 age is after updating  ',c1.age)

# let us compare the both the object after changing data in one object
if c1.compare(c2):
    print('Both the Objects  are same')
else:
    print('Both the Objects are Different')
