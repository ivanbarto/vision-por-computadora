import cv2

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frameRate = cap.get(cv2.CAP_PROP_FPS)


fourcc = cv2.VideoWriter_fourcc('M', 'P', 'E', 'G')

out = cv2.VideoWriter('res/output.avi', fourcc, frameRate, (int(float(width)), int(float(height))))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
out.release()
cv2.destroyAllWindows()
