import numpy as np
import matplotlib.pyplot as plt
import scipy

class ingrediens:

    def __init__(self, namn, kostnad, vitaminA, vitaminB, vitaminC):
        self.namn = namn
        self.kostnad = kostnad

        self.vitaminA = vitaminA
        self.vitaminB = vitaminB
        self.vitaminC = vitaminC

    def __str__(self):
        return f"{self.namn}"

class måltid:

    def __init__(self, namn):
        self.namn = namn
        self.ingridienser = []

    def __str__(self):
        return f"{self.namn}"

    def laggTillIngridiens(self, ingridiens):
        if type(ingridiens) == "ingrediens":
            self.ingridienser.append(ingridiens)
    def taBortIngridiens(self, ingridiens):
        if type(ingridiens) == "ingrediens":
            self.ingridienser.remove(ingridiens)

    def optimera(self):

        # i "krav" så ska hur mycket av varje näringsvärde finnas

        naringsKrav = [1,5,3]
        minimiseraKostnad = []
        scalVitaminA = []
        scalVitaminB = []
        scalVitaminC = []
        for ing in self.ingridienser:
            minimiseraKostnad.append(ing.kostnad)
            scalVitaminA.append(ing.vitaminA)
            scalVitaminB.append(ing.vitaminB)
            scalVitaminC.append(ing.vitaminC)


        # OPTIMERINGSALGORITM KÖR

        pass

    #aldin var här