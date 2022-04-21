# from crypt import methods
# from crypt import methods
# from crypt import methods
from flask import Flask, render_template, flash, request, session
import pymysql
import os
import shutil
from PIL import Image
import random
import time
import sys

app = Flask(__name__)
app.secret_key = "super-secret-key"




@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')
    # session.pop('user')




@app.route("/rec_movie_1", methods=['GET'])
def rec_movie_1():
    return render_template('rec_movie_1.html')




@app.route("/rec_movie_2", methods=['GET'])
def rec_movie_2():
    return render_template('rec_movie_2.html')




@app.route("/rec_movie_3", methods=['GET'])
def rec_movie_3():
    return render_template('rec_movie_3.html')




@app.route("/rec_movie_4", methods=['GET'])
def rec_movie_4():
    return render_template('rec_movie_4.html')




@app.route("/rec_movie_5", methods=['GET'])
def rec_movie_5():
    return render_template('rec_movie_5.html')





@app.route("/rec_movie_6", methods=['GET'])
def rec_movie_6():
    return render_template('rec_movie_6.html')




@app.route("/rec_movie_7", methods=['GET'])
def rec_movie_7():
    return render_template('rec_movie_7.html')





@app.route("/SeatBooking", methods=["GET"])
def SeatBooking():
    return render_template("SeatBooking.html")




# @app.route("/BookNow", methods=["GET"])
# def BookNow():
#     con = pymysql.connect(
#     host='localhost', user='root', password='', database='bookyourshow')
#     cur = con.cursor()
#     cur.execute('select * from theaterinfo')
#     rows = cur.fetchone()

#     # print(rows)
#     return render_template("BookNow.html", rows = rows)



@app.route("/BookNowNew", methods=["GET"])
def BookNowNew():
    con = pymysql.connect(
    host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute('select * from theaterinfo')
    rows = cur.fetchall()

    # print(rows)
    return render_template("BookNowNew.html", rows = rows)



@app.route("/SeatSelecting", methods=["GET"])
def SeatSelecting():
    return render_template("SeatSelecting.html")


################################################# User Registration ###########################################



@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        userid = request.form.get('id')
        username = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('pass')
        # session['email'] = 'email'

        # print(userid, username, email, password)

        if userid == "" or username == "" or email == "" or password == "":
            flash('Required all fields and correct field')
            return render_template("registration.html")

        # elif len(password) < 8:
        #     flash('password must be atleast 8 characters')
        #     return render_template("registration.html")

        else:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='bookyourshow')
            cur = con.cursor()
            cur.execute('select * from registered_users')
            rows = cur.fetchall()
            flag = 0

            # check unique
            for row in rows:
                if row[0] == userid:
                    flag = 1

        if flag == 1:
            flash('Email already exist')
            return render_template("registration.html")
            con.close()
        else:
            cur.execute('insert into registered_users values(%s,%s,%s,%s)',
                        (userid, username, email, password))

            con.commit()

            con.close()

            flash('Success..... Record has been submitted')
            return render_template("/login.html")
            # session.pop('email')

    else:
        return render_template("registration.html")

########################################################################################################################


################################################# Admin Registration ###########################################

@app.route("/adminregistration", methods=['GET', 'POST'])
def adminregistration():
    if request.method == 'POST':
        userid = request.form.get('id')
        username = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('pass')
        # session['email'] = 'email'

        # print(userid, username, email, password)

        if userid == "" or username == "" or email == "" or password == "":
            flash('Required all fields and correct field')
            return render_template("/adminregistration.html")

        # elif len(password) < 8:
        #     flash('password must be atleast 8 characters')
        #     return render_template("registration.html")

        else:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='bookyourshow')
            cur = con.cursor()
            cur.execute('select * from admin')
            rows = cur.fetchall()
            flag = 0

            # check unique
            for row in rows:
                if row[0] == userid:
                    flag = 1

        if flag == 1:
            flash('Email already exist')
            return render_template("/adminregistration.html")
            con.close()
        else:
            cur.execute('insert into admin values(%s,%s,%s,%s)',
                        (userid, username, email, password))

            con.commit()

            con.close()

            flash('Success..... Record has been submitted')
            return render_template("/adminlogin.html")
            # session.pop('email')

    else:
        return render_template("/adminregistration.html")

