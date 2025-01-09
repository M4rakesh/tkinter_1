import sqlite3
from tkinter import Tk, Label, Button, END, messagebox, ttk 

def init_db():
    try:
        conn=sqlite3.connect('kinoteka1.db')
        c= conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS kinoteka (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nosaukums TEXT,
                                zanrs TEXT,
                                gads INTEGER
                                )''')
        conn.commit()
        conn.close() 
    except Exception as e:
        messagebox.showerror("Datubāzes ķļūda",f"Neizdevās inicializēt datubāzi:{e}")
    
def load_kino_nosaukums():
    try:
        kino_combobox['values']= ()#notirit esošos nosaukumus
        conn=sqlite3.connect("kinoteka1.db")
        print("a")
        cursor = conn.cursor("SELECT nosaukums FROM kinoteka")
        print("aa")
        nosaukums=[]
        kino_all=cursor.fetchone()
        print("aaa")
        for kino in kino_all:
            nosaukums.append(kino[0])
            print("aaaa")
        conn.close()

        kino_combobox['values']= nosaukums
    except Exception as e:
        messagebox.showerror("Kļūda",f"Neizdevās nolasīt kino nosaukumus:{e}")

def show_kino_details():
    try:
        selected_kino= kino.combobox.get()
        if not selected_kino:
            messagebox.showwarning("Bridinajums","Lūdzu izvelieties kino no sarakssta")
            return
        conn=sqlite3.connect("kinoteka1.db")
        c=conn.cursor()
        c.execute("SELCT * FROM books WHERE kino=?",(selected_kino))
        kino=c.fetchall()
        conn.close()

        if kino:
            messagebox.showinfo("Kino Informācija", f"Nosaukums: {kino[1]}\nZanrs: {kino[2]}\nGads: {kino[3]}")
        else:
            messagebox.showwarning("Kļūda", "Neizdevās atrast informāciju par kino.")
    except Exception as e:
        messagebox.showerror("Kļūda", f"Neizdevās parādīt kino informāciju: {e}") 


root = Tk()
root.title("Bibliotēkas Kino Sistēma")

Label(root,text="Izveleties Kino").grid(row=0,column=0,padx=10,pady=10)
kino_combobox = ttk.Combobox(root,width=47,state="readonly")
kino_combobox.grid(row=1,column=0,padx=10,pady=10)

Button(root,text="Rādit Informaciju",command=show_kino_details).grid(row=2,column=0,padx=10,pady=10)

init_db()
load_kino_nosaukums()
root.mainloop()
