import pymysql
from selenium import webdriver

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
            
    def Selenium(self):
        try:
            driver = webdriver.Chrome()
            driver.get("login.html")
        except:
            print("err")
            
            
if __name__ == "__main__":
    app = App()
    
    app.SQL_Connect()
    
