#################################################   BOOK YOUR SHOW   #######################################################
############################################################################################################################

from asyncore import write
# from crypt import methods
from distutils.fancy_getopt import wrap_text
from email.mime import image
from pickle import TRUE
from platform import release
from flask import Flask, render_template, request, session
from flask import flash
from flask.helpers import flash
import pymysql
import os
import shutil
from PIL import Image
import random
import time
import base64
import sys

app = Flask(__name__)
app.secret_key = "super-secret-key"


@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')
    # session.pop('user')


@app.route("/seatbooking", methods=["GET"])
def SeatBooking():

    con = pymysql.connect(
        host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute('select theatername from theaterinfo')
    rows = cur.fetchone()
    return render_template("SeatBooking.html" , enumerate = enumerate,rows=rows)



@app.route("/paynow", methods=["POST", "GET"])
def paynow():
    result = request.form
    # print(result)

    # print(result)
    str1 = ''
    str1 = ','.join(result.values())
    # print(str1)
    # print(type(str1))

    con = pymysql.connect(
        host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute('insert into seatbooking values(%s)', (str1))

    return render_template("SeatBooking.html")

########################################### Generic Page ###################################################
############################################################################################################


@app.route("/test/<string:movieID>", methods=["GET", "POST"])
def genericpage(movieID):
    print("************************************************")
    # print(movieID)

    con = pymysql.connect(host='localhost', user='root',
                          password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute("select * from movieinfo where movieid=%s", movieID)
    row = cur.fetchone()
    fn = random.randint(210000, 240000)
    filename = "static/upload/" + str(fn) + ".jpg"
    write_file(row[0], filename)
    # print("************************* done ************************")
    # print(filename)

    # moviename = row[2]
    # print(row)
    return render_template("genericpage.html", row=row, filename=fn, enumerate=enumerate)


@app.route("/BookNowNew", methods=["GET"])
def BookNowNew():
    con = pymysql.connect(
        host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute('select * from theaterinfo')
    rows = cur.fetchall()

    # print(rows)
    return render_template("BookNowNew.html", rows=rows)


@app.route("/BookTheater", methods=["GET"])
def BookTheater():
    con = pymysql.connect(
        host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute('select * from theaterinfo')
    rows = cur.fetchall()

    # print(rows)
    return render_template("BookTheater.html", rows=rows)


@app.route("/SeatSelecting", methods=["GET"])
def SeatSelecting():
    
    # print(rows)

    return render_template("SeatSelecting.html")

###############################################################################################################
################################################# Upload Image ################################################

# define a function for
# compressing an image


def compressMe(file, verbose=False):

    # Get the path of the file
    filepath = os.path.join('static/upload/',
                            file)

    # open the image
    picture = Image.open(filepath).convert('RGB')

    # Save the picture with desired quality
    # To change the quality of image,
    # set the quality variable at
    # your desired level, The more
    # the value of quality variable
    # and lesser the compression
    picture.save('static/upload/'+file,
                 "JPEG",
                 optimize=True,
                 quality=40)
    return


def mainfun():

    verbose = False

    # checks for verbose flag
    if (len(sys.argv) > 1):

        if (sys.argv[1].lower() == "-v"):
            verbose = True

    # finds current working dir
    cwd = 'static/upload'

    formats = ('.jpg', '.jpeg')

    # looping through all the files
    # in a current directory
    for file in os.listdir(cwd):

        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            print('compressing', file)
            compressMe(file, verbose)

    print("Done")


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


# @app.route("/img_upload", methods=['GET', 'POST'])
def img_upload(image1):
    movieid = ''
    moviename = ''
    movieanimation = ''
    language = ''
    movieduration = ''
    releasedate = ''
    aboutmovie = ''
    if True:
        # print("Img upload me aaya **************************")
        path = 'static/upload/'
        if os.path.exists(path):

            # image1=request.files['image1']

            image1.save(path+image1.filename)

            mainfun()
            path1 = path+image1.filename
            # img1 = convertToBinaryData(path1)

            con = pymysql.connect(
                host='localhost', user='root', password='', database='bookyourshow')
            cur = con.cursor()
            cur.execute('insert into movieinfo values(%s, %s, %s, %s, %s, %s, %s, %s)',
                        (img1, movieid, moviename, movieanimation, language, movieduration, releasedate, aboutmovie))
            con.commit()
            con.close()
            flash('Success..... Record has been submitted')
            # return render_template('adminPage.html')

        else:
            os.makedirs(path)
            # image1=request.files['image1']

            image1.save(path+image1.filename)

            mainfun()
            path1 = path+image1.filename
            img1 = convertToBinaryData(path1)

            con = pymysql.connect(
                host='localhost', user='root', password='', database='bookyourshow')
            cur = con.cursor()
            cur.execute('insert into movieinfo values(%s, %s, %s, %s, %s, %s, %s, %s)',
                        (img1, movieid, moviename, movieanimation, language, movieduration, releasedate, aboutmovie))

            con.commit()
            con.close()
            flash('Success..... Record has been submitted')
            # return render_template('adminPage.html')


####################################################################################################################
################################################# USER REGISTRATION ################################################

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
            return render_template("registration.html", token="token")

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


################################################################################################################
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

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


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
        cur.execute('select * from movieinfo')
        result = cur.fetchall()
        i = random.randint(50000, 1000000)
        j = i
        path = 'static/uploading/'

        if os.path.exists(path):
            shutil.rmtree(path)

        for row in result:
            if os.path.exists(path):
                path1 = f'{path}/{i}.jpg'
                image = row[0]
                write_file(image, path1)
                i += 1
            else:
                os.makedirs(path)
                path1 = f'{path}/{i}.jpg'
                image = row[0]
                write_file(image, path1)
                i += 1

        return render_template('home.html', result=result, enumerate=enumerate, num=j)

    elif flag == 2:
        # print("flag one chala")

        flash('Incorrect password')
        return render_template("login.html")
    else:
        flash('Email doesn\'t exist')
        return render_template("login.html")

    # con.close()


################################################ ADMIN LOGIN ################################################
#############################################################################################################

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


############################################# ADD THEATER #####################################################
###############################################################################################################

@app.route("/owner_upload", methods=['GET', 'POST'])
def owner_upload():

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
            return render_template("adminPage.html", rows=rows)
        # session.pop('email')

    else:
        return render_template("adminPage.html")


############################################# DELETE THEATER #####################################################
##################################################################################################################
@app.route("/deleteTheater", methods=['GET', 'POST'])
def deleteTheater():
    if(request.method == 'POST'):
        theaterid = request.form.get("theatername")

        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(theaterid)

        if theaterid == "":
            flash('Movie Id Is Mandatory!!!')

        else:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='bookyourshow')
            cur = con.cursor()
            cur.execute(
                "DELETE from theaterinfo where theaterid = '%s'" % (theaterid))

            con.commit()

            con.close()

            # img_upload( request.files['image1'])

            print('Success..... Record has been deleted')
            return render_template("adminPage.html")
        session.pop('email')

    else:
        # print("data not inserted!!!")
        return render_template("adminPage.html")


############################################## ADD MOVIES #####################################################
###############################################################################################################

@app.route("/add_movies", methods=['GET', 'POST'])
def add_movies():

    if(request.method == 'POST'):

        movieid = request.form.get("movieid")
        moviename = request.form.get("movie")
        movieanimation = request.form.get("animation")
        language = request.form.get("language")
        movieduration = request.form.get("duration")
        releasedate = request.form.get("date")
        aboutmovie = request.form.get("about")

        image1 = request.files['image1']
        img1 = None

        print("Img upload me aaya **************************")
        path = 'static/upload/'
        if os.path.exists(path):

            image1.save(path+image1.filename)

            mainfun()
            path1 = path+image1.filename
            img1 = convertToBinaryData(path1)
            # img1 = base64.b64encode(image1)

        else:
            os.makedirs(path)

            image1.save(path+image1.filename)

            mainfun()
            path1 = path+image1.filename
            img1 = convertToBinaryData(path1)
            # img1 = base64.b64encode(image1)

        if movieid == "" or moviename == "" or movieanimation == "" or language == "" or movieduration == "" or releasedate == "" or aboutmovie == "":
            flash('Required all fields and correct field')
            return render_template("adminPage.html")

        # elif len(password) < 8:
        #     flash('password must be atleast 8 characters')
        #     return render_template("registration.html")

        else:
            # Img upload function call
            # img_upload()
            con = pymysql.connect(
                host='localhost', user='root', password='', database='bookyourshow')
            cur = con.cursor()
            cur.execute('select * from movieinfo')
            rows = cur.fetchall()
            flag = 0

        # check unique
            for row in rows:
                if row[0] == movieid:
                    flag = 1

        if flag == 1:
            flash('movie id already exist')
            return render_template("adminPage.html")
            con.close()
        else:
            cur.execute('insert into movieinfo values(%s,%s,%s,%s,%s,%s,%s,%s)',
                        (img1, movieid, moviename, movieanimation, language, movieduration, releasedate, aboutmovie))

            con.commit()

            con.close()

            # img_upload( request.files['image1'])

            flash('Success..... Record has been submitted')
            return render_template("adminPage.html")
        # session.pop('email')

    else:
        # print("data not inserted!!!")
        return render_template("adminPage.html")


################################################## deleteMovie ################################################
###############################################################################################################

@app.route("/deleteMovie", methods=['GET', 'POST'])
def deleteMovie():
    if(request.method == 'POST'):
        movieid1 = request.form.get("moviename")

        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print(movieid1)

        if movieid1 == "":
            flash('Movie Id Is Mandatory!!!')

        else:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='bookyourshow')
            cur = con.cursor()
            cur.execute("DELETE from movieinfo where movieid = '%s'" %
                        (movieid1))

            con.commit()

            con.close()

            # img_upload( request.files['image1'])

            print('Success..... Record has been deleted')
            return render_template("adminPage.html")
        session.pop('email')

    else:
        # print("data not inserted!!!")
        return render_template("adminPage.html")


##############################------------------ END -------------------###########################################
##############################------------------------------------------###########################################

if __name__ == '__main__':
    app.run(debug=True)
