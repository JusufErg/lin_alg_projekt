from LivsmedelsDB4 import DB as DB
from LivsmedelsDB4 import Parametrar
from scipy.optimize import linprog

class Ing:
    def __init__(self, kostnad, namn, allanäring):
        self.namn = namn
        self.allanäring = allanäring #lista näringsvärden
        self.valdnäring = []
        self.kostnad = int(kostnad)

    def skrivnamn(self):
        print(str(self.namn))

    def väljnäring(self, valdaparametrar):
        print("Valda parametrar: ")
        print("Kostnad (kr)")
        for i in valdaparametrar:
            print(Parametrar[i])
            self.valdnäring.append(self.allanäring[i])


def plusingrediens():
    #sökfunktion
    ing = str(input("Sök ingrediens:")).lower()
    alling = []
    for i in DB:
        if ing in i[0].lower():
            alling.append(i)

    for j in alling:
        print(str(alling.index(j)) + " " + j[0])
    val = int(input("Välj livsmedel med index:"))

    #vald ingrediens
    valding = alling[val].copy()
    Nyingrediens = Ing(input("Ange kostnad för livsmedlet/100g: "), valding[0], valding)
    #ange parametrar nedan i listan i stigande ordning (kostnad redan tillagd) se IndexeringParametrar
    #------------------------------------------------------------------------
    Nyingrediens.väljnäring(
        [1, 3, 4, 59, 60]
    )
    #------------------------------------------------------------------------
    print(Nyingrediens.namn)
    print(Nyingrediens.valdnäring)
    print(Nyingrediens.allanäring)

    return Nyingrediens

#plusingrediens()

class Meal:
    def __init__(self):
        self.ingredienser = []

    def addingredient(self):
        self.ingredienser.append(plusingrediens())

    def printingredienser(self):
        for ing in self.ingredienser:
            print(ing.namn)
    def optimize(self):
        minimerakostnad = []
        for ingred in self.ingredienser:
            minimerakostnad.append(ingred.kostnad)

        #skapar tom matris av rätt dimension
        totnär = []
        for i in self.ingredienser[0].valdnäring:
            totnär.append([])

        #lägger till värden
        for ingred in self.ingredienser:
            for i in range(0, len(ingred.valdnäring)):
                totnär[i].append(-1*ingred.valdnäring[i])


        #--------------lägg in näringskrav per parameter nedan
        näringskrav = [2, 700, 2500, 0, 0]
        #--------------

        närkrav = []
        for krav in näringskrav:
            närkrav.append(-1*krav)

        print(minimerakostnad)
        print(totnär)

        opt = linprog(c=minimerakostnad, A_ub=totnär, b_ub=närkrav, method="revised simplex")
        print(opt)
        self.printingredienser()





t = Meal()
while True:
    print("0: lägg til ingrediens, 1: optimera, 2: lista ingredienser")
    val = int(input())
    if val == 0:
        t.addingredient()
    elif val == 1:
        t.optimize()
        quit()
    elif val == 2:
        t.printingredienser()


