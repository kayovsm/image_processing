import cv2
import numpy as np

# Variáveis globais
drawing = False
ix, iy = -1, -1
color = (0, 255, 0)
img = None

cap = cv2.VideoCapture('atv/atv02/video/video_atv02.mp4')

# Função de retorno de chamada do mouse
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, color, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), color, -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), color, -1)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

# Crie o objeto VideoWriter uma vez fora do loop
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 1.0, (640,480))

# Loop para ler cada quadro
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Crie uma cópia do quadro para desenhar
        img = frame.copy()

        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF

        if k == ord('q'):
            break
        elif k == ord('c'):
            # Mude a cor
            color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
        elif k == ord(' '):
            # Limpe a tela
            img = np.zeros_like(frame)

        # Escreva o quadro de volta no vídeo de saída
        out.write(img)

    else:
        break

# Libere tudo se o trabalho estiver terminado
cap.release()
out.release()
cv2.destroyAllWindows()