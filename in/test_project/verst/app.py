import pymysql
from flask import Flask, render_template, url_for


bd = pymysql.connect("localhost", "root", "4444", "team")

app = Flask(__name__)
api = Api(app)


@app.route('/')
@app.route('/login')
def index():
    return render_template("login.html")
def Name():
    cursor = bd.cursor()
    sql = "SELECT * FROM "


@app.route('/reg')
def reg():
    return render_template("register.html")
            
if __name__ == "__main__":
    app.run(debug=False)
    


