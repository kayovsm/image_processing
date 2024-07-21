import cv2

cap = cv2.VideoCapture('atv/video/video_atv12.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Não foi possível ler o vídeo ou fim do vídeo.")
        break

    # convertendo para a escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # aplicando o filtro de canny
    result = cv2.Canny(gray, 100, 300)

    cv2.imshow('RESULTADO', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()