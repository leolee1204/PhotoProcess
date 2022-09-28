import pyimgur

def img_upload(path):
    CLIENT_ID = "892542f5a55ef38"
    PATH = path #A Filepath to an image on your computer"
    title = "Uploaded with PyImgur"

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title=title)
    return uploaded_image.link
