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

# tabla de joc
tabla = {1: "x", 2: "x", 3: "0",
         4: "", 5: "0", 6: "",
         7: "", 8: "", 9: "0"}

# combinatii castigatoare
moves = [[1, 2, 3],  # Linia 1
         [4, 5, 6],  # Linia 2
         [7, 8, 9],  # Linia 3
         [1, 4, 7],  # Coloana 1
         [2, 5, 8],  # Coloana 2
         [3, 6, 9],  # Coloana 3
         [1, 5, 9],  # Diagonala 1
         [3, 5, 7]]  # Diagonala 2
print(tabla)
#
# moves = [[tabla[1], tabla[2], tabla[3]],
#          [tabla[4], tabla[5], tabla[6]],
#          [tabla[7], tabla[8], tabla[9]],
#          [tabla[1], tabla[4], tabla[7]],
#          [tabla[2], tabla[5], tabla[6]],
#          [tabla[3], tabla[6], tabla[9]],
#          [tabla[1], tabla[5], tabla[9]],
#          [tabla[3], tabla[5], tabla[7]]]

# pozitii strategice
center = 5
corners = [1, 3, 7, 9]
edges = [2, 4, 6, 8]

    # Verifica daca poate castiga calculatorul - ofensiva
    for move in moves:
        count_X = 0
        count_0 = 0
        poz_disponibila = 0
        for pozitie in move:
            if tabla[pozitie] == '0':
                count_0 += 1
            elif tabla[pozitie].upper() == 'X':
                count_X += 1
            elif tabla[pozitie] == '':
                poz_disponibila = pozitie

        if count_0 == 2 and poz_disponibila != 0:
        if count_0 == 2 and poz_disponibila != 0:
            tabla[poz_disponibila] = '0'
            # print(f"am castigat cu pozitia {poz_disponibila}")
            return

    # Daca jucatorul poate castiga la urmatoarea mutare - defensiva
    for move in moves:
        count_X = 0
        count_0 = 0
        poz_disponibila = 0
        for pozitie in move:
            if tabla[pozitie] == '0':
                count_0 += 1
            elif tabla[pozitie].upper() == 'X':
                count_X += 1
            elif tabla[pozitie] == '':
                poz_disponibila = pozitie

            if count_X == 2 and poz_disponibila != 0:
            if count_X == 2 and poz_disponibila != 0:
                tabla[poz_disponibila] = '0'

                # print(f"am contracarat pe pozitia {poz_disponibila}")
                return

    # Ocupa pozitia centrala
    if tabla[center] == '':
        tabla[center] = '0'
        # print("0 pe pozitia centrala")
        return

    # Ocupa prima pozitia din colturi gasita
    lista = []
    for pozitie in corners:
        if tabla[pozitie] == '':
            lista.append(pozitie)
            # tabla[pozitie] = '0'
            # break

    if len(lista) != 0:
        pozitie = random.choice(lista)
        tabla[pozitie] = '0'
        # print(f"0 pe poztia {pozitie}")
        return

    # Ocupa prima pozitia din edges gasita
    lista = []
    for pozitie in edges:
        if tabla[pozitie] == '':
            lista.append(pozitie)
            # tabla[pozitie] = '0'
            # break
    if len(lista) != 0:
        pozitie = random.choice(lista)
        tabla[pozitie] = '0'
        # print(f"0 pe pozitia {pozitie}")
        return

def play_easy(tabla):
    lista = []
    for move in moves:
        for pozitie in move:
            if tabla[pozitie] == '':
                lista.append(pozitie)

    if len(lista) != 0:
        pozitie = random.choice(lista)
        tabla[pozitie] = '0'
        # print(f"0 pe pozitia {pozitie}")
        return

# main
tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

level = intrebare_dificultate_joc()
afisare_tabla_joc()

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
    adauga_mutare('X')
    # afisare_tabla_joc()

    joc_terminat = joc_castigat()  # returneaza (True, X) / (False, None)
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
            adauga_mutare('X')
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
                    adauga_mutare('X')
                    # afisare_tabla_joc()
                # END resetare

    if tabla_este_plina is True:
        break

    mutare_calculator(level, tabla)

    joc_terminat = joc_castigat()  # returneaza (True, X) / (False, None)
    joc_finalizat = joc_terminat[0]
    afisare_tabla_joc()

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