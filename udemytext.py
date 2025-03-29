import numpy as np
import cv2

pic = np.zeros((800,1200,3), dtype='uint8')
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, 'BROTHER BENARD!', (100,100), font, 3, (255,255,255), 4, cv2.LINE_8)

cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
# The cv2.putText() function is used to write text on an image.