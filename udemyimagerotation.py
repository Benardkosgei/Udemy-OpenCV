import  cv2
import numpy as np

pic = cv2.imread('vann.jpg')
cols = pic.shape[1]
rows = pic.shape[0]
center = (cols/2, rows/2)
angle = 90
M = cv2.getRotationMatrix2D(center, angle, 0.7)
rotated = cv2.warpAffine(pic, M, (cols, rows))
cv2.imshow('Rotated Image', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()