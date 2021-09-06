import math

def sum_comps(num1, num2):
    return ((num1[0] + num2[0]), (num1[1] + num2[1]))


def res_comp(num1, num2):
    return (num1[0] - num2[0]), (num1[1] - num2[1])


def mult_comp(num1, num2):
    return (num1[0] * num2[0]) - (num1[1] * num2[1]), (num1[0] * num2[1]) + (num2[0] * num1[1])


def div_comp(num1, num2):
    res = []
    a = num1[0]
    b = num1[1]
    c = num2[0]
    d = num2[1]
    return ((a * c) + (b * d)) / ((c ** 2) + (d ** 2)), ((b * c) - (a * d)) / ((c ** 2) + (d ** 2))


def mod_comp(num):
    a = num[0]
    b = num[1]
    return math.sqrt((a ** 2) + (b ** 2))


def conj_comp(num):
    return mult_comp(num, (-1, 0))


def polar_cart(num):
    x = num[0] * math.cos(num[1])
    y = num[0] * math.sin(num[1])
    return round(x, 5), round(y, 5)


def c_fase(num):
    fase = math.atan(num[1] / num[0])
    if (num[0] < 0 and num[1] < 0) or num[0] < 0:
        return 180 + math.degrees(fase)
    elif num[1] < 0:
        return 360 + math.degrees(fase)
    else:
        return math.degrees(fase)


def cart_polar(num):
    h = mod_comp(num)
    alpha = c_fase(num)
    return h, alpha


def sum_vect(v1, v2):
    res = list()
    for i in range(len(v1)):
        res.append(complex(v1[i])+complex(v2[i]))
    return res


def inv_vect(v1):
    res = list()
    for i in range(len(v1)):
        viner = complex(v1[i]) * -1
        res.append(viner)
    return res

def vect_escalar(v, a):
    result = list()
    for i in range(len(v)):
        result.append(complex(v[i]) * a)
    return result


def sum_matrix_comp(m1, m2):
    result = [[complex(m1[i][j]) + complex(m2[i][j]) for j in range(len(m1[i]))] for i in range(len(m1))]
    return result


def inv_matrix(m):
    result = list()
    for i in range(len(m)):
        result.append(inv_vect(m[i]))
    return result


def matrix_escalar(m, a):
    result = list()
    for i in range(len(m)):
        result.append(vect_escalar(m[i], a))
    return result


def trans(a):
    result = list()
    for i in range(len(a[0])):
        result.append([])
        for j in range(len(a)):
            result[i].append("None")

    for i in range(len(a)):
        for j in range(len(a[i])):
            result[j][i] = a[i][j]
    return result


def conjg(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = a[i][j].conjugate()
    return a


def matrix_adj(m):
    matriz = trans(m)
    return conjg(matriz)


def matrix_matrix(m1, m2):
    result = list()
    for i in range(len(m1)):
        fila = list()
        for j in range(len(m2[0])):
            suma = 0
            for k in range(len(m2)):
                producto = complex(m1[i][k]) * complex(m2[k][j])
                suma += producto
            fila.append(suma)
        result.append(fila)
    return result


def accion_matriz_vector(m, v):
    return matrix_matrix(m,v)


def prod_int_vect(v1, v2):
    result = list()
    for i in range(len(v1)):
        result.append(list())
        v1[i] = complex(v1[i]).conjugate()
        result[i] = (complex(v1[i]) * complex(v2[i]))
    while len(result) > 1:
        result[0] = complex(result[0]) + complex(result[-1])
        result.pop()
    return result[0]


def norma(v):
    result = 0
    for i in v:
        result += i[0]**2 + i[1]**2
    return math.sqrt(result)


def distancia_vecotres(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += (v1[i][0] - v2[i][0])**2 + (v1[i][1] - v2[i][1])**2
    return math.sqrt(result)

def hermitian(m):
    return m == matrix_adj(m)

def producto_tensor(m1, m2):
    lista=[]
    filas = len(m1)*len(m2)
    columnas = len(m1[0])*len(m2[0])
    for x in range(filas):
        lista2=[]
        lista.append(lista2)
        for y in range(columnas):
            lista2.append([])
    for i in range(filas):
        for j in range(columnas):
            a = i//len(m2)
            b = j//len(m2[0])
            res = m1[a][b] * m2
            a2 = i % len(m2)
            b2 = j % len(m2[0])
            lista[i][j] = res[a2][b2]
    return lista

def main():
    sum_vect([9 + 7j, 11 + 0j, 14 - 18j], [6 + 3j, 3 + 1j, 10 - 8j])
    inv_vect([9 + 7j, -4j, 14 - 18j])
    vect_escalar([(-9 - 7j), (-11 + 0j), (-14 + 18j)], 4)
    sum_matrix_comp([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]],
                    [[6 + 3j, 3 + 1j, 10 - 8j], [-8j, 4 + 10j, 2 - 1j]])
    inv_matrix([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]])
    matrix_escalar([[6 + 3j, 3 + 1j, 10 - 8j], [-8j, 4 + 10j, 2 - 1j]], 4)
    trans([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]])
    conjg([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]])
    matrix_adj([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]])
    matrix_matrix([[4 + 8j, 4j, 8 - 3j], [7 + 1j, 6j, 4 + 5j], [8 + 4j, 7 - 8j, 10]],
                  [[6 + 3j, -8j, 5], [3 + 1j, 4 + 10j, 9j], [10 - 8j, 2 - 1j, 10 + 4.5j]])
    prod_int_vect([4 + 8j, 4j, 8 - 3j], [8 + 4j, 7 - 8j, 10])
    norma([(4, 5), (3, 1), (0, -7)])
    distancia_vecotres([(3, 8), (5, -2), (8, -10)], [(8, 9), (3, -7), (6, 14)])
    hermitian([[(3 + 0j), (2 - 1j), (-3j)], [(2 + 1j), (0 + 0j), (1 - 1j)], [(0 + 3j), (1 + 1j), (0 + 0j)]])

if __name__ == '__main__':
    main()