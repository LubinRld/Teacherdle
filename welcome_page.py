import customtkinter as ctk
from tkinter import *
from PIL import Image
import fonctions_bdd as bd

class WelcomePage:
    def __init__(self, master, start_classic_callback, start_citation_callback):
        self.frame = Frame(master, bg="#3B8ED0")
        self.title = ctk.CTkLabel(master, text="Teacherdle", text_color="black", font=("Comic Sans MS", 80), bg_color='#3B8ED0')
        self.title.pack(padx=0.5, pady=10)
        self.label = ctk.CTkLabel(master, text="Devine tes profs de Polytech Dijon", text_color="black", font=ctk.CTkFont("Comic Sans MS", 40), bg_color='#3B8ED0')
        self.label.pack(padx=0.5, pady=0.5)
        classic_btn_img = ctk.CTkImage(Image.open("assets/point-dinterrogation.png"), size=(60, 60))
        citation_btn_img = ctk.CTkImage(Image.open("assets/discuter.png"), size=(60, 60))
        self.classic_button = ctk.CTkButton(
                self.frame,
                text="Classique",
                image=classic_btn_img,
                compound="left",
                font=("Arial", 60),
                bg_color="#3B8ED0",
                width=320,
                height=70,
                anchor="w",
                command=start_classic_callback
                )
        self.classic_button.pack(pady=50)
        self.classic_button.bind("<Enter>", lambda e: self.classic_button.configure(font=("Arial", 62)))
        self.classic_button.bind("<Leave>", lambda e: self.classic_button.configure(font=("Arial", 60)))
        self.frame.pack(padx=100, pady=70)
        self.citation_button = ctk.CTkButton(
            self.frame,
            text="Citation",
            image=citation_btn_img,
            compound="left",
            font=("Arial", 60),
            bg_color="#3B8ED0",
            width=320,
            height=70,
            anchor="w",
            command=start_citation_callback
        )
        self.citation_button.pack(pady=10)
        self.citation_button.bind("<Enter>", lambda e: self.citation_button.configure(font=("Arial", 62)))
        self.citation_button.bind("<Leave>", lambda e: self.citation_button.configure(font=("Arial", 60)))
        self.frame.pack(padx=100, pady=70)

        intro_text = (
            "Ce jeu vous propose de deviner à l'aide d'indices différents professeurs de Polytech Dijon. \n"
            "Toutes les informations que nous avons sont des informations publics, donc potentiellement source d'erreur ou mal daté. \n"
            "De plus, nous utilisons l'expérience de notre promotion comme base pour le jeu, \n"
            "certaines informations peuvent alors être inexactes si vous avez eu un parcours différent. \n"
            "Maintenant, profitez-en pour mieux connaître vos profs ! \n ")

        self.description = ctk.CTkLabel(master, text=intro_text, text_color="black", font=("Comic Sans MS", 18), bg_color='#3B8ED0', anchor='w')
        self.description.pack(padx=0.5, pady=15)
        
    def destroy(self):
            self.title.destroy()
            self.label.destroy()
            self.description.destroy()
            self.frame.destroy()