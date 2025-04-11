from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from flask_session import Session
from flask_mysqldb import MySQL
from datetime import datetime
from werkzeug.utils import secure_filename
import MySQLdb
import json
import os
import datetime
from flask_bcrypt import Bcrypt
 # Load configuration
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

 
app = Flask(__name__)


 
 # Configure MySQL with improved connection handling
app.config['UPLOAD_FOLDERTWO'] = 'static/img'
app.config['MYSQL_USER'] = params['user']
app.config['MYSQL_PASSWORD'] = params['pass']
app.config['MYSQL_HOST'] = params['host']
app.config['MYSQL_DB'] = params['database']
app.config['MYSQL_CURSORCLASS'] = params['cclass']
app.config['MYSQL_POOL_RECYCLE'] = 280  # Recycle connections before MySQL's default timeout (usually 300s)
app.config['MYSQL_POOL_SIZE'] = 10  # Create a connection pool

# Initialize MySQL (only once)
mysql = MySQL(app)
bcrypt = Bcrypt(app)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route('/', methods=['GET', 'POST'])
def home():
    cur=mysql.connection.cursor() 
    if request.method=='POST':
        firstname=request.form.get('firstname')
        lastname=request.form.get('lastname')
        dob=request.form.get('dob')
        address=request.form.get('address')
        state=request.form.get('state')
        country=request.form.get('country')
        aadhaar=request.form.get('aadhaar')
        email=request.form.get('email')
        password=request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        resume=request.files['resume']
        profile_image=request.files['profile']
        funvideo=request.files['funvideo']
        if resume and funvideo:
            resume_filename = secure_filename(resume.filename)
            funvideos_filename = secure_filename(funvideo.filename)
            
            
        else:
            resume_filename = ""
            funvideos_filename = ""
            profile_image_filename = ""
        if profile_image and profile_image.filename:
            print(profile_image,"profile_image")
            profile_image_filename = secure_filename(profile_image.filename)
            profile_image_path=profile_image.save(os.path.join('static/', profile_image_filename))
        if funvideo and funvideo.filename:
            print(funvideo,"funvideos")
            funvideos_path=funvideo.save(os.path.join('static/funvideos/', funvideos_filename))
        if resume and resume.filename:
            print(resume,"resume")
            resume_filename = secure_filename(resume.filename)
            resume_path=resume.save(os.path.join('static/', resume_filename))
            
        else:
            return flash("Please upload a valid PDF file for the resume.")
        cur.execute("INSERT INTO register (first_name, last_name, date_of_birth, address, state, country, aadhar_no, email,password,resume,profile_image, fun_video) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)", (firstname, lastname, dob, address, state, country, aadhaar, email, hashed_password, resume_filename,profile_image_filename,funvideos_filename))
        mysql.connection.commit()
        flash("Registration successful!")
        return redirect(url_for('login'))
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM register WHERE email = %s", (username,))
        user = cur.fetchone()
        print(user['password'])
        print(bcrypt.generate_password_hash(password).decode('utf-8'))
        if  user and bcrypt.check_password_hash(user['password'], password):
            session['loggedin'] = True
            session['user'] = user['email']
            session['user_id'] = user['id']
            session['first_name'] = user['first_name']
            session['last_name'] = user['last_name']
            flash("Login successful!")
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials. Please try again.")
    return render_template('login.html')
        
@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'user_id' not in session:
        flash("Logout successful!")
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM register")
    user = cur.fetchall()
    return render_template('home.html',data=user)
@app.route('/logout',methods=['GET','POST'])
def logout():
    user_id = request.args.get('user_id')
    flash("are you sure you want to logout from your account?","warning")
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        session.clear()
        flash("Logout successful!")
        return redirect(url_for('login'))   
    return render_template('logout.html',user_id=user_id)
@app.route('/action', methods=['GET','POST'])
def action():
    user_id = request.args.get('user_id')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM register WHERE id = %s", (user_id,))
    user = cur.fetchone()
    if request.method == 'POST':
        action = request.form.get('action')
        firstname=request.form.get('firstname')
        lastname=request.form.get('lastname')
        email=request.form.get('email')
        profile_image=request.files['profile']
        new_image_filename=""
        
        
        if profile_image and profile_image.filename!= "":
            print(profile_image,"profile_image")
            pfilename=secure_filename(profile_image.filename)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            new_image_filename = f"{timestamp}_{pfilename}"
            profile_image_path=profile_image.save(os.path.join('static/', new_image_filename))
        else:
            new_image_filename = user['profile_image']
        cur.execute("update register set first_name=%s,last_name=%s,email=%s,profile_image=%s where id=%s",(firstname,lastname,email,new_image_filename,user_id))
        mysql.connection.commit()
        flash("User updated successfully!", "success")
        return redirect(url_for('index',user=user))
    return render_template('action.html', user=user,user_id=user_id)
@app.route('/delete', methods=['GET','POST'])
def delete():
    user_id = request.args.get('user_id')
    flash("are you sure you want to delete your data?","warning")
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM register WHERE id = %s", (user_id,))
        mysql.connection.commit()
        flash("User deleted successfully!", "success")
        return redirect(url_for('index'))
    return render_template('delete.html',user_id=user_id)
@app.route('/profile', methods=['GET','POST'])
def user_profile():
    user_id = request.args.get('user_id')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM register WHERE id = %s", (user_id,))
    user = cur.fetchone()
    if request.method== 'POST':
        action = request.form.get('action')
        firstname=request.form.get('firstname')
        lastname=request.form.get('lastname')
        email=request.form.get('email')
        profile_image=request.files['profile']
    
    

if __name__ == '__main__':
    app.run(debug=True)