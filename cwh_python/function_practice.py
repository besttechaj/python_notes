#function to find the greatest of three
# def greatest(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2>num3:
#             return num2
#         else:
#             return num3
        
# result=greatest(65,21,2)
# print(result)

#function to convert the celcius unit  into fahrenheit unit
# def temp(celcius_value):
#     return (celcius_value*9/5)+32

# print(temp(45))    

#to print all the output in the same line ... by default end="/n" hence the print in built function prints in the new line whenever called
# print("hello",end="")
# print("world",end="")
# print("how",end="")
# print("are",end="")
# print("you",end="")

#recursive function to calculate the sum

# def addition(n):
    
#     if n<=1:
#         print('n belongs to if condition',n)
#         return n
#     else:
#         print('n belongs to else condition',n)
#         return n+addition(n-1)
    
# print(addition(5))
#explanation................................
# suppose n=5
# n+addition(n-1)
# 5+addition(4)
# 4+addition(3)
# 3+addition(2)
# 2+addition(1)
# if n==1 then return n ie now n=1
# so,
# moving from bottom to top

# 2+addition(1)=2+1=3
# 3+addition(2)=3+3=6
# 4+addition(3)=4+6=10
# 5+addition(4)=5+10=15 (answer)

# n=6
# for i in range(n):
#   print("*"*(n-i))

def removeAndSplit(string,word):
    newStr=string.replace(word, "")
    return newStr.strip()

this="   ajay is a good boy    "
print(removeAndSplit(this,"ajay"))

