from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_pymongo import PyMongo
import bcrypt
import os
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
  
app.config["MONGO_URI"] = "mongodb://localhost:27017/Authentication"
app.secret_key = 'your_secret_key'  # Secret key for session
mongo = PyMongo(app)

#@app.route('/')
#def home():
    #return render_template("login.html")
    
UPLOAD_FOLDER = 'static\images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('user'):
        return redirect(url_for('profile'))

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = mongo.db.Login.find_one({"username": username})
    
        if user:
            stored_hashed_password = user["password"]
            #session['user'] = username
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                session['user'] = username  # Lưu username vào session
                return redirect(url_for('profile'))
            
        else:
            return redirect('/', errormessage='Invalid username or password')
           

    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'user' in session:
        user = mongo.db.Login.find_one({"username": session['user']})
        
        profile_picture, name, gender, nationality, email, address, job, dob, phone = (
                        user[key] for key in ["photo_path","full_name", "gender", "nationality", "email", "address", "job", "dob", "phone"]
                    )
                
        return render_template('profile.html', 
                                   profile_picture=profile_picture,
                                   fullname=name, 
                                   gender=gender, 
                                   nationality=nationality, 
                                   email=email, 
                                   address=address, 
                                   job=job, 
                                   dob=dob, 
                                   phone=phone)
    
    return render_template('profile.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        registration_data = {
            'username': username,
            'password': hashed_password
        }
        mongo.db.Login.insert_one(registration_data)
        
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        photo = request.files.get('photo')
        full_name = request.form.get('fullName')
        username = request.form.get('username')
        password = request.form.get('password')
        dob = request.form.get('dob')
        gender = request.form.get('gender')
        phone = request.form.get('phone')
        nationality = request.form.get('nationality')
        email = request.form.get('email')
        address = request.form.get('address')
        job = request.form.get('job')
        
        filename = secure_filename(photo.filename)
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(photo_path)
        registration_data = {
            'photo_path': photo_path, # Store filename in DB
            'full_name': full_name,
            'dob': dob,
            'gender': gender,
            'phone': phone,
            'nationality': nationality,
            'email': email,
            'address': address,
            'job': job
        }
            
        user = mongo.db.Login.find_one({"username": username})
        
        if user:
            stored_hashed_password = user["password"]
            #session['user'] = username
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                session['user'] = username
                mongo.db.Login.update_one({"username": username, "password": stored_hashed_password}, {"$set": registration_data})
                return redirect(url_for('profile'))
        else:
            return jsonify({'message': 'Invalid username or password'}), 401  # Authentication failed
    return redirect('register')        
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True, port=5000)