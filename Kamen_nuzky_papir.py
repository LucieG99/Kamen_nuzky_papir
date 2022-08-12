import random

# uvitani hrace
print("Vítej u hry kámen, nůžky, papír !")
sep = 48 * "="
print(sep)

# pravidla hry
rules = """
    1) Hra je pro dva hráče - tebe a počítač.
    2) Můžeš vybírat z hracích možností - kámen, nůžky, papír.
    3) Nůžky stříhají papír.
    Kámen tupí nůžky.
    Papír balí kámen.
    4) Hra má tolik kol, kolik si zvolíš. 
"""
print("PRAVIDLA HRY:\n", rules)
print(sep)
print("Pojďme hrát !")
print(sep)

# promenne pro smycku hry se vstupy uzivatele
options = ["kámen", "nůžky", "papír"]
# end = "q"
your_score = 0                                       # score uzivatele
comp_score = 0                                       # score pocitace
count = 0                                            # promenna pro scitani score
number_of_rounds = input("Zvol si počet kol:")       # promenna se vstupem uzivatele
# smycka pro overeni ze uyivatel zadava cislo
while True:                                          # overeni ze uzivatel zadava cislo
    if number_of_rounds.isdigit():
        break
    else:
        number_of_rounds = input("Zvol si počet kol:")

print(sep)

# promenne ve smycce pro vystup
win = "Vyhráváš kolo"
lost = "Prohráváš kolo"

# SMYCKA HRY
while count == 0:                                       # zahaji hru pokud je skore nula
    for round in range(int(number_of_rounds)):          # pro pocet zadanych kol plati
        player = input("Tvůj tah:")                     # promenna pro vyber hraci moznosti uzivatelem
        if player not in options:                       # podminka pokud vyber neni v moznostech
            print("Zadej platnou možnost!")             # tiskni zadej platnou moz. dokud nedostanes spravnou
            continue
        # navrat do smycky for po splneni podminky
        print("Hráč:", player.upper())                  # vytiskni hracuv tah velkymi pismeny
        comp = random.choice(options)                   # promenna vyberu pocitace
        print("Počítač:", comp.upper())                 # vytiskni vyber pocitace
        # podminky hry ve smycce for
        if player == "kámen" and comp == "nůžky":
            print(win.upper())
            print(sep)
            count += 1
            your_score += 1                             # pri splneni podminky udel bod uzivateli
        elif player == "nůžky" and comp == "papir":
            print(win.upper())
            print(sep)
            count += 1
            your_score += 1
        elif player == "papír" and comp == "kámen":
            print(win.upper())
            print(sep)
            count += 1
            your_score += 1
        elif player == comp:            # pokud je vyber uzivatele stejny jako vyber pocitace, oznac to jako remizu
            print("Remíza".upper())
            print(sep)
            count += 1
        # elif player == "q":
        #     print("Ukončuji hru.")   # NEFUNGUJE
        #     count += 0
        #     break
        else:
            print(lost.upper())        # co neni uvedeno v podminkach vyse oznac jako prohru uzivatele a udel bod compu
            print(sep)
            count += 1
            comp_score += 1

# ukonceni hry - vystupy
if your_score == comp_score:
    print("Konec hry!".upper())
    print(sep)
    print("Tvoje celkové skore:", your_score)
    print("Celkové skore počítače:", comp_score)
    print(16 * "=", "JE TO REMÍZA !", 16 * "=")

if your_score < comp_score:
    print("Konec hry!".upper())
    print(sep)
    print("Tvoje celkové skore:", your_score)
    print("Celkové score počítače:", comp_score)
    print(12 * "#", "UPS, VYHRÁVÁ POČÍTAČ !", 12 * "#")

if your_score > comp_score:
    print("Konec hry!".upper())
    print(sep)
    print("Tvoje celkové skore:", your_score)
    print("Celkové score počítače:", comp_score)
    print(12 * "*", "VYHRÁL JSI, GRATULUJI!", 12 * "*")


