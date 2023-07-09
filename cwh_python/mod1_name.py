def showName(name):
    print(f'Good Morning, {name}')

# if the current file name is 'main' then use the below code because if this file is exported to other file there it will display the name of this exported file ie __name__ = mod1_name. 
# if you the the above function in the same file itself here the __name__ is 'main'.hence we can use the below code 
if __name__=='main':
  # if you are running this module from this file then use the below code else don't use hence we can implement different logic in other file for the above function
  name=input('Enter your name')
  showName(name)