import random
""" Some functions for basic linear algebra opertations based on python lists. """


def vector_add(a, b):
    if len(a) != len(b):
        raise Exception(
            "[Addition]: Failed at vector size must be equal. {:n} == {:n}".format(len(a), len(b)))

    addition_vector = list()
    for i in range(len(a)):
        addition_vector.append(a[i] + b[i])

    return addition_vector


def vector_sub(a, b):
    if len(a) != len(b):
        raise Exception(
            "[Subtraction]: Failed at vector size must be equal. {:n} == {:n}".format(len(a), len(b)))

    addition_vector = list()
    for i in range(len(a)):
        addition_vector.append(a[i] - b[i])

    return addition_vector


def vector_scalar_mul(r, a):
    if not isinstance(a, list):
        raise Exception("[Skalar Mult.]: Skalar isn't given.")

    addition_vector = list()
    for i in range(len(a)):
        addition_vector.append(r * a[i])

    return addition_vector


def vector_dot(a, b):
    if len(a) != len(b):
        raise Exception(
            "[Dot]: Failed at vector size must be equal. {:n} == {:n}".format(len(a), len(b)))

    addition_vector = list()
    for i in range(len(a)):
        addition_vector.append(a[i] * b[i])

    return sum(addition_vector)


def create_random_matrix(n, m):
    random_matrix = list()
    constant = 255
    for i in range(n):
        random_matrix.append(list())
        for n in range(m):
            random_matrix[i].append(int(random.random() * constant))

    return random_matrix


def matrix_vector_mul(mat, vec):
    mul_matrix = list()

    for i in range(len(mat)):
        mul_matrix.append(list())
        for j in range(len(vec)):
            mul_matrix[i].append(mat[i][j] * vec[j])
        mul_matrix[i] = sum(mul_matrix[i])

    return mul_matrix


def matrix_transpose(a):
    N = len(a)
    M = len(a[0])
    transposed_matrix = list()
    for n in range(N):
        transposed_matrix.append(list())
        for m in range(M):
            transposed_matrix[n].append(a[m][n])

    return transposed_matrix
