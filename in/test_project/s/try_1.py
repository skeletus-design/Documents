import pymysql
from flask import Flask, render_template, request 

class App:
    Con = None
    
    def SQL_Connect(self):
        try:
            self.Con = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="4444",
                database="team",
            )
            print('Connect')
        except:
            print('Allert')
            
    def home(self):
        try:
            return render_template("login.html")
            
        except:
            print("error_flask")
            
            
if __name__ == "__main__":
    app = App()
    
    app.SQL_Connect()
    
