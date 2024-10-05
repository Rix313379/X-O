tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")

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

    return este_castigat, castigatorul

# Functie introducere X sau O
def input_mutare(mutare):
    poz_mutare = int(input(f"{mutare}: "))
    if tabla[poz_mutare] != '':
        while tabla[poz_mutare] != '':
            poz_mutare = int(input("Pozitie ocupata. Introdu pozitie noua: "))
            tabla[poz_mutare] = mutare
            break
    else:
        tabla[poz_mutare] = mutare

# Functie afisare intrebare resetare joc
def intrebare_repeta_jocul():
    rasp = input('Vrei sa repeti jocul (Y/N) ?: ')
    while rasp.upper() != 'Y' or rasp.upper() != 'N':
        rasp = input('Vrei sa repeti jocul (Y/N) ?: ')
    return rasp

# main
joc_finalizat = False
tabla_este_plina = False

while joc_finalizat is False and tabla_este_plina is False:
    input_mutare('X')

    joc_terminat = joc_castigat() # True, X / False, None
    joc_finalizat = joc_terminat[0]
    print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")

    if joc_finalizat:
        print(f'Joc incheiat. Castigatorul este {joc_terminat[1]}')

        # resetare joc dupa terminare runda
        intrebare = intrebare_repeta_jocul()

        if intrebare.upper() == 'N':
            break # iese din while
        elif intrebare.upper() == 'Y':
            joc_finalizat = False
            tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
            input_mutare('X')
            print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")
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
                    input_mutare('X')
                    print(
                        f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")
                # END resetare

    if tabla_este_plina is True:
        break

    # mutare_calculator()
    input_mutare('O')

    joc_terminat = joc_castigat()  # (True, X) / False, None
    joc_finalizat = joc_terminat[0]
    print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")

    if joc_finalizat:
        print(f'Jocul s-a incheiat. Castigatorul este {joc_terminat[1]}')

        # resetare joc dupa terminare runda
        intrebare = intrebare_repeta_jocul()

        if intrebare.upper() == 'N':
            break  # iese din while
        elif intrebare.upper() == 'Y':
            joc_finalizat = False
            tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
            input_mutare('X')
            print(
                f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")
        # END resetare

    if tabla_este_plina is True:
        break

# Caz remiza: 123546879
