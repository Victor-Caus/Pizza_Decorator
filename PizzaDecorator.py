
class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost

class Massa(PizzaComponent):
    cost = 10.0

class Decorator(PizzaComponent):
    def __init__(self, pizza_component):
        self.component = pizza_component

    def getTotalCost(self):
        return self.component.getTotalCost() + super().getTotalCost()

    def getDescription(self):
        return self.component.getDescription() + ' ' + super().getDescription()

class Frango(Decorator): #1
    cost = 4.5
    def __init__(self, pizza_component):
        super().__init__(pizza_component)

class Catupiry(Decorator):
    cost = 5.5
    def __init__(self, pizza_component):
        super().__init__(pizza_component)

class Calabresa(Decorator):
    cost = 4.5
    def __init__(self, pizza_component):
        super().__init__(pizza_component)

class CarneDeSol(Decorator):
    cost = 7.5
    def __init__(self, pizza_component):
        super().__init__(pizza_component)

class Lombo(Decorator):
    cost = 8.4
    def __init__(self, pizza_component):
        super().__init__(pizza_component)

class Mussarela(Decorator):
    cost = 4.5
    def __init__(self, pizza_component):
        super().__init__(pizza_component)

pizzaDeFrangoCatupiry = Frango(Catupiry(Massa()))
print(pizzaDeFrangoCatupiry.getDescription() + " $" + str(pizzaDeFrangoCatupiry.getTotalCost()))
pizzaDeLomboMussarela = Mussarela(Lombo(Massa()))
print(pizzaDeLomboMussarela.getDescription() + " $" + str(pizzaDeLomboMussarela.getTotalCost()))

