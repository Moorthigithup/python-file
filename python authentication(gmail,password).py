from tkinter import*
import tkinter.messagebox as MessageBox
import sqlite3 as db



from socket import *
from threading import *
from tkinter import *





import pyrebase
from getpass import getpass


import pyrebase
from getpass import getpass



root=Tk();   
EMAIL=StringVar()
PASSWORD=StringVar()





def database():


     firebaseConfig = {
    "apiKey": "AIzaSyB9XoyWHj9j8rAW3RUL5v1Tos_uYQPT9EU",
    "authDomain": "moorthi-773be.firebaseapp.com",
    "databaseURL": "https://moorthi-773be.firebaseio.com",
    "projectId": "moorthi-773be",
    "storageBucket": "moorthi-773be.appspot.com",
    "messagingSenderId": "262300063641",
    "appId": "1:262300063641:web:f997e9d0c8614b64ec6508",
    "measurementId": "G-TBZ45N8K0F"
  }


    

    
    
    
     


     firebase=pyrebase.initialize_app(firebaseConfig)
     



     auth=firebase.auth()

     email1=EMAIL.get()
     password1=PASSWORD.get()


     user=auth.create_user_with_email_and_password(email1,password1)

     if len(user)>0:
          root=Tk();
          root.geometry('300x400')
          root.title("welcome")
          lebel=Label(root,text="WELCOME",font=('arial',20),bd=25)
          lebel.pack()
          m=Frame(root)
          m.pack(side=TOP,fill=X)
          name=Label(m,text= "NAME:",font= ('arial',14),bd=15)
          name1=Label(m,text= "PASSWORD:",font= ('arial',14),bd=15)
          nameE=Entry(m,textvariable=EMAIL)
          passE=Entry(m,textvariable=PASSWORD)
          nameE.grid(row=1,column=2)
          passE.grid(row=2,column=2)
          name.grid(row=1,sticky=W)
          name1.grid(row=2,sticky=W)
          login=Button(root,text="LOGIN",command=chek)
          login.place(x=60,y=300)

#
          




def chek():
     firebaseConfig = {
    "apiKey": "AIzaSyB9XoyWHj9j8rAW3RUL5v1Tos_uYQPT9EU",
    "authDomain": "moorthi-773be.firebaseapp.com",
    "databaseURL": "https://moorthi-773be.firebaseio.com",
    "projectId": "moorthi-773be",
    "storageBucket": "moorthi-773be.appspot.com",
    "messagingSenderId": "262300063641",
    "appId": "1:262300063641:web:f997e9d0c8614b64ec6508",
    "measurementId": "G-TBZ45N8K0F"
  }



    
    


     firebase=pyrebase.initialize_app(firebaseConfig)
     



     auth=firebase.auth()

     email1=EMAIL.get()
     password1=PASSWORD.get()


     login=auth.sign_in_with_email_and_password(email1,password1)



     if len(login)>0:
          root=Tk();
          root.geometry('300x400')
          root.title("welcome")
          lebel=Label(root,text="HEY USER",font=('arial',20),bd=25)
          lebel.pack()
          m=Frame(root)
          m.pack(side=TOP,fill=X)

          
          
                   



          
        
     
    
             
               

        
       



        
def register():
    l2=Label(m,text="EMAIL: ",font=('arial',14),bd=25)
    l3=Label(m,text="PASSWORD: ",font=('arial',14),bd=25)
    
    
    l2.grid(row=1,sticky=W)
    l3.grid(row=2,sticky=W)
    
    p_name=Entry(m,textvariable=EMAIL)
    p_password=Entry(m,textvariable=PASSWORD)
    p_name.grid(row=1,column=2)
    p_password.grid(row=2,column=2)
    
    register=Button(root,text="REGISTER",command=database)
    register.place(x=90,y=330)
    exitButton=Button(root,text="EXIT",bg="#EEEEEE",command=root.destroy)
    exitButton.place(x=100,y=360)
 

root.geometry('300x400')
root.title("welcome")
lebel=Label(root,text="WELCOME",font=('arial',20),bd=25)
lebel.pack()
m=Frame(root)
m.pack(side=TOP,fill=X)
name=Label(m,text= "NAME:",font= ('arial',14),bd=15)
name1=Label(m,text= "PASSWORD:",font= ('arial',14),bd=15)
nameE=Entry(m,textvariable=EMAIL)
passE=Entry(m,textvariable=PASSWORD)
nameE.grid(row=1,column=2)
passE.grid(row=2,column=2)
name.grid(row=1,sticky=W)
name1.grid(row=2,sticky=W)
login=Button(root,text="LOGIN",command=chek)
login.place(x=60,y=300)
exitButton=Button(root,text="EXIT",bg="#EEEEEE",command=root.destroy)
exitButton.place(x=85,y=330)

#sign in
signin=Button(root,text="SIGN IN",command=register)
signin.place(x=120,y=300)


root.mainloop()
