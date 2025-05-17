from flask import Flask, render_template, request, session, flash, send_file
# Import from TensorFlow's integrated Keras


import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/FarmerLogin')
def FarmerLogin():
    return render_template('FarmerLogin.html')


@app.route('/NewFarmer')
def NewFarmer():
    return render_template('NewFarmer.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2citrustdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/AFarmerInfo")
def AFarmerInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2citrustdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM farmertb  ")
    data = cur.fetchall()
    return render_template('AFarmerInfo.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2citrustdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName Or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/newfarmer", methods=['GET', 'POST'])
def newfarmer():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2citrustdb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO farmertb VALUES ('','" + name + "','" + mobile + "','" + email + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('User Register successfully')
    return render_template('FarmerLogin.html')


@app.route("/flogin", methods=['GET', 'POST'])
def flogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['fname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2citrustdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from farmertb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('FarmerLogin.html')
        else:

            session['mob'] = data[2]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2citrustdb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM farmertb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('FarmerHome.html', data=data)


@app.route("/FarmerHome")
def FarmerHome():
    fname = session['fname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2citrustdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM farmertb where UserName='" + fname + "'  ")
    data = cur.fetchall()
    return render_template('FarmerHome.html', data=data)


@app.route("/Predict")
def Predict():
    return render_template('Predict.html')


@app.route("/pred", methods=['GET', 'POST'])
def pred():
    if request.method == 'POST':
        import os
        file = request.files['file']
        fname = file.filename
        file.save('static/Out/test.jpg')

        org = 'static/Out/test.jpg'
        import tensorflow as tf
        classifierLoad = tf.keras.models.load_model('Model/model.h5')

        import numpy as np
        from keras.preprocessing import image

        test_image = image.load_img('static/Out/test.jpg', target_size=(100, 100))

        test_image = np.expand_dims(test_image, axis=0)
        result1 = classifierLoad.predict(test_image)
        result = np.argmax(result1, axis=1)
        print(result)

        out = ''
        pre = ''
        if result[0] == 0:

            out = "Apple_Black_rot"
            pre = "You can reduce your risk by drinking plenty of water and making sure you use less than 2,300 mg of sodium a day"
        elif result[0] == 1:
            print("Apple_healthy")
            out = "Apple_healthy"
            pre = ''
        elif result[0] == 2:
            print("Corn_(maize)___healthy")
            out = "Corn_(maize)___healthy"

        elif result[0] == 3:
            print("Corn_(maize)___Northern_Leaf_Blight")
            out = "Corn_(maize)___Northern_Leaf_Blight"
            pre = "Afinitor (Everolimus),Afinitor Disperz (Everolimus)"

        elif result[0] == 4:
            print("Peach___Bacterial_spot")
            out = "Peach___Bacterial_spot"
            pre = "Use sprays containing organic copper compounds to treat D. citri. Initial application should take place at petal fall, followed by a secondary treatment 6-8 weeks later."

        elif result[0] == 5:
            print("Peach___healthy")
            out = "Peach___healthy"
            # pre = "Bacterial blight can be severe in susceptible rice varieties under high nitrogen fertilization"

        elif result[0] == 6:
            print("Pepper_bell___Bacterial_spot")
            out = "Pepper_bell___Bacterial_spot"
            pre = "Always consider an integrated approach with both preventive measures and biological treatments if available. The best way to prevent the disease is to use fungicides (e.g., iprodione, propiconazole, azoxystrobin, trifloxystrobin) as seed treatments."
        elif result[0] == 7:
            print("Pepper_bell___healthy")
            out = "Pepper_bell___healthy"
            pre = ""

        elif result[0] == 8:
            print("Potato___Early_blight")
            out = "Potato___Early_blight"
            pre = "Treat seeds with dilute bleach, hydrochloric acid, or hot water to reduce the potential for seedling infection"
        elif result[0] == 9:
            print("Potato___healthy")
            out = "Potato___healthy"
            pre = ""
        elif result[0] == 10:
            print("Potato___Late_blight")
            out = "Potato___Late_blight"
            pre = "You can reduce your risk by drinking plenty of water and making sure you use less than 2,300 mg of sodium a day"

        elif result[0] == 11:
            print("Tomato___Bacterial_spot")
            out = "Tomato___Bacterial_spot"
            pre = "Treat seeds with dilute bleach, hydrochloric acid, or hot water to reduce the potential for seedling infection"
        elif result[0] == 12:
            print("Tomato___Late_blight")
            out = "Tomato___Late_blight"
            pre = "Apply a fungicide according to the manufacturer’s instructions at the first sign of infectio"
        elif result[0] == 13:
            print("Tomato___Leaf_Mold")
            out = "Tomato___Leaf_Mold"
            pre = "One of the least toxic and most effective is chlorothalonil (sold under the names Fungonil and Daconil)"
        elif result[0] == 14:
            print("Tomato___Septoria_leaf_spot")
            out = "Tomato___Septoria_leaf_spot"
            pre = "Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable"

        return render_template('Result.html', org=org, out=out, pre=pre)





@app.route("/pred1", methods=['GET', 'POST'])
def pred1():
    if request.method == 'POST':
        return render_template('Predict.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
