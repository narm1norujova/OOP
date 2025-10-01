class Dog:
    species = "Canine" # Class variable

    def __init__(self, name, age):

        # Instance variable
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1.species)   # Class variable
print(dog1.name)      # Instance variable
print(dog2.name)      # Instance variable

# Update instance variable
dog1.name = "Max"
print(dog1.name)

# Update class variables
Dog.species = "Feline"
print(dog1.species)
print(dog2.species)





