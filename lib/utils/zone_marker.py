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

zoneIn0 = np.array([
    [250, 169],
    [229, 214],
    [168, 157],
    [198, 125]
])

zoneOut0 = np.array([
    [271, 146],
    [287, 98],
    [218, 81],
    [203, 121]
])

zoneIn1 = np.array([
    [274, 314],
    [322, 356],
    [225, 379],
    [197, 347]
])

zoneOut1 = np.array([
    [230, 225],
    [259, 268],
    [213, 304],
    [187, 272]
])

zoneIn2 = np.array([
    [603, 196],
    [542, 264],
    [626, 309],
    [657, 261]

])

zoneOut2 = np.array([
    [497, 291],
    [473, 345],
    [571, 362],
    [584, 323]
])

zoneIn3 = np.array([
    [572, 97],
    [553, 74],
    [449, 89],
    [494, 147]
])

zoneOut3 = np.array([
    [505, 161],
    [539, 215],
    [587, 155],
    [558, 114]
])

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
