import customtkinter as ctk
from tkinter import * 
import fonctions_bdd as bd
from create_widget import ClassicPage, WelcomePage
from PIL import Image

class TeacherdleApp:
    def __init__(self):
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")
        self.window=ctk.CTk()
        self.window.title("Teacherdle")
        self.window.geometry("1080x720")
        self.window.iconbitmap("assets/Logo.ico")
        self.window.config(background='#3B8ED0')
        self.noms=bd.envoie_noms() 
        self.prof_cible=bd.choix_prof()
        self.current_page = None
        self.show_welcome_page()
        self.window.mainloop()
    
    def clear_current_page(self):
        if self.current_page:
            self.current_page.destroy()
            self.current_page = None

    def show_welcome_page(self):
        self.clear_current_page()
        self.current_page=WelcomePage(
            master=self.window,
            start_classic_callback=self.show_classic_page
        )
    
    def show_classic_page(self):
        self.clear_current_page()
        self.noms= bd.envoie_noms()
        self.prof_cible=bd.choix_prof()
        self.current_page = ClassicPage(
            master=self.window,
            noms=self.noms,
            prof_cible=self.prof_cible,
            back_callback=self.show_welcome_page
        )

if __name__=="__main__":
    TeacherdleApp()
