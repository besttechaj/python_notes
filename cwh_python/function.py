#calculating percentage using function in python

# def percent(marks):
#     p=((marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+marks[5])/600)*100
#     return p;

# marks_jackey=[45,65,87,43,44,90];
# marks_nickey=[45,32,54,66,33,79];

# Jackey=percent(marks_jackey);
# Nickey=percent(marks_nickey);
# print('Percentage of Jackey is ',Jackey)
# print('Percentage of Nickey is ',Nickey)


# def name(user):
#     print('Good Morning!!! ',user)

# name('MEENA')
# name('TEENA')
# name('REENA')


#FUNCTION WITH ARGUMENTS

# def addition(num1,num2):
#     return num1+num2

# result=addition(100000,80008)
# print(result)

#function with default argument
# def name(firstName,lastName='Mishra'):
#     return firstName+ " " +lastName

# result=name('ajay')
# print(result) 

# def factorial(n):
#     product=1
#     for i in range(n):
#         product=product * (i+1)
#     return product
    
# print(factorial(5))


#printing factorial of a number using function recursive
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

print(fact(5))