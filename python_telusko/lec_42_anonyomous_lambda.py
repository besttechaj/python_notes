
# function without a name is known as anonymous Function or lambda

#traditional way
# def square(a):
#     return a**2

# result=square(5)
# print(result)

# we use anonymous function whenever we don't want to run it more than one time

#since functions are objects in python hence we can pass function inside another function

#performing square
# here f is a function
# here a: is the argument 
# return part(ie operation on that argument) is a**2 and anon func are also called lambda hence declaring a lambda inside 

f= lambda a: a**2

result=f(5)
print(type(f))
print('the square of given number is' ,result)
print(type(result))

#performing addition
f2=lambda a,b: a+b
# here f2 is a function
# here a,b: is the argument 
# return part(ie operation on that argument) is a+b and anon func are also called lambda hence declaring a lambda inside 
result2=f2(10,20)
print("The addition of two given number is " ,result2)