############################################################################################################


################################################ USER LOGIN ################################################
@app.route("/login", methods=['GET', 'POST'])
def login():
    username = ""
    password = ""

    print("login m aaya")
    if (request.method == 'POST'):
        print("post m aaya if m aaya")

        username = request.form.get('uname')
        password = request.form.get('pass')
        # print(username, password)

    # print(username, password)

    if username == "" or password == "":
        flash('All fields are Required')
        return render_template("login.html")

    else:
        # print("else vala chala")
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='bookyourshow')
        cur = con.cursor()
        cur.execute('select * from registered_users')
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if row[1] == username and row[3] == password:
                flag = 1

            elif row[1] == username and row[3] != password:
                flag = 2

    if flag == 1:
        # print("flag one chala")

        con = pymysql.connect(host='localhost', user='root',
                              password='', database='bookyourshow')
        cur = con.cursor()
        cur.execute('select * from registered_users')
        result = cur.fetchall()

        return render_template('home.html', result=result, enumerate=enumerate)

    elif flag == 2:
        print("flag one chala")

        flash('Incorrect password')
        return render_template("login.html")
    else:
        flash('Email doesn\'t exist')
        return render_template("login.html")

    con.close()


################################################ ADMIN LOGIN ################################################
@app.route("/Adminlogin", methods=['GET', 'POST'])
def Adminlogin():
    username = ""
    password = ""

    print("login m aaya")
    if (request.method == 'POST'):
        print("post m aaya if m aaya")

        username = request.form.get('uname')
        password = request.form.get('pass')
        # print(username, password)

    # print(username, password)

    if username == "" or password == "":
        flash('All fields are Required')
        return render_template("adminlogin.html")

    else:
        # print("else vala chala")
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='bookyourshow')
        cur = con.cursor()
        cur.execute('select * from admin')
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if row[1] == username and row[3] == password:
                flag = 1

            elif row[1] == username and row[3] != password:
                flag = 2

    if flag == 1:
        # print("flag one chala")

        con = pymysql.connect(host='localhost', user='root',
                              password='', database='bookyourshow')
        cur = con.cursor()
        cur.execute('select * from registered_users')
        result = cur.fetchall()

        return render_template('adminPage.html', result=result, enumerate=enumerate)

    elif flag == 2:
        print("flag one chala")

        flash('Incorrect password')
        return render_template("adminlogin.html")
    else:
        flash('Email doesn\'t exist')
        return render_template("adminlogin.html")

    con.close()

############################################# THEATER INFO ####################################################


@app.route("/owner_upload", methods=['GET', 'POST'])
def owner_upload():
    # con = pymysql.connect(
    # host='localhost', user='root', password='', database='bookyourshow')
    # cur = con.cursor()
    # cur.execute('select * from theaterinfo')
    # rows = cur.fetchall()

    # print(rows)
    

    if(request.method == 'POST'):
        theatername = request.form.get("theater")
        theaterid = request.form.get("theaterId")
        theaterlocation = request.form.get("location")
        theatercityname = request.form.get("city")
        theatershowtime = request.form.get("showTime")

        if theatername == "" or theaterid == "" or theaterlocation == "" or theatercityname == "" or theatershowtime == "":
            flash('Required all fields and correct field')
            return render_template("registration.html")

        # elif len(password) < 8:
        #     flash('password must be atleast 8 characters')
        #     return render_template("registration.html")

        else:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='bookyourshow')
            cur = con.cursor()
            cur.execute('select * from theaterinfo')
            rows = cur.fetchall()
            flag = 0

        # check unique
            for row in rows:
                if row[1] == theaterid:
                    flag = 1

        if flag == 1:
            flash('theater id already exist')
            return render_template("adminPage.html")
            con.close()
        else:
            cur.execute('insert into theaterinfo values(%s,%s,%s,%s,%s)',
                        (theatername, theaterid, theaterlocation, theatercityname, theatershowtime))

            con.commit()

            con.close()

            flash('Success..... Record has been submitted')
            return render_template("adminPage.html", rows = rows)
        # session.pop('email')

    else:
        return render_template("adminPage.html")


###############################################################################################################





###############################################################################################################
if __name__ == '__main__':
    app.run(debug=True)
