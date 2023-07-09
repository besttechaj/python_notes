# In python we have 3 types of methods:
# instance method, class method, static method
# Instance is subdivided into two type ie Accessor and Mutator methods
# Accessor -> whenever we are fetching the value ie getter method apply
# Mutator -> whenever we are modifying the value ie setter method apply
class Students:
    
    # creating a static variable
    school='Kendriya vidyalaya No.1'
    
    def __init__(self,m1,m2,m3):
        # initializing instance variables for each newly object created
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    # Instance Method --> we are passing self which takes the object as an argument
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    """
    # getter method
    def get_m1(self):
        return self.m1
    # setter method
    def set_m1(self,value):
        self.m1=value"""

    #CLASS METHOD --> to work with class variables we use class methods
    @classmethod #this is a preBuilt decorator
    def getSchoolName(cls):# we don't work with instance ,here we are working with class hence we need to pass cls keyword as an params
        print(cls.school)
    
    # static method : When we don't have to do with instance variable and class variables then we use static .eg to get the school details not the students
    @staticmethod  # another  decorator
    def info():
        print('this is student class which comes under chapra university')


# object belong to student 1st
s1=Students(32,43,54)
# object belong to student 2nd
s2=Students(82,73,98)

print('Average of student-1 is ',s1.avg())
print('Average of student-2 is ',s2.avg())

# calling class method
Students.getSchoolName()

# calling static method
Students.info()