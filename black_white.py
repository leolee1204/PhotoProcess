import cv2
import numpy as np
import os

def img_original(img):
    if not os.path.exists('original'): os.mkdir('original')
    image = np.asarray(img)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    cv2.imwrite(f'original/img_original.png', image)


def img_gary(img):
    if not os.path.exists('gray'):os.mkdir('gray')
    image = np.asarray(img)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    cv2.imwrite(f'gray/img_gary.png',image)
    return 'gray/img_gary.png'