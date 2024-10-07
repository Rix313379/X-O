"""
STRATERGIA CALCULATORULUI:

Pas 1 Ofensiva - Verifica daca poate castiga calculatorul == true, atunci
                    mutare castigatare
                altfel Pas 2
Pas 2 Defensiva - Daca jucatorul poate castiga la urmatoarea mutare, atunci
                    calculatorul blocheaza acea mutare (pun pe pozitia castigatoare a jucatorului)
                    altfel Pas 3
Pas 3 Ocupa pozitia centrala - Daca pozitia centrala e libera, calculaorul o ocupa

Pas 4 Colturi: Daca pozitiile din colturi sunt libere, calculatorul aleg un colt

Pas 5 Margini: Calculatorul alege o pozitie libera din locurile ramase
"""

import random

def afisare_tabla_joc(param_tabla):
    
    return f"{param_tabla[1]} | {param_tabla[2]} | {param_tabla[3]}\n---------\n{param_tabla[4]} | {param_tabla[5]} | {param_tabla[6]}\n---------\n{param_tabla[7]} | {param_tabla[8]} | {param_tabla[9]}"
    
    
def joc_castigat(param_tabla):
    este_castigat = False
    castigatorul = None

    if param_tabla[1] == param_tabla[2] == param_tabla[3] and param_tabla[1] != '':
        este_castigat = True
        castigatorul = param_tabla[1]
    if param_tabla[4] == param_tabla[5] == param_tabla[6] and param_tabla[4] != '':
        este_castigat = True
        castigatorul = param_tabla[4]
    if param_tabla[7] == param_tabla[8] == param_tabla[9] and param_tabla[7] != '':
        este_castigat = True
        castigatorul = param_tabla[7]
    if param_tabla[1] == param_tabla[4] == param_tabla[7] and param_tabla[1] != '':
        este_castigat = True
        castigatorul = param_tabla[1]
    if param_tabla[2] == param_tabla[5] == param_tabla[8] and param_tabla[2] != '':
        este_castigat = True
        castigatorul = param_tabla[2]
    if param_tabla[3] == param_tabla[6] == param_tabla[9] and param_tabla[3] != '':
        este_castigat = True
        castigatorul = param_tabla[3]
    if param_tabla[1] == param_tabla[5] == param_tabla[9] and param_tabla[1] != '':
        este_castigat = True
        castigatorul = param_tabla[1]
    if param_tabla[3] == param_tabla[5] == param_tabla[7] and param_tabla[3] != '':
        este_castigat = True
        castigatorul = param_tabla[3]

    return este_castigat, castigatorul

# Functie introducere X sau O
def adauga_mutare(mutare, param_tabla):
    poz_mutare = int(input(f"{mutare}: "))
    if param_tabla[poz_mutare] != '':
        while param_tabla[poz_mutare] != '':
            poz_mutare = int(input("Pozitie ocupata. Introdu pozitie noua: "))
            param_tabla[poz_mutare] = mutare
            break
    else:
        param_tabla[poz_mutare] = mutare
    return param_tabla

# Functie afisare intrebare resetare joc
def intrebare_repeta_jocul():
    rasp = input('Vrei sa repeti jocul (Y/N) ?: ')
    while rasp.upper() != 'Y' and rasp.upper() != 'N':
        rasp = input('Vrei sa repeti jocul (Y/N) ?: ')
    return rasp

# Functie afisare dificultate joc
def intrebare_dificultate_joc():
    rasp = input('Dificultate joc (usor/greu) ?: ')
    while rasp.upper() != 'USOR' and rasp.upper() != 'GREU':
        rasp = input('Dificultate joc (usor/greu) ?: ')
    return rasp

# Algoritm mutare calculator
def mutare_calculator(dificultate, param_tabla, param_moves):
    if dificultate.upper() == 'USOR':
        param_tabla = play_easy(param_tabla, param_moves)
    elif dificultate.upper() == 'GREU':
        param_tabla = play_hard(param_tabla, param_moves)
    
    return param_tabla
    

