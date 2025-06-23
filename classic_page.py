import customtkinter as ctk
from tkinter import *
import fonctions_db as db
import threading
import random

class ClassicPage:
    def __init__(self, master, names, target_teacher, back_callback, restart_callback):
        self.master = master 
        self.names = names
        self.target_teacher = target_teacher
        self.try_counter = 0
        self.current_row = 1
        self.search_var = ctk.StringVar()
        self.is_animation = False
        self.back_callback = back_callback
        self.restart_callback = restart_callback

        self.frame = ctk.CTkFrame(master, fg_color="#3B8ED0", corner_radius=0)
        self.label = ctk.CTkLabel(master, text="Teacherdle", text_color="black", font=("Comic Sans MS", 60), bg_color='#3B8ED0')
        self.label.pack(padx=0.5, pady=0.5)
        self.label2 = ctk.CTkLabel(master, text="Devine tes profs de Polytech Dijon", text_color="black", font=ctk.CTkFont("Comic Sans MS", 20), bg_color='#3B8ED0')
        self.label2.pack(padx=0.5, pady=0.5)
        self.frame.pack(fill="both", expand=True)

        self.menu_button = ctk.CTkButton(self.frame, text="Menu Principal", font=ctk.CTkFont(size=20), fg_color="#6062f9", command=back_callback)
        self.menu_button.pack(anchor="nw", padx=100, pady=10)

        self.create_search_bar()
        self.create_table()

    def destroy(self):
        self.label.destroy()
        self.label2.destroy()
        self.frame.destroy()

    def create_table(self): # Méthode permétant d'afficher le tableau des reponse
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
        
        correct = 0
        for col, info in enumerate(data[0]):
            answer = self.target_teacher[col]
            if answer == info:
                correct += 1

            label = ctk.CTkLabel(
                self.table_frame,
                text=info + self.create_arrow(info, answer),
                fg_color=self.create_color(info, answer),
                text_color="black",
                font=ctk.CTkFont(size=14),
                width=120,
                height=30,
                corner_radius=8
            )
            label.grid(row=self.current_row, column=col, sticky="nsew", padx=1, pady=5)

       
        self.try_counter += 1
        self.current_row += 1
        if correct == 6:
            self.show_win_animation()
        elif self.try_counter >= 6:
            self.show_defeat_animation()
            return
        

    def create_arrow(self, info, answer):
        num = 0
        if len(answer) == len(info):
            for i in range(0,len(answer)):
                if answer[i] and info[i] in "1234567890":
                    num +=1
        arrow = ""
        if num == 4:
            if info > answer:
                arrow = " ▼"
            elif answer > info:
                arrow = " ▲"
        else:
            arrow = ""
        return arrow
    
    def create_color(self, info, answer):
        bg = "#ff6666"  # rouge clair
        infos_split = info.split()
        answer_split = answer.split()
        split = 0
        for k in infos_split:
            for l in answer_split:
                if k == l :
                    split +=1
                
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

        self.buttons_frame = ctk.CTkFrame(self.frame_win, fg_color="transparent")
        self.buttons_frame.place(relx=0.5, rely=0.85, anchor="center")
        self.buttons_frame.place_forget()

        menu_button = ctk.CTkButton(
        self.buttons_frame,
        text="Retour au menu",
        font=ctk.CTkFont(size=14),
        command=lambda: not self.is_animation and (self.frame_win.destroy(), self.back_callback())
        )
        menu_button.pack(side="left", padx=20)

        restart_button = ctk.CTkButton(
        self.buttons_frame,
        text="Relancer",
        font=ctk.CTkFont(size=14),
        command=lambda: not self.is_animation and (self.frame_win.destroy(), self.restart_callback())
        )
        restart_button.pack(side="left", padx=20)

        close_button = ctk.CTkButton(
        self.buttons_frame,
        text="Revoir vos guess",
        font=ctk.CTkFont(size=14),
        command=lambda: not self.is_animation and self.frame_win.destroy()
        )
        close_button.pack(side="left", padx=20)

        # Lance l’animation dans un thread
        self.is_animation = True
        threading.Thread(target=self.confetti_animation, daemon=True).start()


    def confetti_animation(self):
        for i in range(150):
            if self.frame_win.winfo_exists():
                label = ctk.CTkLabel(
                self.frame_win,
                text="✨",
                font=ctk.CTkFont(size=random.randint(20, 50)),
                bg_color="transparent",
                text_color=random.choice(["#ff5e5e", "#f7c948", "#5ec576", "#5ea8ff", "#b15eff"])
                )
                label.place(x=self.get_coord_x(), y=self.get_coord_y())
                self.frame_win.after(random.randint(800, 2000), label.destroy)
        self.frame_win.after(1500, lambda: (setattr(self, "is_animation", False), self.buttons_frame.place(relx=0.5, rely=0.85, anchor="center")))

    def get_coord_x(self):
        self.x = random.randint(0, 2000)
        return self.x

    def get_coord_y(self):
        y = random.randint(0,2000)
        while 200 < y < 330:
            y = random.randint(0, 2000)
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
            text=f"La bonne réponse était :\n{self.target_teacher}",
            font=ctk.CTkFont(size=20),
            text_color="white",
            justify="center"
        )
        reveal_label.place(relx=0.5, rely=0.5, anchor="center")

        buttons_frame = ctk.CTkFrame(frame_defeat, fg_color="transparent")
        buttons_frame.place(relx=0.5, rely=0.85, anchor="center")

        menu_button = ctk.CTkButton(
        buttons_frame,
        text="Retour au menu",
        font=ctk.CTkFont(size=14),
        command=lambda: (frame_defeat.destroy(), self.back_callback())
        )
        menu_button.pack(side="left", padx=20)

        restart_button = ctk.CTkButton(
        buttons_frame,
        text="Relancer",
        font=ctk.CTkFont(size=14),
        command=lambda: (frame_defeat.destroy(), self.restart_callback())
        )
        restart_button.pack(side="left", padx=20)

        close_button = ctk.CTkButton(
        buttons_frame,
        text="Revoir vos guess",
        font=ctk.CTkFont(size=14),
        command=frame_defeat.destroy
        )

        close_button.pack(side="left", padx=20)


    def create_search_bar(self):        # Méthode pour la barre de recherche
        # Ajoute un traceur sur la variable de recherche : chaque fois que l'utilisateur écrit,
        # la méthode update_suggestions() est appelée pour mettre à jour les propositions.
        self.search_var.trace_add("write", lambda *args: self.update_suggestions()) 
        
        # Crée un cadre principal à l'intérieur du cadre parent (self.frame).
        main_frame = ctk.CTkFrame(self.frame, fg_color=None)
        main_frame.pack(padx=40, pady=40)

        # Crée un sous-cadre pour contenir la barre de recherche et le bouton.
        search_frame = ctk.CTkFrame(main_frame, fg_color=None)
        search_frame.pack(fill="x", pady=(0, 15))

        # Crée le champ de saisie
        entry = ctk.CTkEntry(search_frame, textvariable=self.search_var, font=ctk.CTkFont("Arial", 18))
        entry.pack(side="left", fill="x", expand=True)

        # Crée le bouton Entrer
        button = ctk.CTkButton(search_frame, text="Entrer", command=self.enter_pressed, fg_color="#6062f9", font=ctk.CTkFont("Arial", 16))
        button.pack(side="right", padx=(15, 0))

        # Crée une liste déroulante (Listbox) pour afficher les suggestions,
        # avec une hauteur de 5 lignes, car que 5 prof on la même initiale.
        self.suggestions_list = Listbox(main_frame, height=db.count_max_same_initial(), font=("Arial", 20), bg="white", selectbackground="#00e1ff")
        self.suggestions_list.pack(fill="x", pady=(5, 0))
        
        # Lie la sélection d'un élément dans la liste et appelle la méthode select_suggestion.
        self.suggestions_list.bind("<<ListboxSelect>>", self.select_suggestion)

        # Permet de faire la même action en appuyant sur la touche Entrée qu'en appuyant sur le bouton.
        self.master.bind("<Return>", lambda event: self.enter_pressed())
    
    def update_suggestions(self):
        search_term = self.search_var.get().lower()         # Récupère le texte saisi en minuscules
        self.suggestions_list.pack(fill="x", pady=(5, 0))   # Affiche la liste des suggestions si elle n’est pas déjà visible
        self.suggestions_list.delete(0, ctk.END)            # Vide le contenu précédent de la liste

        # Si le champ est vide, on ne met pas de suggestions, mais la Listbox reste visible (vide)
        if not search_term:
            return
        # Sinon, on filtre les noms correspondant à la saisie
        suggestions = [name for name in self.names if name.lower().startswith(search_term)]
        # Et on les ajoute à la liste
        for s in suggestions:
            self.suggestions_list.insert(ctk.END, s)

    def select_suggestion(self, event):
        if self.suggestions_list.curselection():    # Vérifie qu’un élément est bien sélectionné dans la liste.
            selected = self.suggestions_list.get(self.suggestions_list.curselection())    # Récupère le texte de l’élément sélectionné.
            self.search_var.set(selected)   # Remplace le contenu de la barre de recherche par la suggestion choisie

    def enter_pressed(self):
        name = self.search_var.get()         # Récupère le nom actuellement saisi dans la barre de recherche
        if name in self.names:                # Vérifie si ce nom est dans la liste des noms de prof
            data = db.get_infos_prof(name)   # Récupère les informations associées au prof via la base de données
            self.create_answer(data)        # Affiche ces informations dans l’interface
            self.names.remove(name)           # Retire ce nom de la liste pour éviter qu’il ne soit deviné à nouveau
            self.search_var.set("")         # Réinitialise le champ de saisi
            self.update_suggestions()       # Met a jour les suggestions
