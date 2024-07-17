from flask import Flask, render_template
import random
app = Flask(__name__, template_folder = "templates")

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/fortune")
def fortune(): 	
	possible_fortunes = ["You will have the best room IN IASA",
	"You will be Abdallahs bestie",
	"You will have a vending machine of your own", 
	"Yhe vending machine will eat you", 
	"You will get lost IN IASA AND the dragon will eat you",
	"your suitcase will fall in the stairs and crash you",
	"you will get a brand new laptop as a present from Lilach",
	"IASA will make your favorite food for dinner",
	"your room in IASA will have a porch",
	"you will get bald next week"]
	random_num = random.randint(0,9)
	return render_template("fortune.html", fortune1 = possible_fortunes[random_num])

if __name__ == '__main__':
   app.run(debug=True)