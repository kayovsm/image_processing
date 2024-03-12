import cv2
import numpy as np

# Variáveis globais
drawing = False
ix, iy = -1, -1
color = (255, 255, 0)
img = None

cap = cv2.VideoCapture('atv/atv03/video/video_atv03.mp4')

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# novo video
out = cv2.VideoWriter('rabiscado.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# função de desenhar na tela
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, color, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (ix, iy), (x, y), color, 5)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (ix, iy), (x, y), color, 5)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

# ler cada quadro e salvar a alteração
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       
        img = frame.copy()

        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF

        if k == ord('q'):
            break
        elif k == ord('c'):
            color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
        elif k == ord(' '): 
            img = np.zeros_like(frame)
        elif k == ord('w'):
            cv2.imwrite('frame.jpg', img)

        out.write(img)
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()