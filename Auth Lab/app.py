from flask import Flask, render_template, redirect, request, url_for
from flask import session as login_session
import random
import pyrebase

app = Flask(__name__, template_folder = "template" , static_folder = "static")


app.config['SECRET_KEY'] = "super_secret_key"


firebaseConfig = {
  "apiKey": "AIzaSyDfB84nH1mkiwi9uCdHkKLGR4mmzlPBZb4",
  "authDomain": "auth-lab1.firebaseapp.com",
  "projectId": "auth-lab1",
  "storageBucket": "auth-lab1.appspot.com",
  "messagingSenderId": "436281478397",
  "appId": "1:436281478397:web:fecebf77d3276b7de6c294",
  "measurementId": "G-HL09DTTCZW",
  "databaseURL":"https://auth-lab1-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  error = ""
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
      login_session['quotes'] = []
      login_session['user'] = auth.create_user_with_email_and_password(email, password)
      return redirect(url_for('home'))
    except Exception as hadar:
      print(hadar)
      error = "Authentication failed"
      print(error)
  return render_template("signup.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
   error = ""
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      try:
        login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        return redirect(url_for('home'))
      except:
        error = "Authentication failed"
   return render_template("signin.html")

@app.route('/signout')
def signout():
  login_session['user'] = None
  auth.current_user = None
  return redirect(url_for('home'))

@app.route('/home', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    qoute = request.form['qoute']
    login_session['quotes'].append(qoute)
    login_session.modified = True

    return redirect(url_for('thanks'))
  else:
    return render_template("home.html")

@app.route('/display', methods=['GET', 'POST'])
def display():
  if request.method == 'GET':
    return render_template('display.html')
  else:
    return render_template("home.html")

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
  if request.method == 'GET':
    return render_template('thanks.html')
  else:
    return render_template("home.html")

@app.route('/', methods=['GET', 'POST'])
def main():
  if request.method == 'GET':
    return render_template('/.html')
  else:
    return render_template("signup.html")


if __name__ == '__main__':
   app.run(debug=True)