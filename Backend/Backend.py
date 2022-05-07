#################################################   BOOK YOUR SHOW   #######################################################
############################################################################################################################
import ast
# from crypt import methods
# from asyncore import write
# from crypt import methods
# from crypt import methods
from distutils.fancy_getopt import wrap_text
from email.mime import image
from operator import length_hint
from pickle import TRUE
from platform import release
from turtle import showturtle
from flask import Flask, render_template, request, session
from flask import Flask, redirect, url_for
from flask import flash
from flask.helpers import flash
from flask import Flask, flash
from flask_mail import Mail, Message
import pymysql
import os
import shutil
from PIL import Image
import random
import time
import base64
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# from localStoragePy import localStoragePy


app = Flask(__name__)
app.secret_key = "super-secret-key"


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'biditvalueforyourvaluables@gmail.com'
app.config['MAIL_PASSWORD'] = 'systango@@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


def sentEmail(seats, time, moviename):
    fromaddr = "biditvalueforyourvaluables@gmail.com"
    password = "systango@@"
    toaddr = "jatinsadhwani.1234@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "BookYourShow"

    body = f"Your Movie is {moviename} and seats are {seats} and Time : {time}"
    print(moviename)
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    server.send_message(msg)

    server.quit()


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # session.pop('user')




@app.route("/movie/<string:movieID>/booktheater/<string:theaterid>/<string:time>/seatbooking", methods=["GET"])
def SeatBooking(movieID, theaterid, time):
    print(time)
    theaterid = int(theaterid)
    movieID = int(movieID)
    con = pymysql.connect(
        host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()

    cur.execute(
        'select * from seatbooking where theaterid = %s AND movieid = %s AND showtime=%s', (theaterid, movieID, time))
    bookedSeats = cur.fetchall()

    totalBookedSeats = []
    for i in bookedSeats:
        res = ast.literal_eval(i[0])
        for j in res:
            totalBookedSeats.append(j)

    # print(totalBookedSeats)
    return render_template("SeatBooking.html", enumerate=enumerate, movieID=movieID, theaterid=theaterid, totalBookedSeats=totalBookedSeats, str=str)


@app.route("/movie/<string:movieID>/booktheater/<string:theaterid>/<string:time>/seatbooking/paynow", methods=["POST", "GET"])
def paynow(movieID, theaterid, time):
    # print("DATA ================", movieID, theaterid)

    result = request.form.to_dict()
    # print(result, type(result))

    seats = []
    for val in result.values():
        seats.append(val)

    print(time, type(time))

    seats = str(seats)

    con = pymysql.connect(
        host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute('insert into seatbooking values(%s,%s,%s,%s)',
                (seats, int(theaterid), int(movieID) , time ))

    cur1 = con.cursor()
    cur1.execute("select moviename from movieinfo where movieid = %s", movieID)
    moviename = cur1.fetchone()

    con.commit()
    con.close()
    sentEmail(seats, time, moviename)
    return redirect(f'/movie/{movieID}')
    # return redirect(f'/pay')
    


########################################### Generic Page ###################################################
############################################################################################################

@app.route("/movie/<string:movieID>", methods=["GET", "POST"])
def genericpage(movieID):
    # print("************************************************")
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

    return render_template("genericpage.html", row=row, filename=fn, enumerate=enumerate, movieID=movieID)




@app.route("/showtheaters", methods=["GET"])
def Showtheaters():
    con = pymysql.connect(
        host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute('select * from theaterinfo')
    rows = cur.fetchall()

    # print(rows)
    return render_template("showTheaters.html", rows=rows)




@app.route("/showmovies", methods=["GET"])
def Showmovies():
    con = pymysql.connect(
        host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute('select * from movieinfo')
    rows = cur.fetchall()

    # print(rows)
    return render_template("showMovies.html", rows=rows)




@app.route("/movie/<string:movieID>/booktheater", methods=["GET", "POST"])
def BookTheater(movieID):
    # print(movieID)
    con = pymysql.connect(
        host='localhost', user='root', password='', database='bookyourshow')
    cur = con.cursor()
    cur.execute("select * from movieinfo where movieid = %s", movieID)
    rows = cur.fetchone()

    showtimes = []
    times = ast.literal_eval(rows[5])
    for i in times:
        showtimes.append(i)
    

    theaters = []

    # Convert string of array into array
    res = ast.literal_eval(rows[9])

    cur1 = con.cursor()
    for i in res:
        # print("**************************************************")
        print(i)
        t_id = int(i)
        cur1.execute("select * from theaterinfo where theaterid = %s", t_id)
        theater = cur1.fetchone()

        theaters.append(theater)

        # theaters.append({
        #     "theatername":theater[0],
        #     "theaterid":theater[1],
        #     "theaterlocation":ast.literal_eval(theater[2]),
        #     "showtime":ast.literal_eval(theater[3])
        # })

    return render_template("BookTheater.html", rows=rows, movieID=movieID, theaters=theaters, showtimes=showtimes)




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
                 quality=50)
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
            # print('compressing', file)
            compressMe(file, verbose)

    print("Done")


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


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
    return render_template("login.html")


@app.route("/loggedin", methods=['GET', 'POST'])
def loginhome():
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
        print("HOMEE")
        return redirect("/home")

    elif flag == 2:
        # print("flag one chala")

        flash('Incorrect password')
        return render_template("login.html")
    else:
        flash('Email doesn\'t exist')
        return render_template("login.html")

    # con.close()



@app.route('/home', methods=['GET','POST'])
def userHome():
    if(request.method=='POST' or request.method=='GET'):
        con = pymysql.connect(host='localhost', user='root',
                              password='', database='bookyourshow')
        cur = con.cursor()
        cur.execute('select * from movieinfo')
        result = cur.fetchall()
        i = random.randint(50000, 1000000)
        j = i

        path = 'static/uploading/'

        path2 = 'static/upload/'

        if os.path.exists(path):
            shutil.rmtree(path)

        if os.path.exists(path2):
            shutil.rmtree(path2)

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
        for row in result:
            if os.path.exists(path2):
                path3 = f'{path2}/{i}.jpg'

                image = row[0]
                write_file(image, path3)
                i -= 1

            else:
                os.makedirs(path2)
                path3 = f'{path2}/{i}.jpg'

                image = row[0]
                write_file(image, path3)

                i -= 1

        return render_template('home.html', result=result, enumerate=enumerate, num=j)
    # return render_template('home.html',enumerate=enumerate, num=j)

################################################ ADMIN LOGIN ################################################
#############################################################################################################


@app.route('/adminhome', methods=['GET', 'POST'])
def adminhome():

    con = pymysql.connect(host='localhost', user='root',
                          password='', database='bookyourshow')
    curT = con.cursor()
    curT.execute('select * from theaterinfo')
    theater = curT.fetchall()

    curM = con.cursor()
    curM.execute('select * from movieinfo')
    movies = curM.fetchall()

    movieid= 1
    theaterid = 1
    if len(theater) > 0:
        theaterid = theater[-1][1]+1

    if len(movies) > 0:
        movieid= movies[-1][1]+1

        

    return render_template('adminPage.html', enumerate=enumerate, 
                                            theater=theater, 
                                            movieid=movieid, 
                                            theaterid=theaterid)


@app.route("/adminlogin", methods=['GET', 'POST'])
def Adminlogin():
    return render_template("adminlogin.html")


@app.route("/adminloggedin", methods=['GET', 'POST'])
def Adminloggedin():
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
        return redirect("/adminlogin")

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

        return redirect('/adminhome')
        # return render_template("adminlogin.html")

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

@app.route("/addtheater", methods=['GET', 'POST'])
def owner_upload():

    if(request.method == 'POST'):
        # movieid = request.form.get("movieid")
        theatername = request.form.get("theater")
        theaterid = request.form.get("theaterId")


        if theatername == "" or theaterid == "" :
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
            # return render_template("adminPage.html")
            return redirect('/adminhome')
            con.close()
        else:
            cur.execute('insert into theaterinfo values(%s,%s)',
                        (theatername, theaterid))

            con.commit()

            con.close()

            flash('Success..... Record has been submitted')



            return redirect('/adminhome')
            # return render_template("adminPage.html", rows=rows)
        
        
        
        
        
        # session.pop('email')

    else:
        return render_template("adminPage.html")


############################################# DELETE THEATER #####################################################
##################################################################################################################
@app.route("/deleteTheater", methods=['GET', 'POST'])
def deleteTheater():
    if(request.method == 'POST'):
        theaterid = request.form.get("theatername")

        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print(theaterid)

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
            return redirect("/adminhome")
        session.pop('email')

    else:
        # print("data not inserted!!!")
        return redirect('/adminhome')


############################################## ADD MOVIES #####################################################
###############################################################################################################

@app.route("/add_movies", methods=['GET', 'POST'])
def add_movies():
    if(request.method == 'POST'):
        movieid = request.form.get("movieid")
        moviename = request.form.get("movie")
        movieanimation = request.form.getlist("animation")
        language = request.form.getlist("language")
        showtime = request.form.getlist("showtime")
        movieduration = request.form.get("duration")
        releasedate = request.form.get("date")
        aboutmovie = request.form.get("about")
        theaterid = request.form.getlist("theaterId")
        image1 = request.files['image1']
        img1 = None

        while("" in theaterid):
            theaterid.remove("")

        theaterid = str(theaterid)
        language = str(language)
        movieanimation = str(movieanimation)
        showtime = str(showtime)

        # print("Img upload me aaya **************************")
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

        if movieid == "" or moviename == "" or movieanimation == "" or language == "" or movieduration == "" or releasedate == "" or aboutmovie == "":
            flash('Required all fields and correct field')
            return redirect('/adminhome')

        else:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='bookyourshow')
            cur = con.cursor()
            cur.execute('select * from movieinfo')
            # cur.execute('select theatername from theaterinfo')
            rows = cur.fetchall()
            flag = 0

        # check unique
            for row in rows:
                if row[0] == movieid:
                    flag = 1

        if flag == 1:
            flash('movie id already exist')
            return render_template("adminPage.html")

        else:
            cur.execute('insert into movieinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        (img1, movieid, moviename, movieanimation, language,
                         showtime, movieduration, releasedate, aboutmovie,
                         theaterid))

            con.commit()

            con.close()
            flash('Success..... Record has been submitted')
            return redirect('/adminhome')

    else:
        return redirect('/adminlogin')


################################################## Delete Movie ################################################
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
            return redirect('/adminhome')
        session.pop('email')

    else:
        # print("data not inserted!!!")
        return redirect('/adminhome')


##############################------------------ END -------------------###########################################
##############################------------------------------------------###########################################

if __name__ == '__main__':
    app.run(debug=True)
