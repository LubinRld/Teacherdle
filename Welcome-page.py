import customtkinter as ctk
import fonctions_bdd
import customtkinter as ctk
from tkinter import *
from PIL import Image
import random
import threading
import time

# Configuration de la fenêtre principale
ctk.set_appearance_mode("Light")  # Mode clair
ctk.set_default_color_theme("blue")  # Thème bleu

Main_window = ctk.CTk()
Main_window.title("Teacherdle")
Main_window.geometry("1080x720")
Main_window.iconbitmap("assets/Logo.ico")
Main_window.config(background="#3B8ED0")
Label_Teacherdle = ctk.CTkLabel(Main_window, text = "Teacherdle", text_color='black', font=("Comic Sans MS", 60), bg_color='#3B8ED0')
Label_Teacherdle.pack(padx=0.5, pady=10)
global x


def show_win_animation():
    # frame_win frame on the main window
    frame_win = ctk.CTkFrame(Main_window, fg_color="white", corner_radius=0)
    frame_win.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Center message
    congrats_label = ctk.CTkLabel(
        frame_win,
        text="🎉 Bravo ! Tu as deviné 🎉",
        font=ctk.CTkFont(size=32, weight="bold"),
        text_color="green"
    )
    congrats_label.place(relx=0.5, rely=0.4, anchor="center")

    # Close animation button
    close_button = ctk.CTkButton(
        frame_win,
        text="Continuer",
        font=ctk.CTkFont(size=16),
        command=frame_win.destroy
    )
    close_button.place(relx=0.5, rely=0.85, anchor="center")

    # Confetti animation
    def confetti_animation():
        for _ in range(100):
            label = ctk.CTkLabel(
                frame_win,
                text="✨",
                font=ctk.CTkFont(size=random.randint(1, 50)),
                bg_color="transparent",
                text_color=random.choice(["#ff5e5e", "#f7c948", "#5ec576", "#5ea8ff", "#b15eff"])
            )
            label.place(x = get_coord_x(),y = get_coord_y())
            frame_win.after(random.randint(800, 2000), label.destroy)
    threading.Thread(target=confetti_animation, daemon=True).start()

global current_try
current_try = 0
MAX_TRIES = 6

def get_coord_y():
    global x
    y=random.randint(20, 720)
    if x > 320 and x < 720:
        while (x > 320 and x < 720) and  (y > 360 and y < 460):
            y=random.randint(20, 720)
    
    return y

def get_coord_x():
    global x
    x=random.randint(20, 1040)
    while x > 320 and x < 720:
        x=random.randint(20, 1040)
    return x

def show_defeat_animation(correct_answer):
    frame_defeat = ctk.CTkFrame(Main_window, fg_color="black", corner_radius=0)
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
        text=f"La bonne réponse était :\n{correct_answer}",
        font=ctk.CTkFont(size=20),
        text_color="white",
        justify="center"
    )
    reveal_label.place(relx=0.5, rely=0.5, anchor="center")

    retry_button = ctk.CTkButton(
        frame_defeat,
        text="Réessayer",
        font=ctk.CTkFont(size=16),
        command=lambda: (frame_defeat.destroy())
    )
    retry_button.place(relx=0.5, rely=0.7, anchor="center")

tableau_recherche = fonctions_bdd.choix_prof()
noms = fonctions_bdd.envoie_noms()
print(noms)

# Effet survol bouton
def on_enter(e, button, size):
    button.configure(font=("Arial", size +2))  # Augmente la taille de la police

def on_leave(e, button, size):
    button.configure(font=("Arial", size))  # Rétablit la taille originale

