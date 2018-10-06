from flask import Flask, render_template, request
import os
from flask_uploads import UploadSet, configure_uploads, IMAGES

PEOPLE_FOLDER = os.path.join('static', 'people')
print (PEOPLE_FOLDER)

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['DOWNLOAD_PHOTOS'] = PEOPLE_FOLDER
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
#app.config['DOWNLOAD_PHOTOS_DEST'] = 'static/out'
configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        print(request.form['cloth'])
        filename = photos.save(request.files['photo'])
        output = os.path.join(app.config['DOWNLOAD_PHOTOS'], 'output.jpg')
        #return render_template('upload.html',user_image=output)
        print (output)
        return render_template('upload.html',user_image=output)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)