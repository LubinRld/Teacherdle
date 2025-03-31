from tkinter import *

Main_window = Tk()
Main_window.title("Teacherdle")
Main_window.geometry("1080x720")
Main_window.iconbitmap("Logo.ico")
Main_window.config(background='#00e1ff')
Label_Teacherdle = Label(Main_window, text = "Teacherdle", font=("Helvetica", 40), bg='#00e1ff')
Label_Teacherdle.pack(padx=0.5, pady=12)

def Create_Welcome_page():
    Button_Frame = Frame(Main_window, bg= '#00e1ff')
    Label_Description = Label(Main_window, text = "Devine tes profs de Polytech Dijon",font=("Helvetica", 20), bg='#00e1ff')
    Label_Description.pack(padx=0.5, pady=0.5)
    Classique_button = Button(Button_Frame, text = "Classique", font=("Arial", 30), bg='#00e1ff', width=10, command=lambda:(Button_Frame.destroy(), Label_Description.destroy()))
    Citation_button = Button(Button_Frame, text = "Citation", font=("Arial", 30), bg= '#00e1ff', width=10, command=lambda:(Button_Frame.destroy(), Label_Description.destroy()))
    Classique_button.pack(padx=10, pady=0)
    Citation_button.pack(padx=10, pady=50)
    Button_Frame.pack(padx=10, pady=70)

Create_Welcome_page()
Main_window.mainloop()