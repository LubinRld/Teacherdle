import customtkinter as ctk
import programme

# Setup
ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("blue")
import tkinter as tk
from tkinter import *
Main_window = ctk.CTk()
Main_window.title("Teacherdle")
Main_window.geometry("1080x720")
Main_window.iconbitmap("Logo.ico")
Main_window.configure(fg_color='#00e1ff')
global x
import random
import threading
import time

def show_win_animation():
    # Overlay frame on the main window
    overlay = ctk.CTkFrame(Main_window, fg_color="white", corner_radius=0)
    overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Center message
    congrats_label = ctk.CTkLabel(
        overlay,
        text="🎉 Bravo ! Tu as deviné 🎉",
        font=ctk.CTkFont(size=32, weight="bold"),
        text_color="green"
    )
    congrats_label.place(relx=0.5, rely=0.4, anchor="center")

    # Close animation button
    close_button = ctk.CTkButton(
        overlay,
        text="Continuer",
        font=ctk.CTkFont(size=16),
        command=overlay.destroy
    )
    close_button.place(relx=0.5, rely=0.85, anchor="center")

    # Confetti animation
    def confetti_animation():
        for _ in range(100):
            label = ctk.CTkLabel(
                overlay,
                text="✨",
                font=ctk.CTkFont(size=random.randint(1, 50)),
                bg_color="transparent",
                text_color=random.choice(["#ff5e5e", "#f7c948", "#5ec576", "#5ea8ff", "#b15eff"])
                
            )
            label.place(
                x = get_coord_x(),
                y = get_coord_y()
            )
            overlay.after(random.randint(800, 2000), label.destroy)

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

# def get_y():
#     y=random.randint(20, 720)
#     while y > 260 and y < 460:
#         y=random.randint(20, 720)
#     return y

def show_defeat_animation(correct_answer):
    overlay = ctk.CTkFrame(Main_window, fg_color="black", corner_radius=0)
    overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

    defeat_label = ctk.CTkLabel(
        overlay,
        text="❌ Dommage ! Tu as perdu 😢",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="red"
    )
    defeat_label.place(relx=0.5, rely=0.35, anchor="center")

    reveal_label = ctk.CTkLabel(
        overlay,
        text=f"La bonne réponse était :\n{correct_answer.split()[0]}",
        font=ctk.CTkFont(size=20),
        text_color="white",
        justify="center"
    )
    reveal_label.place(relx=0.5, rely=0.5, anchor="center")

    retry_button = ctk.CTkButton(
        overlay,
        text="Réessayer",
        font=ctk.CTkFont(size=16),
        command=lambda: (overlay.destroy(), reset_game())
    )
    retry_button.place(relx=0.5, rely=0.7, anchor="center")

Label_Teacherdle = ctk.CTkLabel(
    Main_window,
    text="Teacherdle",
    font=ctk.CTkFont(family="Helvetica", size=40, weight="bold"),
    text_color="black"
)
Label_Teacherdle.pack(pady=12)

tableau_recherche = programme.choix_prof()
noms = programme.envoie_noms()
print(noms)

# Fonction pour gérer l'effet de survol
def on_enter(e, button, size):
    button['font'] = ("Arial", size + 2)  # Augmente la taille de la police

def on_leave(e, button, size):
    button['font'] = ("Arial", size)  # Rétablit la taille originale

def Create_Welcome_page():
    Button_Frame = Frame(Main_window, bg= '#00e1ff')
    Label_Description = Label(Main_window, text = "Devine tes profs de Polytech Dijon",font=("Helvetica", 20), bg='#00e1ff')
    Label_Description.pack(padx=0.5, pady=0.5)
    
    Classique_button = Button(Button_Frame, text = "Classique", font=("Arial", 30), bg='#00e1ff', width=10, command=lambda:(Button_Frame.destroy(), Label_Description.destroy(), Create_Classic_page(), init_compteur(), create_data()))
    Classique_button.pack(padx=10, pady=0)
    Classique_button.bind("<Enter>", lambda e, b=Classique_button: on_enter(e, b, 30))
    Classique_button.bind("<Leave>", lambda e, b=Classique_button: on_leave(e, b, 30))
    
    Citation_button = Button(Button_Frame, text = "Citation", font=("Arial", 30), bg= '#00e1ff', width=10, command=lambda:(Button_Frame.destroy(), Label_Description.destroy()))
    Citation_button.pack(padx=10, pady=50)
    Citation_button.bind("<Enter>", lambda e, b=Citation_button: on_enter(e, b, 30))
    Citation_button.bind("<Leave>", lambda e, b=Citation_button: on_leave(e, b, 30))
    Button_Frame.pack(padx=10, pady=70)

def init_compteur():
    global compteur_essais
    compteur_essais = 0

def Create_Classic_page():
    Classic_frame = Frame(Main_window, bg= '#00e1ff')
    Menu_Buton = Button(Classic_frame, text="Menu Principal", font=("Arial", 10), bg = 'purple', command=lambda:(Classic_frame.destroy(), Create_Welcome_page()))
    Menu_Buton.pack(anchor='nw', padx=100, pady=10)
    Classic_frame.pack(fill="both", expand=True)

