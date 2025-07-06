# single inheritance
class Animal:
    def __init__(self,name):
        self.name = name
    def barks(self):
        print(self.name,"always bark.")
class Dog(Animal):
    def bark(self):
        print(self.name,"never barks.")

dog1 = Animal("Street dogs")
dog1.barks()

dog2 = Dog("Bruno")
dog2.bark()

# MULTIPLE inheritance - where the child class inherits from different parent class. 
class A:
    def method_a(self):
        print("I am method A")
class B:
    def method_b(self):
        print("I am method B")
class C(A,B):
    pass
obj = C() # here we created an object using class C and it inherits methods from classes A and classes B.
obj.method_a()  # to print the above statements we have to call that method
obj.method_b()

# MULTI-LEVEL inheritance - it includes a Grandparent class, parent class and a child class
class Grandparent:
    def display(self):
        print("I am a grandparent class")
class Parent(Grandparent):
    pass  # This will inherit from the Grandparent class
class Child(Parent):
    pass  # And this will inherit from the Parent class, as the parent class inherits from grandparent class the child class indirectly inherits from the grandparent class.
childobj = Child() 
childobj.display() # the display method is only declared in grandparent class but when accessing child class it gives output it indirectly inherits from the grandparent class.

# SUPER() method - allows you to call methods from the parent class.
# Most commonly inside the child class __init__() to call the parent’s __init__()\
class Parent :
    def __init__(self):
        print("I am the parent class.")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am a child class.")
child1 = Child() # here we no need to specifically call the parent class cause we used super method which automatically initializes the init() method of parent class.
