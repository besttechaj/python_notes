# # creating a class 
# class RailwayForm:
#     # defining a function 
#     def printData(self):
#         print(f"Name of the passenger is {self.name}")
#         print(f"Train is {self.train}")

# # creating an object of class and using it as an template
# harrysApplication=RailwayForm()
# harrysApplication.name='Harry Potter'
# harrysApplication.train='Mumbai Ltt Express'

# # running the above method 
# harrysApplication.printData()



# # company form
# class Employee:
#     # creating instance attribute for class ie class attribute
#     company='Google'
#     salary=300000

# # creating an object for class
# ajay=Employee()
# prashant=Employee()

# # creating instance attribute for object ie instance attribute
# ajay.salary=500000
# prashant.salary=5000000
# print(f"current salary of ajay is {ajay.salary} and prashant mishra is {prashant.salary} ")
# ajay.address='delhi'
# prashant.address='mathura'
# print('employee company before: ',Employee.company)
# print(ajay.company)
# print(prashant.company)
# #  changing the company name
# Employee.company='Youtube'
# print(ajay.company)
# print(prashant.company)
# print('employee company after: ',Employee.company)


# static and self concept

# class Employee:
#     #creating an class instance attribute
#     company='Google' 
#     def getSalary(self,signature):
#         print(f'salary for this employee working in {self.company} is {self.salary}\n{signature}')

#     @staticmethod
#     def greet(name):
#         print(f'Good Morning {name}')
        

# #creating an object instance attribute
# harry=Employee()
# harry.salary=100000
# #passing signature
# harry.getSalary('Thanks_chaman') #Employee.getSalary(harry)
# # running an static method
# harry.greet('jackey')

# class Employee:
#     # creating a constructor and passing some arguments
#     def __init__(self,name,salary,subunit):
#         # storing the name ,salary , subunit inside object 
#         self.name=name
#         self.salary=salary
#         self.subunit=subunit
#         print('this id is belongs to self from constructor',id(self))
       
    
#     def getDetails(self):
#         print(f'employee name is {self.name}')
#         print(f'employee salary is {self.salary}')
#         print(f'employee subunit  is {self.subunit}')
#         print('this id is belongs to self from getDetails',id(self))


#     #creating an class instance attribute
#     company='Google' 
#     def getSalary(self,signature):
#         print(f'salary for this employee working in {self.company} is {self.salary}\n{signature}')
#         print('this id is belongs to self from getSalary method',id(self))

#     @staticmethod
#     def greet(name):
#         print('this is static method')
#         print(f'Good Morning {name}')

# ###############################################
# #creating an object instance attribute
# #object can be initiated using constructor ie constructor('harry',100,'youtube')
# harry=Employee('harry',100,'youtube')
# print('the id of object harry is ',id(harry))

# harry.getDetails()
# harry.getSalary('signature')

        
# class Programmer:
#     company='Microsoft'
#     def getDetails(self):
#         print(f'Employee name is {self.name}\n')
#         print(f'Having position as a  {self.position}\n')
#         print(f'working in {self.company}\n')

# #  instance attribute for object
# worker1=Programmer() 
# worker1.name='harry cwh'
# worker1.position='Senior Software Developer'

# #  instance attribute for object
# worker2=Programmer() 
# worker2.name='Thapa Technical'
# worker2.position='Manager'

# worker1.getDetails()
# worker2.getDetails()

# class Programmer:
#     company='Microsoft'

#     def __init__(self,name,product):
#         self.name=name
#         self.product=product
        
#     def getDetails(self):
#         print(f'Employee name is {self.name}\n')
#         print(f'Working on product - {self.product}\n')
#         print(f'working in {self.company}\n')

# #  instance attribute for object
# worker1=Programmer('harry','github') 
# worker2=Programmer('thapa','skype')

# worker1.getDetails()
# worker2.getDetails()  

# class Calculator:
#     def __init__(self,number):
#         self.number=number
    
#     def square(self):
#         result=self.number**2
#         print(result)
        
#     def cube(self):
#       result=self.number**3
#       print(result)
    
#     def squareRoot(self):
#      result=self.number**0.5
#      print(result)

# obj=Calculator(9)
# obj.square()
# obj.cube()
# obj.squareRoot()


# class Greeting:
#     @staticmethod
#     def greet(name):
#         print(f'hello Good Morning, {name}')

# obj=Greeting()
# obj.greet('AJAY MISHRA')

# class Train:
#     railway='WELCOME TO INDIAN-RAILWAYS'

