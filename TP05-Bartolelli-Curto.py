import cv2
import numpy as np

cropping = False
ix, iy = -1, -1
global crop

def select_rectangle(event, x, y, flags, param):
    global ix, iy, cropping,crop

    if event == cv2.EVENT_LBUTTONDOWN: #evento que indica que el boton izq del mouse es presionado
        ix, iy = x, y
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        crop = img[iy:y, ix:x]
        cv2.destroyAllWindows()
        cv2.imshow("recorte", crop)

img = cv2.imread("res/goal.png")
cv2.namedWindow('image')
cv2.imshow('image',img)
cv2.setMouseCallback('image',select_rectangle)

while(True):
    k = cv2.waitKey(1) & 0xFF
    if k == ord ('g'):
        cv2.imwrite("res/recorte_goal.png", crop)
    if k == ord ('r'):
        cv2.destroyAllWindows()
        cv2.imshow('image',img)
        cv2.setMouseCallback('image', select_rectangle)
    elif k == ord('q'):
        break

cv2.destroyAllWindows()

