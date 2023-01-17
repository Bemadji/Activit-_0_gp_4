from tkinter import *
import tkinter as tkinter

root=Tk()
root.title("Bienvenue sur la plateforme d'Orientation Universitaire !")
root.geometry("900x500+150+30")
logo=Canvas(root,width=900,height=500,bg="blue")
logo.place(x=0,y=7)
log=Label(logo,text="Bienvenue sur la plateforme",font=("arial",19,"bold"))
log.place(x=20,y=10)
identifiant=Label(logo,text="Saisir le email ou le tel",bg="blue",font=("arial",15,"bold"),fg="#fff")
identifiant.place(x=350,y=130)

mdp=Button(logo,text="Mot de passe",bg="blue",font=(arial,15))
mdp.place(x=400,y=190)

mdpentry=Entry(width=50,show="*",relief=FLAT,font="arial",12)
mdpentry.place(x=250,y=220)
identry=Entry(width=50,show="*",relief=FLAT,font="arial",12)

identifiantEntry=Entry(logo,width=40,relief=FLAT,font="arial",12)
identifiant.place(x=250,y=160)



root.mainloop()
