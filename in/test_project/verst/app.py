import pymysql
from flask import Flask, render_template, url_for


    
def SQL_Connect():
    try:
        Con = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="4444",
            database="team",
        )
        print('Connect')
    except:
        print('Allert')

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
    


