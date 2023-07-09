import Demo

print("name of the module is : ",__name__)

def add():
    print('adding two number ')

def sub():
    print('subtracting two number ')

# defining the entry point of this module
def main():
    add()
    sub()

main()