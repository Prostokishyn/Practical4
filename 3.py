class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        
    def __str__(self):
        return f"{self.species} {self.name}"

class Zoopark:
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def remove_animal(self, animal):
        self.animals.remove(animal)
        
    def __str__(self):
        return f"Зоопарк містить {len(self.animals)} тварин: {', '.join(str(animal) for animal in self.animals)}"
        
monkey = Animal("Мавпа", "Банановий монстр")
lion = Animal("Лев", "Шерсть")
zoopark = Zoopark()
zoopark.add_animal(monkey)
zoopark.add_animal(lion)
print(zoopark)
zoopark.remove_animal(monkey)
print(zoopark)