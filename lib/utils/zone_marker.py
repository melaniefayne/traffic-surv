import cv2
import numpy as np

# Load and display the frame
frame = cv2.imread("../assets/cleanFrame.png")

# Define the polygon
# cv2.imshow("Frame", frame)
# cv2.setMouseCallback("Frame", get_coordinates)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# View the polygon
polygon = np.array([[1805, 583], [1792, 835], [2188, 838], [2179, 625]])
cv2.polylines(frame, [polygon], isClosed=True, color=(0, 255, 0), thickness=2)
cv2.imshow("Zones", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
