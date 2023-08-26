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

# List --> In python arrays are known as List
# list can store different datatypes
l1= ['ram','hard-disk','cd-rom','computer','laptop','cpu','mouse','keyboard']
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

def netWorth():
    return person['assets']-person['deb']

def introducer():
    
  person={
    "name":"SANJAY VERMA",
    'email':'vermaji@gmail.com',
    'number':2234443434,
    'address':'tamil-Nadu',
    'assets':1000,
    'deb':50,
    'net-worth':lambda : person['assets']-person['deb']
  }
  print(f'Hi my name is {person["name"]}, Currently I am living in {person["address"]} and my net worth is {person['net-worth']()}')

introducer()