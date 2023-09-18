# tip calculator App
# float division (//) : divide two numbers and return the result after rounding off to its nearest value (ie. remove the float values)

# meal_Amount=float(input('Enter the meal amount: $'))
# # converting percentage into decimal 
# tip_Percentage=float(input('Enter the tip amount (in %) '))/100

# # datatype of argument should be float,int and return value must be an integer
# def calculateFoodTotalAmount(meal_Amount:float,tip_Percentage:int) -> int:
#     #  to add an extra line
#     print('\n')
#     print('\n')
#     print('\n')
#     print('-----------------------------------')
#     print(f'Food Amount: ${meal_Amount}')
#     tip_Amount= meal_Amount*tip_Percentage
#     print(f'Tip Amount: ${tip_Amount}')
#     total_Amount=meal_Amount+tip_Amount
#     # to add an extra line
#     print('\n')
#     print(f'Total pay: ${str(total_Amount)}')
#     print('-----------------------------------')

# calculateFoodTotalAmount(meal_Amount,tip_Percentage)
# ============================================================

# lambda function -> Anonymous function

# syntax ::    lambda arg1,arg2.. : <Expression>

# implicit return -> returns automatically
# sum2 = lambda a,b : a * b
# print(sum2(2,4))

#=============================================================

# assert -> Assertions allow you to test the correctness of your code by checking if some specific conditions remain true, which can come in handy while you're debugging code.
# example 
# defining a function 
# def add(a,b):
#     return a + b;

# def multiplication(a,b):
#     return a*b

# # # testing
# # assert add(1,2)==3 # if there is no error then it will return nothing else describes the error
# # assert multiplication(10,20)==200

# # the best way to use assert is use it inside a function test function hence this will make code more reliable
# def test_code():
#     print('Running test code function.....')
#     assert add(2,2)==4
#     assert multiplication(2,3)==6 
#     assert calculateFoodTotalAmount(1000,2)==1020
#     print('code has been successfully tested')
# test_code()
#============================================================

# Data Types	Classes	Description in python
# Numeric :	int, float, complex	: holds numeric values
# String : str :	holds sequence of characters
# Sequence :	list, tuple, range :	holds collection of items
# Mapping	: dict :	holds data in key-value pair form
# Boolean	: bool :	holds either True or False
# Set :	set, frozeenset : hold collection of unique items

# List --> In python arrays are known as List
# list can store different datatypes 
# l1= ['ram','hard-disk','cd-rom','computer','laptop','cpu','mouse','keyboard']
# print(l1)
# appending using list
# l1.append('motherboard')
# print(l1)
# indexing using list
# print(l1[1])
# print(l1[2])
# to get the last element inside an array
# if we are considering the array from backward direction then it starts from negative values
# [....-5,-4,-3,-2,-1]
# print(l1[-1])
# print(l1[-2])
# SLICING using list
# print(l1)
# print(f'The length of Array/list is {l1.__len__()}')
# print(l1[0:2])
# print(f'The length of list is {len(l1)}')
# # to get all the elements except the last one
# print(l1[0:len(l1)-1])
# #slicing based on strings
# print('Good Morning, Hi this is mishra'[0:10])
# print('Good Morning, Hi this is mishra'[-5:-1])
# print('Good Morning, Hi this is mishra'[0:-2])
# print('Good Morning, Hi this is mishra'[0:-1])
# print(l1)
# [ from : to : step By (jump) ]
# this allows you to step over by 0th element
# print(l1[0:len(l1):1 (ie go forward direction)]) 
# step over by 1 - element
# print(l1[0:len(l1):2])
# to reverse the array/list [from : to : -1 (ie. go backward direction)]
# print(l1[::-1])


### DICTIONARY ### 
# In python, Objects are known as Dictionary



# def introducer():
    
#   person={
#     "name":"SANJAY VERMA",
#     'email':'vermaji@gmail.com',
#     'number':2234443434,
#     'address':'tamil-Nadu',
#     'assets':1000,
#     'deb':50,
#     'net-worth':lambda : person['assets']-person['deb'],
#     # it can even hold another array/list
#     'favoriteFruits':['Mango-Shake','Strawberry-Shake']
#   }
#   print(f"Hi my name is {person['name']}.\nCurrently I am living in {person['address']} \nAnd my net worth is ${person['net-worth']()}.\nMy favorite Fruit juice is {person['favoriteFruits']}")
#   # to get all the values
#   # print(person.values())
#   # to get all the keys
#   # print(person.keys())
#   # to get all the values in list form
#   print(list(person.values()))

# introducer()

#=============================================================
# TUPLES (DATA_TYPE)
# numbers=(1,2,4)
# print(numbers)
# # tuples are immutable
# numbers[0]=21 # error
# print(numbers)

#============================================================
# SETS {} : Used for getting unique elements
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and un-indexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

# Sets are written with curly brackets.


# list1=['ruby','python','javascript']
# list2=['ruby','sql','core-java','javascript']

# unique_elements=set(list1+list2)
# print(unique_elements)
# print(type(unique_elements)) # set - class 

# # To check whether element exist or not inside a list by using 'in' keyword
# print('ruby' in unique_elements)
# print('mahi' in unique_elements)

