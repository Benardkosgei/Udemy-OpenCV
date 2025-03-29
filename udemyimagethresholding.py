import cv2
import numpy as np

pic = cv2.imread('vann.jpg',0)
threshold_value = 200
(T_value,binary_threshold) = cv2.threshold(pic,threshold_value,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Binary Threshold', binary_threshold)
cv2.waitKey(0)

cv2.destroyAllWindows