#разработка форсы авторизации

from flask import Flask, request, redirect, url_for, render_template
import pymysql

@app.route('/login', methods=['GET', 'POST'])
def login(self):
    if request.method == 'POST':
        self.username = request.form('username')
        self.password = request.form('password')
        
        self.Con = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="4444",
                database="test",
            )
        
        cur = self.Con.cursor()
        cur.execute("select * from login")
        self.result = cur.fetchall()
        cur.close()
        
        if self.username in 'admin' and self.password in '4444':
            print("suc") and self.main()