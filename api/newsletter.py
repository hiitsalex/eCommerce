from flask import Flask
from flask import render_template
from flask import request,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
 
@app.route('/waitingList')
def waitinglist():
    return render_template("waitinglist.html")
@app.route('/api/newsletter', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')