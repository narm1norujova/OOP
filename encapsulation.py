class Dog:
    def __init__(self, name, breed, age):
        self.name = name    # Public attribute
        self._breed = breed # Protected attribute
        self.__age = age    # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"
    
    # getter and setter for private attributes
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            return self.__age
        else:
            print("Invalid age!")

dog = Dog("Buddy", "Labrador", 3)
print(dog.name)
print(dog._breed)
print(dog.get_age())
dog.set_age(5)
print(dog.get_info())
        
    
    
    
