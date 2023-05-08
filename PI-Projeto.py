def mapeia(img, m, n, i, j, marcado):
    marcado[i][j] = 1
    if marcado[i+1][j] != 1 and img[i+1][j] == 1 and i+1 < m and j < n:
        mapeia(img, m, n, i+1, j, marcado)
    elif marcado[i+1][j+1] != 1 and img[i+1][j+1] == 1 and i+1 < m and j+1 < n:
        mapeia(img, m, n, i+1, j+1, marcado)
    elif marcado[i][j+1] != 1 and img[i][j+1] == 1 and i < m and j+1 < n:
        mapeia(img, m, n, i, j+1, marcado)
    elif marcado[i-1][j+1] != 1 and img[i-1][j+1] == 1 and i-1 < m and j+1 < n:
        mapeia(img, m, n, i-1, j+1, marcado)
    

def conta_obj(img, m, n, mark):
    n_obj = 0
    for i in range(n):
        for j in range(m):
            if mark[i][j] != 1:
                if img[i][j] == 0:
                    mark[i][j] = 1
                elif img[i][j] == 1:
                    mapeia(img, m, n, i, j, mark)
                    print(marcado)
                    n_obj +=1      
    return n_obj


with open('teste.ppm', 'rb') as f:
    data = f.read()

data_str = str(data, 'utf-8')

lines = data_str.split('\n')
lines = [line for line in lines if not line.startswith('#') and not line.startswith('P1')]

dimensions = [int(x) for x in lines[0].split()]
largura = dimensions[0]
altura = dimensions[1]

img = []

for i in range(1, altura+1):
    line = [int(dig) for dig in lines[i].strip(" \r") if dig != " "]
    img += [line]

marcado = []
for i in range(altura):
    linha_marcado =[]
    for j in range(largura):
        linha_marcado += [0]
    marcado += [linha_marcado]

print(conta_obj(img, largura, altura, marcado))
#print(img)
#print(marcado)
