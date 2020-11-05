# Classes, objects and instants

# How to create class
# Syntax: class name_of_class starting with a Capital letter
# good naming convention is required

# classes are a way to bring data and functionally together

class Dog:

    def __init__(self, name, colour): # initialising Dog Class
        self.name = name
        self.colour = colour
        self.animal_kind = "canin"



    def bark(self): # self refers to current class
        return "woof"
# in order to execute a class we have to create an object of this class
fido = Dog("fido", "brown")  # creating an object of our Dog class also and instant of the class

print(fido.name) # This would print the path of where you can find whats in the Dog() class
print(fido.animal_kind) # prints the animal_kind variable in the fido/dog() class
print(fido.color)
print(fido.bark())
## fido.animal_kind = "Big Dog" # this changes the animal_kind for fido but not for the whole Dog() class
## print(lassie.animal_kind)  # This means that the animal_kind for lassie wont change.