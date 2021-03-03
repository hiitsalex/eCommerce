from flask import Flask
from flask import render_template
from flask import request, redirect,flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/waitingList')
def waitinglist():
    return render_template("waitinglist.html")


@app.route('/newsletter', methods=['POST'])
def signup():
    email = request.form['email']
    name = request.form['name']
    file = open("Emails.txt", "a")
    input = name+", "+email+";\n"
    file.write(input)
    file.close()
    
    flash("Your response was recorded. Thank you! To be continued..")
    
    return render_template("page.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
