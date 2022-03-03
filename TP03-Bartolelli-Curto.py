import sys
import cv2

# ---
# if len(sys.argv) > 1:
#     filename = sys.argv[1]
#
# else:
#     print(' Pass a filename as first argument ')
#     sys.exit(0)
#
# cap = cv2.VideoCapture(filename)
cap = cv2.VideoCapture('res/motogp_crash.mp4')
fps = int(float(cap.get(cv2.CAP_PROP_FPS)))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(fps) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
