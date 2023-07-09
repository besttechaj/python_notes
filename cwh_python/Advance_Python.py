# Exceptions
"""while(True):
    print('##%%%%%% WELCOME TO THE GAME %%%%%%%%##')
    print('Press Q to quit this game')
    a=input('Enter a  number : ')

    if a=='q':
        # if user presses q then exit the loop else continue
        break
    
    # exception handling

    try:
        a=int(a)
        if a>6:
            print('You have Entered a number which is greater than 6')
        else:
            print('You have Entered a number which is less than 6')
    except Exception as e:
        print(f'Your input resulted in an error {e}')
        print('please Enter a valid number')
print('##%%%%%%%% THIS IS THE END. THANKS FOR PLAYING!! %%%%%%%%##')"""

# handling diffErent ExCEPTIONS
"""while(True):
    try:
        a=int(input('Enter any number '))
        b=int(input('Enter any number '))
        result= a/b
        print('the division of given number is : ',result)
        print('THANKS FOR USING THIS CODE')
    except ValueError as e:
        print('Exception-1 Occurred : ',e)
        print('hey user, please enter a valid number')
    
    except ZeroDivisionError as e:
        print('Exception-2 Occurred : ',e)
        print('hey user, please enter a non zero number')
    
    except Exception as e:
        print('Exception-3 occurred')
        print(e)"""

# custom exception
"""def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError('Hey User, please enter a valid number')
    
res=increment('sd')
print(res)"""

# try with else : if there is no exception occurred inside try block then print else block also
"""try:
    i=0
    c=1/i
    print(c)
except Exception as e:
    print('Exception Occurred: ',e)
else:
    print('We were successful without any Exception occurred')"""

# try with finally keyword : irrespective of the exception or termination of program(ie exit the program), finally block will execute.
"""try:
    i=0
    c=1/i
    print(c)
    # exiting program
    exit()
except Exception as e:
    print('Exception Occurred: ',e)
else:
    print('We were successful without any Exception occurred')
finally:
    print('This is the end')

# below line will not execute since the program has been exited 
print('thanks for using the program')
    """

# module import
"""import mod1_name
mod1_name.showName('CODE_with_AJAY')
# imported module
print('the imported module name is ',mod1_name.__name__) # mod1_name

# current module/file
print('the current module name is ',__name__) #main"""

# global variable
"""a=22

def fun1():
    # to give priority to global variable use global keyword
    global a 
    # updating the global variable
    a=11
    print(a)

fun1()
print(a)"""

# enumerate functions : to get the items from a list with their index
"""
list=['sanjay rana',323,98.98,True,False]

for index,item in enumerate(list):
    print(f'item - {index} : {item}')"""


# list comprehension : refactor the code [ shortcut for loops logic ]

# old way: to isolate even and odd numbers from a list
"""list=[12,32,54,7,2,4,6,8,9,34,90,97,555,444,333]
# consider a empty list for even no.
even=[]
# consider a empty list for odd no.
odd=[]

for item in list:
    if item%2==0:
        even.append(item)
    else:
        odd.append(item)
print('The even numbers are ',even)
print('The odd numbers are ',odd)"""

# comprehension new way:[operation loop]
"""list=[12,32,54,7,2,4,6,8,9,34,90,97,555,444,333,1000,10001]
# to get all even numbers, consider a new list "even" to store result and write logic in it
even = [item for item in list if item%2==0]
odd = [item for item in list if item%2!=0]
print('The even numbers are ',even)
print('The odd numbers are ',odd)"""


# ASSIGNMENT
# creating a function to read any file , if the file is not present that displaying an alert

"""def readFile(filename):
    try:
        if filename:
            with open(filename,'r') as f:
             print(f.read())
    except Exception as e:
       print('no such file is present :',e)

readFile('cwh_python/copy.txt')
readFile('cwh_python/abc.txt')
readFile('cwh_python/xtxt.txt')"""

# based on enumerator function
"""list=['sanjay rana',2,43,54,76,98,True,9.87]

for index,item in enumerate(list):
    if index==2 or index==4 or index==6:
         print(index ,  item)"""
 

# based on list comprehension : print table and store it in a newly created file
"""n=int(input('Enter any number to get its table'))

table=[n*i for i in range(1,11)]
print(table)

with open('data.txt','w') as f:
    f.write(str(table))
"""
# virtual Environment : 
# check virtualenv file


# pip freeze ( VERY IMPORTANT ) : to check all the installed packages inside the current environment 

# lambda expression

"""func = lambda a : a+5

x=1000
print(func(x))

# calculating area of rectangle using lambda function
area = lambda length,breadth: length * breadth

print(area(1001,2001))"""

# join method : joins any thing after list items and return a complete sentence string from it
"""
l=['camera','laptop','hard disk','iphone','smart phone']

sentence = " and ".join(l)
print(sentence)"""

# format methods  : f- string  ( f"good morning , {name}") declaration before python 3.5 

"""name='ajay'
channel='code_with_ajay'

a='hello everyone, this is your host {} and my youtube channel name is {}'.format(name,channel)

print(a)"""


# Map function : 2 ways

