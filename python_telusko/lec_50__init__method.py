class Computer:
    #this constructor will run whenever an object is created
    def __init__(self,cpu,ram):
        # self is the current object
        # __init__(cpu,ram) are the local parameters
        # self.cpu and self.ram -> storing the variables inside current object
        self.cpu=cpu
        self.ram=ram
    
    def config(self):
        # self-> stores the current method
        print('This is config method')
        # we cannot directly access the cpu and ram variable because they are stored inside object. we call them using current object ie. self.cpu and self.ram  
        print('Cpu is :',self.cpu)
        print('Cpu is :',self.ram)

# Note: We can have multiple instance object for a single class 
# creating an instance object for the class
# passing local variables as an argument inside constructor
com1=Computer('i5','8GB') # at back the syntax becomes Computer(com1,i5,8gb)
com2=Computer('i7','16GB')

# THERE ARE TWO WAYS TO CALL A METHOD WHICH IS PRESENT INSIDE CLASS
# 1 --> BY USING CLASSnAME (passing the object as an argument)
# 2 --> BY USING object ITSELF

#let's go with object ITSELF : 
# if there were n no. of object also there is no confusion because com1 is an object belongs to Computer class and here with the help of object name we are calling config method  
com1.config() # at back this syntax is converted into Computer.config(com1)
com2.config()