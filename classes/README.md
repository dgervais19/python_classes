# This lesson will cover Classes in Python
**This is part of OOP (Object Oriented Programming)**

# There are four pillar:
* Inheritance (mostly used)
    - **Eliminates redundant code**
    - We can use all functions and variables from parent class

* Encapsulation
    - **Reduce complexity and increase reusability**
    -
* Abstraction
    - **Reduce complexity and isolate impact of changes**


* Polymorphism - poly (many) morphism (form)
    - **Refractor code or case statements**
    - Allows us to change attributes/variables
    
## What are classes and why
* Class is the main factor that is
* we can create multiple objects within a class that is used to implement any of the pillars.

## Creating a class
```
# Classes, objects and instants

# How to create class
# Syntax: class name_of_class starting with a Capital letter
# good naming convention is required

# classes are a way to bring data and functionally together

class Dog:

    animal_kind = "canin"

    def bark(self): # self refers to current class
        return "woof"
```

## Creating an object to execute the class

```
# in order to execute a class we have to create an object of this class
fido = Dog()  # creating an object of our Dog class also and instant of the class
lassie = Dog()
print(fido) # This would print the path of where you can find whats in the Dog() class

print(fido.animal_kind) # prints the animal_kind variable in the fido/dog() class
```

## Managing objects within a class
```
fido.animal_kind = "Big Dog" # this changes the animal_kind for fido but not for the whole Dog() class
print(fido.animal_kind)
print(lassie.animal_kind)  # This means that the animal_kind for lassie wont change. 
```

