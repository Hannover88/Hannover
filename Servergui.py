from tkinter import *
import socket
import threading
from tkinter import messagebox
import tkinter.messagebox
import time
t = Tk()
t.geometry("450x400")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections = []
text = []
localtime = time.asctime( time.localtime(time.time()) )


#Server Funktionen 
def verbinden_1 ():
    print("Verbinde............")
    entry_text = port_entry.get()
    port = entry_text
    port = int(port)
    sock.bind(("", port))
    sock.listen(2)
    dThread= threading.Thread(target=erstellen)
    dThread.daemon = True
    dThread.start()

def send(kom, addr):
    localtime = time.asctime( time.localtime(time.time()) )

    global connections
    while True:
        data = kom.recv(1024)
        text.append(data,)
        text.append(localtime)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(kom)
            kom.close()
            break

def erstellen():
    print ("Verbunden!")
    while True:
        kom, addr = sock.accept()
        cThread = threading.Thread(target=send, args=(kom, addr))
        cThread.daemon = True
        cThread.start()
        connections.append(kom)
       
#Admin Liste
def admin ():
    m_text = "\
************************\n\
Jonas \n\
Lennart \n\
************************"
    messagebox.showinfo(message=m_text, title = "Admin")

#zeigt angemeldete Benutzer
def show_connections_2():
    show_connections=connections
    tkinter.messagebox.showinfo("Benutzer",show_connections)

#zeigt Chatverlauf
def show_text():
    show_text=text
    tkinter.messagebox.showinfo("Chat",show_text)

#Port
port_label = Label(t, text="Port: ") 
port_entry = Entry(t, bd=5, width=30)

#Speichern
er_stellen = Button(t, text="Speichern", command= verbinden_1)

#Grid
port_label.grid(column=1, row=1) 
port_entry.grid(column=2, row=1)
er_stellen.grid(column=2, row=2)

#Menuleiste
menuleiste = Menu(t)
einstellung_menu = Menu(menuleiste, tearoff=0)
einstellung_menu.add_command(label="Admin", command=admin)
einstellung_menu.add_command(label="User", command=show_connections_2)
einstellung_menu.add_command(label="Chat", command=show_text)
einstellung_menu.add_command(label="Exit", command=t.quit)

menuleiste.add_cascade(label="Einstellung", menu=einstellung_menu)

t.config(menu=menuleiste)






t.mainloop()
