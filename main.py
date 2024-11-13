import cv2
import numpy as np
from typing import Literal

width, height = (1280, 720)         # Tamanho da tela (HD)
preview_name = 'Cards Detector'     # Nome da tela

top_left = (width // 2 - 150, height // 2 - 225)
bottom_right = (width // 2 + 150, height // 2 + 225)
text_position = (width // 2 - 150, height // 2 - 250)
result_position = (width // 2, height // 2 + 250)

# Retângulo com o tamanho da área que queremos computar
rectagle_mask = np.zeros((height, width, 3), dtype=np.uint8)
rectagle_mask = cv2.rectangle(rectagle_mask, top_left, bottom_right, (255, 255, 255), -1)

# Limiar da média de vermelho na imagem
RED_THRESHOLD = 6.0

# Filtro HSV ajustado para vermelho
RED_FILTER = {
    'min': {
        'hue': 100,
        'saturation': 21,
        'value': 62 
    },
    'max': {
        'hue': 179,
        'saturation': 211,
        'value': 255
    }
}

# Configuração do Simple Blob Detector
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 700
params.maxArea = 2050
params.filterByCircularity = True
params.minCircularity = 0.3
params.filterByConvexity = False
params.filterByInertia = False
detector = cv2.SimpleBlobDetector_create(params)

def detect_card_color(frame: cv2.typing.MatLike) -> Literal['red', 'black']:
    '''
    Returns color red or black in the given card image
    '''
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv, np.array(list(RED_FILTER['min'].values())), np.array(list(RED_FILTER['max'].values())))
    frame_filtered = cv2.bitwise_and(frame, frame, mask=red_mask)
    croped_frame_filtered = frame_filtered[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    croped_frame_filtered_inverted = cv2.bitwise_not(croped_frame_filtered)
    return 'red' if np.mean(croped_frame_filtered_inverted) > RED_THRESHOLD else 'black'

blobs_sum = 0
count = 0

def detect_card_number(frame: cv2.typing.MatLike, mask: cv2.typing.MatLike) -> tuple[int, list[cv2.KeyPoint]]:
    '''
    Returns number of the card and where the symbols where found in the image
    '''

    frame_masked = np.where(mask==255, frame, mask)
    keypoints = detector.detect(frame_masked)

    count = 1
    blobs_count = len(keypoints) - 2
    blobs_sum = blobs_count
    card_number = round(blobs_sum/count)

    if count >= 50:
        count = 0
        blobs_sum = 0

    return card_number, keypoints

cv2.namedWindow(preview_name)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Falha na captura de imagem")
        break

    # Detectando a cor da carta
    card_color = detect_card_color(frame)

    # Contando o número de símbolos na carta
    card_number, keypoints = detect_card_number(frame, rectagle_mask)

    # Desenhando os keypoints encontrados pelo simple blob detector
    frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Desenhando o retângulo onde pede a carta
    cv2.rectangle(frame_with_keypoints, top_left, bottom_right, (255, 128, 128), 2)
    cv2.putText(frame_with_keypoints, 'Posicione a carta aqui', text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 128, 128), 2, cv2.LINE_AA)

    # Resultado
    cv2.putText(frame_with_keypoints, f'{card_number} {card_color}', result_position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 128, 128), 2, cv2.LINE_AA)

    # Mostra a frame
    cv2.imshow(preview_name, frame_with_keypoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
