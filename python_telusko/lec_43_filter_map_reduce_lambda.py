# Performing FILTER in python
# consider a list in python
# num=[3,2,6,8,4,6,2,9]

# def is_even(n):
    # return true if the remainder is zero
    # return n%2==0

# filter will take 2 parameters here one is function where we implement filter logic and other is input ie list,sequence
# evens=list(filter(is_even,num)) 

# print('the even number list is : ',evens)

## Refactoring the above code using lambda ##
# num=[3,2,6,8,4,6,2,9]
# evens=list(filter(lambda n: n%2==0,num))
# print(evens)
#################################################


# Performing Map in python

# targetList=[2, 6, 8, 4, 6, 2]

# def updateValue(n):
#     return n*2

# Map will take 2 parameters here one is function where we implement filter logic and other is input ie list,sequence
# doublesTheValue=list(map(updateValue,targetList)) 

# print('the list doubled values are : ',doublesTheValue)

## Refactoring the above code using lambda ##
# targetList=[2, 6, 8, 4, 6, 2]
# doublesTheValue=list(map(lambda n: n*2,targetList))
# print(doublesTheValue)
##################################################

# Performing Reduce in python to get single Output

#In python reduce is belongs to functools module hence initially we need to import it 
from functools import reduce

# targetList=[2, 6, 8, 4, 6, 2]
# def addValues(a,b):
#     return a+b


# Reduce will take 2 parameters here one is function where we implement filter logic and other is input ie list,sequence

# result=reduce(addValues,targetList)

# print(result)

## Refactoring the above code using lambda ##
targetList=[2, 6, 8, 4, 6, 2]

result2=reduce(lambda a,b: a+b,targetList)
print(result2)
print(type(result2))