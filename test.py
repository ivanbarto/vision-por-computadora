import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('res/fachada_habitacion.png')
rows,cols,ch = img.shape

# pts1 = np.float32([[360,50],[2122,470],[2264, 1616],[328,1820]])
selected_pts = []

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
  global selected_pts, img

  if event == cv2.EVENT_LBUTTONDOWN:
    selected_pts.append([x, y])
    cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=3)


def select_points(image, ancho_marco, alto_marco):
  # relacion_aspecto = ancho_marco / alto_marco
  # # Los puntos se deben seleccionar de izquierda a derecha y de arriba hacia abajo
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
                  color=(0, 255, 0), thickness=1, fontScale=0.6, lineType=cv2.LINE_AA, text=str(ancho_marco) + "cm")
    if k == 27 or len(selected_pts) == 3:
      cv2.line(img, (selected_pts[0][0], selected_pts[0][1]), (selected_pts[2][0], selected_pts[2][1]),
               (0, 255, 0), thickness=1)
      cv2.putText(img=img, org=(selected_pts[2][0], int((selected_pts[2][1] + selected_pts[0][1]) / 2)),
                  fontFace=cv2.FONT_ITALIC,
                  color=(0, 255, 0), thickness=1, fontScale=0.6, lineType=cv2.LINE_AA, text=str(alto_marco) + "cm")
    if k == 27 or len(selected_pts) == 4:
      break

  cv2.destroyAllWindows()

  return np.array(selected_pts, dtype=np.float32)


pts1 = select_points(img, 76, 206)


ratio=1.77
cardH=math.sqrt((pts1[2][0]-pts1[1][0])*(pts1[2][0]-pts1[1][0])+(pts1[2][1]-pts1[1][1])*(pts1[2][1]-pts1[1][1]))
cardW=ratio*cardH;
pts2 = np.float32([[pts1[0][0],pts1[0][1]], [pts1[0][0]+cardW, pts1[0][1]], [pts1[0][0]+cardW, pts1[0][1]+cardH], [pts1[0][0], pts1[0][1]+cardH]])

M = cv2.getPerspectiveTransform(pts1,pts2)

offsetSize=500
transformed = np.zeros((int(cardW+offsetSize), int(cardH+offsetSize)), dtype=np.uint8);
dst = cv2.warpPerspective(img, M, transformed.shape)

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()




