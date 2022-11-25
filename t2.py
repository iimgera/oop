class Bird():
    wings = 'I have wings'

    def can_fly(self):
        print('I can fly')

    def cannot_fly(self):
        print('I cannot fly')

    def can_swim(self):
        print('I can swim')


class Fish():
    gills = 'I have gills'

    def can_swim(self):
        print('I can swim')



class Mammal():
    lungs = 'I have lungs'
    babies_eat_milk = 'Babies eat milk'

    def can_swim(self):
        print('I can swim')



class Predator():
    def eat(self):
        print('I eat meat')



class Herbivore():
    def eat(self):
        print('I eat plants')



class Falcon(Bird, Predator):
    def __init__(self, species):
        self.species = species
    def display_species(self):
        print(f'\nSpecies: {self.species}')
    


class Penguin(Bird, Predator):
    def __init__(self, type, age):
        self.type = type
        self.age = age 
    def display_type_age(self):
        print (f'\nType: {self.type}\nAge: {self.age}')
    

class Trout(Fish, Predator):
    def __init__(self, species):
        self.species = species

    def display_species(self):
        print(f'\nSpecies: {self.species}')



class Whale(Mammal, Predator):
    def __init__(self, species):
        self.species = species
    def display_species(self):
        print(f'\nSpecies: {self.species}')



p = Penguin("Royal", "1")
p.display_type_age()
print(p.wings)
p.cannot_fly()
p.eat()
p.can_swim()


f = Falcon("Falco newtoni")
f.display_species()
print(f.wings)
f.can_fly()
f.eat()


t = Trout("Salmo obtusirostris")
t.display_species()
print(t.gills)
t.can_swim()
t.eat()


w = Whale("Mysticeti")
print(w.babies_eat_milk)
w.display_species()
print(w.lungs)
w.can_swim()
w.eat()






































































































































































































































































































































