#     # initializing attributes using constructor for class
#     def __init__(self,trainName,totalTrainFare,AvailableSeats):

#         # storing the attributes inside object attributes
#         self.name=trainName
#         self.fare=totalTrainFare
#         self.seats=AvailableSeats
    
#     # getting the current status
#     def getStatus(self):
#         print(f'Train : {self.name}')
#         print(f'Train Fair : Rs.{self.fare}')
#         print(f'Train Available Seats : {self.seats}')
    
#     # to book seats
#     def getBooked(self):
#         if(self.seats>0):
#             print('Seats are available to book\n')
#             print('click ok to confirm your seat')
#             print(f'Your seat number is {self.seats}')
#             self.seats=self.seats-1
#         else:
#             print('Sorry, Seats are not available this time')

#     # to cancel a ticket
#     def getCancel(self):
#         print('press cancel button to cancel your ticket\n') 
#         self.seats=self.seats+1
 

# panchvatiExpress=Train('PUNJAB MAIL', 1600, 2)
# panchvatiExpress.getStatus()
# #booking seat one time
# panchvatiExpress.getBooked()
# # checking status after seat has been issued to the customer
# panchvatiExpress.getStatus()
# print('************************************')

# #booking seat second time
# panchvatiExpress.getBooked()
# # checking status after seat has been issued to the customer
# panchvatiExpress.getStatus()
# print('************************************')

# #booking seat third time
# panchvatiExpress.getBooked()
# # checking status after seat has been issued to the customer
# panchvatiExpress.getStatus()
# print('************************************')
# #suppose a user cancelled his ticket
# panchvatiExpress.getCancel()
# # checking status after ticket has been cancelled by the customer
# panchvatiExpress.getStatus()

#Inheritance............
 
# class Employee:
#     company='Google'

#     def showDetails(self):
#         print('this showDetails method is belongs to base/parent class')
# class Programmer(Employee):
#     language='Python'
#     # overriding 
#     company='MicroSoft'

#     def getLanguage(self):
#         print(f'the language is {self.language}')
#         print(f'the company in child/derived class is {self.company}')
#     # overriding
#     #creating another clone of parent's class method inside child/derived class     
#     def showDetails(self):
#         print('Clone of showDetails method inside child/derived class')


# e=Employee()
# p=Programmer()

# e.showDetails()
# p.showDetails()
# # p.getLanguage()
# print('Accessing inside Programmer class : ',p.company)
# print('Accessing inside Employee class : ',e.company)

# MULTIPLE INHERITANCE --> child/derived class acquiring the attributes and methods from different Parent classes present at same level
# class Employee:
#     company='Visa'
#     ecode=120
#     def showDetails(self):
#         print('this showDetails method is belongs to base/parent class')

# class Freelancer:
#     company='M-technology'
#     level=0
#     def upgradeLevel(self):
#         self.level=self.level+1

# class Programmer(Employee, Freelancer):
#     name='Ajay'

# # e=Employee()
# p=Programmer()
# print(p.ecode)
# print('Before freelancer level was ',p.level)
# p.upgradeLevel()
# print('After upgrading, the freelancer level is ',p.level)
# # print('Accessing inside Programmer class : ',p.company)
# # print('Accessing inside Employee class : ',e.company)

# # IF both parent class have same method name and same variable name then it will call method and variable depending upon FIFO concept which is passed during Inheritance ie Programmer(Employee,Freelancer) . Since Employee is Inherited first so higher priority will be given to Employee Class 
# print(p.company)

# MULTI-Level INHERITANCE --> child/derived class acquiring the attributes and methods from different Parent classes present at different level

# class Person:
#     company='Microsoft'
#     country='India'
#     def takeBirth(self):
#         print('Born in india')

# class Employee(Person):
#     company='Honda'
#     def getSalary(self):
#         print(f'Salary is {self.salary}')

#     def takeBirth(self):
#         print('I am an Employee belongs to Employee class')

# class Programmer(Employee):
#     # company='Fiverr'
#     def getSalary(self):
#         print('No salary to programmers')

# p=Person()
# e=Employee()
# pr=Programmer()
# # class Programmer(Employee): FIFO
# print(pr.company) #FIFO concept is applied 
# print(pr.takeBirth()) #FIFO concept is applied

# # method override 
# pr.getSalary()

# super class concept ie super() always calls their parent class
# also --> super() can be used to call constructor

# class Person:
#     company='Microsoft'
#     country='India'
#     def __init__(self):
#          print('Initializing Constructor from person CLASS')      
#     def takeBirth(self):
#         print('Take birth belongs to Person class')