def Create_Welcome_page():
    Button_Frame = Frame(Main_window, bg= '#3B8ED0')
    Label_Description = ctk.CTkLabel(Main_window, text = "Devine tes profs de Polytech Dijon", text_color="black", font = ctk.CTkFont("Comis Sans MS", 20), bg_color='#3B8ED0')
    Label_Description.pack(padx=0.5, pady=0.5)
    
    classiquebtn_image = ctk.CTkImage(Image.open('assets/point-dinterrogation.png'), size=(40, 40))

    Classique_button = ctk.CTkButton(Button_Frame, text = "Classique", image=classiquebtn_image, compound = 'left', font=("Arial", 40), bg_color='#3B8ED0', width=320, height=70, anchor='w', command=lambda:(Button_Frame.destroy(), Label_Description.destroy(), Create_Classic_page(), init_compteur(), create_data()))
    Classique_button.pack(pady=60)
    Classique_button.bind("<Enter>", lambda e, b=Classique_button: on_enter(e, b, 40))
    Classique_button.bind("<Leave>", lambda e, b=Classique_button: on_leave(e, b, 40))
    citationbtn_image = ctk.CTkImage(Image.open('assets/discuter.png'), size= (40, 40))
    Citation_button = ctk.CTkButton(Button_Frame, text = "Citation", image = citationbtn_image, compound='left', font=("Arial", 40), bg_color= '#3B8ED0', width=320, height=70, anchor='w', command=lambda:(Button_Frame.destroy(), Label_Description.destroy()))
    Citation_button.pack(padx=10, pady=0)
    Citation_button.bind("<Enter>", lambda e, b=Citation_button: on_enter(e, b, 40))
    Citation_button.bind("<Leave>", lambda e, b=Citation_button: on_leave(e, b, 40))
    Button_Frame.pack(padx=100, pady=70)

def init_compteur():
    global compteur_essais
    compteur_essais = 0

def Create_Classic_page():
    Classic_frame = ctk.CTkFrame(Main_window, fg_color="#3B8ED0", corner_radius=0)
    Menu_Buton = ctk.CTkButton(Classic_frame, text="Menu Principal", font=ctk.CTkFont(size=20), fg_color="#6062f9", command=lambda:(Classic_frame.destroy(), Create_Welcome_page()))
    Menu_Buton.pack(anchor='nw', padx=100, pady=10)
    Classic_frame.pack(fill="both", expand=True)
    create_search_bar(Classic_frame, noms)

    table_container = ctk.CTkFrame(Classic_frame, fg_color="#3B8ED0", corner_radius=0)
    table_container.pack(fill="both", expand=True, padx=20, pady=10)
    create_table(table_container)

    global lignes_container
    lignes_container = ctk.CTkFrame(Classic_frame, fg_color="#3B8ED0", corner_radius=0)
    lignes_container.pack(fill="both", expand=True)

    global current_row
    current_row = 1

def create_table(parent):
    global table_frame
    table_frame = ctk.CTkFrame(parent, fg_color="white", corner_radius=8)
    table_frame.pack(fill="both", padx=20, pady=20)

    categories = ["Professeur", "Genre", "Date de thèse", "type", "Matière", "Fonction particulière"]
    for col in range(len(categories)):
        table_frame.grid_columnconfigure(col, weight=1)
    for col, title in enumerate(categories):
        header = ctk.CTkLabel(
            table_frame,
            text=title,
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            fg_color="white",
            text_color="black",
            padx=15,
            pady=10,
            corner_radius=0
        )
        header.grid(row=0, column=col, sticky="nsew", padx=5, pady=5)
        table_frame.grid_columnconfigure(col, weight=1)

def create_answer(data, tableau_recherche):
    global current_row
    global compteur_essais
    if compteur_essais >= 6:
        return 0  # défaite

    donnees = data
    reussi = 0
    for col, info in enumerate(donnees[0]):
        answer = tableau_recherche[col]
        if answer == info:
            reussi += 1
        if reussi == 6:
            show_win_animation()  # VICTOIRE

        case = ctk.CTkLabel(
            table_frame,
            text=info + create_fleche(info, answer),
            fg_color=create_color(info, answer),
            text_color="black",
            font=ctk.CTkFont(size=14),
            width=120,
            height=30,
            corner_radius=8
        )
        case.grid(row=current_row, column=col, sticky="nsew", padx=1, pady=5)

    current_row += 1

