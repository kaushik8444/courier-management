# from cgitb import text
# from email.mime import image
from tkinter import *
# from tkinter import ttk
from tkinter import messagebox
# from tkinter import font
# from turtle import width
import mainPage


checkUsername = 'kaushik'
checkPassword = '8522'

def loginWin():
    # onClick action
    def btn_click():
        username = username_enter.get()
        password = password_enter.get()
        # mainPage.win()
        if(username == checkUsername and password == checkPassword):
            window.destroy()
            mainPage.win()
        else:
            messagebox.showerror(title="Error" , message="Invalid Credentials")

    # window creation
    window = Tk()

    # width = window.winfo_screenwidth()
    # height = window.winfo_screenheight()
    # # window.geometry("%dx%d" % (width,height))
    # # window.eval('tk::PlaceWindow . center')

    window.title("Login Page")

    '''

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Labels, Buttons and textEntry
    ttk.Label(frm,text="User Name:",padding=10).grid(column=0,row=0)
    username_enter = Entry(frm)
    username_enter.grid(column=1,row=0)

    ttk.Label(frm,text="Password:",padding=10).grid(column=0,row=1)
    password_enter = Entry(frm)
    password_enter.grid(column=1,row=1)

    loginImg = PhotoImage(file=r"courierBackground.png").subsample(25,25)
    # loginImg = photo.subsample(25,25)

    loginBtn = ttk.Button(frm, text="Login", command=btn_click,image=loginImg,compound = RIGHT)
    loginBtn.grid(column=1,row=3)

    logoutImg = PhotoImage(file=r"courierBackground.png").subsample(25,25)
    # logoutImg = photo1.subsample(25,25)
    exitBtn = ttk.Button(frm, text="Exit", command=window.destroy, image=logoutImg,compound = RIGHT)
    exitBtn.grid(column=1,row=4)


'''

    window.geometry("1350x720")

    my_canvas = Canvas(window,width=1350,height=720,)
    my_canvas.pack(fill="both",expand=True)
    bg1 = PhotoImage(file='courierBackground.png')
    # bg = bg1.subsample(4,4)

    my_canvas.create_image(0,0,image=bg1,anchor="nw")
    my_canvas.create_text(675,100,text="WELCOME TO EXPRESS DELIVERY",font=("Helvetica",30,"bold"),fill="black")

    # Labels
    my_canvas.create_text(625,335,text="USERNAME:",font=(30),fill="black")
    my_canvas.create_text(625,360,text="PASSWORD:",font=(30),fill="black")

    username_enter = Entry(window)
    my_canvas.create_window(740,335, window=username_enter)

    password_enter = Entry(window)
    my_canvas.create_window(740,360, window=password_enter)

    # Buttons
    loginImg = PhotoImage(file=r"courierBackground.png").subsample(30,30)
    btn1 = Button(window, text="Login", command=btn_click)

    logoutImg = PhotoImage(file=r"courierBackground.png").subsample(30,30)   
    btn2 = Button(window, text="Exit", command=window.destroy)

    btn1_win = my_canvas.create_window(675,405, window=btn1)
    btn2_win = my_canvas.create_window(675,440, window=btn2)

    '''
    bg1 = PhotoImage(file='C:\courierBackground.png')
    bg = bg1.subsample(4,4)
    bg_label = Label(window,image=bg)
    bg_label.place(x=0,y=0,relwidth=1,relheight=1)

    Label(window,text="User Name:").pack(pady=10)
    username_enter = Entry(window)
    username_enter.pack()
'''
    window.mainloop()
    

loginWin()
