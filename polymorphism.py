# there are three types in polymorphism they are:
# 1. Method overriding
# 2. Method overloading
# 3. Built-in - len() function

# methodoverriding - same method name, same attributes , different behaviour
class Student1:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print(f"My name is {self.name}, and my roll no is {self.rollno}")
class Student2(Student1):
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print(f"My name is { self.name},and my roll no is {self.rollno} (child's version)")
stu1 = Student2("Sathvika",267)
stu1.display()

# methodoverloading - same method name, different attributes
# in python method overloading is not directly supported.
# 1.Using Default Arguments
class Math:
    def cal(self,a,b,c=0): # here c=0 is the default argument, if the user doesn't specify value then the program uses that default value
        return a+b+c
calculate = Math()
print(calculate.cal(2,3))
print(calculate.cal(3,5,7)) # this achieves method overloading like behaviour

# 2.Using *args
class Mathematics:
    def calculate(self,*args):
        return sum(args)
cal = Mathematics()
print(cal.calculate(2,3,4,5)) # takes any number of arguments as inputs.

# 3.len() function

