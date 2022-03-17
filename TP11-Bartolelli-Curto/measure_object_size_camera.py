import cv2
from object_detector import *
import numpy as np
import requests
import imutils

# Carga de detector aruco
parameters = cv2.aruco.DetectorParameters_create()
# Cargamos un diccionario de 50 marcadores aruco de 5x5
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

# URL de cámara utilizada desde celular para transmitir imagen de video
url = "http://192.168.0.84:8080/shot.jpg"


# Carga de detector de objetos
detector = HomogeneousBgDetector()


while True:
    # Obtención de imagen desde la URL para decodificarla y mostrarla
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)


    # detectar esquinas del marcador Aruco
    corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    if corners:

        # Dibuja un polígono alrededor de la imagen
        int_corners = np.int0(corners)
        cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

        # Obtiene perímetro de Aruco
        aruco_perimeter = cv2.arcLength(corners[0], True)

        # Relacion (ratio) de pixeles por CM --> las open cv nos da el perimetro en pixeles
        pixel_cm_ratio = aruco_perimeter / 20

        contours = detector.detect_objects(img)

        # Dibujo de los contornos
        for cnt in contours:
            # Obtiene datos del rectangulo generado por el contorno
            rect = cv2.minAreaRect(cnt)
            (x, y), (w, h), angle = rect

            # Obtiene ancho y largo en cm de los objetos en función del ratio de pixel a cm
            object_width = w / pixel_cm_ratio
            object_height = h / pixel_cm_ratio

            # obtener las esquinas de la caja
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            #punto en el centro de la caja
            cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

            cv2.polylines(img, [box], True, (255, 0, 0), 2)

            cv2.putText(img, "Ancho {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(img, "Altura {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)



    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()