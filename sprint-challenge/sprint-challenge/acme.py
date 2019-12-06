import random
class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):

        self.identifier = identifier
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
    

    def stealability(self):
        ratio = float(self.price)/float(self.weight)
        if ratio < 0.5:
            return 'Not so stealbale...'
        elif ratio < 1:
            return 'Kinda stealable.'
        return 'Very stealable!'


    def explode(self):
        x = self.flammability * float(self.weight)
        if x < 10:
            return '...fizzle.'
        elif x < 50:
            return '...boom!'
        return '...BABOOM!'

class BoxingGlove(Product):
    def __init__(self, name):
        super().__init__(name)
        self.weight = 10
    

    def explode(self):
        return "...it's a glove."
    

    def punch(self):
        w = self.weight
        if w < 5:
            return 'That tickles.'
        elif w < 15:
            return 'Hey that hurt!'
        return 'OUCH!'