# Class Definition
class Human:
    # Constructor
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    # Method
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "play tennis")

        elif self.occupation == "actor":
            print(self.name, "shoots film")

    def speaks(self):
        print(self.name, "says how are you?")

# Creating an Object and Calling Methods
tom = Human("tom cruise", "actor")
tom.do_work()
tom.speaks()