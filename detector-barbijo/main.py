import cv2
import serial
import time
import mediapipe as mp

# inicializamos puerto serie
serial_port = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

# inicializamos el detector facial
mp_face_detection = mp.solutions.face_detection

LABELS = ["Autorizado", "NO AUTORIZADO"]

# Leer el modelo
face_mask = cv2.face.LBPHFaceRecognizer_create()
face_mask.read("face_mask_model.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_face_detection.FaceDetection(
        min_detection_confidence=0.5) as face_detection:
    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame = cv2.flip(frame, 1)

        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # se procesa la imagen de la cara y se devuelva la posicion de la cara detectada
        results = face_detection.process(frame_rgb)

        if results.detections is not None:
            for detection in results.detections:
                xmin = int(detection.location_data.relative_bounding_box.xmin * width)
                ymin = int(detection.location_data.relative_bounding_box.ymin * height)
                w = int(detection.location_data.relative_bounding_box.width * width)
                h = int(detection.location_data.relative_bounding_box.height * height)
                if xmin < 0 and ymin < 0:
                    continue

                face_image = frame[ymin: ymin + h, xmin: xmin + w]
                face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

                # se recorta la cara a partir de su posicion
                face_image = cv2.resize(face_image, (72, 72), interpolation=cv2.INTER_CUBIC)

                # se le pasa la cara para reconocer, en escala de grises porque el algoritmo trabaja así
                result = face_mask.predict(face_image)
                # como resultado, obtenemos un valor de confianza (1) y la etiqueta asociada (0)

                print(result[1])
                if result[1] < 150:
                    color = (0, 255, 0) if LABELS[result[0]] == "Autorizado" else (0, 0, 255)

                    # si está autorizada, mandamos una 'p' a través del puerto serie para prender el led verde
                    # de lo contrario, mandamos una 'n' para prender el led rojo
                    if LABELS[result[0]] == "Autorizado":
                        serial_port.write(b'p')
                    else:
                        serial_port.write(b'n')

                    #agregamos la etiqueta y dibujamos un rectángulo en la cara
                    cv2.putText(frame, "{}".format(LABELS[result[0]]), (xmin, ymin - 15), 2, 1, color, 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), color, 2)

        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1)
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
serial_port.close()
