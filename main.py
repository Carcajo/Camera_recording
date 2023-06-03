import cv2

print('Запись началась, нажмите q чтобы остановить')


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 24)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) 


codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Запись.avi', codec, 25.0, (1280, 720))


while True:
    ret, frame = cap.read()
    cv2.imshow('Web-camera', frame)
    out.write(frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()