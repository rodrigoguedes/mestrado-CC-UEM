#https://gist.github.com/shunk031/b2b7a4f69ca0e889beaf4209e244d1aa
#https://en.wikipedia.org/wiki/Otsu's_method
#https://www.ppgia.pucpr.br/~facon/Binarizacao/LimiarOstuNovo3.PDF

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Carregar Imagem
imRGB = cv2.imread('dvd.JPG')

#Imagem em tons de Cinza
imgHSV = cv2.cvtColor(imRGB, cv2.COLOR_RGB2HSV)

imgH = imgHSV[:, :, 0]
imgS = imgHSV[:, :, 1]
imgV = imgHSV[:, :, 2]

cv2.imwrite('saida_H.jpg', imgH);
cv2.imwrite('saida_S.jpg', imgS);
cv2.imwrite('saida_V.jpg', imgV);

plt.hist(imgV.ravel(), 256, [0, 256])
plt.title("Histograma Imagem Tons de Cinza")
plt.savefig('histograma.png')

ret3,th3 = cv2.threshold(imgV,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret2,th2 = cv2.threshold(imgV,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imwrite('saida_Otsu.jpg', th2);
plt.hist(th2.ravel(), 256, [0, 256])
plt.title("Histograma Otsu")
plt.savefig('histograma_otsu.png')


# ###################################

#http://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html
#Histograms Equalization in OpenCV
# equ = cv2.equalizeHist(imgV)
# res = np.hstack((imgV,equ))
# cv2.imwrite('saida_V3.jpg', res)

#CLAHE (Contrast Limited Adaptive Histogram Equalization)
# clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
# imgV2 = clahe.apply(imgV)
# cv2.imwrite('saida_V2.jpg', imgV2)

img = cv2.bitwise_and(imgV, imgV, mask = th2)
cv2.imwrite('saida_Mascara.jpg', img);

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max() / cdf.max()

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())

cdf = np.ma.filled(cdf_m, 0).astype('uint8')

img2 = cdf[img];

cv2.imwrite('saida_V4.jpg', img2)

#cv2.copy

#img3  = cv2.bitwise_and(img2, img2, mask = th2)
#img3  = cv2.subtract(img2, img, mask = th2)
#imgcop = imgV.copy()
#imgcop = img2[th2]
#print(np.ma.getmask(th2))

#cv2.imwrite('saida_resultado_cinza2.jpg', imgcop);

#masked_image = cv2.bitwise_and(img2, th2)
# masked_image = img2.crop(th2)
# cv2.imwrite('saida_resultado_cinza2.jpg', masked_image);

# outside = np.ma.masked_where(th2, img2)
# average_color = outside.mean()
# img2[th2] = average_color
#
# bytemask = np.asarray(th2*255, dtype=np.uint8)
# inpainted = cv2.inpaint(img2, bytemask, inpaintRadius=10, flags=cv2.INPAINT_TELEA)
#
# cv2.imwrite('saida_V5.jpg', inpainted)

imgFundo = np.where(th2, 255, imgV)
cv2.imwrite('saida_fundo.jpg', imgFundo)
imgObjeto = np.where(th3, 255, img2)
cv2.imwrite('saida_objeto.jpg', imgObjeto)

#img2 = cv2.bitwise_and(imgObjeto, imgFundo, mask = th3)
#img2 = cv2.bitwise_not(imgObjeto, imgFundo)
#img2 = 0.5 * imgFundo + 0.5 * imgObjeto
#img2 = imgFundo + imgObjeto
#img2 = cv2.addWeighted(imgFundo,0.5,imgObjeto,0.5,0)

#imgFundo[th2[:] == 0, ...] = imgObjeto[th2[:] == 0, ...];

rows, cols = imgFundo.shape
roi = imgV[0:rows, 0:cols]
mask_inv = cv2.bitwise_not(th2)
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv2.bitwise_and(imgObjeto,imgObjeto,mask = th2)
dst = cv2.add(img1_bg,img2_fg)
imgV[0:rows, 0:cols ] = dst

cv2.imwrite('saida_V5.jpg', imgV)


imgHSV[:, :, 2] = imgV

imgOriginal = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2RGB)
cv2.imwrite('saida_Original.png', imgOriginal)

# ###################################

# FUNCIONANDO!!!!!!!!
# img2 = np.where(th3, 255, img2)
# cv2.imwrite('saida_V5.jpg', img2)
#
# imgHSV[:, :, 2] = img2
#
# imgOriginal = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2RGB)
# cv2.imwrite('saida_Original.png', imgOriginal)



#
# img2=imgV[:,:,0].copy()
# n,m=img2.shape
# bag=sort(img2.reshape([1,n*m]))
# plt.hist(img2)
# plt.savefig('histograma2.png')
##plt.hist(img2)


# result = imgV.copy()
# result = imgV.copy()
# result[..., 0] = np.clip(result[..., 0], 0, 11)
# cv2.imwrite('saida_limiarizada.jpg', result);

# result = imgV.copy()
# idx = result[:,:,0] > 10
# result[idx,0] = 10
# cv2.imwrite('saida_limiarizada.jpg', result);

#Binarizar

#Gerar o histograma

#Pegar a área em tons de cinza e clarear

#Salvar o resultado em tons de cinza

#temtar voltar a imagem colorida