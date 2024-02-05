# Object-Oriented Programming, jahreem jeffers, V0.0

class Person: # Use pascalCase fro ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.weakness = None
        self.nemesis = None
    
    # To String Function -- How the object appears as a string.
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\n They weigh {self.weight} pounds.\n"

    def classFunction(self):
        print("This is an example of a class function.\n")
        print("It only works when called on an object of that class.")


person1 = Person("aiden Redfield", 25, 103)
print(person1)

person2 = Person ("jaiden Blitzspear", 18, 120)
print(person2)

# if person1.weight > person2.weight:
#     print(f"{person1.name} weighs more than {person2.name}.")
# elif person1.weight == person2.weight: 
#     print("both of the 2 is a heavy freak.\n")
# else:
#     print(f"{person2.name} weighs more than {person1.name}.")

# person1.classFunction()


print(person1.name)
person1.name = "JXJ"
print(person1.name)

# Deleting properties -- DANGER WILL ROBINSON< DANGER!
# THIS IS DOES NOT 'RESET' A PROPERTY, IT DELETES IT COMPLETLY.
print(person1.name)
del person1.name
#print(person1.name)

#deleting objects -- Delete them if you're finished with
del person1 

# Adding properties to Objects
person2.weakness = "kryptonite"
print(person2)
print(person2.weakness)