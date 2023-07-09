

# decorators --> we can add extra features in our existing functions
#In Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.

#The outer function is called the decorator, which #takes the original function as an argument and returns a modified version of it.

#Before we learn about decorators, we need to understand a few important concepts related to Python functions. Also, remember that everything in Python is an object, even functions are objects.

#Prerequisites for learning decorators
# A --> NESTED FUNCTION IN PYTHON
# note:Everything in python is an object eg class,functions etc
# below eg--> https://www.programiz.com/python-programming/decorator
#consider one function 
'''
def inc(x):
    return x+10
# passing the above function inside another function whose notation is func1  as an argument
def operate(func1,x): # here x is belongs to outer function attribute
    result=func1(x)
    return result
# passing the actual parameters
print(operate(inc,3))
'''

# B --> In python we can define function into another function
'''
# consider one outer function
def print_message(message):
    greeting='Hello'

    #declaring another function inside the scope of outer function
    def printer():
        print(greeting,message)
    #calling the printer function  inside print_message function due to lexical scope
    printer()
# calling the parent function
print_message('Programmer')

'''
# C -->Closure:  function can also return another function as a value
'''
def print_message(message):
    greeting='Hello'

    #declaring another function inside the scope of outer function
    def printer():
        print(greeting,message)
    #Instead of calling the printer function to run  I am returning this function as an value
    return printer  

# Since we are returning a function hence storing it inside another function and calling it
# here the outer function ie print_message has done its work and it means all the local variables of outer function has been deleted after doing their work here.However when we call the result function we  still have the access to the variable greeting and message inside inner printer  function such a function is called closure.
#Closure definition A closure simply an inner function that remembers the values and variables in its enclosing scope even if the outer function is done executing.  
result=print_message('Ajay')
result()
'''
# 

              #part - 1 decorators without parameters

#

# python decorators --> a python decorator function acts as a wrapper, it allowed us to add some functionality to the past function without changing the code of the original function. 
# Python Decorator -> a python decorator is a function that takes in a function, adds some functionality to it and returns the original function

# declaring a function
"""def printer():
    print('Hello World')

""# passing a function inside another function
def display_info(func):
    # creating an inner function
    def inner():
        # using dunder name function attribute to get the function name
        print('Executing',func.__name__,"function")
        #calling the function to execute
        func()
        print('Finished Execution')
    #returning the value from parent function(ie inner function)
    return inner  

# since we are returning a function 
decorated__func=display_info(printer)  
# calling the function to execute

decorated__func()"""

#In python we have a much more elegant way of writing the above last two line implicitly using teh @-symbol
"""def display_info(func):
    # creating an inner function
    def inner():
        # using dunder name function attribute to get the function name
        print('Executing',func.__name__,"function")
        #calling the function to execute
        func()
        print('Finished Execution')
    #returning the value from parent function(ie inner function)
    return inner

@display_info
def printer():
    print('hello world!!') 

printer()"""

# 

              #part - 2 decorators with parameters

#

# example : you want to divide two numbers and you have to make sure that numerator should be greater than denominator ie a>b  [ a/b ]
#using old way
"""def divide(a,b):
    print(a/b)

def smart_divide(func):
    def inner(a,b):
        if b==0:
            print('cannot divide by zero')
            return 'not possible'
        if a<b:
            print('Since the denominator is greater than the numerator ,swapping the value of a & b')
            a,b=b,a
        return func(a,b)

    return inner

result=smart_divide(divide)
result(2,4)    """

#the above line of  codes can be refactor using @ symbol


# def smart_divide(func):
#     def inner(a,b):
#         print('dividing',a,'by',b)
#         if b==0:
#             print('cannot divide by zero')
#             return
#         return func(a,b)
#     return inner

# here we are passing divide function as an argument in smart_divide function
# @smart_divide
# def divide(a,b):
#     return a/b


# result1=divide(10,20)
# print('result 1 is ',result1)

# result3=divide(40,100)
# print('result 3 is ',result3)
# result4=divide(400,0)
# print('result 4 is ',result4)


#
              # part 3 - In python a function be decorated multiple times with different or the same decorators
#

# defining a decorator which takes functions
"""def star(func):
    # passing the argument(message) to the inner function
    def inner(args):
        print("*"*30)
        func(args)
        print("*"*30)
    return inner

# defining another decorator which takes functions
def percent(func):
    # passing the argument(message) to the inner function
    def inner(args):
        print("%"*30)
        func(args)
        print("%"*30)
    return inner

# initializing multiple decorators on a single function

@star
@percent
def printer(msg):
    print(msg)

printer('Decorators are wonderful')"""