def create_fleche(info, answer):
    num = 0
    arrow = ''
    for i in range(len(info)):
        if info[i].isdigit():
            num += 1
    if num == 4:
        if info > answer:
            arrow = ' ▼'
        elif answer > info:
            arrow = ' ▲'
    return arrow

def create_color(info, answer):
    bg = "#ff6666"  # rouge clair
    infos_split = info.split()
    answer_split = answer.split()
    split = 0
    for k in infos_split:
        for l in answer_split:
            if k == l:
                split += 1
    if split > 0:
        bg = "#ffa500"  # orange
    if info == answer:
        bg = "#66ff66"  # vert clair
    return bg

def create_data():
    global noms, tableau_recherche
    noms = fonctions_bdd.envoie_noms()
    tableau_recherche = fonctions_bdd.choix_prof()

def update_suggestions(*args):
    search_term = search_var.get().lower()
    if not search_term:
        suggestions_list.pack_forget()
    else:
        suggestions_list.pack()
        suggestions_list.delete(0, ctk.END)
        suggestions = [word for word in noms if word.lower().startswith(search_term)]
        for word in suggestions:
            suggestions_list.insert(ctk.END, word)

def select_suggestion(event):
    if suggestions_list.curselection():
        selected = suggestions_list.get(suggestions_list.curselection())
        search_var.set(selected)

def remove_selected_item():
    selected_text = search_var.get()
    global compteur_essais
    if selected_text in noms:
        compteur_essais += 1
        if compteur_essais >= 6:
            show_defeat_animation(tableau_recherche)
        else:
            noms.remove(selected_text)
            search_var.set("")
            update_suggestions()
            print(f"'{selected_text}' a été supprimé de la liste")

def enter_pressed(event=None):
    if search_var.get():
        create_answer(fonctions_bdd.get_infos_prof(search_var.get()), tableau_recherche)
        remove_selected_item()

def create_search_bar(window, noms):
    global search_var, suggestions_list

    search_var = ctk.StringVar() # Variable pour stocker le texte de recherche
    search_var.trace_add("write", lambda *args: update_suggestions()) # trace est une méthode qui "espionne" la variable. Dès qu'elle est modifiée, elle appelle une fonction.

    main_frame = ctk.CTkFrame(window, fg_color=None)
    main_frame.pack(padx=40, pady=40)

    search_button_frame = ctk.CTkFrame(main_frame, fg_color=None)
    search_button_frame.pack(fill="x", pady=(0, 15))

    # Barre de recherche
    search_entry = ctk.CTkEntry(
        search_button_frame,
        textvariable=search_var,
        width=100,
        font=ctk.CTkFont(family='Arial', size=18)
    )
    search_entry.pack(side="left", fill="x", expand=True)

    # Bouton d'entrer (comfirmation)
    enter_button = ctk.CTkButton(
        search_button_frame,
        text="Entrer",
        command=enter_pressed,
        bg_color="#6062f9",
        fg_color="#6062f9",
        font=ctk.CTkFont(family='Arial', size=16),
        width=100,
        height=40
    )
    enter_button.pack(side="right", padx=(15, 0))

    # Liste de suggestions
    suggestions_frame = ctk.CTkFrame(main_frame, fg_color=None)
    suggestions_frame.pack(fill="x")
    suggestions_list = Listbox(
        suggestions_frame,
        width=50,
        height=8,
        font=('Arial', 25),  # Plus gros
        bg='white',
        activestyle='dotbox',
        highlightthickness=2,
        relief="solid",
        selectbackground='#00e1ff'
    )
    suggestions_list.pack(fill="x", pady=(5, 0))

    suggestions_list.bind("<<ListboxSelect>>", select_suggestion)

    Main_window.bind("<Return>", lambda event: enter_pressed())

Create_Welcome_page()
Main_window.mainloop()
