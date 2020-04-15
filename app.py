from flask import Flask

UPLOAD_FOLDER = 'D:/Project Fix/Python Project/absensi_sd/img_faces/'
UPLOAD_FOLDER2 = 'D:/Project Fix/Python Project/absensi_sd/img_location/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER2'] = UPLOAD_FOLDER2
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
