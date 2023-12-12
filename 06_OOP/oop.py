# Object-Oriented Programming, jahreem jeffers, V0.0

class Person: # Use pascalCase fro ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    # To String Function -- How the object appears as a string.
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\n They weigh {self.weight} pounds.\n"


person1 = Person("aiden Redfield", 25, 201)
print(person1)

person2 = Person ("jaiden Blitzspear", 18, 120)
print(person2)

if person1.weight > person2.weight:
    print(f"{person1.name} weighs more than {person2.name}.")
elif person1.weight == person2.weight: 
    print("both of the 2 is a heavy freak.\n")
else:
    print(f"{person2.name} weighs more than {person1.name}.")