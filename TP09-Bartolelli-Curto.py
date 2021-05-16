# import necessary libraries

import cv2
import numpy as np

# Turn on Laptop's webcam
cap = cv2.VideoCapture(0)

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global selected_pts, background_img

    if event == cv2.EVENT_LBUTTONDOWN:
        selected_pts.append([x, y])
        cv2.circle(background_img, (x, y), 1, (255, 0, 0), thickness=-1)


def select_points(image, points_num):
    global selected_pts

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

    while True:
        cv2.imshow("image", image)
        k = cv2.waitKey(1)

        if k == 27 or len(selected_pts) == points_num:
            break

    cv2.destroyAllWindows()

    return np.array(selected_pts, dtype=np.float32)

src_pts = select_points(background_img, 4)


while True:

    ret, frame = cap.read()

    # Locate points of the documents or object which you want to transform
    pts1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])
    pts2 = np.float32([[0, 0], [400, 0], [0, 640], [400, 640]])

    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (500, 600))
    # Wrap the transformed image

    cv2.imshow('frame', frame)  # Inital Capture
    cv2.imshow('frame1', result)  # Transformed Capture

    if cv2.waitKey(24) == 27:
        break

cap.release()
cv2.destroyAllWindows()