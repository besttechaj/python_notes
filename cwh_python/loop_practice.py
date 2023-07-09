# printing the table of 2
# num=2
# for i in range(1,11):
#     print(i*num) 
    

# num=int(input('Enter the number to get its table'))
# for i in range(1,11):
#     result=str(num)+" X "+str(i)+" = "+ str(num*i)
#     print(result)

#advance way to print table
# num=int(input('Enter the number'))

# for i in range(1,11):
#     print(f"{num}X{i}={num*i}")


# num=int(input('Enter the number'))
# prime=True
# for i in range(2,num):
#   if(num%i==0):
#     prime=False
#     break

# if prime:
#   print('number is prime')
# else:
#   print('number is not prime')

num=int(input('Enter the number'))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
   
    
print(factorial)