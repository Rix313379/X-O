
tabla = {1 : "", 2 : "", 3 : "x", 
         4 : "", 5 : "xz", 6 : "", 
         7 : "", 8 : "", 9 : ""}

moves = [[tabla[1],tabla[5],tabla[9]],
         [tabla[3],tabla[5],tabla[7]],
         [tabla[1],tabla[4],tabla[7]], 
         [tabla[2],tabla[5],tabla[8]],
         [tabla[3],tabla[6],tabla[9]], 
         [tabla[1],tabla[2],tabla[3]], 
         [tabla[4],tabla[5],tabla[6]],
         [tabla[7],tabla[8],tabla[9]]]

corners = [tabla[1],tabla[3],tabla[7],tabla[9]]

def counting (lista):
    return lista.count('x'), lista.count('0')

for i,v in enumerate(moves):
    print(counting(moves[i]))

if tabla[5] == '':
    tabla[5] = '0'
elif tabla[5] == 'x':
    if "" in corners:
        print("trueee")
        