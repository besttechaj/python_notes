#To find a word 

# opening the file 
# f=open('sample.txt','r')
# reading the content 
# content=f.read()
# if 'React' in content:
#     print('React is present')
# else:
#     print('no such word is found')
# f.close()



#CREATING A GAME FUNCTION, IF THE NEW SCORE IS GREATER THAN THE PREVIOUS ONE THEN OVERRIDE THE PREVIOUS VALUE WITH THE NEW HIGH SCORE VALUE ELSE DO NOTHING
# def game(user_score):
    
#     #fetching  the previous score file
#     f=open('highScore.txt','r')
#     #converting string to int and storing the old score 
#     oldScore=f.read()
#     print(type(oldScore))
#     f.close()

#     #if there is no score existed then update it
#     if oldScore=='':
#         print('adding a new score')
#         with open('highScore.txt','w') as f:
#             f.write(str(user_score))
    
#     #if there is an existed score then checks the condition and process the result
#     elif user_score>int(oldScore):
#         print('NEW HIGH SCORE ACHIEVED')
#         with open('highScore.txt','w') as f:
#             f.write(str(user_score))

        
#     else:
#         print('Failed to broke the high score')


# game(2000)



#printing the tables from 2 to 20

# for i in range(1,21):
#         with open(f"tables/Multiplication_of_{i}.txt",'w') as t:
#                 for j in range(1,11):    
#                         t.write(f"{i} * {j} = {i*j}")
#                         if j!=10:
#                                 t.write('\n')


#replace a word in the file
# with open('sample.txt','r') as f:
#     content=f.read()

# #replacing the content with updated value
# content=content.replace('donkey','this is a replaced value')

# #updating the whole file
# with open('sample.txt','w') as f:
#     f.write(content)


#replacing/beeping the bad multiple words inside a  file with censored message

# bad_words=['dog','fat','kid','animal']

# with open('sample.txt','r') as f:
#     content=f.read()


# for word in bad_words:
#     #replacing the content with updated value
#     content=content.replace(word,'$@##$&&$')
#     #updating the whole file
#     with open('sample.txt','w') as f:
#         f.write(content)

#initializing the value
# i=1
# content=True


# with open('log.txt') as f:
#     #to enter the loop making content=true
#     while content:
#         #reading the data line by line
#         content=f.readline()

#         if 'python' in content.lower():
#          print(content)
#          print('line no',i)    
#         else:
#          i+=1


# Accessing a file to copy to content and paste it into another file 
# with open('this.txt') as f:
#     content=f.read()

# with open('copy.txt','w') as f:
#     f.write(content)
#     print(f)

# checking whether the files are identical or not 
# file1="copy.txt"
# print(type(file1))
# file2="this.txt"
# with open(file1) as f:
#     f1=f.read() 

# with open(file2) as f :
#     f2=f.read()

# if(f1==f2):
#     print('files are identical')
# else:
#     print('Files are not identical')

# wap to wipe the content of a file 
# with open('sample.txt','w') as my_file:
#     my_file.write("this file data has been wiped out")
#     print(my_file)

# wap to rename a file --> logic: copy the content of previous file into new file(give name to this new file ) and delete the old file 
oldfile='sample3.txt'
newfile='sample2.txt'

with open(oldfile) as file:
    content=file.read()

with open(newfile,'w') as file:
    file.write(content)

# to delete previous file 
import os
os.remove(oldfile)