from tkinter import *
import socket
import threading
import time
from tkinter import messagebox
import tkinter.messagebox
fenster=Tk()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def Speichern():
    entry_text=eingabefeld.get()
    entry_text2= eingabefeld2.get()
    entry_text2=int(entry_text2)
    s.connect((entry_text, entry_text2))
    ip = entry_text
    verbinden(ip)

 

def antwort(ip):
    antwort=s.recv(1024)
    print("[{}]{}".format(ip,antwort.decode()))


def nachricht ():
    nachricht = input("Nachricht: ")
    s.send(nachricht.encode())
def verbinden (ip):
    while True:
        time.sleep(0.5)   
        dThread  = threading.Thread(target = nachricht)
        dThread.daemon= True
        dThread.start()
        cThread  = threading.Thread(target = antwort, args = (ip, ))
        cThread.daemon=True
        cThread.start()
def Credits():
    m_text = "\
************************\n\
Autor: LENNART\n\
Date: IRGENDWANN\n\
Version: 1.07alpha\n\
************************"

    messagebox.showinfo(message=m_text, title = "Credits")

def show_ip():
    show_ip=eingabefeld.get()
    tkinter.messagebox.showinfo("IP",show_ip)
def show_port():
    show_port=eingabefeld2.get()
    tkinter.messagebox.showinfo("Port",show_port)
    

#GUI
fenster.geometry("450x400")
fenster.title("CLIENT")

#Netzwerk
eingabefeld= Entry(fenster, bd=5, width=30)
my_label=Label(fenster, text="Gib die IP Adresse ein:")
button_speichern=Button(fenster, text="Speichern",command=Speichern)
button_quit=Button(fenster, text="Beenden",command=fenster.quit)
ip_label=Label(fenster)
menuleiste=Menu(fenster)
my_label2=Label(fenster, text="Gib den Port ein:")
eingabefeld2=Entry(fenster, bd=5, width=30)

#Menuleiste
help_menu=Menu(menuleiste, tearoff=0)
credits_menu=Menu(menuleiste, tearoff=0)
menuleiste.add_cascade(label="Help",menu=help_menu)
menuleiste.add_cascade(label="Credits",menu=credits_menu)
credits_menu.add_command(label="Credits!",command=Credits)
fenster.config(menu=menuleiste)
help_menu.add_command(label="IP",command=show_ip)
help_menu.add_command(label="Port",command=show_port)

#wo stehen sie?
eingabefeld2.grid(row=2,column=1)
my_label2.grid(row=2,column=0)
ip_label.grid(row=0,column=1)
button_quit.grid(row=3, column=1)
button_speichern.grid(row=3, column=0)
my_label.grid(row=1, column=0)
eingabefeld.grid(row=1,column=1)



fenster.mainloop()

