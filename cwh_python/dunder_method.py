
# operator(+,-,*,% etc) Overloading --> is used to overload operator(+,-,/,etc) in python using predefined dunder methods[dunder-> doubleUnderscore methods](eg __add__(), __sub__(), __mul__()) to perform all these operators on BETWEEN CLASS's created  objects
# suppose we print(3+3), the output will be 6 because + operator can be applied to string and integer literals 

# but when we add two class objects that is object1 + object2 # this will throw an error hence to perform such operations in class we use some special methods known as doubleUnderscore(__preDefined__) or dunder method or magic methods
"""
class Calculation:
    # MAGIC/dunder methods type --> [__init__  also called constructor ]
    def __init__(self,num):
        # here self takes the current object
        # assigning value from local var to every object's instance variables
        # here we are passing one parameter  inside object instance 
        self.num=num
        print('Individual object instance are',self.num)
    
    #Another pre-defined MAGIC/DUNDER METHODS type --> [ special method ]
    # here self store the first object and num2 stores the second object
    def __add__(self, num2):
        print('Address of 1st Object',id(self))
        print('Address of 2nd Object',id(num2))
        print('Performing addition')
        return self.num+num2.num
    
    def __sub__(self,num2):
        return self.num-num2.num

# creating two objects
n1=Calculation(3)
n2=Calculation(4)

print('the sum of two number is ',n1+n2)
print('The subtraction of two numbers is ',n1-n2)

"""
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

#youtube- https://www.youtube.com/watch?v=hYLEEVjDvQw
"""
class Student:
    def __init__(self,name, email, score):
        self.name=name
        self.email=email
        self.score=score
    
    
    # dunder method , Runs for every object which is created
    def __str__(self):
        print('This is dunder pre defined str method')
        return self.name+" "+self.email+" "+str(self.score)
#creating Objects 
student_1=Student('Tom','tom@gmail.com',89)
student_2=Student('Jack','jack@gmail.com',39)

# without using predefined :  __str__ dunder/magic/special Method, the below two lines print address of the objects
# print(student_1)
# print(student_2)

# using predefined :  __str__ dunder/magic/special Method, the below two lines print the return value from the dunder method
# here with the use of __str__ dundle method developers can return a  meaningful address instead of displaying 3324423x3312 output to its users
print(student_1)
print(student_2)
"""
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

# __repr__() method --> to tell a particular User that how a particular object is created ie  gives more idea about class and its object.
# if there is no __str__() method is present then by default __repr__() will run 

# the difference between repr and str is that repr gives more information than str about your class and their objects

"""class Student:
    def __init__(self,name, email, score):
        self.name=name
        self.email=email
        self.score=score
    
    
    # dunder method , Runs for every object which is created
    # def __str__(self):
    #     print('This is dunder pre defined str method')
    #     return self.name+" "+self.email+" "+str(self.score)
    
    def __repr__(self):
        print('Running repr method')
        return  f"Student('{self.name}','{self.email}','{self.score}')"

#creating Objects 
student_1=Student('Tom','tom@gmail.com',89)
student_2=Student('Jack','jack@gmail.com',39)


# print(student_1)
# repr --> gives more idea about class and its object
# repr ---> If there is no __str__() is present then by default __repr__() will run 
# print(student_2.__repr__())
# running by default __repr__() by disabling the __str__() method
print(student_1)"""

##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##
# + operator is supported for string and integer but not object ie 
# print('a'+'b')=ab 
# print(1+1)=2
# creating obj from a class
#obj1=Student()
#obj2=Student()
# print(obj1+obj2) Error 
# ques. How Will you print two object of a class ??
# Answer : using __add__() dunder/magical/special method   
# __add__() --> it is used to add two objects of a class 

class Student:
    def __init__(self,name, email, score):
        # print('Initializing object instances variables value')
        self.name=name
        self.email=email
        self.score=score
        # print('object instance has been loaded')
        # print('##%%%%%%%%%%%%%%%%%%%%%%##')
    
    def __repr__(self):
        # self -> stores the latest object
        # print('Running repr method')
        return  f"Student('{self.name}','{self.email}','{self.score}')"
    
    # let us add the score of two objects
    # here my first object will be stored in self and second object will be stored in 'other' variable and after adding the first two objects , we are storing the resultant of two objects inside local variable and passing that local variable again  to our class constructor, now the class constructor again initialize its resultant object value and stored them inside object's data then that resultant object will be refer by 'self' parameter  of __add__() method and and the third object which is passed by the user will be refer by 'other' variable after that it add the both ie resultant object(obj1+obj2) with third user's object . if there is no user's passed parameter object is remaining then it will return the result  that is class with a new object
    def __add__(self,other):
        # print('accessing add dunder method')
        name=self.name + other.name
        email=self.email + other.email
        score=self.score + other.score
        return Student(name, email, score)
    

#creating Objects 
student_1=Student('Tom','tom@gmail.com',89)
student_2=Student('Jack','jack@gmail.com',39)
student_3=Student('Rat','rat123@gmail.com',69)

# since the add dunder method is returning an object we need to store it inside an object then fetch and print the values
adding_students=student_1+student_2+student_3
print(adding_students.score)
print(adding_students.name)
print(adding_students.email)


print(type(student_1+student_2+student_3))

