import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
        
     

print('Computer Turn: Snake(s) Water(w) or Gun(g)?')

randNum=random.randint(1,3)
print(randNum)


if randNum==1:
    comp='s'
elif randNum==2:
    comp='w'
else:
    comp='g'    


you=input(" Your Turn: Snake(s) Water(w) Gun(g)?")

if(comp=='s' or comp=='g' or comp=='w'):
    print('The computer selected ',comp)

print('The user selected ',you)


result=gameWin(comp,you)

if(result==None):
    print('The Game is Tie!!')
elif result:
    print('You Win')
else:
    print('Computer Wins')