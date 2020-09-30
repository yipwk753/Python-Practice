#https://realpython.com/instance-class-and-static-methods-demystified/
class Farm(object):
    animal = "chickens"

    def checkchickens(self, eggs):
        self.eggs = eggs
        #self is needed else animal is not defined
        print(f"Today the {self.animal} have produced {self.eggs} eggs.")

    #checkchickens needed to assign eggs to self.eggs
    #so that the property could be accessed in other instance methods
    def printeggs(self):
        print("eggs", self.eggs)

    def changemethod(self):
        @staticmethod
        def a():
            print("change method")
        #class behavior can be modified through self
        self.__class__.roostercall = a

    #cannot access instance attributes
    @classmethod
    def changeAnimal(cls, animal):
        cls.animal = animal
    
    #cannot access either self or cls
    @staticmethod
    def roostercall():
        print("Rooster wakes everyone up at dawn.")

farm = Farm()
farm.checkchickens(5)
#class method can be called from the class itself
Farm.changeAnimal("turkeys")
farm.checkchickens(5)
#static method can be called from the class itself
Farm.roostercall()
#and from the instance itself
farm.roostercall()
farm.changemethod()
Farm.roostercall()
farm.printeggs()