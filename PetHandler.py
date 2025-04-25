class Pets:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def display_info(self):
        print(f"{self.name} is a {self.species} and is {self.age} years old")
class Dog:
    def __init__(self, name):
        self.name = name

        
class PetFunctionality:
    def __init__(self):
        self.pets = [

        ]
    def addPet(self, pet):
        self.pets.append(pet)
    
    def adoptPet(self, name):
        for peto in self.pets:
            if peto.name.lower() == name.lower():
                self.pets.remove(peto)
                return True
        print(f"Sorry, {name} is not available unfortunetly")
        return False
    def display_all_pets(self):
        if not self.pets:
            print("No Pets!")
        else:
            for pet in self.pets:
                pet.display_info()



        
