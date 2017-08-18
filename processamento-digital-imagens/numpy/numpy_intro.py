# -*- coding: utf-8 -*-

"""

Created on Wed Mar 25 16:26:54 2015



@author: frank

"""

import numpy as np

# import cv2

# ndarray

# a = np.array([2, 4, 6, 8, 10])
#
# print("a:\n", a)
# #[ 2  4  6  8 10]
#
# print("a.ndim:\n", a.ndim)
# # 1
#
# print("a.shape:\n", a.shape)
# #(5,)
#
# print("a.dtype:\n", a.dtype)
# #int64
#
# a.dtype = np.uint8
#
# print("a.dtype:\n", a.dtype)
# #uint8

# ###################################

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
# print("a:\n", a)
# # [[1 2 3 4]
# #  [5 6 7 8]]
#
# print("a.ndim:\n", a.ndim)
# # 2
#
# print("a.shape:\n", a.shape)
# # (2, 4)
#
# print("a.dtype:\n", a.dtype)
# # int64

# ###################################

# print(np.zeros((3, 3)))
# # [[ 0.  0.  0.]
# #  [ 0.  0.  0.]
# #  [ 0.  0.  0.]]
#
# print()
#
# print(np.ones((2, 3)))
# # [[ 1.  1.  1.]
# #  [ 1.  1.  1.]]
#
# print()
#
# print(np.empty((2, 2)))
# # [[  0.00000000e+000  -1.28822983e-231]
# #  [  2.12387378e-314   2.78136370e-309]]
#
# print()
#
# print(np.empty((2, 2), 'bool'))
# # [[False  True]
# #  [ True  True]]
#
# print()
#
# print(np.eye(3))
# # [[ 1.  0.  0.]
# #  [ 0.  1.  0.]
# #  [ 0.  0.  1.]]

# ###################################

# arange e linspace

# print(np.arange(5))
# # [0 1 2 3 4]
#
# print()
#
# print(np.arange(2, 6))
# # [2 3 4 5]
#
# print()
#
# print(np.arange(0, 2, 0.5))
# # [ 0.   0.5  1.   1.5]
#
# print()
#
# print(np.linspace(0, 2, 5))
# # [ 0.   0.5  1.   1.5  2. ]

# ###################################

# # Fatiamento (Slicing) (VETOR)
#
# # exemplo
#
# # indice negativo
#
# # passo negativo
#
# # supressao de indices e passo
#
# a = np.arange(15) * 10
#
# print(a)
# # [  0  10  20  30  40  50  60  70  80  90 100 110 120 130 140]
#
# print()
#
# print(a[::3])
# # [  0  30  60  90 120]
#
# print()
#
# print(a[-1::-1])
# # [140 130 120 110 100  90  80  70  60  50  40  30  20  10   0]

# ###################################

# # Fatiamento (Slicing) (MATRIZ)
#
# # exemplo
#
# # linhas e colunas
#
# # indices negativos e passo
#
# a = np.arange(25)
#
# a = a.reshape(5, 5)
#
# print(a)
# # [[ 0  1  2  3  4]
# #  [ 5  6  7  8  9]
# #  [10 11 12 13 14]
# #  [15 16 17 18 19]
# #  [20 21 22 23 24]]
#
# print()
#
# print(a[::-1, ::-1])
# # [[24 23 22 21 20]
# #  [19 18 17 16 15]
# #  [14 13 12 11 10]
# #  [ 9  8  7  6  5]
# #  [ 4  3  2  1  0]]

# ###################################

# ## Ravel
#
# a = np.arange(15)
#
# a = a.reshape(3, 5)
#
# print(a)
# # [[ 0  1  2  3  4]
# #  [ 5  6  7  8  9]
# #  [10 11 12 13 14]]
#
# print()
#
# print(a.ravel())
# # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

# ###################################

