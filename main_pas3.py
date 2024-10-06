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


def counting(lista):
    return lista.count('x'), lista.count('0')


def mutare_calculator(parametru: {}):
    # Verifica daca poate castiga calculatorul - ofensiva
    for move in moves:
        count_X = 0
        count_0 = 0
        poz_disponibila = 0
        for pozitie in move:
            if tabla[pozitie] == '0':
                count_0 += 1
            elif tabla[pozitie] == 'x':
                count_X += 1
            elif tabla[pozitie] == '':
                poz_disponibila = pozitie

        if count_0 == 2 and poz_disponibila != 0:
            tabla[poz_disponibila] = '0'
            print(f"am castigat cu pozitia {poz_disponibila}")
            return

    # Daca jucatorul poate castiga la urmatoarea mutare - defensiva
    for move in moves:
        count_X = 0
        count_0 = 0
        poz_disponibila = 0
        for pozitie in move:
            if tabla[pozitie] == '0':
                count_0 += 1
            elif tabla[pozitie] == 'x':
                count_X += 1
            elif tabla[pozitie] == '':
                poz_disponibila = pozitie

            if count_X == 2 and poz_disponibila != 0:
                tabla[poz_disponibila] = '0'
                print(f"am contracarat pe pozitia {poz_disponibila}")
                return

    # Ocupa pozitia centrala
    if tabla[5] == '':
        tabla[5] = '0'
        print("0 pe pozitia centrala")
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
        print(f"0 pe poztia {pozitie}")
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
        print(f"0 pe pozitia {pozitie}")
        return

mutare_calculator(tabla)