import sys
import os
import numpy as np
import cv2
from datetime import date
import tensorflow as tf


from werkzeug.utils import secure_filename


from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL, MySQLdb
import bcrypt


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'covid19_detection'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.secret_key = 'Aniket123'
mysql = MySQL(app)



def prepare(filepath):
  IMG_SIZE=60
  img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
  new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
  return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def aboutus():
    return render_template('about-us.html')

@app.route('/login', methods=['GET','POST'])
def loginuser():
    error = ' '
    if request.method == 'POST':
        user_email_log = request.form['user-email-log']
        user_pass_log = request.form['user-password-log'].encode('utf-8')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM register WHERE Email_Id = %s ',(user_email_log,))
        user = cur.fetchone()
        cur.close()
        try:

            if len(user) != 0:
                if bcrypt.hashpw(user_pass_log,user['Password'].encode('utf-8')) == user['Password'].encode('utf-8'):
                    session['Email_Id'] = user_email_log
                    session['First_Name'] = user['First_Name']

                    return redirect(url_for('aiwebapp'))
                else:
                    error = 'Password is not correct! Please use valid password'
                    return render_template('log-in.html', error=error)

            else:
                error = 'Credentials are not valid! Please use valid credentials'
                return render_template('log-in.html', error = error)

        except Exception as e:
            error = 'Credentials are not valid. Please use valid credentials !'
            return render_template('log-in.html', error=error)


    else:
        return render_template('log-in.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register', methods=['GET','POST'])
def registeruser():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        user_email = request.form['user-email']
        user_pass = request.form['user-pass'].encode('utf-8')
        hash_pass = bcrypt.hashpw(user_pass,bcrypt.gensalt())

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO register (First_Name,Last_Name,Email_Id,Password) VALUES(%s,%s,%s,%s)', (first_name,last_name,user_email,hash_pass))
        mysql.connection.commit()
        session['Email_Id'] = user_email
        session['First_Name'] = first_name
        return redirect(url_for('aiwebapp'))


@app.route('/patients-data')
def doctorsdata():
    db_email_id = session['Email_Id']

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT Id FROM register WHERE Email_Id = %s ', (db_email_id,))
    user = cur.fetchone()

    user_id = user['Id']

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM doctors_data WHERE User_Id = %s ', (user_id,))
    data = cur.fetchall()
    return render_template('all-patients-result.html', data = data)

@app.route('/ai-webapp',methods=['GET','POST'])
def aiwebapp():

    CATEGORIES = ['Covid-19 Positive', 'Normal']
    MODEL_PATH = 'static/AI-model/covid-19-updated.h5'
    UPLOAD_PATH_IMG = 'static/upload_images/'
    model = tf.keras.models.load_model(MODEL_PATH)

    if request.method == 'POST':
        patient_name = request.form['patient_name']
        f = request.files['user_image']
        image_name = secure_filename(f.filename)
        filepath = os.path.join(UPLOAD_PATH_IMG,secure_filename(f.filename))
        f.save(filepath)

        upload_date = date.today()
        db_email_id = session['Email_Id']


        prediction = model.predict([prepare(filepath)])

        result = CATEGORIES[int(prediction[0][0])]

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT Id FROM register WHERE Email_Id = %s ', (db_email_id,))
        user = cur.fetchone()


        user_id = user['Id']
        cur.execute('INSERT INTO doctors_data (User_Id,Patient_Name,Prediction_Status,Img_Name,Date) VALUES(%s,%s,%s,%s,%s)',
                    (user_id, patient_name, result, image_name,upload_date))
        mysql.connection.commit()

        cur.close()
        return render_template('ai-webapp.html',result=result)

    return render_template('ai-webapp.html')

if __name__ == "__main__":
    app.run(debug=True)