# # Copy
#
# a = np.arange(15)
#
# b = a.copy()
#
# c = a
#
# print(a)
# # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
#
# print()
#
# print(b)
# # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
#
# print()
#
# print(c)
# # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

# ###################################

# # Operacoes
#
# a = np.arange(6)
#
# a = a.reshape(2, 3)
#
# b = np.array([1, 3, 2, 4, 2, 1])
#
# b = b.reshape(3, 2)
#
# print(a)
# # [[0 1 2]
# #  [3 4 5]]
#
# print()
#
# print(b)
# # [[1 3]
# #  [2 4]
# #  [2 1]]
#
# print()
#
# print(b.T)
# # [[1 2 2]
# #  [3 4 1]]
#
# print()
#
# print(a + b.T)
# # [[1 3 4]
# #  [6 8 6]]
#
# print()
#
# print(3 * a)
# # [[ 0  3  6]
# #  [ 9 12 15]]
#
# print()
#
# print(a.dot(b))
# # verifica (Produto Escalar)
# # [[ 6  6]
# #  [21 30]]

# ###################################

# # Mais operacoes
#
# a = np.array([1, 3, 4, 2])
#
# print(a)
# # [1 3 4 2]
#
# print()
#
# print(a.sum())
# # 10
#
# a = np.array([[1, 8, 9, 16], [2, 7, 10, 15], [3, 6, 11, 14], [4, 5, 12, 13]])
#
# print(a)
# # [[ 1  8  9 16]
# #  [ 2  7 10 15]
# #  [ 3  6 11 14]
# #  [ 4  5 12 13]]
#
# print()
#
# print(a.max())
# # 15
#
# print(a.min())
# # 1
#
# print(a.sum())
# # 136
#
# print(a.cumsum())
# # Aritimética Modular
# # [  1   9  18  34  36  43  53  68  71  77  88 102 106 111 123 136]
#
# print()
#
# print(a.max(0))
# # [ 4  8 12 16]
#
# print()
#
# print(a.sum(1))
# # [34 34 34 34]
#
# print()
#
# print(a.mean(0))
# # [  2.5   6.5  10.5  14.5]
#
# print(a.cumsum())
# # [  1   9  18  34  36  43  53  68  71  77  88 102 106 111 123 136]
#
# print()
#
# print(a.cumsum(0))
# # [[ 1  8  9 16]
# #  [ 3 15 19 31]
# #  [ 6 21 30 45]
# #  [10 26 42 58]]
#
# print(a.cumprod(0))
# # [[    1     8     9    16]
# #  [    2    56    90   240]
# #  [    6   336   990  3360]
# #  [   24  1680 11880 43680]]

# ###################################

# # indices
#
# l, c = np.indices((4, 5))
#
# print(l)
# # [[0 0 0 0 0]
# #  [1 1 1 1 1]
# #  [2 2 2 2 2]
# #  [3 3 3 3 3]]
#
# print()
#
# print(c)
# # [[0 1 2 3 4]
# #  [0 1 2 3 4]
# #  [0 1 2 3 4]
# #  [0 1 2 3 4]]
#
# print()
#
# print((l + c) % 2)
# # [[0 1 0 1 0]
# #  [1 0 1 0 1]
# #  [0 1 0 1 0]
# #  [1 0 1 0 1]]

# ###################################

# # meshgrid
#
# a = np.array([-1.5, -1.0, -0.5, 0.0, 0.5])
#
# b = np.array([-20, -10, 0, 10, 20, 30])
#
# # pode-se usar linspace para gerar os parametros 'a' e 'b'
#
# l, c = np.meshgrid(a, b, indexing='ij')
#
# l, c = np.meshgrid(a, b)
#
# print(a)
# # [-1.5 -1.  -0.5  0.   0.5]
#
# print()
#
# print(b)
# # [-20 -10   0  10  20  30]
#
# print()
#
# print(l)
# # [[-1.5 -1.  -0.5  0.   0.5]
# #  [-1.5 -1.  -0.5  0.   0.5]
# #  [-1.5 -1.  -0.5  0.   0.5]
# #  [-1.5 -1.  -0.5  0.   0.5]
# #  [-1.5 -1.  -0.5  0.   0.5]
# #  [-1.5 -1.  -0.5  0.   0.5]]
#
# print()
#
# print(c)
# # [[-20 -20 -20 -20 -20]
# #  [-10 -10 -10 -10 -10]
# #  [  0   0   0   0   0]
# #  [ 10  10  10  10  10]
# #  [ 20  20  20  20  20]
# #  [ 30  30  30  30  30]]

