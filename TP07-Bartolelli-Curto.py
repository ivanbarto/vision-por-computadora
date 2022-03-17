import cv2
import numpy as np

pi = 22 / 7
rad_conversor = pi / 180

def scaled_euclidean_transformation(img, angle, tx, ty, s=1.0):
    (h, w) = (img.shape[0], img.shape[1])
    transformation_matrix = np.float32([[np.cos(angle * rad_conversor) * s, np.sin(angle * rad_conversor)* s, tx],
                                        [-np.sin(angle * rad_conversor)* s, np.cos(angle * rad_conversor)* s, ty]])
    shifted = cv2.warpAffine(img, transformation_matrix, (w, h))

    return shifted


img = cv2.imread("res/hondaVFR.png")
cv2.imwrite("res/trans_euclideana_escalada.png", scaled_euclidean_transformation(img, 12, 120, -120, 1.2))
transformed_img = cv2.imread("res/trans_euclideana_escalada.png")
cv2.imshow("transformacion euclideana", transformed_img)
cv2.waitKey(0)
