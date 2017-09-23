import cv2
import numpy as np

from collections import Counter

def encoder(Cr, Cb, b, c):

    cv2.imwrite('saida_Cr.jpg', Cr)
    cv2.imwrite('saida_Cb.jpg', Cb)

    subCr = Cr[:: int(2 if c == 0 else 1), ::int(4/b)]
    subCb = Cb[:: int(2 if c == 0 else 1), ::int(4/b)]

    cv2.imwrite('saida_subCr.jpg', subCr)
    cv2.imwrite('saida_subCb.jpg', subCb)

    subCrCb = np.zeros((subCr.shape[0], subCr.shape[1], 3))
    subCrCb[:,:,1] = subCr
    subCrCb[:,:,2] = subCb

    cv2.imwrite('saida_subCrCb.jpg', subCrCb)

    return subCrCb;

def decoder(Cr, Cb, b, c):

    upSampCr = np.repeat((np.repeat(Cr, int(2 if c == 0 else 1), axis=0)), int(4/b), axis=1);
    upSampCb = np.repeat((np.repeat(Cb, int(2 if c == 0 else 1), axis=0)), int(4/b), axis=1);

    cv2.imwrite('saida_upCr.jpg', upSampCr)
    cv2.imwrite('saida_upCb.jpg', upSampCb)

    upCrCb = np.zeros((upSampCr.shape[0], upSampCr.shape[1], 3))
    upCrCb[:, :, 1] = upSampCr
    upCrCb[:, :, 2] = upSampCb

    cv2.imwrite('saida_upCrCb.jpg', upCrCb)

    return upCrCb

# imRGB = cv2.imread('Barns_grand_tetons.jpg')
imRGB = cv2.imread('lenna.tif')

total_pixels = imRGB.shape[0] * imRGB.shape[0]
print('Total de Pixels:')
print(total_pixels)
#print(imRGB[100, 100])

unique_pixels = np.vstack({tuple(r) for r in imRGB.reshape(-1,3)})
print(unique_pixels[1])

# colors = [rgb for _, rgb in img.getcolors(width * height)]

imgYCrCb = cv2.cvtColor(imRGB, cv2.COLOR_BGR2YCrCb)

#notation a:b:c
b = 1
c = 0

Y = imgYCrCb[:,:,0]
Cr = imgYCrCb[:,:,1]
Cb = imgYCrCb[:,:,2]

subCrCb = encoder(Cr, Cb, b, c)

upSampCrCb = decoder(subCrCb[:,:,1], subCrCb[:,:,2], b, c)

reconstruct_YCrCb = imgYCrCb
reconstruct_YCrCb[:,:,1] = upSampCrCb[:len(imgYCrCb),:, 1]
reconstruct_YCrCb[:,:,2] = upSampCrCb[:len(imgYCrCb),:, 2]

reconstruct_RGB = cv2.cvtColor(reconstruct_YCrCb, cv2.COLOR_YCrCb2BGR)

cv2.imwrite('saida.jpg', reconstruct_RGB)
