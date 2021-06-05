# 206 DE ALTO
# 76 DE ANCHO
import cv2
import numpy as np

img = cv2.imread("res/fachada_habitacion.png")
selected_pts = []
relacion_aspecto = 0


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global selected_pts, img

    if event == cv2.EVENT_LBUTTONDOWN:
        selected_pts.append([x, y])
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=3)


def select_points(image, ancho_marco, alto_marco):
    relacion_aspecto = ancho_marco/alto_marco
    # Los puntos se deben seleccionar de izquierda a derecha y de arriba hacia abajo
    global selected_pts

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

    while True:
        cv2.imshow("image", image)
        k = cv2.waitKey(1)

        # Se evalua que se marquen 4 puntos
        if k == 27 or len(selected_pts) == 2:
            cv2.line(img, (selected_pts[0][0], selected_pts[0][1]), (selected_pts[1][0], selected_pts[1][1]),
                     (0, 255, 0), thickness=1)
            cv2.putText(img=img, org=(selected_pts[0][0], selected_pts[0][1]), fontFace=cv2.FONT_ITALIC,
                        color=(0, 255, 0), thickness=1, fontScale=0.6, lineType=cv2.LINE_AA, text=str(ancho_marco)+"cm")
        if k == 27 or len(selected_pts) == 3:
            cv2.line(img, (selected_pts[0][0], selected_pts[0][1]), (selected_pts[2][0], selected_pts[2][1]),
                     (0, 255, 0), thickness=1)
            cv2.putText(img=img, org=(selected_pts[2][0], int((selected_pts[2][1] + selected_pts[0][1])/2)), fontFace=cv2.FONT_ITALIC,
                        color=(0, 255, 0), thickness=1, fontScale=0.6, lineType=cv2.LINE_AA, text=str(alto_marco)+"cm")
        if k == 27 or len(selected_pts) == 4:
            break

    cv2.destroyAllWindows()

    return np.array(selected_pts, dtype=np.float32)


src_pts = select_points(img, 76, 206) #pasar ancho y alto


while True:

    # Dimensiones de destino
    dst_dimension = np.float32([[0, 0], [img.shape[1], 0], [0, img.shape[0]], [img.shape[1], img.shape[0]]])

    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(src_pts, dst_dimension)
    result = cv2.warpPerspective(img, matrix, (img.shape[1], img.shape[0]))
    # Wrap the transformed image

    cv2.imshow('perspective transform', result)  # Transformed Capture

    if cv2.waitKey(24) == 27:
        break


cv2.destroyAllWindows()
