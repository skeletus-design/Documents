import pymysql
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/login')
def index():
    return render_template("login.html")



@app.route('/reg')
def reg():
    return render_template("register.html")
            
if __name__ == "__main__":
    app.run(debug=False)
    

