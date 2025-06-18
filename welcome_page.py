import customtkinter as ctk
from tkinter import *
from PIL import Image
import fonctions_bdd as bd

class WelcomePage:
    def __init__(self, master, start_classic_callback, start_citation_callback):
        self.frame = Frame(master, bg="#3B8ED0")
        self.label = ctk.CTkLabel(master, text="Teacherdle", text_color="black", font=("Comic Sans MS", 60), bg_color='#3B8ED0')
        self.label.pack(padx=0.5, pady=0.5)
        self.label2 = ctk.CTkLabel(master, text="Devine tes profs de Polytech Dijon", text_color="black", font=ctk.CTkFont("Comic Sans MS", 20), bg_color='#3B8ED0')
        self.label2.pack(padx=0.5, pady=0.5)
        classic_btn_img = ctk.CTkImage(Image.open("assets/point-dinterrogation.png"), size=(40, 40))
        citation_btn_img = ctk.CTkImage(Image.open("assets/discuter.png"), size=(40, 40))
        self.classic_button = ctk.CTkButton(
            self.frame,
            text="Classique",
            image=classic_btn_img,
            compound="left",
            font=("Arial", 40),
            bg_color="#3B8ED0",
            width=320,
            height=70,
            anchor="w",
            command=start_classic_callback
        )
        self.classic_button.pack(pady=60)
        self.classic_button.bind("<Enter>", lambda e: self.classic_button.configure(font=("Arial", 42)))
        self.classic_button.bind("<Leave>", lambda e: self.classic_button.configure(font=("Arial", 40)))
        self.frame.pack(padx=100, pady=70)
        self.citation_button = ctk.CTkButton(
            self.frame,
            text="Citation",
            image=citation_btn_img,
            compound="left",
            font=("Arial", 40),
            bg_color="#3B8ED0",
            width=320,
            height=70,
            anchor="w",
            command=start_citation_callback
        )
        self.citation_button.pack(pady=60)
        self.citation_button.bind("<Enter>", lambda e: self.citation_button.configure(font=("Arial", 42)))
        self.citation_button.bind("<Leave>", lambda e: self.citation_button.configure(font=("Arial", 40)))
        self.frame.pack(padx=100, pady=70)
        
    def destroy(self):
            self.label.destroy()
            self.label2.destroy()
            self.frame.destroy()