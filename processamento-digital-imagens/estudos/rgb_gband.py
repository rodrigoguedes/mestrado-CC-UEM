import cv2

image_green = cv2.imread('files/telecaster_guedes.jpg')

#image_green[:, :, 0] = 0
#image_green[:, :, 2] = 0
image_green[:, :, 1] = 255

cv2.imwrite('files/telecaster_green.jpg', image_green)

##############################################

image_blue = cv2.imread('files/telecaster_guedes.jpg')

#image_blue[:, :, 0] = 255
image_green[:, :, 2] = 0

cv2.imwrite('files/telecaster_blue.jpg', image_blue)

##############################################

image_red = cv2.imread('files/telecaster_guedes.jpg')

#image_red[:, :, 0] = 0
#image_red[:, :, 1] = 0
image_red[:, :, 2] = 255

print(image_red)

cv2.imwrite('files/telecaster_red.jpg', image_red)