import customtkinter as ctk
from tkinter import *
from PIL import Image
import fonctions_bdd as bd

class WelcomePage:
    def __init__(self, master, start_classic_callback):
        self.frame = Frame(master, bg="#3B8ED0")
        self.label = ctk.CTkLabel(master, text="Devine tes profs de Polytech Dijon", text_color="black", font=ctk.CTkFont("Comic Sans MS", 20), bg_color='#3B8ED0')
        self.label.pack(padx=0.5, pady=0.5)
        classic_btn_img = ctk.CTkImage(Image.open("assets/point-dinterrogation.png"), size=(40, 40))
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
        
    def destroy(self):
            self.label.destroy()
            self.frame.destroy()

class ClassicPage:
    def __init__(self, master, noms, prof_cible, back_callback):
        self.master = master
        self.noms = noms
        self.prof_cible = prof_cible
        self.compteur_essais = 0
        self.current_row = 1
        self.search_var = ctk.StringVar()

        self.frame = ctk.CTkFrame(master, fg_color="#3B8ED0", corner_radius=0)
        self.frame.pack(fill="both", expand=True)

        self.menu_button = ctk.CTkButton(self.frame, text="Menu Principal", font=ctk.CTkFont(size=20), fg_color="#6062f9", command=back_callback)
        self.menu_button.pack(anchor='nw', padx=100, pady=10)

        self.create_search_bar()
        self.create_table()

    def destroy(self):
        self.frame.destroy()

    def create_table(self):
        categories = ["Professeur", "Genre", "Date de thèse", "type", "Matière", "Fonction particulière"]
        self.table_frame = ctk.CTkFrame(self.frame, fg_color="white", corner_radius=8)
        self.table_frame.pack(fill="both", padx=20, pady=20)

        for col in range(len(categories)):
            self.table_frame.grid_columnconfigure(col, weight=1)
            header = ctk.CTkLabel(
                self.table_frame, text=categories[col], font=ctk.CTkFont("Arial", 16, weight="bold"),
                fg_color="white", text_color="black", padx=15, pady=10
            )
            header.grid(row=0, column=col, sticky="nsew", padx=5, pady=5)

    def create_search_bar(self):
        self.search_var.trace_add("write", lambda *args: self.update_suggestions())

        main_frame = ctk.CTkFrame(self.frame, fg_color=None)
        main_frame.pack(padx=40, pady=40)

        search_frame = ctk.CTkFrame(main_frame, fg_color=None)
        search_frame.pack(fill="x", pady=(0, 15))

        entry = ctk.CTkEntry(search_frame, textvariable=self.search_var, font=ctk.CTkFont("Arial", 18))
        entry.pack(side="left", fill="x", expand=True)

        button = ctk.CTkButton(search_frame, text="Entrer", command=self.enter_pressed, fg_color="#6062f9", font=ctk.CTkFont("Arial", 16))
        button.pack(side="right", padx=(15, 0))

        self.suggestions_list = Listbox(main_frame, height=5, font=("Arial", 20), bg="white", selectbackground="#00e1ff")
        self.suggestions_list.pack(fill="x", pady=(5, 0))
        self.suggestions_list.bind("<<ListboxSelect>>", self.select_suggestion)

        self.master.bind("<Return>", lambda event: self.enter_pressed())

    def update_suggestions(self):
        search_term = self.search_var.get().lower()
        if not search_term:
            self.suggestions_list.pack_forget()
        else:
            self.suggestions_list.pack()
            self.suggestions_list.delete(0, ctk.END)
            suggestions = [nom for nom in self.noms if nom.lower().startswith(search_term)]
            for s in suggestions:
                self.suggestions_list.insert(ctk.END, s)

    def select_suggestion(self, event):
        if self.suggestions_list.curselection():
            selected = self.suggestions_list.get(self.suggestions_list.curselection())
            self.search_var.set(selected)

    def enter_pressed(self):
        nom = self.search_var.get()
        if nom in self.noms:
            self.noms.remove(nom)
            self.compteur_essais += 1
            # logique de victoire/défaite + ajout des infos au tableau
            print(f"Tentative {self.compteur_essais} : {nom}")
            self.search_var.set("")
            self.update_suggestions()