def create_table(parent):
    global table_frame 
    table_frame = Frame(parent, bg='white')
    table_frame.pack(fill=BOTH, padx=20, pady=20)
    categories = ["Professeur", "Genre", "Date de thèse", "type", "Matière", "Fonction particulière"]
    for col in range(len(categories)):
        table_frame.grid_columnconfigure(col, weight=1)
    for col, title in enumerate(categories):
        header = Label(
        table_frame,
        text=title,
        font=("Arial", 14, "bold"),
        bg="white",
        padx=15,
        pady=10,
        relief=GROOVE,
        borderwidth=2
        )
        header.grid(row=0, column=col, sticky="nsew", padx=5, pady=5)
        table_frame.grid_columnconfigure(col, weight=1)

def create_answer(data, tableau_recherche):
    global current_row
    global compteur_essais
    if compteur_essais >=6:
        return 0 #defaite
    donnees = data
    reussi = 0
    for col, info in enumerate(donnees[0]):
        answer = tableau_recherche[col]
        if answer == info:
            reussi+=1
        if reussi == 6:
            print("fin de truc")#VICTOIRE
        
        case = Label(
            table_frame,
            text=info + create_fleche(info,answer),  
            bg=create_color(info, answer), #mettre la fonction pour déterminer la couleur
            fg="black",
            font=("Arial", 10),
            padx=10,
            pady=10,
            relief="solid",
            borderwidth=1,
            wraplength=120,
            justify="center"
        )
        case.grid(row=current_row, column=col, sticky="nsew", padx=1, pady=5)
    # Incrémenter la ligne pour les prochaines données
    current_row += 1

def create_fleche(info,answer):
    num = 0
    arrow = ''
    for i in range(0,len(info)):
        if info[i] in ['1','2','3','4','5','6','7','8','9','0']:
            num += 1
    if num ==4:
        if info > answer:
            arrow =' ▼'
        elif answer > info: 
            arrow =' ▲'
    return arrow

def create_color(info, answer):
    bg ="red"
    infos_split = info.split()
    answer_split = answer.split()
    split = 0
    for k in infos_split:
        for l in answer_split:
            if k==l:
                split +=1
    if split > 0:
        bg ="orange"
    if(info==answer):
        bg="green"
    return bg


def create_data():
    global noms, tableau_recherche
    noms = programme.envoie_noms()
    tableau_recherche = programme.choix_prof()

def update_suggestions(*args):
    search_term = search_var.get().lower()
    if not search_term:
        suggestions_list.pack_forget()
    else:
        suggestions_list.pack()
        suggestions_list.configure(state="normal")  # Enable editing
        suggestions_list.delete("1.0", "end")       # Clear all text
        suggestions = [word for word in noms if word.lower().startswith(search_term)]
        for word in suggestions:
            suggestions_list.insert("end", word + "\n")
        suggestions_list.configure(state="disabled")  # Make read-only again


def select_suggestion(event):
    if suggestions_list.curselection():
        selected = suggestions_list.get(suggestions_list.curselection())
        search_var.set(selected)

def remove_selected_item():
    selected_text = search_var.get()
    global compteur_essais
    if selected_text in noms:
        compteur_essais +=1
        if compteur_essais >= 6:
            print("perdu sale noob")
        else:
            noms.remove(selected_text)
            
            search_var.set("")  # Vide la barre de recherche
            update_suggestions()  # Met à jour la liste
            print(f"'{selected_text}' a été supprimé de la liste") 

def enter_pressed(event=None):  # event=None pour gérer les appels avec ou sans événement
    if search_var.get():  # Ne rien faire si la barre de recherche est vide
        
        create_answer(programme.get_infos_prof(search_var.get()), tableau_recherche)
        remove_selected_item()

def create_search_bar(window, noms):
    global search_var, suggestions_list

    search_var = ctk.StringVar()
    search_var.trace_add("write", lambda *args: update_suggestions())

    main_frame = ctk.CTkFrame(window, fg_color="transparent")
    main_frame.pack(pady=20)

    search_button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    search_button_frame.pack(fill="x")

    search_entry = ctk.CTkEntry(
        search_button_frame,
        textvariable=search_var,
        font=ctk.CTkFont(size=14),
        width=400
    )
    search_entry.pack(side="left", fill="x", expand=True)

    # Bouton d'entrer(confirmation)
    enter_button = Button(
        search_button_frame, 
        text="Entrer", 
        command= enter_pressed,
        bg="#ff9999",
        font=('Arial', 12)
    )
    enter_button.pack(side="right", padx=10)

    suggestions_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    suggestions_frame.pack(fill="x")

    suggestions_list = ctk.CTkTextbox(
        suggestions_frame,
        height=120,
        width=400,
        font=ctk.CTkFont(size=12),
        corner_radius=0,
        scrollbar_button_color="#cccccc"
    )
    suggestions_list.pack()
    suggestions_list.bind("<<ListboxSelect>>", select_suggestion)

    # Bind de la touche Entrée
    Main_window.bind("<Return>", lambda event: enter_pressed())
    
Create_Welcome_page()
Main_window.mainloop()
