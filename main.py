import classes as cl

allaIngridienser = []

def finnsMaltid(allaMaltider):
    textAnswer = input("Skriv måltid du önskar att redigera:")
    answer = 0
    for each in allaMaltider:
        if textAnswer == each.namn:
            answer = 1
    return answer,textAnswer

def finnsIngridiens():
    textAnswer = input("Skriv ingridiens:")
    answer = 0
    for each in allaIngridienser:
        if textAnswer == each.namn
            answer = 1
    return answer,textAnswer

def main():
    allaMaltider = []
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
                for each in allaIngridienser:
                    print(each)
            elif svar == 2:
                for each in allaMaltider:
                    print(each)
            elif svar == 3:
                if finnsMaltid(allaMaltider)[0] == 0:
                    allaMaltider.append(cl.måltid(allaMaltider[1]))
                else:
                    print("Måltid fanns redan registrerad bitch")
            elif svar == 4:
                if finnsMaltid(allaMaltider)[0] == 1:
                    if finnsIngridiens()[0] == 1:

            elif svar == 5:
                if finnsMaltid(allaMaltider)[0] == 1:
                    if finnsIngridiens()[0] == 1:

            elif svar == 6:
                if finnsMaltid(allaMaltider)[0] == 1:
        else:
            continue

main()
