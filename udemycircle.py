import cv2
import numpy as np

# Create a black image
image = np.zeros((500, 500, 3), dtype="uint8")

# Define center and radius of the circle
center = (250, 250)
radius = 100

# Define color (BGR format) and thickness (-1 for filled circle)
color = (0, 255, 0)  # Green color
thickness = 2

# Draw the circle
cv2.circle(image, center, radius, color, thickness)

# Display the image
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()