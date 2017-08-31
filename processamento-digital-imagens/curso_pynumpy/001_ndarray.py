import numpy as np


# ###########################
# CRIAÇÃO NDARRAY
# ###########################

# Cria um array
a = np.array([2, 3, 4, -1, 2])

print('Dimensões: a.shape=', a.shape)
print('Tipos dos elemetros: a.type=', a.dtype)
print('Imprimindo o array completo:\n a=', a)
print('--------------------------------------')

# Matriz bidimensional
b = np.array( [ [1.5, 2.3, 5.2],
                [4.2, 5.6, 4.4] ] )
print('Um array bidimensional, dimensões:(b.shape=', b.shape)
print('Tipo dos elementos: b.type', b.dtype)
print('Número de colunas:', b.shape[-1])
print('Número de linhas:', b.shape[-2])
print('Elementos, b=\n', b)
print('--------------------------------------')

# ###########################
# MANIPULAÇÃO DE ARRAYS
# ###########################

# Cria um Array de Zeros com 2 linhas e 4 colunas -> BIDIMENSIONAL
d = np.zeros( (2,4) )
print('Array de 0s: \n', d)
print('--------------------------------------')

# Cria um Array de 3 dimensões de uns inteiro - com 2 linhas e 5 colunas -> TRIDMENSIONAL
d = np.ones( (3, 2, 5), dtype='int16' )
print('\n\nArray de 1s: \n', d)
print('--------------------------------------')

# Cria um array de boleanos com 2 linhas e 3 colunas
d = np.empty( (2, 3), 'bool' )
print('Array não inicializado (vazio):\n', d)
print('--------------------------------------')

# ################################
# ARRAYS COM VALORES SEQUENCIAIS
# ################################

# Gera um sequência apartir de valor inicial e final
print('np.arange( 10) = ', np.arange( 10))
print('np.arange( 3, 8) = ', np.arange( 3,8))
print('np.arange( 0, 2, 0.5) = ', np.arange( 0, 2, 0.5))

# Gera uma sequência com valor inicial (1), final (2) e número de elemetros
print('np.arange( 0, 2, 5) = ', np.linspace( 0, 2, 5))
print('np.arange( 0, 2, 5) = ', np.linspace( 0, 10, 4))
print('--------------------------------------')



