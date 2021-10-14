import cv2


class HomogeneousBgDetector():
    def __init__(self):
        pass

    def detect_objects(self, frame):
        # Conversión a escala de grises para facilitar el análisis
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Segmenta la imagen y calcula el valor del umbral para un cada segmento de pixeles.
        # https://www.pyimagesearch.com/2021/05/12/adaptive-thresholding-with-opencv-cv2-adaptivethreshold/
        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)

        # A partir de la máscara (img) generada devuelve una lista con todos los bordes (contornos) en la misma
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        objects_contours = []

        for cnt in contours:
            # Calcula el área a partir de los vértices del contorno
            area = cv2.contourArea(cnt)
            # Establece un filtro para tomar bordes de objetos que tengan un área considerable (mayor a 2000 pixeles)
            if area > 2000:
                # Si el área supera este tamaño, agrega ese contorno a la lista de contornos
                objects_contours.append(cnt)

        return objects_contours