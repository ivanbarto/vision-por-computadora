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
MILLISECOND = 1000
cap = cv2.VideoCapture('res/motogp_crash.mp4')
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

if int(major_ver) < 3:
    fps = int(float(cap.get(cv2.CAP_PROP_FPS)))
else:
    fps = int(float(cap.get(cv2.CAP_PROP_FPS)))

print(fps)

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(int(MILLISECOND/fps)) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
