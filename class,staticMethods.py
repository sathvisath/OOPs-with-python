class Utility:
    app_version = 1.0  # here we did not initialize any __init__ constructor
    @classmethod
    def get_version(self):   
        print(f"The version of this app is:{self.app_version}")
    @staticmethod
    def greet():
        print("Hello! welcome to adult world, it sucks!")
        
# here we did not create any special object we just used the class itself directly to call the function.
Utility.get_version()  
Utility.greet()   