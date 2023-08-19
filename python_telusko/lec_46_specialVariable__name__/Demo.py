
# youtube- https://www.youtube.com/watch?v=7hjgRn-vfVQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=52

# declaring a function
def func0():
    print('this is func0 function from demo module')
    print('Hello New UserName,Please Click SingUp button to register yourself')
    print('Hello',__name__)

# declaring another function
def func1():
    print('this is func 1 from demo module')

# this function has no ban hence can be imported outside this module
func1()

def func2():
    print('this is func 2 from demo module')

# Execute  this function only if the module name is __main__ else do not use/execute this function if some one importing it. Because name=__main__ is the entry point of any program file 
if __name__=='__main__':
    # these below function will not be execute outside this file because I have banned the entry point of this file
    func0()
    func2()


# the above line if __name__=='__main__': means that
'''
def main():
  func2()

the above main function will not execute until main() is called itself
'''