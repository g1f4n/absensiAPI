import os
import urllib.request
from app import app
import mysql.connector
from flask import Flask, redirect, jsonify, session
from flask import flash, request, Response
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import jsonpickle
from PIL import Image
from io import BytesIO
import json


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="absensi"
)

# extensi file yang di izinkan
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# dapatkan nama file dan extensinya
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# select join data guru + kelas
@app.route('/guru_all')
def dataGuruAll():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT tbl_guru.*, ruang_kelas, jml_siswa FROM tbl_guru LEFT JOIN tbl_kelas ON tbl_guru.id_kelas = tbl_kelas.id_kelas")
        row_headers=[x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))
        resp = jsonify(json_data)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# select join data siswa + ortu + kelas
@app.route('/all')
def dataAll():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT tbl_siswa.*, ruang_kelas, jml_siswa FROM tbl_siswa LEFT JOIN tbl_kelas ON tbl_siswa.id_kelas = tbl_kelas.id_kelas")
        row_headers=[x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))
        resp = jsonify(json_data)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# select semua data dari table guru
@app.route('/guru')
def dataGuru():
    # try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tbl_guru")
        row_headers=[x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))
        resp = jsonify(json_data)
        resp.status_code = 200
        return resp
    # except Exception as e:
    #     print(e)
    # finally:
    #     mycursor.close()

# select data by nip dari table guru
@app.route('/guruById/<string:id>')
def dataGuruById(id):

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tbl_guru WHERE nip = '"+ id +"'")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    json_data = []
    for result in myresult:
        json_data.append(dict(zip(row_headers, result)))
    resp = jsonify(json_data)
    resp.status_code = 200
    return resp

# Add data guru
@app.route('/add_guru', methods = ['POST'])
def addGuru():
    try:
        _nip = request.form['nip']
        _nama_guru = request.form['nama_guru']
        _jk = request.form['jk']
        _alamat = request.form['alamat']
        _no_hp = request.form['no_hp']
        _username = request.form['username']
        _password = request.form['password']
        _id_kelas = request.form['id_kelas']

        

        if _nip and _nama_guru and _jk and _alamat and _no_hp and _username and _password and _id_kelas and request.method == 'POST':
            _hash_password = generate_password_hash(_password)
            # insert data
            mycursor = mydb.cursor()
            sql = "INSERT INTO tbl_guru (nip, nama_guru, jk, alamat, no_hp, username, password, id_kelas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (_nip, _nama_guru, _jk, _alamat, _no_hp, _username, _hash_password, _id_kelas,)
            mycursor.execute(sql, val)
            mydb.commit()
            resp = jsonify("Data Berhasil Di Tambahkan")
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# update data guru
@app.route('/update_guru', methods = ['POST'])
def updateGuru():
    try:
        _nip = request.form['nip']
        _nama_guru = request.form['nama_guru']
        _jk = request.form['jk']
        _alamat = request.form['alamat']
        _no_hp = request.form['no_hp']
        _id_kelas = request.form['id_kelas']
        
        if _nip and _nama_guru and _jk and _alamat and _no_hp and  _id_kelas and request.method == 'POST':
            # update data
            mycursor = mydb.cursor()    
            sql = "UPDATE tbl_guru SET nama_guru = %s, jk = %s, alamat = %s, no_hp = %s, id_kelas = %s WHERE nip = '"+_nip+"'"
            val = (_nama_guru, _jk, _alamat, _no_hp, _id_kelas,)
            mycursor.execute(sql, val)
            mydb.commit()
            resp = jsonify("Data Berhasil Di Ubah")
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# delete data guru
@app.route('/delete_guru/<string:id>')
def deleteGuru(id):
    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM tbl_guru WHERE nip = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        resp = jsonify("Data Berhasil di Hapus")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# select data kelas 
@app.route('/kelasAll')
def dataKelas():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tbl_kelas")
        row_headers=[x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))
        resp = jsonify(json_data)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# select data kelas by id
@app.route('/kelasById/<int:id>')
def dataKelasById(id):

    mycursor = mydb.cursor()
    sql = "SELECT * FROM tbl_kelas WHERE id_kelas = %s"
    val = (id,)
    mycursor.execute(sql, val)
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    json_data = []
    for result in myresult:
        json_data.append(dict(zip(row_headers, result)))
    resp = jsonify(json_data)
    resp.status_code = 200
    return resp