# ###################################

# a = np.array([1, 2, 4, 8, 16, 8, 4, 2, 1])
#
# b = np.array([1, 2, 4, 8, 4, 2, 1])
#
# l, c = np.meshgrid(a, b, indexing='ij')
#
# x = l + c
#
# print(a)
# # [ 1  2  4  8 16  8  4  2  1]
#
# print()
#
# print(b)
# # [1 2 4 8 4 2 1]
#
# print()
#
# print(l)
# # [[ 1  1  1  1  1  1  1]
# #  [ 2  2  2  2  2  2  2]
# #  [ 4  4  4  4  4  4  4]
# #  [ 8  8  8  8  8  8  8]
# #  [16 16 16 16 16 16 16]
# #  [ 8  8  8  8  8  8  8]
# #  [ 4  4  4  4  4  4  4]
# #  [ 2  2  2  2  2  2  2]
# #  [ 1  1  1  1  1  1  1]]
#
# print()
#
# print(c)
# # [[1 2 4 8 4 2 1]
# #  [1 2 4 8 4 2 1]
# #  [1 2 4 8 4 2 1]
# #  [1 2 4 8 4 2 1]
# #  [1 2 4 8 4 2 1]
# #  [1 2 4 8 4 2 1]
# #  [1 2 4 8 4 2 1]
# #  [1 2 4 8 4 2 1]
# #  [1 2 4 8 4 2 1]]
#
# print()
#
# print(x)
# # [[ 2  3  5  9  5  3  2]
# #  [ 3  4  6 10  6  4  3]
# #  [ 5  6  8 12  8  6  5]
# #  [ 9 10 12 16 12 10  9]
# #  [17 18 20 24 20 18 17]
# #  [ 9 10 12 16 12 10  9]
# #  [ 5  6  8 12  8  6  5]
# #  [ 3  4  6 10  6  4  3]
# #  [ 2  3  5  9  5  3  2]]

# ###################################

# # nonzero
#
# a = np.array([0, 32, 0, 14, 0, 0, 83, 0, 110, 0, 0, 21, 0, 0, 0, 0])
#
# (b,) = a.nonzero()
#
# print()
#
# print(a)
# # [  0  32   0  14   0   0  83   0 110   0   0  21   0   0   0   0]
#
# print()
#
# print(b)
# # Indice do array que não é zero
# # [ 1  3  6  8 11]
#
# print()
#
# print(a[b])
# # [ 32  14  83 110  21]
#
# print()
#
# a = np.array([[0, 32, 0, 14], [0, 0, 83, 0], [110, 0, 0, 21], [0, 0, 0, 0]])
#
# (b, b2) = a.nonzero()
#
# print(a)
# # [[  0  32   0  14]
# #  [  0   0  83   0]
# #  [110   0   0  21]
# #  [  0   0   0   0]]
#
# print()
#
# print(b)
# # [0 0 1 2 2]
#
# print()
#
# print(b2)
# # [1 3 2 0 3]
#
# print()
#
# print(a[a.nonzero()])
# # [ 32  14  83 110  21]

# ###################################

