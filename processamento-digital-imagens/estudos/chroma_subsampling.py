# http://fabiorogeriosj.com.br/2016/10/26/Trabalho-aplicacao-de-chroma-subsampling/

import numpy as np
import cv2


def quantiz(arr, n):
    print('---------------')
    print(arr)
    nmin = np.min(arr)
    nmax = np.max(arr)
    print('nmin---------------')
    print(nmin)
    print('nmax---------------')
    print(nmax)
    b = np.float32(arr) / (nmax - nmin)
    print('b---------------')
    print(b)
    print('=============')
    c = np.round(b * (n - 1))
    d = np.round(c / (n - 1) * (nmax - nmin))
    d = d + nmin
    return d


def alteraCor(arr, n):
    b = quantiz(arr, n)
    b = np.uint8(b)
    return b


img = cv2.imread('files/telecaster_guedes.jpg')

#print(img)

cv2.imshow("in", img)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_img)
n = 18
hNovo = alteraCor(h, n)
sNovo = alteraCor(s, n)


imgFinal = np.dstack((np.dstack((hNovo, sNovo)), v))

out = cv2.cvtColor(imgFinal, cv2.COLOR_HSV2BGR)
cv2.imshow("out", out)

cv2.imwrite('files/telecaster_guedes_compactado.jpg', out)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
