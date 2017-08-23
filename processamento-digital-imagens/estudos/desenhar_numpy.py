import cv2
import numpy

# OpenCV
# Lê imagem em tons de cinza
imageGrayScale = cv2.imread('files/telecaster_guedes.jpg', cv2.IMREAD_GRAYSCALE)

print(imageGrayScale)
print(imageGrayScale[0])
print(len(imageGrayScale))
print(len(imageGrayScale[0]))

# for row in range(200, 220):
#     for column in range(50, 100):
#         image[row][column] = [0, 255, 255]

for row in range(200, 220):
    for column in range(50, 100):
        imageGrayScale[row][column] = 100


cv2.imwrite('files/telecaster_guedes_risco_cinza.jpg', imageGrayScale)

##################################

imageColor = cv2.imread('files/telecaster_guedes.jpg')

print(imageColor)
print(imageColor[0])
print(len(imageColor))
print(len(imageColor[0]))

for row in range(200, 220):
    for column in range(50, 100):
        imageColor[row][column] = [0, 255, 255]  # RGB

cv2.imwrite('files/telecaster_guedes_risco_colorido.jpg', imageColor)
