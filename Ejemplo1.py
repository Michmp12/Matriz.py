nombres = [['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','Ñ','S'],['T','U','V','W']]

for i in range(len(nombres)):
    for j in range(len(nombres[i])):
        print(nombres[i][j], end=' ')
    print()
print(nombres)