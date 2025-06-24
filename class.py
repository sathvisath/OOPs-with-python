# Make a class called Pet, then create an object called my_pet with name "Simba" and age 2
class pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(speaks):  # not only self we can use any type of nicknames
        print("Hi my name is",speaks.name,"I am ",speaks.age,"years old.")

s1 = pet("simba",2)  # s1 is the object
s1.speak()

# Modify Object Properties
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
my_pet = Pet("simba",2) # my_pet is an object # here we defined the age as 2
my_pet.age = 3 # but here we can change the value 
print(my_pet.age) # it will output the updated value only

# Delete Object Properties
del my_pet.name
print(my_pet.name)