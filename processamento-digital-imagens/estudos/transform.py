import numpy as np
import cv2
import time


def amost_down(a, n):
    return a[::n, ::n]


def amost_up(a, n):
    return np.repeat((np.repeat(a, n, axis=0)), n, axis=1)


def pause():
    time.sleep(0.1)

img = cv2.imread('files/dog2.jpg', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
n = 1
maxn = 30

while n < maxn:
    cv2.imshow('image', amost_up(amost_down(img, n), n))
    cv2.waitKey(5)
    n = n + 1
    pause()

img = cv2.imread('files/dog3.jpg', 0)
n = maxn

while n > 0:
    cv2.imshow('image', amost_up(amost_down(img, n), n))
    cv2.waitKey(5)
    n = n - 1
    pause()

cv2.imshow('image', img)
cv2.waitKey(0)
