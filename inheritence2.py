# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's name: {self.name}")

class Labrador(Dog): # Single Inheritance
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritence
class GuideDog(Labrador):   # Multilevel Inheritence
    def guide(self):
        print(f"{self.name} Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):   # Multiple Inheritance
    def sound(self):
        print("Golden Retriever barks")


lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()
guide_dog.sound()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.sound()
retriever.greet()

