import time as t
import classes as cl

allaIngridienser = []

def finnsMaltid(allaMaltider):
    truePosition = 0
    textAnswer = input("Skriv måltid: ")
    answer = 0
    iteration = -1
    for each in allaMaltider:
        iteration = iteration + 1
        if textAnswer == each.namn:
            answer = 1
            truePosition = iteration

    return answer,textAnswer,truePosition

def finnsIngridiens():
    truePosition = 0
    textAnswer = input("Skriv ingridiens: ")
    answer = 0
    iteration = -1
    for each in allaIngridienser:
        if textAnswer == each.namn:
            answer = 1
            truePosition = iteration
    return answer,textAnswer,truePosition

def main():
    allaMaltider = []
    while True:
        t.sleep(4)
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
                    for eacheach in each.ingridienser:
                        z = "    " + eacheach
                        print(z)

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
                    svaringridiens = finnsIngridiens()
                    if svaringridiens[0] == 1:
                        allaMaltider[svaringridiens[2]].laggTillIngridiens(svaringridiens[2])

            elif svar == 5:
                svarMaltid = finnsMaltid(allaMaltider)
                if svarMaltid[0] == 1:
                    svaringridiens = finnsIngridiens()
                    if svaringridiens[0] == 1:
                        allaMaltider[svaringridiens[2]].taBortIngridiens(svaringridiens[2])

            elif svar == 6:
                svarMaltid = finnsMaltid(allaMaltider)
                if svarMaltid[0] == 1:
                    allaMaltider[2].optimera()

        else:
            continue

main()

#snopp
