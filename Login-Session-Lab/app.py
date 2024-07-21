from flask import Flask, render_template, redirect, request, url_for
from flask import session as login_session
import random

app = Flask(__name__, template_folder = "templates")
app.config['SECRET_KEY'] = "hadar"
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['Name']
		bmonth = request.form['Bmonth']
		login_session['Name'] = name
		login_session['bmonth'] = bmonth

		return render_template("home.html", Bmonth = bmonth, Name = name)



# @app.route('/home', methods=['GET', 'POST'])
# def home():
# 	if request.method == 'GET':
# 		return render_template('home.html')
# 	else:
# 		birthday = request.form['Birthday']
# 		return redirect(url_for("fortune", bmonth = birthday))




@app.route("/fortune", methods=['GET','POST'])
def fortune(): 	
	possible_fortunes = ["You will have the best room IN IASA",
	"You will be Abdallahs bestie",
	"You will have a vending machine of your own", 
	"the vending machine will eat you", 
	"You will get lost IN IASA AND the dragon will eat you",
	"your suitcase will fall in the stairs and crash you",
	"you will get a brand new laptop as a present from Lilach",
	"IASA will make your favorite food for dinner",
	"your room in IASA will have a porch",
	"you will get bald next week"]
	random_num = random.randint(0,9)
	len_of_month = len(login_session['bmonth'])
	fortune2 = possible_fortunes[9]
	if len_of_month < 10:
		fortune2 = possible_fortunes[len_of_month-1]
	else:
		fortune2 = "unavailable"
	return render_template("fortune.html", fortune = fortune2)

if __name__ == '__main__':
   app.run(debug=True)