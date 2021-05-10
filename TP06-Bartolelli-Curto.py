import cv2
import numpy as np

pi = 22 / 7
rad_conversor = pi / 180


def euclidean_transformation(img, angle, tx, ty):
    (h, w) = (img.shape[0], img.shape[1])
    transformation_matrix = np.float32([[np.cos(angle*rad_conversor), np.sin(angle*rad_conversor), tx],
                                        [-np.sin(angle*rad_conversor), np.cos(angle*rad_conversor), ty]])
    shifted = cv2.warpAffine(img, transformation_matrix, (w, h))

    return shifted


img = cv2.imread("res/hondaVFR.png")
cv2.imwrite("res/trans_euclideana.png", euclidean_transformation(img, 10, 0, 0))
transformed_img = cv2.imread("res/trans_euclideana.png")
cv2.imshow("transformacion euclideana", transformed_img)
cv2.waitKey(0)
