# python doesn't support abstraction directly but we use ABC module to achieve abstraction in python

from abc import ABC,abstractmethod  # ABC means abstract base class 
class Computer(ABC): # Computer class inherits from ABC class to become an abstract class
    @abstractmethod # to declare a method as abstract method.
    def process(self):
        print("Running")  # now we can't create any objects using this class.
#com = Computer()
#com.process() # we will get an error.

class Laptop(Computer): # creating another class that inherits from Computer class
    #pass # if we do not give definition to the class it inherits the abstraction class from computer
    def process(self):
        print("Laptop is  working")
com1 = Laptop()
com1.process()



