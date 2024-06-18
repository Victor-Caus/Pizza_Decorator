# Pizza example using decorators

class PizzaComponent: # Componente
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Plate(PizzaComponent):
    cost = 0.0

class Decorator(PizzaComponent):
    def __init__(self, pizza_component):
        self.component = pizza_component

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)

class Frango(Decorator):  #Decorator Concreto A
    cost = 4.5
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Catupiry(Decorator):  #Decorator Concreto A
    cost = 5.5
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)



pizzaDeFrango = Frango(Catupiry(Plate))
print(pizzaDeFrango.getDescription() + "$" + str(pizzaDeFrango.getTotalCost()))