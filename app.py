from flask import Flask,render_template,request,send_from_directory
from flask import render_template, request
from black_white import img_gary,img_original
from io import BytesIO
from image_cartoon import *
from img_upload_test import img_upload
from LBP_test import lbp_transfer
import os
from RemovingBackgrounds import img_removebackground
#sudo pip install gunicorn
#sudo gunicorn -w 1 -b 0.0.0.0:80 app:app --daemon
#opencv-python-headless==4.5.3.56
#如抱錯刪除 torch下的libiomp5md.dll

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #網頁中文


@app.route('/')
def upload_test():
    return render_template('index.html')

@app.route('/up_photo',methods=['POST'],strict_slashes=False)
def api_upload():
    f = request.files['photo'].read()
    image_data = BytesIO(f)
    img = Image.open(image_data)
    img_original(img)

    if request.values['photo']=='black':
        path = img_gary(img)
        index_html = 'index2.html'
    elif request.values['photo'] == 'catroon':
        path = handle('original/img_original.png', 'cartoon/')
        index_html = 'index3.html'
    elif request.values['photo'] == 'lbp':
        path = lbp_transfer(img)
        index_html = 'index4.html'
    else:
        path = img_removebackground(img)
        index_html = 'index5.html'

    link = img_upload(path)
    return render_template(index_html,user_template=link)

@app.route('/download/<string:filename>',methods=['POST'])
def download(filename):
    if request.method == 'POST':
        if request.values['photo'] == 'black':
            return send_from_directory('gray',filename,as_attachment=True)
        elif request.values['photo'] == 'cartoon':
            return send_from_directory('cartoon', filename, as_attachment=True)
        elif request.values['photo'] == 'lbp_test':
            return send_from_directory('lbp', filename, as_attachment=True)
        elif request.values['photo'] == 'removebackground':
            return send_from_directory('removeBackground', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8443)))
