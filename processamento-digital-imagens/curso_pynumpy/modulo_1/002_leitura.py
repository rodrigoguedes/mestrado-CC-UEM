import cv2
import numpy as np
import scipy.misc

# ###########################
# LEITURA DE UMA IMAGEM
# ###########################

f = cv2.imread('medias/cookies.tif', cv2.IMREAD_GRAYSCALE)

print('Tamanho de f: ', f.shape)
print('Tipo do pixel:', f.dtype)
print('Número total de pixels:', f.size)
print('Pixels:\n', f)
print('--------------------------------------')

# ###########################
# VISUALIZAR UMA IMAGEM
# ###########################

# cv2.imshow('Imagem cookies.tif', f)
# cv2.waitKey(0)


f_bin = f > 128
print('Tipo do pixel:', f_bin.dtype)
print(f_bin)

#b = cv2.threshold(f_bin, 12, 255, cv2.THRESH_BINARY)
#cv2.imshow('Imagem binária', f_bin)
#cv2.imshow('Imagem binária', np.from
#           fromstring(f_bin, np.uint8))

# rgb = scipy.misc.toimage(np_array)
# cv2.imwrite('bw_image.png', rgb)
# cv2.waitKey(0)
