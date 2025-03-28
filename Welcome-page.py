from tkinter import *

Welcome_window = Tk()
Welcome_window.title("Teacherdle")
Welcome_window.geometry("1080x720")
Welcome_window.iconbitmap("Logo.ico")
Welcome_window.config(background='#00e1ff')
Button_Frame = Frame(Welcome_window, bg= '#00e1ff')
Label_Teacherdle = Label(Welcome_window, text = "Teacherdle", font=("Helvetica", 40), bg='#00e1ff')
Label_Teacherdle.pack()
Classique_button = Button(Button_Frame, text = "Classique", font=("Arial", 30), bg='#00e1ff', width=10)
Citation_button = Button(Button_Frame, text = "Citation", font=("Arial", 30), bg= '#00e1ff', width=10)



Classique_button.pack()
Citation_button.pack()
Button_Frame.pack()
Welcome_window.mainloop()