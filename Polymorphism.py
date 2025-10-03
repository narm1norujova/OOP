# Compile-time polymorphism:
# Overloading(static)
# Not true overloading but with *args = mimic overloading
class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())
print(calc.multiply(4))
print(calc.multiply(7))

# Using multiple arguments
print(calc.multiply(2,3))
print(calc.multiply(2, 3, 4))


