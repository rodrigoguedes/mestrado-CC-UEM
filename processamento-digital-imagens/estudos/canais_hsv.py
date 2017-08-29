import cv2

img = cv2.imread('files/telecaster_guedes_original.jpg')

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_img)

cv2.imwrite('files/telecaster_hsv_canal_hue.jpg', h)

cv2.imwrite('files/telecaster_hsv_canal_saturation.jpg', s)

cv2.imwrite('files/telecaster_hsv_canal_value.jpg', v)
