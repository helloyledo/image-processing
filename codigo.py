image = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0 ,0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1 ,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
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
                    for x1, y1 in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
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
    jlft = min(j)
    jrgt = max(j)
    for x in range(isup+1,iinf-1):
        for y in range(jlft+1,jrgt-1):
            if imagem[x][y] == 0:
                return True
    return False 

blbla = get_objects_with_holes(image)
print(blbla[0][1])
print(num_holes(blbla[0][1],image))




