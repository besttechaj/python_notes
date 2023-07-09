
class Computer:
    def config(self):
        print('i5, 16gb, 1TB')


# Note: We can have multiple instance object for a single class 
# creating an instance object for the class
com1=Computer()
com2=Computer()

# THERE ARE TWO WAYS TO CALL A METHOD WHICH IS PRESENT INSIDE CLASS
#BY USING CLASSnAME (passing the object as an argument)
#BY USING object ITSELF

#let's go with bu using classNAME :

# Computer.config() Error: Computer.config() missing 1 required positional argument: 'self'

# The reason for the above error is that suppose we have n no. of object so to use them for a method we need to pass each and every object as a parameter inside method since it is expecting an argument known as self --> Computer.config(com1)
# Computer.config(com1)
# Computer.config(com2)

#let's go with object ITSELF : 
# if there were n no. of object also there is no confusion because com1 is an object belongs to Computer class and here with the help of object name we are calling config method  
com1.config() # at back this syntax is converted into Computer.config(com1)