# import necessary libraries

import cv2
import numpy as np

img = cv2.imread("res/bombones.jpeg")
selected_pts = []

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global selected_pts, img

    if event == cv2.EVENT_LBUTTONDOWN:
        selected_pts.append([x, y])
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)


def select_points(image):
    # Los puntos se deben seleccionar de izquierda a derecha y de arriba hacia abajo
    global selected_pts

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

    while True:
        cv2.imshow("image", image)
        k = cv2.waitKey(1)

        # Se evalua que se marquen 4 puntos
        if k == 27 or len(selected_pts) == 4:
            break

    cv2.destroyAllWindows()

    return np.array(selected_pts, dtype=np.float32)

src_pts = select_points(img)


while True:

    # Dimensiones de destino
    dst_dimension = np.float32([[0, 0], [800, 0], [0, 600], [800, 600]])

    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(src_pts, dst_dimension)
    result = cv2.warpPerspective(img, matrix, (800, 600))
    # Wrap the transformed image

    cv2.imshow('perspective transform', result)  # Transformed Capture

    if cv2.waitKey(24) == 27:
        break

cv2.destroyAllWindows()