# creating a function which will return unique values from a given list
# def unique(languages):
#   # returning list after completion of data processing
#   return list(set(languages))

# result = unique(['python','sql','javascript','java','java','sql'])
# print(result)
# print(type(result))

# performing the above operation using lambda function
# languages=['hindi','hindi','english','marathi','english','tamil']
# unique= lambda languages: list(set(languages))
# print(unique(languages))
# print(type(unique))
#=============================================================================
### Loops ###
# for - loop
# fruits=['apple','orange','papaya','grapes','banana']
# i=0
# for fruit in fruits:
#   print(f'fruit {i} : {fruit}')
#   i=i+1
# to get the index of the above list's items we use enumerate() function
# enumerate()-> takes a collection (eg. tuple,list) and returns it as an enumerate object. The enumerate() function adds a counter as the key of the enumerate object.
# print(list(enumerate(fruits))) 
# some more points ..
# fruits=['apple','orange','papaya','grapes','banana']
# for fruit in enumerate(fruits):
#   # enumerates(list(index/key, pair))
#   print(f'fruit : {fruit[1]} , {fruit[0]}')
#   print(f'fruit : {fruit[0]} , {fruit[1]}')

## Tuple  UN-PACKING 
# fruits=['apple','orange','papaya','grapes','banana']
# for index, fruit in enumerate(fruits):
#   # enumerates(list(index/key, pair))
#   print(f' fruit {index} : {fruit}')

# range() function -> returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
# fruits=['apple','orange','papaya','grapes','banana']
# using range function let us append some more fruits inside the fruit list
# for _ in range(10):
#   fruits.append('pineapple')
# print(fruits)

# While loop -> it is used to iterate over a block of code as long as the test expression(condition) is true
# num=int(input('Enter a number '))
# def table(num):
#   counter=1

#   while counter<11:
#     print(f'{num}*{counter} = {num*counter}')
#     counter=counter+1

# table(num)

## Revision ----------->  BASED ON LIST

# task -> need to double the every element present inside the list
"""numbers=[12,33,455,78,455,878,8]
def double(numbers:list)->list:# return must be the list
  # consider an empty list
  empty_List=[]
  for values in numbers:
    # Appending every new value inside list after updating 
    empty_List.append(values*2)
    print(empty_List)

  return empty_List

data =  double(numbers)
print(data)"""

# task --> count the number of words present inside a given string
"""
phrase=input('Please Enter a random phrase : ')
def count_words(phrase:str)->int:
      # split returns a list
      isolate=phrase.split()# by default split uses split(' ') 
      # print(isolate.__len__())
      print(f'your new list is : {phrase.split()}')
      return len(isolate)
result = count_words(phrase)
print(f'The number of words present inside the given string is {result}')"""

# task --> sum of a given list
"""empty_list=[]
n=0
while n<10:
  # filling the empty list
  empty_list.append(int(input('Enter your list numbers : ')))
  print(empty_list)
  n+=1
print(f'your newly generated list is : {empty_list}')
def list_sum(empty_list:list)->int:
  sum=0
  for element in empty_list:
    sum=sum+element
  return sum
result = list_sum(empty_list)
print(f'the sum of all the elements present inside a given list is : {result}')"""

# task --> to find the max value from a list
# consider a list 
"""list1= [23,21,45,765,868,43,75,8]
def getMax(lt:list)->int:# return must be a number
  currentMax=lt[0]
  for element in lt:
    if element > currentMax:
      currentMax=element
  return currentMax

result = getMax(list1)
print(f'The largest value in the list is : {result}')"""

## Revision ----------> Based on Dictionary
# task --> word frequency : calculates the number of word occurred in the given Phrase
"""data = input('Enter your Phrase : ')

def word_Frequency(phrase:str):
    # step-1 turn the phrase into a list to easily manipulate the items inside 
    print('Converting string into list using split method')
    print(phrase.split())
    words_list=phrase.split()
    # step-2 Assume an empty Dictionary
    empty_Dictionary={}
    # step-3 Looping through the words_list
    for element in words_list:
        # step-4 filter out the matched items from the list
        if element not in empty_Dictionary:
            # we are storing element as key and the no. of occurrence as value 
            empty_Dictionary[element]=1
        else: 
            empty_Dictionary[element] +=1
    return empty_Dictionary

print('Printing out the result >>> ',word_Frequency(data))"""

## HIGHER ORDER FUNCTION ##
# map 
# filter  
"""
>>> task - double the list
"""
"""# map : It is a function that works as an iterator to return a result after applying a function to every item of an iterable. Map takes two two inputs as a function and an iterable object. 

def doubleTheNumber(number):
  return number*2
# call the list function on the map to be able to iterate and print each item inside
print(list(map(doubleTheNumber,[1,2,3])))
# to make it more short code use lambda
result = list(map((lambda number: number*2),[10,20,30]))
print(type(result))
print(result)
# to square the numbers present inside list
print(list(map((lambda num:num ** 2),[12,13,14,15,16])))
"""
"""# filter : the filter() methods filters the given sequence with the help of a function that tests   each element in the sequence to be true or not.

# >>> task - to filter out the even numbers from the given list

print(list(filter((lambda num : num % 2==0),[1,3,5,6,7,2,23,2004,405])))
"""