# add data kelas
@app.route('/add_kelas', methods = ['POST'])
def addKelas():
    try:
        _ruang_kelas = request.form['ruang_kelas']
        _jml_siswa = request.form['jml_siswa']

        if _ruang_kelas and _jml_siswa and request.method == 'POST':

            # insert data
            mycursor = mydb.cursor()
            sql = "INSERT INTO tbl_kelas (ruang_kelas, jml_siswa) VALUES (%s, %s)"
            val = (_ruang_kelas, _jml_siswa,)
            mycursor.execute(sql, val)
            mydb.commit()
            resp = jsonify("Data Berhasil Di Tambahkan")
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# update data kelas
@app.route('/update_kelas', methods = ['POST'])
def updateKelas():
    try:
        _id_kelas = request.form['id_kelas']
        _ruang_kelas = request.form['ruang_kelas']
        _jml_siswa = request.form['jml_siswa']

        if _ruang_kelas and _jml_siswa and _id_kelas and request.method == 'POST':
            # update data
            mycursor = mydb.cursor()
            sql = "UPDATE tbl_kelas SET ruang_kelas = %s, jml_siswa = %s WHERE id_kelas= %s"
            val = (_ruang_kelas, _jml_siswa, _id_kelas)
            mycursor.execute(sql, val)
            mydb.commit()
            resp = jsonify("Data Berhasil Di Ubah")
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
    finally:
        return mycursor.close()   

# delete data kelas
@app.route('/delete_kelas/<string:id>')
def deleteKelas(id):
    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM tbl_kelas WHERE id_kelas = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        resp = jsonify("Data Berhasil di Hapus")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# select data ortu 
@app.route('/ortuAll')
def dataOrtu():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tbl_ortu")
        row_headers=[x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))
        resp = jsonify(json_data)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# select data ortu by id
@app.route('/ortuById/<string:id>')
def dataOrtuById(id):

    mycursor = mydb.cursor()
    sql = "SELECT * FROM tbl_ortu WHERE username = %s"
    val = (id,)
    mycursor.execute(sql, val)
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    json_data = []
    for result in myresult:
        json_data.append(dict(zip(row_headers, result)))
    resp = jsonify(json_data)
    resp.status_code = 200
    return resp

# add data ortu
@app.route('/add_ortu', methods = ['POST'])
def addOrtu():
    # try:
        _username = request.form['username']
        _password = request.form['password']
        _nis = request.form['nis']
        _nama_ortu = request.form['nama_ortu']

        if _username and _password and _nis and _nama_ortu and request.method == 'POST':
            _hashed_password = generate_password_hash(_password)
            # insert data
            mycursor = mydb.cursor()
            sql = "INSERT INTO tbl_ortu (username, password, nis, nama_ortu) VALUES (%s, %s, %s, %s)"
            val = (_username, _hashed_password, _nis, _nama_ortu)
            mycursor.execute(sql, val)
            mydb.commit()
            resp = jsonify("Data Berhasil Di Tambahkan")
            resp.status_code = 200
            return resp
    # except Exception as e:
    #     print(e)
    # finally:
    #     mycursor.close()

@app.route('/update_ortu', methods = ['POST'])
def UpdateOrtu():
    try:
        _username = request.form['username']
        _nama_ortu = request.form['nama_ortu']

        if _username and _nama_ortu and request.method == 'POST':
            # update data
            mycursor = mydb.cursor()
            sql = "UPDATE tbl_ortu SET nama_ortu = %s WHERE username = '"+_username+"'"
            val = (_nama_ortu,)
            mycursor.execute(sql, val)
            mydb.commit()
            resp = jsonify("Data Berhasil Di Ubah")
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# delete data ortu
@app.route('/delete_ortu/<string:id>')
def deleteOrtu(id):
    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM tbl_ortu WHERE username = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        resp = jsonify("Data Berhasil di Hapus")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# select data siswa 
