"""Cloud Foundry test"""
from flask import Flask,request,render_template
import os

app = Flask(__name__)

if os.getenv("VCAP_APP_PORT"):
    port = int(os.getenv("VCAP_APP_PORT"))
else:
    port = 8080

@app.route('/')
def index():
    return render_template("numinput.html")
@app.route("/main", methods=["POST"])
def calculator():
	if request.form['option'] == "+": 
		calculation=str(int(request.form['Number'])+int(request.form['Number2']))
		return calculation
	elif request.form['option'] == "-": 
		calculation=str(int(request.form['Number'])-int(request.form['Number2']))
		return calculation
	elif request.form['option'] == "/": 
		calculation=str(int(request.form['Number'])/int(request.form['Number2']))
		return calculation
	elif request.form['option'] == "*": 
		calculation=str(int(request.form['Number'])*int(request.form['Number2']))
		return calculation
	elif request.form['option'] == "**": 
		calculation=str(int(request.form['Number'])**int(request.form['Number2']))
		return calculation
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
