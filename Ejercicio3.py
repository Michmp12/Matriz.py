matriz = [['-','-','-'],['-','-','-'],['-','-','-']]

def fnt_agregar(dato, x, y):
    if matriz[x][y] == '-':
        matriz[x][y] = dato.upper()
    elif matriz[x][y] == 'x':
        print('\nEl espacio esta ocupado <ENTER>') 
def fnt_impression_matriz():          
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='   ')
        print()

sw = True
while sw == True:
    fnt_impression_matriz()
    fnt_agregar(input('Dato: '),int(input('Fila: ')),int(input('Columna: ')))