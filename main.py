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

# tabla de joc
tabla = {1: "", 2: "", 3: "",
         4: "", 5: "", 6: "",
         7: "", 8: "", 9: ""}

# combinatii castigatoare
moves = [[1, 2, 3],  # Linia 1
         [4, 5, 6],  # Linia 2
         [7, 8, 9],  # Linia 3
         [1, 4, 7],  # Coloana 1
         [2, 5, 8],  # Coloana 2
         [3, 6, 9],  # Coloana 3
         [1, 5, 6],  # Diagonala 1
         [3, 5, 7]]  # Diagonala 2

# moves = [[tabla[1], tabla[2], tabla[3]],
#          [tabla[4], tabla[5], tabla[6]],
#          [tabla[7], tabla[8], tabla[9]],
#          [tabla[1], tabla[4], tabla[7]],
#          [tabla[2], tabla[5], tabla[6]],
#          [tabla[3], tabla[6], tabla[9]],
#          [tabla[1], tabla[5], tabla[9]],
#          [tabla[3], tabla[5], tabla[7]]]

#pozitii strategice
center = 5
corners = [1, 3, 7, 9]
edges = [2, 4, 6, 8]

#

def counting (lista):
    return lista.count('x'), lista.count('0')

for i,v in enumerate(moves):
    print(counting(moves[i]))

if tabla[5] == '':
    tabla[5] = '0'
elif tabla[5] == 'x':
    if "" in corners:
        print("trueee")
        