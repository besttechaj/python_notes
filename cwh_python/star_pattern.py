# providing row
# for i in range(5):
#     print("*"*(i+1))

# n=3 providing row
n=3
for i in range(3):
    # providing space
    print(" "*(n-i-1),end="")
    # printing star
    print("*"*(2*i+1),end="")
    # providing space
    print(" "*(n-i-1))
   

  