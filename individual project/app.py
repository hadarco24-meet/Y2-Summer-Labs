from flask import Flask, render_template, redirect, request, url_for
from flask import session as login_session
import random
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCVtU7-psUDApYSWR-dLUIhmTrIxAolRPk",
  "authDomain": "individual-proj-18060.firebaseapp.com",
  "databaseURL": "https://individual-proj-18060-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "individual-proj-18060",
  "storageBucket": "individual-proj-18060.appspot.com",
  "messagingSenderId": "807689978960",
  "appId": "1:807689978960:web:ae38200b49ae912934fd55",
  "measurementId": "G-PMPRPYTE1X",
  "databaseURL":"https://individual-proj-18060-default-rtdb.europe-west1.firebasedatabase.app/"

};

app = Flask(__name__, template_folder = "templates" , static_folder = "static")
app.config['SECRET_KEY'] = "super_secret_key"
firebase=pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      try:
        user = auth.create_user_with_email_and_password(email, password)            
        db.child("signup").push({
          "email": email,
          "password": password 
        })            
        login_session['user'] = user
        return redirect(url_for('home'))
      except Exception as e:
        error = "Authentication failed: {}".format(e)
        print(error)
    return render_template("signup.html", error=error)

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

@app.route('/comments', methods=['GET', 'POST'])
def comments():
  if request.method == 'POST':
    return redirect(url_for('comments'))
  else:
    return render_template("comments.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    comments = request.form['comments']        
    if 'comments' not in login_session:
      login_session['comments'] = []        
      login_session['comments'].append(comments)
      login_session.modified = True        
      db.child("comments").push({"comments": comments})        
      return redirect(url_for('home'))
    else:
      return render_template("home.html")
  else:
    return render_template("home.html")

@app.route('/main', methods=['GET', 'POST'])
def main():
  if request.method == 'POST':
    return redirect(url_for('main'))
  else:
    return render_template("main.html")

@app.route('/Chopin', methods=['GET', 'POST'])
def Chopin():
  if request.method == 'POST':
    return redirect(url_for('Chopin'))
  else:
    return render_template("Chopin.html")

@app.route('/Bach', methods=['GET', 'POST'])
def Bach():
  if request.method == 'POST':
    return redirect(url_for('Bach'))
  else:
    return render_template("Bach.html")

@app.route('/Schubert', methods=['GET', 'POST'])
def Schubert():
  if request.method == 'POST':
    return redirect(url_for('Schubert'))
  else:
    return render_template("Schubert.html")

@app.route('/Mozart', methods=['GET', 'POST'])
def Mozart():
  if request.method == 'POST':
    return redirect(url_for('Mozart'))
  else:
    return render_template("Mozart.html")

@app.route('/Schuman', methods=['GET', 'POST'])
def Schuman():
  if request.method == 'POST':
    return redirect(url_for('Schuman'))
  else:
    return render_template("Schuman.html")


if __name__ == '__main__':
   app.run(debug=True)