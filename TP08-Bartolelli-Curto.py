from __future__ import print_function
import cv2 as cv2
import numpy as np

background_img = cv2.imread("res/sportivo.png")
foreground_img = cv2.imread("res/publicidad.png")

selected_pts = []


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global selected_pts, background_img

    if event == cv2.EVENT_LBUTTONDOWN:
        selected_pts.append([x, y])
        cv2.circle(background_img, (x, y), 1, (255, 0, 0), thickness=-1)


def select_points(image, points_num):
    global selected_pts
    selected_pts = []

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

    while True:
        cv2.imshow("image", image)
        k = cv2.waitKey(1)

        if k == 27 or len(selected_pts) == points_num:
            break

    cv2.destroyAllWindows()

    return np.array(selected_pts, dtype=np.float32)


src_pts = select_points(background_img, 3)

print(src_pts)

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

srcTri = np.array([[0, 0], [background_img.shape[1] - 1, 0], [0, background_img.shape[0] - 1]]).astype(np.float32)
dstTri = src_pts.astype(np.float32)

warp_mat = cv2.getAffineTransform(srcTri, dstTri)
warp_dst = cv2.warpAffine(foreground_img, warp_mat, (background_img.shape[1], background_img.shape[0]))

# cv2.imshow('Source image', background_img)
# cv2.imshow('Warp', warp_dst)

imgadd = cv2.add(background_img, warp_dst)
# cv2.imshow('imgadd', imgadd)
cv2.destroyAllWindows()

while (1):
    # cv2.imshow("image", background_img)
    cv2.imshow('resultado', imgadd)
    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()
