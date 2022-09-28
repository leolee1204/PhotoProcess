import requests
import cv2
import numpy as np
import io
import json
import os

def img_removebackground(img):
    if not os.path.exists('removeBackground'): os.mkdir('removeBackground')
    image = np.asarray(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_encode = cv2.imencode('.png', image)
    str_encode = img_encode[1].tostring()
    cc = io.BytesIO(str_encode)

    # # 從二進位制檔案到圖片(numpy.ndarray):
    #
    # # aaa=np.fromstring(x, np.uint8)
    # # img = cv2.imdecode(aaa ,cv2.IMREAD_COLOR)
    #
    response = requests.request(
    "POST",
    "https://techhk.aoscdn.com/api/tasks/visual/segmentation",
    headers= {'X-API-KEY': 'wx5gzhjj9alg4ch9z'},
    data={'sync': '1'},
    files= {'image_file': cc}
    )
    link =(json.loads(response.text)['data']['image'])
    res = requests.get(link)
    with open('removeBackground/removebackground.png','wb')as f:
        f.write(res.content)
    return 'removeBackground/removebackground.png'
