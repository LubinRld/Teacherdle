import customtkinter as ctk
from tkinter import *
from PIL import Image
import fonctions_bdd as bd
import threading
import random

class WelcomePage:
    def __init__(self, master, start_classic_callback):
        self.frame = Frame(master, bg="#3B8ED0")
        self.label = ctk.CTkLabel(master, text="Teacherdle", text_color="black", font=("Comic Sans MS", 60), bg_color='#3B8ED0')
        self.label.pack(padx=0.5, pady=0.5)
        self.label2 = ctk.CTkLabel(master, text="Devine tes profs de Polytech Dijon", text_color="black", font=ctk.CTkFont("Comic Sans MS", 20), bg_color='#3B8ED0')
        self.label2.pack(padx=0.5, pady=0.5)
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
            self.label2.destroy()
            self.frame.destroy()

class ClassicPage:
    def __init__(self, master, noms, prof_cible, back_callback):
        self.master = master 
        self.noms = noms
        self.prof_cible = prof_cible
        self.compteur_essais = 0
        self.current_row = 1
        self.search_var = ctk.StringVar()
        self.back_callback = back_callback

        self.frame = ctk.CTkFrame(master, fg_color="#3B8ED0", corner_radius=0)
        self.label = ctk.CTkLabel(master, text="Teacherdle", text_color="black", font=("Comic Sans MS", 60), bg_color='#3B8ED0')
        self.label.pack(padx=0.5, pady=0.5)
        self.label2 = ctk.CTkLabel(master, text="Devine tes profs de Polytech Dijon", text_color="black", font=ctk.CTkFont("Comic Sans MS", 20), bg_color='#3B8ED0')
        self.label2.pack(padx=0.5, pady=0.5)
        self.frame.pack(fill="both", expand=True)

        self.menu_button = ctk.CTkButton(self.frame, text="Menu Principal", font=ctk.CTkFont(size=20), fg_color="#6062f9", command=back_callback)
        self.menu_button.pack(anchor='nw', padx=100, pady=10)

        self.create_search_bar()
        self.create_table()

    def destroy(self):
        self.label.destroy()
        self.label2.destroy()
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
    
    def create_answer(self, data):
        

        reussi = 0
        for col, info in enumerate(data[0]):
            answer = self.prof_cible[col]
            if answer == info:
                reussi += 1

            label = ctk.CTkLabel(
                self.table_frame,
                text=info + self.create_fleche(info, answer),
                fg_color=self.create_color(info, answer),
                text_color="black",
                font=ctk.CTkFont(size=14),
                width=120,
                height=30,
                corner_radius=8
            )
            label.grid(row=self.current_row, column=col, sticky="nsew", padx=1, pady=5)

        if reussi == 6:
            self.show_win_animation()
        elif self.compteur_essais >= 6:
            self.show_defeat_animation()
            return
        else:
            self.compteur_essais += 1
            self.current_row += 1

    def create_fleche(self, info, answer):
        num = sum(1 for i in info if i.isdigit())
        arrow = ""
        if num == 4:
            if info > answer:
                arrow = " ▼"
            elif answer > info:
                arrow = " ▲"
        return arrow
    
    def create_color(self, info, answer):
        bg = "#ff6666"  # rouge clair
        infos_split = info.split()
        answer_split = answer.split()
        split = sum(1 for k in infos_split for l in answer_split if k == l)
        if split > 0:
            bg = "#ffa500"  # orange
        if info == answer:
            bg = "#66ff66"  # vert clair
        return bg
    
    def show_win_animation(self):
        self.frame_win = ctk.CTkFrame(self.master, fg_color="white", corner_radius=0)
        self.frame_win.place(relx=0, rely=0, relwidth=1, relheight=1)

        congrats_label = ctk.CTkLabel(
        self.frame_win,
        text="🎉 Bravo ! Tu as deviné 🎉",
        font=ctk.CTkFont(size=32, weight="bold"),
        text_color="green"
        )
        congrats_label.place(relx=0.5, rely=0.4, anchor="center")

        close_button = ctk.CTkButton(
        self.frame_win,
        text="Revoir vos guess",
        font=ctk.CTkFont(size=16),
        command=self.frame_win.destroy
        )
        close_button.place(relx=0.5, rely=0.85, anchor="w")
        menu_button = ctk.CTkButton(
            self.frame_win,
            text="retour au menu",
            font=ctk.CTkFont(size=16),
            command=lambda: (self.frame_win.destroy(), self.back_callback())
        )
        menu_button.place(relx=0.5, rely=0.85, anchor="e")

    # Lance l’animation dans un thread
        threading.Thread(target=self.confetti_animation, daemon=True).start()


    def confetti_animation(self):
        for _ in range(100):
            if self.frame_win.winfo_exists():
                label = ctk.CTkLabel(
                self.frame_win,
                text="✨",
                font=ctk.CTkFont(size=random.randint(1, 50)),
                bg_color="transparent",
                text_color=random.choice(["#ff5e5e", "#f7c948", "#5ec576", "#5ea8ff", "#b15eff"])
                )
                label.place(x=self.get_coord_x(), y=self.get_coord_y())
                self.frame_win.after(random.randint(800, 2000), label.destroy)

    def get_coord_x(self):
        self.x = random.randint(20, 1040)
        while 320 < self.x < 720:
            self.x = random.randint(20, 1040)
        return self.x

    def get_coord_y(self):
        y = random.randint(20, 720)
        if 320 < self.x < 720:
            while 360 < y < 460:
                y = random.randint(20, 720)
        return y
    
    def show_defeat_animation(self):
        frame_defeat = ctk.CTkFrame(self.master, fg_color="black", corner_radius=0)
        frame_defeat.place(relx=0, rely=0, relwidth=1, relheight=1)

        defeat_label = ctk.CTkLabel(
            frame_defeat,
            text="❌ Dommage ! Tu as perdu 😢",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="red"
        )
        defeat_label.place(relx=0.5, rely=0.35, anchor="center")

        reveal_label = ctk.CTkLabel(
            frame_defeat,
            text=f"La bonne réponse était :\n{self.prof_cible}",
            font=ctk.CTkFont(size=20),
            text_color="white",
            justify="center"
        )
        reveal_label.place(relx=0.5, rely=0.5, anchor="center")

        retry_button = ctk.CTkButton(
            frame_defeat,
            text="Réessayer",
            font=ctk.CTkFont(size=16),
            command=frame_defeat.destroy
        )
        retry_button.place(relx=0.5, rely=0.7, anchor="center")


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
            data = bd.get_infos_prof(nom)
            self.create_answer(data)
            self.noms.remove(nom)
            # logique de victoire/défaite + ajout des infos au tableau
            print(f"Tentative {self.compteur_essais} : {nom}")
            self.search_var.set("")
            self.update_suggestions()


