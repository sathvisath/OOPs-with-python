# we use encapsulation to avoid the unnecessary changes in the value of an attribute

class Student:
    def __init__(self,name):
        self.name = name   
s1 = Student("Sathvika")
s1.name = "Lakshmi"  # here we can change the value how ever we want , to avoid this we use encapsulation.
print(s1.name) 

# this is getter method
class Student:
    def __init__(self,name):
        self.__name = name  #here __name (double underscore) is used to encapsulate the name attribute to class itself.
    def get_name(self):
        return self.__name  # the name attribute cannot be accessed outside the class directly so we create a seperate method to get the value of that attribute. 
s1 = Student("Sathvika")
print(s1.get_name())

# if incase we want to change the value of that attribute we use setter method
class Student:
    def __init__(self,name):
        self.__name = name  
    def get_name(self):
        return self.__name  
    def set_name(self,surname):  # this method is a setter its job is to just update value we have to print the "get_name" method to print the updated value
        self.__name = self.__name_again(surname) # we have to store the updated value in self.__name itself cause it cant be accessed directly.
    def __name_again(self,surname):  # same like private attribute this is a private method. we use __
        return self.__name +" " + surname

s1 = Student("Sathvika")
s1.set_name("Kothari")
print(s1.get_name()) # this will take the surname input and print the value
