import customtkinter as ctk
import programme

# Setup
ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("blue")

Main_window = ctk.CTk()
Main_window.title("Teacherdle")
Main_window.geometry("1080x720")
Main_window.iconbitmap("Logo.ico")
Main_window.configure(fg_color='#00e1ff')

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
        for _ in range(40):
            label = ctk.CTkLabel(
                overlay,
                text="✨",
                font=ctk.CTkFont(size=random.randint(14, 20)),
                text_color=random.choice(["#ff5e5e", "#f7c948", "#5ec576", "#5ea8ff", "#b15eff"])
            )
            label.place(
                x=random.randint(20, 1040),
                y=random.randint(20, 700)
            )
            overlay.after(random.randint(800, 2000), label.destroy)

    threading.Thread(target=confetti_animation, daemon=True).start()

global current_try
current_try = 0
MAX_TRIES = 6



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

def Create_Welcome_page():
    Button_Frame = ctk.CTkFrame(Main_window, fg_color='#00e1ff')
    Label_Description = ctk.CTkLabel(
        Main_window,
        text="Devine tes profs de Polytech Dijon",
        font=ctk.CTkFont(family="Helvetica", size=20),
        text_color="black"
    )
    Label_Description.pack()

    Classique_button = ctk.CTkButton(
        Button_Frame,
        text="Classique",
        font=ctk.CTkFont(size=30),
        width=200,
        command=lambda: (
            Button_Frame.destroy(),
            Label_Description.destroy(),
            Create_Classic_page()
        )
    )
    Citation_button = ctk.CTkButton(
        Button_Frame,
        text="Citation",
        font=ctk.CTkFont(size=30),
        width=200,
        command=lambda: (
            Button_Frame.destroy(),
            Label_Description.destroy()
        )
    )
    Classique_button.pack(pady=10)
    Citation_button.pack(pady=30)
    Button_Frame.pack(pady=70)

def Create_Classic_page():
    Classic_frame = ctk.CTkFrame(Main_window, fg_color='#00e1ff')
    Classic_frame.pack(fill="both", expand=True)

    create_search_bar(Classic_frame, noms)

    table_container = ctk.CTkFrame(Classic_frame, fg_color='#00e1ff')
    table_container.pack(fill="both", expand=True, padx=20, pady=10)
    create_table(table_container)

    global lignes_container
    lignes_container = ctk.CTkFrame(Classic_frame, fg_color='#00e1ff')
    lignes_container.pack(fill="both", expand=True)

    global current_row
    current_row = 1

def create_table(parent):
    global table_frame
    table_frame = ctk.CTkFrame(parent, fg_color="white")
    table_frame.pack(fill="both", padx=20, pady=20)

    categories = ["Professeur", "Genre", "Date de thèse", "type", "Matière", "Fonction particulière"]

    for col, title in enumerate(categories):
        header = ctk.CTkLabel(
            table_frame,
            text=title,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="black",
            bg_color="white"
        )
        header.grid(row=0, column=col, sticky="nsew", padx=5, pady=5)
        table_frame.grid_columnconfigure(col, weight=1)

def create_answer(data, tableau_recherche):
    global current_row, current_try

    current_try += 1
    donnees = data

    for col, info in enumerate(donnees[0]):
        answer = tableau_recherche[col]
        case = ctk.CTkLabel(
            table_frame,
            text=info,
            text_color="black",
            font=ctk.CTkFont(size=12),
            fg_color=create_color(info, answer),
            bg_color="white",
            width=100,
            corner_radius=6
        )
        case.grid(row=current_row, column=col, sticky="nsew", padx=2, pady=4)

    current_row += 1

    if all(info == ans for info, ans in zip(donnees[0], tableau_recherche)):
        show_win_animation()
    elif current_try >= MAX_TRIES:
        correct = "\n".join(tableau_recherche)
        show_defeat_animation(correct)


def create_color(info, answer):
    bg ="red"


    # elif len(info)==len(answer):
    #     compteur = 0
    #     for i in range (0,len(info)):
    #         if info[i] == answer[i] and info[i] != " ":
    #             compteur +=1
    #     if compteur >= 2:
    #         bg="orange"
    # else:
    #     print(info)
    #     print(answer)
    #     if info.find(answer) != -1:
    #         bg="orange"
    #     elif answer.find(info) != -1:
    #         bg="orange"

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
    if selected_text in noms:
        noms.remove(selected_text)
        search_var.set("")
        update_suggestions()
        print(f"'{selected_text}' a été supprimé de la liste")

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

    enter_button = ctk.CTkButton(
        search_button_frame,
        text="Entrer",
        font=ctk.CTkFont(size=12),
        command=lambda: (
            create_answer(programme.get_infos_prof(search_var.get()), tableau_recherche),
            remove_selected_item()
        )
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
    search_entry.bind("<Return>", lambda event: remove_selected_item())

def check_win_condition(info, answer):
    return info == answer




Create_Welcome_page()
Main_window.mainloop()
