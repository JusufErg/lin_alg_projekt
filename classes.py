import numpy as np
import matplotlib.pyplot as plt
import scipy

class ingrediens:

    def __init__(self, kostnad, vitaminA, vitaminB, vitaminC):
        self.kostnad = kostnad

        self.vitaminA = vitaminA
        self.vitaminB = vitaminB
        self.vitaminC = vitaminC

class måltid:

    def __init__(self):
        self.ingridienser = []

    def nyIngridiens(self, ingridiens):
        if type(ingridiens) == "ingrediens":
            self.ingridienser.append(ingridiens)
    def taBortIngridiens(self, ingridiens):
        if type(ingridiens) == "ingrediens":
            self.ingridienser.remove(ingridiens)

    def optimera(self):

        # OPTIMERINGSALGORITM KÖR

        pass

class regel:

