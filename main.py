import time as t
import classes as cl

testingridiens1 = cl.ingrediens("test1",20,1,0,12)
testingridiens2 = cl.ingrediens("test2",50,7,2,0)
testingridiens3 = cl.ingrediens("test3",30,5,1,7)
allaIngridienser = [testingridiens1,testingridiens2,testingridiens3]



def finnsMaltid(allaMaltider):
    truePosition = 0
    textAnswer = input("Skriv måltid: ")
    answer = 0
    iteration = -1
    trueAnswer = None
    for each in allaMaltider:
        iteration = iteration + 1
        if textAnswer == each.namn:
            answer = 1
            truePosition = iteration
            trueAnswer = each

    return answer,textAnswer,truePosition,trueAnswer

def finnsIngridiens():
    truePosition = 0
    textAnswer = input("Skriv ingridiens: ")
    answer = 0
    iteration = -1
    trueAnswer = None
    for each in allaIngridienser:
        iteration = iteration + 1
        if textAnswer == each.namn:
            answer = 1
            truePosition = iteration
            trueAnswer = each
    return answer,textAnswer,truePosition,trueAnswer

def main():

    # Skapar en exempelmåltid som heter "bajs" för att snabbt kunna göra experiment på
    allaMaltider = []
    pre_defined_maltid = cl.måltid("bajs")
    pre_defined_maltid.laggTillIngridiens(testingridiens1)
    pre_defined_maltid.laggTillIngridiens(testingridiens2)
    pre_defined_maltid.laggTillIngridiens(testingridiens3)
    allaMaltider.append(pre_defined_maltid)

    while True:
        for a in range(4):
            print(" ")
        print("---------")
        print("Vänligen välj alternativ")
        print("1 - Lista registrerade ingridienser")
        print("2 - Lista registrerade måltider")
        print("3 - Ny måltid")
        print("4 - Lägg till ingridiens i måltid")
        print("5 - Ta bort ingridiens i måltid")
        print("6 - OPTIMERA MÅLTID")

        svar = int(input("Alternativ"))
        if svar in range(0,7):
            if svar == 1:
                print("LISTA AV INGRIDIENSER:")
                for each in allaIngridienser:
                    print(each)

            elif svar == 2:
                print("LISTA AV MÅLTIDER:")
                for each in allaMaltider:
                    print(each)
                    listI = each.ingridienser
                    for doe in listI:
                        z = " --- " + doe.namn
                        print(z)
                    print(" ")

            elif svar == 3:
                svarMaltid = finnsMaltid(allaMaltider)
                if svarMaltid[0] == 0:
                    allaMaltider.append(cl.måltid(svarMaltid[1]))
                    print("MÅLTID TILLAGD")
                else:
                    print("Måltid fanns redan registrerad bitch")

            elif svar == 4:
                svarMaltid = finnsMaltid(allaMaltider)
                if svarMaltid[0] == 1:
                    svarIngridiens = finnsIngridiens()
                    if svarIngridiens[0] == 1:
                        print("Ingridiens tillagd")
                        allaMaltider[svarMaltid[2]].laggTillIngridiens(svarIngridiens[3])
                    else:
                        print("misslyckades")

            elif svar == 5:
                svarMaltid = finnsMaltid(allaMaltider)
                if svarMaltid[0] == 1:
                    svarIngridiens = finnsIngridiens()
                    if svarIngridiens[0] == 1:
                        allaMaltider[svarIngridiens[2]].taBortIngridiens(svarIngridiens[3])

            elif svar == 6:
                svarMaltid = finnsMaltid(allaMaltider)
                if svarMaltid[0] == 1:
                    allaMaltider[svarMaltid[2]].optimera()
                else:
                    print("Hittade ej måltid")

        else:
            continue

main()
