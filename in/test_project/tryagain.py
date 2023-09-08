import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class App:
    Con = None

    def SQL_Connect(self):
        try:
            self.Con = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="4444",
                database="test",
            )
            
            cur = self.Con.cursor()
            cur.execute("select * from new_table")
            self.result = cur.fetchall()
            cur.close()

        except:
            messagebox.showerror("","Error")
            
    def clear(self):
        for i in self.my_tree.get_children():
            self.my_tree.delete(i)
            
    def update(self):
        cur = self.Con.cursor()
        cur.execute("select * from new_table")
        self.result = cur.fetchall()
        cur.close()
        [self.my_tree.insert('', 'end', values=row) for row in self.result]
            
    def add(self):
        self.icon = Tk()
        self.icon.geometry('600x250')
        self.icon.resizable('False','False')
        
        self.ent2 = ttk.Entry(self.icon)
        self.ent2.pack(anchor=NW, padx=0, pady=5)
        self.ent2.get()
        
        self.ent3 = ttk.Entry(self.icon)
        self.ent3.pack(anchor=NW, padx=0, pady=10)
        self.ent3.get()
        
        self.ent4 = ttk.Entry(self.icon)
        self.ent4.pack(anchor=NW, padx=0, pady=15)
        self.ent4.get()
        
        bt = ttk.Button(self.icon, text='Добавить', command=self.add_this)
        bt.place(x=0, y=140)
        
        
        
        self.icon.mainloop()
        
    def add_this(self):
        cur = self.Con.cursor()
        cur.execute(f"INSERT INTO new_table (col, col2, col3) VALUES ('{self.ent2.get()}','{self.ent3.get()}','{self.ent4.get()}');")
        self.Con.commit()
        cur.close()
        self.icon.destroy()
        self.clear()
        self.update()
        
        
        
    def delete(self):
        cur = self.Con.cursor()
        cur.execute(f"delete from new_table where id={self.my_tree.set(self.my_tree.selection(), '#1')};")
        self.Con.commit()
        cur.close()
        self.clear()
        self.update()
        
    
    def insert(self):
        [self.my_tree.insert('', 'end', values=row) for row in self.result]
    
    def main(self):
        self.window = Tk()
        self.window.geometry('600x600')
        self.window.resizable('False','False')
        self.lb()
        self.buttons()
        self.tree()
        self.insert()
    
    def tree(self):
        self.my_tree = ttk.Treeview(self.window, columns=('id', 'col1', 'col2', 'col3'), show='headings')
        self.my_tree.column("id", width=70)
        self.my_tree.column("col1", width=70)
        self.my_tree.column("col2", width=70)
        self.my_tree.column("col3", width=70)
        self.my_tree.grid(column=0, row=0)
        self.SQL_Connect()

    def lb(self):
        self.lb = Label(self.window, text="текст", font="bald 30") 
        self.lb.place(x=100, y=500)

    def buttons(self):
        self.bt1 = ttk.Button(text="Добавить", command=self.add)
        self.bt1.place(x=100,y=450)
        self.bt2 = ttk.Button(text="Удалить", command=self.delete)
        self.bt2.place(x=170, y=450)
        self.bt3 = ttk.Button(text="test", command=self.update)
        self.bt3.place(x=270, y=450)

if __name__ == "__main__":
    app = App()
    
    app.main()

    app.window.mainloop()

