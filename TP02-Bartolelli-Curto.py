import cv2

img = cv2.imread("res/hoja.png", 0)
ancho, alto = img.shape

for col in range(0, ancho):
    for row in range(0, alto):
        if img[col, row] < 230:
            img[col, row] = 0

cv2.imwrite("res/imagen_filtrada.png", img)
cv2.imshow("image filtrada", img)
cv2.waitKey(0)
