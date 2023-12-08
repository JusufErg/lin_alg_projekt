import numpy as np
import scipy
from scipy.optimize import linprog

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
        #if type(ingridiens) == "ingrediens":
        self.ingridienser.append(ingridiens)
    def taBortIngridiens(self, ingridiens):
        #if type(ingridiens) == "ingrediens":
        self.ingridienser.remove(ingridiens)

    def optimera(self):

        # i "krav" så ska hur mycket av varje näringsvärde finnas

        naringsKrav = [100,500,300]
        minimiseraKostnad = []
        scalVitaminA = []
        scalVitaminB = []
        scalVitaminC = []
        for ing in self.ingridienser:
            minimiseraKostnad.append(ing.kostnad)
            scalVitaminA.append((-1)*(ing.vitaminA))
            scalVitaminB.append((-1)*(ing.vitaminB))
            scalVitaminC.append((-1)*ing.vitaminC)
        totalKombination = [scalVitaminA, scalVitaminB, scalVitaminC]
        totalNaringsKrav = []
        for each in naringsKrav:
            totalNaringsKrav.append((-1)*each)

        print("minkost:")
        print(minimiseraKostnad)
        print("totKomb:")
        print(totalKombination)
        print("tot när:")
        print(totalNaringsKrav)

        opt = linprog(c=minimiseraKostnad, A_ub=totalKombination, b_ub=totalNaringsKrav, method="revised simplex")
        print(opt)
        print("hej")
        print(type(opt))


        # OPTIMERINGSALGORITM KÖR

        pass

    #aldin var här