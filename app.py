from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):
        # create db object
        self.image_result = None
        self.image_input = None
        self.dbo = Database()
        self.apio = API()


        # Load Login GUI
        self.name_input = None
        self.password_input = None
        self.email_input = None
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):

        self.clear()

        heading = Label(self.root,text='NeuroVerse',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root,text='Enter email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root,text='Login',width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now',command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text='NeuroVerse', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        # Clear the existing GUI
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from GUI
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success','Registration Successful. You can Login Now')
        else:
            messagebox.showerror('Error','Email already exists')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email/password')

    def home_gui(self):

        self.clear()

        heading = Label(self.root, text='NeuroVerse', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        image_btn = Button(self.root, text='Image Generation', width=30, height=4, command=self.image_gui)
        image_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='NER', width=30, height=4, command=self.perform_registration)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4, command=self.perform_registration)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def image_gui(self):

        self.clear()

        heading = Label(self.root, text='NeuroVerse', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Image Generation', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the prompt')
        label1.pack(pady=(20, 10))

        self.image_input = Entry(self.root, width=50)
        self.image_input.pack(pady=(5, 10), ipady=4)

        image_btn = Button(self.root, text='Generate your image', command=self.do_image_generation)
        image_btn.pack(pady=(10, 10))

        self.image_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.image_result.pack(pady=(20, 10))
        self.image_result.configure(font=('verdana', 16))


        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_image_generation(self):

        text = self.image_input.get()
        result = self.apio.image_generation(text)
        print(result)





nlp = NLPApp()









