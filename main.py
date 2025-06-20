import customtkinter as ctk
from tkinter import * 
import fonctions_bdd as bd
from citation_page import *
from classic_page import *
from welcome_page import *
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
            start_classic_callback=self.show_classic_page,
            start_citation_callback=self.show_citation_page
        )
    
    def show_classic_page(self):
        self.clear_current_page()
        self.names= bd.send_names()
        self.target_teacher=bd.choice_teachers()
        self.current_page = ClassicPage(
            master=self.window,
            names=self.names,
            target_teacher=self.target_teacher,
            back_callback=self.show_welcome_page,
            restart_callback=self.show_classic_page
        )

    def show_citation_page(self):
        self.clear_current_page()
        self.name= bd.send_names()
        self.citation=bd.choice_citations()
        self.current_page = CitationPage(
            master=self.window,
            name=self.name,
            citation=self.citation,
            back_callback=self.show_welcome_page,
            restart_callback=self.show_citation_page
        )
if __name__=="__main__":
    TeacherdleApp()
