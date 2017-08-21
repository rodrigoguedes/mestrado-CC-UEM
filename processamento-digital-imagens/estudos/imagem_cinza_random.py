import cv2
import numpy
import os

randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('files/cinza_random.png', grayImage)
