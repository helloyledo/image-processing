import sys

def get_objects_with_holes(matrix):
    matrix_copy = [row[:] for row in matrix]
    objects = []
    num_objects = 0
    num_objects_with_holes = 0
    for i in range(len(matrix_copy)):
        for j in range(len(matrix_copy[i])):
            if matrix_copy[i][j] == 1:
                num_objects += 1
                object_pixels = [(i, j)]
                matrix_copy[i][j] = 0
                k = 0
                while k < len(object_pixels):
                    x, y = object_pixels[k]
                    k += 1
                    for x1, y1 in [(x-1, y), (x+1, y), (x, y-1), (x, y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]:
                        if 0 <= x1 < len(matrix_copy) and 0 <= y1 < len(matrix_copy[x1]):
                            if matrix_copy[x1][y1] == 1:
                                object_pixels.append((x1, y1))
                                matrix_copy[x1][y1] = 0
                objects.append(object_pixels)
    return objects, num_objects

def num_holes(objeto,imagem):
    i = []
    j = []
    for x in objeto:
        i.append(x[0])
        j.append(x[1])
    isup = min(i)
    iinf = max(i)
    quantidade = []
    maxi = 0
    mini = len(imagem[0])
    for x in range(isup,iinf+1):      
        for y in objeto:
            if x == y[0] and y[1] > maxi:
                maxi = y[1]
            if x == y[0] and y[1] < mini:
                mini = y[1]
        quantidade.append((x,maxi,mini))
    for x in range(len(quantidade)):
        for y in range(quantidade[x][1]-quantidade[x][2]):
            if imagem[quantidade[x][0]][quantidade[x][2]+y+1] == 0:
                return True 
    return False


def resultado(imagem):
  objetos = get_objects_with_holes(imagem)
  num_obj_with_holes = 0
  num_obj_wthout_holes = 0
  for x in objetos[0]:
    if num_holes(x,imagem):
      num_obj_with_holes += 1
    else:
      num_obj_wthout_holes += 1
  return objetos[1],num_obj_with_holes, num_obj_wthout_holes


if __name__ == '__main__':
    filename = sys.argv[1]      
    with open(filename, 'rb') as f:
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



    print("O numero de objetos na imagem e: " + str(resultado(img)[0])+"\n" + 
        "O numero de objetos com furo na imagem e: " + str(resultado(img)[1])+"\n" + 
        "O numero de objetos sem furo na imagem e: "+ str(resultado(img)[2])+"\n")

