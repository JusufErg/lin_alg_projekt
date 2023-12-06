from LivsmedelsDB4 import DB as DB
from LivsmedelsDB4 import Parametrar

class Ing:
    def __init__(self, kostnad, namn, allanäring):
        self.namn = namn
        self.allanäring = allanäring #lista näringsvärden
        self.valdnäring = [int(kostnad)]

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
    Nyingrediens = Ing(input("Ange kostnad för livsmedlet: "), valding[0], valding)
    #ange parametrar nedan i listan i stigande ordning (kostnad redan tillagd) se IdexeringParametrar
    #------------------------------------------------------------------------
    Nyingrediens.väljnäring(
        [1, 3, 4, 59, 60]
    )
    #------------------------------------------------------------------------
    print(Nyingrediens.namn)
    print(Nyingrediens.valdnäring)
    print(Nyingrediens.allanäring)

    return Nyingrediens

plusingrediens()