# class Employee(Person):
#     company='Honda'

#     def __init__(self):
#          super().__init__()
#          print('Constructor from Employee class')

#     def getSalary(self):
#         print(f'Salary is {self.salary}')

#     def takeBirth(self):
#         super().takeBirth()
#         print('Take birth belongs to Employee class')

# class Programmer(Employee):
#         company='Fiverr'
#         def __init__(self):
#           #  super().__init__()
#            print('Constructor from Programmer class')
#         def getSalary(self):
#             print('No salary to programmers')        
#         def takeBirth(self):
#             super().takeBirth()

#             print('take birth belongs to Programmer class')

# # p=Person()
# # p.takeBirth()

# # e=Employee()
# # e.takeBirth()

# pr=Programmer()
# # pr.takeBirth()


# topic --> class method (decorator)

# class Employee:
#     #creating class attribute
#     company='Camel'
#     salary=100
#     location='Delhi'

'''
    def changeSalary(self,sal):
        # updating the instance attribute
        self.salary=sal

        # method -1 to change class salary attribute (here self.__class__ is the class-> Employee)
        self.__class__.salary=sal
    '''
    # method - 2 to change class salary attribute  by using decorator known as class method
#     @classmethod # this is a decorator which is used to access class
#     def changeSalary(cls,sal): # here cls is class's reference
#      cls.salary=sal

# e=Employee()
# print('salary from class attribute :',e.salary)
# e.changeSalary(40)
# print('salary from  instance attribute',e.salary)
# print('salary from class attribute :',Employee.salary)

# class Employee:
#     company='Bharat Gas'
#     salary=5600
#     salaryBonus=400

# #   PERFORMING ABSTRACTION

#     @property #property (getter method) decorator --> this is a function but works as a property   
#     def totalSalary(self):
#         return self.salary+self.salaryBonus
    
#     @totalSalary.setter #setter method
#     def totalSalary(self,val): #here val is the total salary
#         print('Fetching the new updated total salary : ',val)
#         self.salaryBonus=val-self.salary
# e=Employee()
# print('Employee total Salary is : ',e.totalSalary) # this is a property hence no () required
# print('Employee current Bonus is : ',e.salaryBonus)     
# e.totalSalary=5800 # updating the property
# print('Updating the total salary Again : ',e.totalSalary)
# print('Employee current Bonus is : ',e.salaryBonus)     

# operator(+,-,*,% etc) Overloading --> is used to overload operator(+,-,/,etc) in python using predefined dunder methods[dunder-> doubleUnderscore methods](eg __add__(), __sub__(), __mul__()) to perform all these operators on BETWEEN CLASS's created  objects

# suppose we print(3+3), the output will be 6 because + operator can be applied to string and integer literals 

# but when we add two class objects that is object1 + object2 # this will throw an error hence to perform such operations in class we use some special methods known as doubleUnderscore(__preDefined__) or dunder method or magic methods

"""class Calculation:
    # MAGIC/dunder methods type --> [__init__  also called constructor ]
    def __init__(self,num):
        # here self takes the current object
        # assigning value from local var to every object's instance variables
        # here we are passing one parameter  inside object instance 
        self.num=num
        print('Individual object instance are',self.num)
    
    #Another pre-defined MAGIC/DUNDER METHODS type --> [ special method ]
    # here self store the first object and num2 stores the second object
    #defining function through predefined function for "+" operator to perform operation between class's  objects
    def __add__(self, num2):
        print('Address of 1st Object',id(self))
        print('Address of 2nd Object',id(num2))
        print('Performing addition')
        return self.num+num2.num
    
    # defining function through predefined functions for "-" operator to perform operation between class's objects
    def __sub__(self,num2):
        # here self take first object
        # here num2 takes second object
        return self.num-num2.num
    
    def __mul__(self,other):
        print('performing multiplication')
        return self.num * other.num

# creating two objects
n1=Calculation(3)
n2=Calculation(4)

print('the sum of two objects is ',n1+n2)
print('The subtraction of two objects is ',n1-n2)
print('The multiplication of two objects is ',n1*n2)
"""

