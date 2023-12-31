import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from flask import Flask, request, redirect, url_for, render_template

class App:
    Con = None

    def SQL_login(self):
        try:
            self.Conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="4444",
                database="test",
            )
            curr = self.Conn.cursor()
            curr.execute("select * from login")
            self.ress = curr.fetchall()
            curr.close()
            
            self.keys = self.ress
            
            
            
        except:
            messagebox.showerror("","Error")                   
        
    #Функция создает подключение к локальной бд
    def SQL_Connect(self):
        try:
            self.Con = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="4444",
                database="test",
            )
            #Курсор, выбирающий данные из таблицы с помощью запроса
            cur = self.Con.cursor()
            cur.execute("select * from new_table")
            self.result = cur.fetchall()
            cur.close() #Важно, что перед открытием следующего курсора, необходимо закрывать текущий, чтобы это не вызывало ошибок
        except:
            messagebox.showerror("","Error")#Чисто косметический messagebox, который просто показывает ошибку подключения, в случае если та возникла
    
    #Функция очищает дерево таблицу от текущих данных
    def clear(self):
        for i in self.my_tree.get_children():
            self.my_tree.delete(i)
    
    #Функция обновляет таблицу актуальными в момент запроса данными из БД       
    def update(self):
        cur = self.Con.cursor()
        cur.execute("select * from new_table")
        self.result = cur.fetchall()
        cur.close()
        [self.my_tree.insert('', 'end', values=row) for row in self.result]
    
    #Функция открывает новое окно для добавления данных в бд        
    def add(self):
        self.icon = Tk()
        self.icon.geometry('200x250')
        self.icon.resizable('False','False')
        self.icon.title('')
        
        self.ent2 = ttk.Entry(self.icon)
        self.ent2.pack(anchor=NW)
        self.ent2.get()
        self.lbl = ttk.Label(self.icon, text='col1')
        self.lbl.place(x=140, y=1)
        
        self.ent3 = ttk.Entry(self.icon)
        self.ent3.pack(anchor=NW, pady=20)
        self.ent3.get()
        self.lbl2 = ttk.Label(self.icon, text='col2')
        self.lbl2.place(x=140, y=41)
        
        self.ent4 = ttk.Entry(self.icon)
        self.ent4.pack(anchor=NW, pady=5)
        self.ent4.get()
        self.lbl3 = ttk.Label(self.icon, text="col3")
        self.lbl3.place(x=140, y=85)
        
        bt = ttk.Button(self.icon, text='Добавить', command=self.add_this)
        bt.place(x=0, y=180)
        
        
        
        self.icon.mainloop()
    
    #Функция добавляет вписанные в предыдущем окне данные в таблицу    
    def add_this(self):
        cur = self.Con.cursor()
        cur.execute(f"INSERT INTO new_table (col, col2, col3) VALUES ('{self.ent2.get()}','{self.ent3.get()}','{self.ent4.get()}');")
        self.Con.commit()
        cur.close()#закрытие курсора
        self.icon.destroy()#закрытие окна функции add
        self.clear()#очищение данных дерева
        self.update()#обновление данных дерева
        
        
    #По схожей логике работает функция для обновления данных    
    def delete(self):
        cur = self.Con.cursor()
        cur.execute(f"delete from new_table where id={self.my_tree.set(self.my_tree.selection(), '#1')};")
        self.Con.commit()
        cur.close()
        self.clear()
        self.update()
        
    #Функция внесения данных в таблицу дерева
    def insert(self):
        [self.my_tree.insert('', 'end', values=row) for row in self.result]
    
    #Открытие основного окна, она вызывается первой, следущие функции в основном работают по очереди как каскад
    def main(self):
        self.window = Tk()
        self.window.geometry('600x400')
        self.window.title('Редактор')
        self.window.configure(bg="#FFFFE0")
        self.window.resizable('False','False')
        self.lb() #лебл
        self.buttons() #кнопки
        self.tree() #дерево
        self.insert() #добавление в начальную таблицу
        
        self.SQL_Connect
    
    #Дерево таблицы
    def tree(self):
        self.my_tree = ttk.Treeview(self.window, columns=('id', 'col1', 'col2', 'col3'), show='headings')
        self.my_tree.column("id", width=90)
        self.my_tree.column("col1", width=90)
        self.my_tree.column("col2", width=90)
        self.my_tree.column("col3", width=90)
        self.my_tree.grid(column=0, row=0)
        self.SQL_Connect()
        
    #Лейбл
    def lb(self):
        self.lb = Label(self.window, text="текст", font="bald 30")
        self.lb.configure(bg="blue") 
        self.lb.place(x=100, y=500)

    #Функция кнопок добавить и удалить
    def buttons(self):
        self.style = ttk.Style()        
        
        self.bt1 = ttk.Button(text="Добавить", command=self.add)
        self.bt1.place(x=100,y=350)
        self.bt2 = ttk.Button(text="Удалить", command=self.delete)
        self.bt2.place(x=180, y=350)
        
    def login(self):
        #Окно формы авторизации
        self.login1 = Tk()
        self.login1.geometry('300x250')
        self.login1.resizable('False','False')
        self.login1.title()
        
        #Поле ввода для логина
        self.entry1 = ttk.Entry(self.login1)
        self.entry1.pack(anchor=NW, pady=5)
        self.entry1.get()
        self.login_label = ttk.Label(self.login1, text="Логин")
        self.login_label.place(x=140, y=5)
        
        #Поле ввода пароля
        self.entry2 = ttk.Entry(self.login1)
        self.entry2.pack(anchor=NW, pady=20)
        self.entry2.get()
        self.password_label = ttk.Label(self.login1, text="Пароль")
        self.password_label.place(x=140, y=50)
        
        self.ab = ttk.Button(self.login1, text="Авторизоваться", command=self.login_try)
        self.ab.place(x=140, y=200)
        
        self.SQL_login()
    
    def login_try(self):
        self.login_ = 'admin'
        self.password = 'admin'
    
        if  self.ress == (f"'1', '{self.entry1.get()}', '{self.entry2.get()}'"):
        #self.login_ == self.entry1.get() and self.entry2.get():
            self.login1.destroy()
            self.main()
            
        else:
            messagebox.showerror("","Error")
            
                    
if __name__ == "__main__":
    app = App()
    
    app.login() 

    app.login1.mainloop()
    

((1, 'admin', 'admin'),)