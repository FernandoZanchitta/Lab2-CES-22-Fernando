# Decorator all decorators Pizza py
# Pizza example using decorators
class PizzaComponent: # Componente
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Massa(PizzaComponent): #Componente Concreto
    cost = 0.0

class Decorator(PizzaComponent): #Decorador
    def __init__(self,pizzacomponent):
        self.component = pizzacomponent
    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)

class Calabresa(Decorator): #Decorador concreto A
    cost = 8.00
    def __init__(self,pizzacomponent):
        Decorator.__init__(self,pizzacomponent)

class Mussarela(Decorator): #Decorador concreto B
    cost = 7.00
    def __init__(self,pizzacomponent):
        Decorator.__init__(self,pizzacomponent)

class Cebola(Decorator): #Decorador concreto C
    cost = 1.50
    def __init__(self,pizzacomponent):
        Decorator.__init__(self,pizzacomponent)

class Tomate(Decorator): #Decorador concreto D
    cost = 1.50
    def __init__(self,pizzacomponent):
        Decorator.__init__(self,pizzacomponent)

class Alho(Decorator): #Decorador concreto E
    cost = 1.00
    def __init__(self,pizzacomponent):
        Decorator.__init__(self,pizzacomponent)

class Cheddar(Decorator): #Decorador concreto F
    cost = 2.50
    def __init__(self,pizzacomponent):
        Decorator.__init__(self,pizzacomponent)

class Rucula(Decorator): #Decorador concreto G
    cost = 1.0
    def __init__(self,pizzacomponent):
        Decorator.__init__(self,pizzacomponent)

PizzaCalabresa = Calabresa(Mussarela(Cebola(Massa())))
print(PizzaCalabresa.getDescription() + ": $"+ str(PizzaCalabresa.getTotalCost()))
PizzaMarguerita = Tomate(Mussarela(Rucula(Massa())))
print(PizzaMarguerita.getDescription() + ": $"+ str(PizzaMarguerita.getTotalCost()))

