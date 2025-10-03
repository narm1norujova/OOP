# Run-time polymorphism
# Overriding(dynamic)
class Animal:
    def sound(self):
        return "some sound"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
#Polymorphic behaviour
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())
    
    

