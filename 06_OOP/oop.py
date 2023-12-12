# Object-Oriented Programming, jahreem jeffers, V0.0

class Person: # Use pascalCase fro ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    # To String Function -- How the object appears as a string.
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\n They weigh {self.weight} pounds.\n"


person1 = person("aiden redfield", 25, 201)
