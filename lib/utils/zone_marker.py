import cv2
import numpy as np
import supervision as sv

# Load and display the frame
# source_video_path = "data/traffic1.mov"
source_video_path = "data/traffic2.mp4"
frame_generator = sv.get_video_frames_generator(source_path=source_video_path)
frame = next(frame_generator, None)


def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"[{x}, {y}]")


# # Define the polygon
# cv2.imshow("Frame", frame)
# cv2.setMouseCallback("Frame", get_coordinates)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # View the polygon

zoneIn0 = np.array([[77, 65], [56, 99], [160, 150], [186, 115]])

zoneOut0 = np.array([[137, 90], [159, 57], [245, 91], [233, 134]])

zoneIn1 = np.array([[192, 398], [168, 366], [259, 320], [292, 358]])

zoneOut1 = np.array([[63, 337], [98, 379], [170, 336], [118, 289]])

zoneIn2 = np.array([[663, 325], [674, 271], [609, 225], [573, 282]])

zoneOut2 = np.array([[634, 343], [614, 383], [532, 352], [553, 312]])

zoneIn3 = np.array([[601, 77], [578, 60], [450, 87], [489, 141]])

zoneOut3 = np.array([[692, 95], [639, 65], [556, 119], [609, 174]])

cv2.polylines(frame, [
    zoneIn0,
    zoneOut0,
    zoneIn1,
    zoneOut1,
    zoneIn2,
    zoneOut2,
    zoneIn3,
    zoneOut3,
], isClosed=True, color=(0, 255, 0), thickness=2)
cv2.imshow("Zones", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
