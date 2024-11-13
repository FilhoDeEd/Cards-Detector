import cv2
import numpy as np
from typing import Literal

top_left = (width // 2 - 150, height // 2 - 225)
bottom_right = (width // 2 + 150, height // 2 + 225)
text_position = (width // 2 - 150, height // 2 - 250)

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

# Threshold do filtro vermelho
RED_THRESHOLD = 6.0

# Configuração do Simple Blob Detector
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 1000
params.maxArea = 1000000
params.filterByCircularity = True
params.minCircularity = 0.3
params.filterByConvexity = False
params.filterByInertia = False
detector = cv2.SimpleBlobDetector_create(params)

def crop_frame(frame:cv2.typing.MatLike) -> cv2.typing.MatLike:
    '''
        Crop the frame on the dimensions set in constants.py
    '''
    return frame[c.top_left[1]:c.bottom_right[1], c.top_left[0]:c.bottom_right[0]]
     
def drawKeypoints(frame: cv2.typing.MatLike, keypoints: list[cv2.KeyPoint]) -> cv2.typing.MatLike:
    '''
    Draw the circles in the frame where keypoints were found
    '''
    return cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 255, 255),
                                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
def red_or_black(frame: cv2.typing.MatLike) -> Literal['red', 'black']:
    '''
    Returns if color is red or black
    '''
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv, np.array(RED_FILTER['min'].values()), np.array(RED_FILTER['max'].values()))
    frame_filtered = cv2.bitwise_and(frame, frame, mask=red_mask)
    croped_frame_filtered = frame_filtered[c.top_left[1]:c.bottom_right[1], c.top_left[0]:c.bottom_right[0]]
    if np.mean(croped_frame_filtered) > RED_THRESHOLD:
        return 'red'
    else:
        return 'black'

def number_of_card(frame: cv2.typing.MatLike, mask: cv2.typing.MatLike) -> tuple[int, list[cv2.KeyPoint]]:
    '''
    Returns number of the card and where the symbols where found in the image
    '''
    frame_masked = np.where(mask==255, frame, mask) # Achar um nome melhor
    keypoints = detector.detect(frame_masked)

    i = 0
    sum = 0
    for keypoint in keypoints:
        i += 1
        # Calcula a circularidade para cada keypoint
        diameter = keypoint.size
        radius = diameter / 2
        area = np.pi * (radius ** 2)
        perimeter = np.pi * diameter

        # Circularidade
        sum += diameter

    if i != 0:
        print(sum/i)
    #Somatória de blobs na tela
    blobs_sum = 0
    #Contador
    count = 0
    count += 1
    blobs_count = len(keypoints) - 2
    blobs_sum += blobs_count
    card_number = round(blobs_sum/count)
    if count >= 50:
        count = 0
        blobs_sum = 0
    return card_number, keypoints

def draw_rectangle(frame:cv2.typing.MatLike) -> None:
    '''
    Draws retangle with text "Posicione a carta aqui" above
    '''
    cv2.rectangle(frame, c.top_left, c.bottom_right, (0, 255, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Posicione a carta aqui", c.text_position, font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
