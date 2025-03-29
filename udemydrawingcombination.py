import numpy as np
import cv2

pic =np.zeros((800,1200,3), dtype='uint8')
cv2.rectangle(pic,(20,20),(1000,300),(123, 200,98),1, lineType=8, shift=0)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, 'DRAWING COMBINATION!', (100,100), font, 3, (255,255,255), 4, cv2.LINE_8)
cv2.circle(pic,(447,63), 63, (0,0,255),1)
cv2.line(pic, (350, 350), (500, 350), (0, 0, 255))
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
# The cv2.rectangle() function is used to draw a rectangle on an image.