def play_hard(param_tabla, param_moves):
    # pozitii strategice
    center = 5
    corners = [1, 3, 7, 9]
    edges = [2, 4, 6, 8]

    # Verifica daca poate castiga calculatorul - ofensiva
    for move in param_moves:
        count_X = 0
        count_0 = 0
        poz_disponibila = 0
        for pozitie in move:
            if param_tabla[pozitie] == '0':
                count_0 += 1
            elif param_tabla[pozitie].upper() == 'X':
                count_X += 1
            elif param_tabla[pozitie] == '':
                poz_disponibila = pozitie

        if count_0 == 2 and poz_disponibila != 0:
            param_tabla[poz_disponibila] = '0'
            # print(f"am castigat cu pozitia {poz_disponibila}")
            return param_tabla

    # Daca jucatorul poate castiga la urmatoarea mutare - defensiva
    for move in param_moves:
        count_X = 0
        count_0 = 0
        poz_disponibila = 0
        for pozitie in move:
            if param_tabla[pozitie] == '0':
                count_0 += 1
            elif param_tabla[pozitie].upper() == 'X':
                count_X += 1
            elif param_tabla[pozitie] == '':
                poz_disponibila = pozitie

            if count_X == 2 and poz_disponibila != 0:
                param_tabla[poz_disponibila] = '0'
                # print(f"am contracarat pe pozitia {poz_disponibila}")
                return param_tabla

    # Ocupa pozitia centrala
    if param_tabla[center] == '':
        param_tabla[center] = '0'
        # print("0 pe pozitia centrala")
        return param_tabla

    # Ocupa prima pozitia din colturi gasita
    lista = []
    for pozitie in corners:
        if param_tabla[pozitie] == '':
            lista.append(pozitie)
            # param_tabla[pozitie] = '0'
            # break

    if len(lista) != 0:
        pozitie = random.choice(lista)
        param_tabla[pozitie] = '0'
        # print(f"0 pe poztia {pozitie}")
        return param_tabla

    # Ocupa prima pozitia din edges gasita
    lista = []
    for pozitie in edges:
        if param_tabla[pozitie] == '':
            lista.append(pozitie)
            # param_tabla[pozitie] = '0'
            # break
    if len(lista) != 0:
        pozitie = random.choice(lista)
        param_tabla[pozitie] = '0'
        # print(f"0 pe pozitia {pozitie}")
        return param_tabla
    
def play_easy(param_tabla, param_moves):
    lista = []
    for move in param_moves:
        for pozitie in move:
            if param_tabla[pozitie] == '':
                lista.append(pozitie)

    if len(lista) != 0:
        pozitie = random.choice(lista)
        param_tabla[pozitie] = '0'
        # print(f"0 pe pozitia {pozitie}")
        return param_tabla

# main
tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

level = intrebare_dificultate_joc()
print(afisare_tabla_joc(tabla))

# combinatii castigatoare
moves = [[1, 2, 3],  # Linia 1
         [4, 5, 6],  # Linia 2
         [7, 8, 9],  # Linia 3
         [1, 4, 7],  # Coloana 1
         [2, 5, 8],  # Coloana 2
         [3, 6, 9],  # Coloana 3
         [1, 5, 9],  # Diagonala 1
         [3, 5, 7]]  # Diagonala 2

joc_finalizat = False
tabla_este_plina = False

while joc_finalizat is False and tabla_este_plina is False:
    adauga_mutare('X', tabla)
    # afisare_tabla_joc()

    joc_terminat = joc_castigat(tabla)  # returneaza (True, X) / (False, None)
    joc_finalizat = joc_terminat[0]

    if joc_finalizat:
        print(f'Joc incheiat. Castigatorul este {joc_terminat[1]}')

        # resetare joc dupa terminare runda
        intrebare = intrebare_repeta_jocul()

        if intrebare.upper() == 'N':
            break  # iese din while
        elif intrebare.upper() == 'Y':
            joc_finalizat = False
            tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
            level = intrebare_dificultate_joc()
            adauga_mutare('X', tabla)
            # afisare_tabla_joc()
        # END resetare
    else:
        tabla_are_spatii_goale = True
        for i in tabla:
            if tabla[i] == '':
                tabla_are_spatii_goale = False
                break
            elif i == len(tabla):
                tabla_este_plina = True
                print('Este remiza.')

                # resetare joc dupa terminare runda
                intrebare = intrebare_repeta_jocul()

                if intrebare.upper() == 'N':
                    break  # iese din while
                elif intrebare.upper() == 'Y':
                    joc_finalizat = False
                    tabla_este_plina = False
                    tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
                    level = intrebare_dificultate_joc()
                    adauga_mutare('X', tabla)
                    # afisare_tabla_joc()
                # END resetare

    if tabla_este_plina is True:
        break

    mutare_calculator(level, tabla, moves)

    joc_terminat = joc_castigat(tabla)  # returneaza (True, X) / (False, None)
    joc_finalizat = joc_terminat[0]
    print(afisare_tabla_joc(tabla))

    if joc_finalizat:
        print(f'Jocul s-a incheiat. Castigatorul este {joc_terminat[1]}')

        # resetare joc dupa terminare runda
        intrebare = intrebare_repeta_jocul()

        if intrebare.upper() == 'N':
            break  # iese din while
        elif intrebare.upper() == 'Y':
            joc_finalizat = False
            tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
            level = intrebare_dificultate_joc()
        # END resetare

    if tabla_este_plina is True:
        break

# Caz remiza: 1 9 3 8 4
