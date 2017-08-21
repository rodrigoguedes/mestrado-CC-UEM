import cv2
import numpy
import numpy as np
import matplotlib.image as mpimg

# OpenCV
# Lê imagem em tons de cinza
image = cv2.imread('files/telecaster_guedes.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('files/telecaster_guedes_novo.jpg', image)

# transforma a imagem em array
grayImage = numpy.array(bytearray(image))
print(grayImage.shape)
print(grayImage)

#mpimg.imread('files/telecaster_guedes.jpg')