# # tile
#
# a = np.array([1, 2, 3])
#
# print(a)
# # [1 2 3]
#
# print()
#
# print(np.tile(a, 5))
# # [1 2 3 1 2 3 1 2 3 1 2 3 1 2 3]
#
# print()
#
# print(np.tile(a, (2, 3)))
# # [[1 2 3 1 2 3 1 2 3]
# #  [1 2 3 1 2 3 1 2 3]]
#
# print()
#
# a = np.array([[1, 2], [3, 4]])
#
# print(a)
# # [[1 2]
# #  [3 4]]
#
# print()
#
# print(np.tile(a, 2))
# # [[1 2 1 2]
# #  [3 4 3 4]]
#
# print()
#
# print(np.tile(a, (2, 2)))
# # [[1 2 1 2]
# #  [3 4 3 4]
# #  [1 2 1 2]
# #  [3 4 3 4]]

# ###################################

# # repeat
#
# a = np.array([[1, 2], [3, 4]])
#
# print(a)
# # [[1 2]
# #  [3 4]]
#
# print()
#
# print(np.repeat(a, 3, axis=0))
# # [[1 2]
# #  [1 2]
# #  [1 2]
# #  [3 4]
# #  [3 4]
# #  [3 4]]
#
# print()
#
# print(np.repeat((np.repeat(a, 3, axis=0)), 3, axis=1))
# # [[1 1 1 2 2 2]
# #  [1 1 1 2 2 2]
# #  [1 1 1 2 2 2]
# #  [3 3 3 4 4 4]
# #  [3 3 3 4 4 4]
# #  [3 3 3 4 4 4]]

# ###################################

# # Falar do vstack, hstack e dstack
#
# # clip
#
# a = np.arange(20)
#
# print(a)
# # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
#
# print()
#
# print(np.clip(a, 1, 12))
# # [ 1  1  2  3  4  5  6  7  8  9 10 11 12 12 12 12 12 12 12 12]
#
# print()
#
# a = a.reshape(4, 5)
#
# print(a)
# # [[ 0  1  2  3  4]
# #  [ 5  6  7  8  9]
# #  [10 11 12 13 14]
# #  [15 16 17 18 19]]
#
# print()
#
# print(np.clip(a, 5, 10))
# # [[ 5  5  5  5  5]
# #  [ 5  6  7  8  9]
# #  [10 10 10 10 10]
# #  [10 10 10 10 10]]

# ###################################

# # sort
#
# a = np.array([8, 5, 3, 1, 7, 4, 9, 2])
#
# print(a)
# # [8 5 3 1 7 4 9 2]
#
# print()
#
# print(np.sort(a))
# # [1 2 3 4 5 7 8 9]

# ###################################

# a = np.array([[3, 15, 6, 12], [8, 10, 4, 14], [5, 1, 9, 16], [2, 7, 11, 13]])
#
# print(a)
# # [[ 3 15  6 12]
# #  [ 8 10  4 14]
# #  [ 5  1  9 16]
# #  [ 2  7 11 13]]
#
# print()
#
# print(np.sort(a))
# # [[ 3  6 12 15]
# #  [ 4  8 10 14]
# #  [ 1  5  9 16]
# #  [ 2  7 11 13]]
#
# print()
#
# print(np.sort(a, axis=0))
# # [[ 2  1  4 12]
# #  [ 3  7  6 13]
# #  [ 5 10  9 14]
# #  [ 8 15 11 16]]
#
# print()
#
# print(np.sort(a, axis=None))
# # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]

# ###################################

# # argsort
#
# a = np.array([8, 5, 3, 1, 6, 4, 7, 2])
#
# idx = np.arange(8)
#
# print(idx)
# # indices do array tamanho 8
# # [0 1 2 3 4 5 6 7]
#
# print()
#
# print(a)
# # [8 5 3 1 6 4 7 2]
#
# print()
#
# print(np.argsort(a))
# # Ordenado pelo valor mas apresentado pelo indice
# # [3 7 2 5 1 4 6 0]
#
# print()
#
# print(a[np.argsort(a)])
# # utiliza o resultado de argsort para mostrar os valores ordenados
# # [1 2 3 4 5 6 7 8]

##
