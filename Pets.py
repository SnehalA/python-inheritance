class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def getName(self):
        return self.name
    def getSpecies(self):
        return self.species
    def hatesDogs(self):
        return False;
    def chasesCats(self):
        return False;

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

class Dog(Pet):
    def __init__(self, name, chases_cats=True):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats
    def chasesCats(self):
        return self.chases_cats

class Cat(Pet):
    def __init__(self, name, hates_dogs=True):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs
    def hatesDogs(self):
        return self.hates_dogs

class my_factory():
    def getInstance(self,name="",type="",species=""):
        if  type=="Pet":
            return Pet(name,species)
        if type=="Cat":
            return Cat(name)
        if type=="Dog":
            return Dog(name)

def test(mister_pet):
    print mister_pet, '!\t', mister_pet.getName(),':', mister_pet.getSpecies(), '\tchase cats :', mister_pet.chasesCats(), '\thates dog : ', mister_pet.hatesDogs()
    return dir(mister_pet)

dory=my_factory().getInstance("Dory", "Pet", "Fish")
bolt = my_factory().getInstance("Bolt", "Dog")
tom = my_factory().getInstance("Tom", "Cat")
jerry=my_factory().getInstance("Jerry", "Pet", "Mouse")


test(bolt)
test(tom)
test(jerry)
x=test(dory)
print "\n\nDORY functions :\n" ,x

