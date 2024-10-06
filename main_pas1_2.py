tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")



# print(tabla[3])
# print(tabla[int(poz_x)])
def input_x():
    poz_x = int(input("Pozitia X: "))
    if tabla[poz_x] != '':
        while tabla[poz_x] != '':
            poz_x = int(input("Pozitie ocupata. Introdu pozitie noua: "))
            tabla[poz_x] = 'X'
            break
    else:
        tabla[poz_x] = 'X'

joc_finalizat = False

def joc_castigat():
    este_castigat = False
    castigatorul = None
    if tabla[1] == tabla[2] == tabla[3] and tabla[1] != '':
        este_castigat = True
        castigatorul = tabla[1]
    if tabla[4] == tabla[5] == tabla[6] and tabla[4] != '':
        este_castigat = True
        castigatorul = tabla[4]
    if tabla[7] == tabla[8] == tabla[9] and tabla[7] != '':
        este_castigat = True
        castigatorul = tabla[7]
    if tabla[1] == tabla[4] == tabla[7] and tabla[1] != '':
        este_castigat = True
        castigatorul = tabla[1]
    if tabla[2] == tabla[5] == tabla[8] and tabla[2] != '':
        este_castigat = True
        castigatorul = tabla[2]
    if tabla[3] == tabla[6] == tabla[9] and tabla[3] != '':
        este_castigat = True
        castigatorul = tabla[3]
    if tabla[1] == tabla[5] == tabla[9] and tabla[1] != '':
        este_castigat = True
        castigatorul = tabla[1]
    if tabla[3] == tabla[5] == tabla[7] and tabla[3] != '':
        este_castigat = True
        castigatorul = tabla[3]

    return (este_castigat, castigatorul)

while joc_finalizat is False:
    input_x()
    joc_terminat = joc_castigat() # True, X / False, None
    joc_finalizat = joc_terminat[0]
    # mutare_calculator()
    print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")
    print(f'S-a terminat? {joc_terminat}')
