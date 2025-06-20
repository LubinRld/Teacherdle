import customtkinter as ctk
from tkinter import *
from PIL import Image
import fonctions_db as db
import threading
import random

class CitationPage:
    def __init__(self, master, name, citation, back_callback, restart_callback):
        self.master = master
        self.name = name
        self.citation = citation
        self.try_counter = 0
        self.current_row = 1
        self.search_var = ctk.StringVar()
        self.is_animation = False
        self.frame = ctk.CTkFrame(master, fg_color="#3B8ED0", corner_radius=0)
        self.back_callback = back_callback
        self.restart_callback = restart_callback

        self.label = ctk.CTkLabel(self.frame, text="Teacherdle", text_color="black", font=("Comic Sans MS", 60), bg_color='#3B8ED0')
        self.label.pack(padx=0.5, pady=0.5)
        self.label2 = ctk.CTkLabel(self.frame, text="qui a dit : <<{}>>".format(citation[0][1]), text_color="black", font=ctk.CTkFont("Comic Sans MS", 20), bg_color='#3B8ED0')
        self.label2.pack(padx=0.5, pady=0.5)
        self.menu_button = ctk.CTkButton(self.frame, text="Menu Principal", font=ctk.CTkFont(size=20), fg_color="#6062f9", command=back_callback)
        self.menu_button.pack(anchor='nw', padx=100, pady=10)
        self.frame.pack(fill="both", expand=True)
  
        self.create_search_bar()
        self.create_table()

        self.hint_wait_label = ctk.CTkLabel(
            self.frame,
            text="Un indice sera disponible dans 3 essais",
            text_color="black",
            font=ctk.CTkFont(size=16),
            bg_color="#3B8ED0"
        )
        self.hint_wait_label.pack()

        self.hint_button = ctk.CTkButton(
            self.frame,
            text="Cliquez pour voir l'indice",
            font=ctk.CTkFont(size=16),
            command=self.reveal_hint,
            fg_color="#FFA500"
        )

        self.hint_button.pack(pady=5)
        self.hint_button.pack_forget()  # Cacher au début

        self.hint_label = ctk.CTkLabel(
            self.frame,
            text="",  # Vide au début
            text_color="black",
            font=ctk.CTkFont(size=18),
            bg_color="#3B8ED0"
        )
        self.hint_label.pack()
        self.hint_label.pack_forget()  # Cacher au début

    def destroy(self):
        self.frame.destroy()
        self.label.destroy()
        self.label2.destroy()

    def create_table(self):
        categories = ["Professeur"]
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
        
        target = data[0][0]
        answer = self.citation[0][2] 
        if answer == data[0][0]:
            self.show_win_animation()

        label = ctk.CTkLabel(
            self.table_frame,
            text=target,
            fg_color=self.create_color(target, answer),
            text_color="black",
            font=ctk.CTkFont(size=14),
            width=120,
            height=30,
            corner_radius=8
        )
        label.grid(row=self.current_row, column=0, sticky="nsew", padx=1, pady=5)
        
        self.try_counter += 1
        self.current_row += 1
        try_left = 3 - self.try_counter
        if try_left > 0:
            self.hint_wait_label.configure(text=f"Un indice sera disponible dans {try_left} essai(s)")
        elif self.try_counter == 3:
            self.hint_wait_label.pack_forget()
            self.hint_button.pack()
        elif self.try_counter >= 6:
            self.show_defeat_animation()
            return
    
    def reveal_hint(self):
        subject = db.get_subject_prof(self.citation)
        self.hint_label.configure(text=f"La matière du professeur à deviner est {subject}")
        self.hint_label.pack()
        self.hint_button.pack_forget()
    

    def create_color(self, info, answer):
        bg = "#ff6666"  # rouge clair
        target_split = info.split()
        answer_split = answer.split()
        split = 0
        for k in target_split:
            for l in answer_split:
                if k == l:
                    split += 1
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
        for _ in range(150):
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
                self.frame_win.after(3000, lambda: (setattr(self, "is_animation", False), self.buttons_frame.place(relx=0.5, rely=0.85, anchor="center")))

    def get_coord_x(self):
        self.x = random.randint(0, 2000)
        return self.x

    def get_coord_y(self):
        y = random.randint(0,2000)
        while 230 < y < 330:
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
            text=f"La bonne réponse était :\n{self.citation[0][2]}",
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
            suggestions = [nom for nom in self.name if nom.lower().startswith(search_term)]
            for s in suggestions:
                self.suggestions_list.insert(ctk.END, s)

    def select_suggestion(self, event):
        if self.suggestions_list.curselection():
            selected = self.suggestions_list.get(self.suggestions_list.curselection())
            self.search_var.set(selected)

    def enter_pressed(self):
        name = self.search_var.get()
        if name in self.name:
            data = db.get_infos_prof(name)
            self.create_answer(data)
            self.name.remove(name)
            # logique de victoire/défaite + ajout des infos au tableau
            self.search_var.set("")
            self.update_suggestions()