# other dunder's methods
"""class Number:
    # MAGIC/dunder methods type --> [__init__  also called constructor ]
    def __init__(self,num,name):
        self.num=num
        self.name=name
    
    def __add__(self, num2):
        return self.num+num2.num
    
    def __sub__(self,num2):
        return self.num-num2.num
    
    def __mul__(self,other):
        print('performing multiplication')
        return self.num * other.num
    
    # to print related to object
    def __str__(self):
        return f'Decimal Number: {self.num}'
    
    # to print object len
    def __len__(self):
        return len(self.name)

# creating two objects
n1=Number(3,'wonderful')
# print(n1) : Without defining  __str__() dunder method it will give object memory location

# if we want to print something related to object specific object we need to define the __str__() dunder method
print(n1)

# if we print the len(object) without __len__() dunder method it will throw an error ie no len
print('The length of the name instance is ',len(n1))
"""

#  Oops -> ASSIGNMENT 
# class -1 
"""class V2d: # 2-d vector class 

    # creating an object instance for 2d vector to load object variables
    def __init__(self,i,j):
        print('loading parent object instance')
        self.icap=i
        self.jcap=j
        print('parent object loading process is completed')

    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

# Inheriting child from parent class 

# class -2
class V3d(V2d): # 3-d vector class
    # creating an object instance for 3d vector to load object variables
    def __init__(self,i,j,k):
        print('loading child object instance')
        # here we are passing the i and j to super class constructor
        super().__init__(i,j)
        print('this is child class')
        self.kcap=k
        print('child object loading process is completed')
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d=V2d(10,20)
v3d=V3d(99,299,399)
# printing object of both classes 
print(v2d)
print(v3d)  """


# formula --> salaryAfterIncrement= salary * increment
"""class Employee:
     # static variable
     salary=1000
     increment=1.5

     # creating a getter method 
     # the use of @property is that we can use it an variable also 
     @property
     def salaryAfterIncrement(self):
          return self.salary * self.increment
     
     # creating a setter method 
     @salaryAfterIncrement.setter
     # here the sai takes the literal of salaryAfterIncrement
     # formula --> salaryAfterIncrement= salary * increment
     def salaryAfterIncrement(self,sai):
          self.increment=sai/self.salary

e=Employee()
print('Current salary :',e.salary)
print('current increment is ',e.increment)
print('salary after increment is ',e.salaryAfterIncrement)

print('%%%%%%%%%%%%%%%%%%%%%')
# updating new salary with increment
e.salaryAfterIncrement=2000 # sai=2000
print('salary after increment is ',e.salaryAfterIncrement)
print('Current salary :',e.salary)
print('current increment is ',e.increment)"""

"""class Complex:
    def __init__(self,r,i):
        print('loading values')
        self.realNumber=r
        self.imaginaryNumber=i

    # defining dunder method for + operator
    def __add__(self,other):
        print('performing operation')
        # To create a new object again we are passing the result as a parameter to class so that constructor will initialize realNumber and imaginaryNumber  values inside new object and with the help of self keyword.
        return Complex(self.realNumber + other.realNumber, self.imaginaryNumber + other.imaginaryNumber)
    
    # defining dunder method for * operator
    def __mul__(self,other):
        # formula: (a+bi)(c+di)=(ac-bd)+(ad+bc)i

        realPart=self.realNumber * other.realNumber - self.imaginaryNumber * other.imaginaryNumber

        imgPart=self.realNumber * other.imaginaryNumber + self.imaginaryNumber * other.realNumber

        # return: passing parameters to Complex class so that constructor create a new object 
        return Complex(realPart,imgPart)
    
    # fetching the newly created object
    #while returning the __add__ the result representation will be returning object and location . To display the proper result we are defining __str__ method
    def __str__(self):
        return  f"{self.realNumber} +  {self.imaginaryNumber}i"

c1=Complex(3,2) 
c2=Complex(1,7)

print(c1+c2)
print(c1*c2)"""


class Vector:
    # initializing the vector inside the object
    def __init__(self,vec):
        self.vec=vec
    
    def __str__(self):
        index=0
        stri=''
        for i in self.vec:
            #here i is the list values
            stri +=f' {i}a{index} +'
            index +=1
        # to remove the last + element, we go for slicing
        return stri[:-1] # it means stri[0:-1]
    
    def __add__(self,other):
        # considering a new list
        newList=[]
        for i in range(len(self.vec)):
                newList.append(self.vec[i]+other.vec[i])
        return Vector(newList)
    
    # to get dot product of two vectors
    def __mul__(self,other):
        # considering a new list
        sum=0
        for i in range(len(self.vec)):
                sum=sum+(self.vec[i]*other.vec[i])
        return sum
                


# passing a list in vector-1 
v1=Vector([1,4,6])
v2=Vector([1,6,9])

print(v1)
print(v2)
# returns another object using Vector(newList)
print(v1+v2)
print(v1*v2)