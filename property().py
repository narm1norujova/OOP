class Dog:
    def __init__(self, name, breed, age):
        self.name = name     # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age     # Private attribute

    # Getter using property decorator
    @property
    def age(self):
        return self.__age

    # Setter for age
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Invalid age!")

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"


dog = Dog("Buddy", "Labrador", 3)
print(dog.name)     #  Public
print(dog._breed)   #  Protected (still accessible)
print(dog.age)      #  Calls @property (getter)
dog.age = 5         #  Calls @age.setter
print(dog.get_info())