# MAP - OLD WAY
"""li=[9,8,0,10]
def cube(item):
    return item**3

# applying for loop
resultList=[]
for item in li:
    resultList.append(cube(item))

print(resultList)

# MAP - NEW WAY
l=[2,3,4,5,6]
def square(item):
    return item*item
# since we getting the map object so we need to type cast the result to list again 
result=(map(square,l))
print(type(result))
result=list(result)
print(result)"""

# Filter function : 
# new way:
"""l=[54,32,65,32,32,90,2,10,430,43050,12,20,4]
def greaterthan_20(num):
    if num>20:
        return num
# filter out the number which are greater than 20
# we need to type cast the result of filter to result else it will return filter object 
result=list(filter(greaterthan_20,l))
print(result)

#above example using lambda function
greaterResult=lambda element: element>20

result2=list(filter(greaterResult,l))
print(result2)"""

# reduce function : 
"""from functools import reduce
l=[12,23,34,45,100]
addition = lambda element1, element2 : element1 + element2

additionResult=reduce(addition,l)
print(additionResult)"""


# ASSIGNMENTS 


# to create a new virtual_env: virtualenv "virtualenv_projectName"
# error : Set-ExecutionPolicy Unrestricted -Scope Process
# to activate virtual_environment : .\myvirtualpython2\Scripts\activate.ps1
# to install any package pip install 'packageName'
# to run the package first use "python"
# to exit : deactivate
# to copy all the installed packages from the virtualenv type pip freeze > requirements.py
# to delete environment : delete the directory 
# to install the previous environment requirements file to another new virtual environment: pip install requirements.txt


"""name=input('Enter your Name : ')
greet=input('Enter a greet Message : ')
sentence="hello Good Morning {}. Have a {} day"
output=sentence.format(name, greet)
print(output)
"""
"""num=10
# consider an empty list
tableList=[]
def table(element):
    for i in range(1,11):
        tableList.append(element*i)
    return tableList
print(table(num))
print(type(table(num)))"""

# using list comprehension : 
# Also Note: to use join the result should be in string format 
"""l=[str(i*7) for i in range(1,11)]
print(l)
print(type(l))

verticalTable='\n'.join((l))
print(verticalTable)
print(type(verticalTable))
 """
"""list1=[12,23,34,45,100]
def maxi(l):
    print(l)
    print(type(l))
    # Assume first number in list is largest
    # initially and assign it to variable "largest"
    largest=l[0]
    # Now traverse through the list and compare
    # each number with "largest" value. Whichever is
    # largest assign that value to "largest'.
    for i in l:
        for j in range(0,len(l)-1):
          if i > l[j]:
              largest=i
          j +=1
        i +=1
    return largest
print('The largest number in the list is ',maxi(list1))"""

# from functools import reduce 
# l=[12,23,34,45,100]
# # we have in-built max(a,b) function
# result=reduce(max, l)
# print(result)

"""# running a server using flask
from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

if __name__=='__main__':
    app.run(debug=True)"""


# PROJECT : BASED ON LIBRARY

class Library:
    # Accepting the list of Book to store in library
    def  __init__(self,bookList):
        self.books=bookList
    
    # creating a function to display available books
    def displayAvailableBooks(self):
         print('Books Available in the library are : ')
         for index,book in enumerate(self.books):
              print(f"{index} ~ {book}")

    # Borrowing a book
    def borrowBook(self,bookName):
         #checking whether given book name is present or not
         if bookName in self.books:
              print(f'You have been issued {bookName}. Please keep it safe and return it within 30days. Else penalty charges will be issue')
              # removing the book from library book list
              self.books.remove(bookName)
              return True
         else:
              print('Sorry, this book has been already issued to someone else. Please wait until the book is returned')
              return False
    
    # returning a book
    def returnBook(self,bookName):
         self.books.append(bookName)
         print('Thanks for returning this book! Hope you enjoyed reading it')

class Student:
    
    def student_borrowBook(self):
         self.bookName=input('Enter the name of the book you want to borrow : ')
         print('You have request to issue a book named as ',self.bookName)
         return self.bookName
    
    def student_returnBook(self):
         self.bookName=input('Enter the name of the book you want to return : ')
         print('You are returning a book named as ',self.bookName)
         return self.bookName



if __name__=='__main__':
        # creating an object to initialize library
        centralLibrary=Library(['Html','Css','JavaScript','NodeJs','ExpressJs','Python','MongoB'])
        
        # creating student here
        student=Student()

        # creating a menu
        while(True):
             msg='''
                WELCOME TO THE CENTRAL LIBRARY
             Please choose an option:
             1. List all the books
             2. Request a book
             3. Add/Return a book
             4. Exit the library
             '''
             print(msg)
             a=input('Enter your chosen option : ')

             # to get all records
             if a=='1':
                  centralLibrary.displayAvailableBooks()
            
             elif a=='2':
             # borrowing a book
                  centralLibrary.borrowBook(student.student_borrowBook())
            
             elif a=='3':
             # returning the book
                  centralLibrary.returnBook(student.student_returnBook())
            
             elif a=='4':
             # exit the library
                  print('Thanks for using the central library')
                  exit()
            
             else:
                  print('please enter a valid number')


            