@app.route('/siswaAll')
def dataSiswa():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tbl_siswa")
        row_headers=[x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        json_data = []
        for result in myresult:
            json_data.append(dict(zip(row_headers, result)))
        resp = jsonify(json_data)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# select data siswa by id
@app.route('/siswaById/<string:id>')
def dataSiswaById(id):

    mycursor = mydb.cursor()
    sql = "SELECT * FROM tbl_siswa WHERE nis = %s"
    val = (id,)
    mycursor.execute(sql, val)
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    json_data = []
    for result in myresult:
        json_data.append(dict(zip(row_headers, result)))
    resp = jsonify(json_data)
    resp.status_code = 200
    return resp

# add data siswa
@app.route('/add_siswa', methods = ['POST'])
def addSiswa():
    try:
        _nis = request.form['nis']
        _nama_siswa = request.form['nama_siswa']
        _id_kelas = request.form['id_kelas']
        _jam_masuk = request.form['jam_masuk']
        _jam_keluar = request.form['jam_keluar']
        _username = request.form['username']
        _password = request.form['password']

        if _nis and _nama_siswa and _id_kelas and _jam_masuk and _jam_keluar and _username and _password and request.method == 'POST':
            _hashed_password = generate_password_hash(_password)
           
            if 'lokasi_terakhir' and 'data_wajah' not in request.files:
               resp = jsonify({'message' : 'tidak ada gambar'})
               resp.status_code = 400
               return resp
            file = request.files['lokasi_terakhir']
            file2 = request.files['data_wajah']
            if file == '' and file2 == '':
                resp = jsonify({'message': 'gambar belum di input'})
                resp.status_code = 400
                return resp
            # if file.filename and file2.filename and allowed_file(file.filename) and allowed_file(file2.filename):
            if allowed_file(file.filename) == True and allowed_file(file2.filename) == True:
                filename1 = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER2'], filename1))            
                filename2 = secure_filename(file2.filename)
                file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
                # insert data
                mycursor = mydb.cursor()
                sql = "INSERT INTO tbl_siswa (nis, nama_siswa, id_kelas, lokasi_terakhir, data_wajah,  jam_masuk, jam_keluar, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (_nis, _nama_siswa, _id_kelas, filename1, filename2, _jam_masuk, _jam_keluar, _username, _hashed_password,)
                mycursor.execute(sql, val)
                mydb.commit()
                resp = jsonify("Data Berhasil Di Tambahkan")
                resp.status_code = 200
                return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# upload image
@app.route('/absen', methods = ['POST'])
def absen():
    # try:
        # if 'data_wajah' not in request.files:
        #     resp = jsonify({'message' : 'No file part in the request'})
        #     resp.status_code = 400
        #     return resp
        # file = request.files['data_wajah']
        # if file.filename == '':
        #     resp = jsonify({'message' : 'No file selected for uploading'})
        #     resp.status_code = 400
        #     return resp
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     mycursor = mydb.cursor()
        #     sql = "INSERT INTO tbl_siswa(data_wajah) VALUES (%s)"
        #     val = (filename,)
        #     mycursor.execute(sql, val)
        #     mydb.commit()
        #     resp = jsonify({'message' : 'File successfully uploaded'})
        #     resp.status_code = 201
        #     return resp
        # else:
        #     resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        #     resp.status_code = 400
        #     return resp
    # except Exception as e:
    #     print(e)
    # finally:
    #     mycursor.close()
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # # dataName = r.json.data
    
    # imgName = r.data
    print(r.data)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # # do some fancy processing here....
    # # file = request.files[img]
    p = os.path.sep.join([app.config['UPLOAD_FOLDER'], 'gifan.jpg'])
    cv2.imwrite(p, img)
    # imgName = p.split()
    # # print(r.data)
    # print(nparr)
    # # mycursor = mydb.cursor()
    # # sql = "INSERT INTO tbl_siswa(data_wajah) VALUES (%s)"
    # # val = (p,)
    # # mycursor.execute(sql, val)
    # # mydb.commit()

    
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

# update data siswa
@app.route('/update_siswa', methods = ['POST'])
def updateSiswa():
    try:
        _nis = request.form['nis']
        _nama_siswa = request.form['nama_siswa']
        _id_kelas = request.form['id_kelas']
        _jam_masuk = request.form['jam_masuk']
        _jam_keluar = request.form['jam_keluar']

        if _nis and _nama_siswa and _id_kelas and _jam_masuk and _jam_keluar  and request.method == 'POST':
    
            # if 'lokasi_terakhir' and 'data_wajah' not in request.files:
            #    resp = jsonify({'message' : 'tidak ada gambar'})
            #    resp.status_code = 400
            #    return resp
            file = request.files['lokasi_terakhir']
            if allowed_file(file.filename) == True:
                filename1 = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER2'], filename1))            
                # update data
                mycursor = mydb.cursor()
                sql = "UPDATE tbl_siswa SET nama_siswa = %s, id_kelas = %s, lokasi_terakhir = %s, jam_masuk = %s, jam_keluar = %s WHERE nis = '"+_nis+"'"
                val = (_nama_siswa, _id_kelas, filename1, _jam_masuk, _jam_keluar,)
                mycursor.execute(sql, val)
                mydb.commit()
                resp = jsonify("Data Berhasil Di Update")
                resp.status_code = 200
                return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# delete data siswa
@app.route('/delete_siswa/<string:id>')
def deleteSiswa(id):
    try:
        mycursor = mydb.cursor()
        sql = "DELETE FROM tbl_siswa WHERE nis = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        resp = jsonify("Data Berhasil di Hapus")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        mycursor.close()

# error handler
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

# login ortu
@app.route('/login_ortu', methods = ['POST'])
def login_ortu():
    mycursor = None
    try:
        _username = request.form['username']
        _password1 = request.form['password']

        # validasi username dari tbl username
        if _username != '' and _password1 != '' :
            mycursor = mydb.cursor()
            sql = "SELECT * FROM tbl_ortu WHERE username = %s"
            sql_where = (_username,)
            mycursor.execute(sql, sql_where)
            row = mycursor.fetchone()
            # hashpass = generate_password_hash(_password1)
            # print(check_password_hash(row[1], _password1))
            # print(row[1] + " " + _password1)

            if row:
                if check_password_hash(row[1], _password1):
                    session['username_ortu'] = row[0]
                    session['nis_siswa'] = row[3]
                    session['nama_ortu'] = row[4]
                    mycursor.close()
                    return jsonify({"message": "login berhasil"})
                else:
                    # print(_username + " " + _password)
                    resp = jsonify({"message": "login gagal"})
                    resp.status_code = 400
                    return resp
            else:
                resp = jsonify({"message": "username tidak di temukan"})
                resp.status_code = 400
                return resp
        else:
            resp = jsonify({"message": "username / password tidak boleh kosong"})
            resp.status_code = 400
            return resp
    except Exception as e:
        print(e)
    finally:
        if mycursor:
            mycursor.close()

@app.route('/login_guru', methods = ['POST'])
def login_guru():
    mycursor = None
    try:
        _username = request.form['username']
        _password = request.form['password']

        # validasi username dari tbl username
        if _username != '' and _password != '' :
            mycursor = mydb.cursor()
            sql = "SELECT * FROM tbl_guru WHERE username = %s"
            sql_where = (_username,)
            mycursor.execute(sql, sql_where)
            row = mycursor.fetchone()
            hashpass = generate_password_hash(_password)
            # print(check_password_hash(hashpass, _password))
            # print(_password + " " + row[1])

            if row:
                if check_password_hash(hashpass, _password):
                    session['nip'] = row[0]
                    session['nama_guru'] = row[1]
                    mycursor.close()
                    return jsonify({"message": "login berhasil"})
                else:
                    # print(_username + " " + _password)
                    resp = jsonify({"message": "login gagal"})
                    resp.status_code = 400
                    return resp
            else:
                resp = jsonify({"message": "username tidak di temukan"})
                resp.status_code = 400
                return resp
        else:
            resp = jsonify({"message": "username / password tidak boleh kosong"})
            resp.status_code = 400
            return resp
    except Exception as e:
        print(e)
    finally:
        if mycursor:
            mycursor.close()

# logout
@app.route('/logout_ortu', methods = ['POST'])
def logout_ortu():
    if 'username_ortu' in session:
        session.pop('username_ortu', None)
    return jsonify({"message": "logout berhasil"})

# run program
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)