from skimage import feature as skft
import cv2,os
import numpy as np
import os

def lbp_transfer(img):
    if not os.path.exists('lbp'):os.mkdir('lbp')
    image = np.asarray(img)
    gray = cv2.cvtColor(image,cv2.COLOR_RGBA2GRAY)
    lbp = skft.local_binary_pattern(gray,P=8,R=1,method='var')
    lbp = lbp.astype(np.uint8)
    cv2.imwrite('lbp/LBP.png',lbp)
    return 'lbp/LBP.png'