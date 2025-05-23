from tkinter import *
from tkinter import ttk
import programme

Main_window = Tk()
Main_window.title("Teacherdle")
Main_window.geometry("1080x720")
Main_window.iconbitmap("Logo.ico")
Main_window.config(background='#00e1ff')
Label_Teacherdle = Label(Main_window, text = "Teacherdle", font=("Helvetica", 40), bg='#00e1ff')
Label_Teacherdle.pack(padx=0.5, pady=12)


tableau_recherche = programme.choix_prof() #pour les tests
# Liste de nom de professeur

print(tableau_recherche)

noms = programme.envoie_noms()
#print(noms)

def Create_Welcome_page():
    Button_Frame = Frame(Main_window, bg= '#00e1ff')
    Label_Description = Label(Main_window, text = "Devine tes profs de Polytech Dijon",font=("Helvetica", 20), bg='#00e1ff')
    Label_Description.pack(padx=0.5, pady=0.5)
    Classique_button = Button(Button_Frame, text = "Classique", font=("Arial", 30), bg='#00e1ff', width=10, command=lambda:(Button_Frame.destroy(), Label_Description.destroy(), Create_Classic_page(),init_compteur()))
    Citation_button = Button(Button_Frame, text = "Citation", font=("Arial", 30), bg= '#00e1ff', width=10, command=lambda:(Button_Frame.destroy(), Label_Description.destroy()))
    Classique_button.pack(padx=10, pady=0)
    Citation_button.pack(padx=10, pady=50)
    Button_Frame.pack(padx=10, pady=70)
def init_compteur():
    global compteur_essais
    compteur_essais = 0


def Create_Classic_page():
    Classic_frame = Frame(Main_window, bg= '#00e1ff')
    Classic_frame.pack(fill="both", expand=True)
    create_search_bar(Classic_frame, noms)
    table_container = Frame(Classic_frame, bg='#00e1ff')
    table_container.pack(fill=BOTH, expand=True,padx=20, pady=10)
    create_table(table_container)
    global lignes_container
    lignes_container = Frame(Classic_frame, bg='#00e1ff')
    lignes_container.pack(fill=BOTH, expand=True)
    global current_row
    current_row=1


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
        header.grid(row=0, column=col,sticky="nsew", padx=1, pady=1)

def create_answer(data, tableau_recherche):
    global current_row

    donnees = data
    reussi = 0
    for col, info in enumerate(donnees[0]):
        answer = tableau_recherche[col]
        if answer == info:
            reussi+=1
        if reussi == 6:
            print("fin de truc")
        
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
    # Met à jour la liste des suggestions en fonction du texte saisi
    search_term = search_var.get().lower()
    # Cacher la liste si le champ est vide
    if not search_term:
        suggestions_list.pack_forget()
    else:
        # Afficher la liste et mettre à jour les suggestions
        suggestions_list.pack()
        suggestions_list.delete(0, END)  # Effacer les anciennes suggestions
        # Filtrer les mots qui commencent par le texte saisi
        suggestions = [word for word in noms if word.lower().startswith(search_term)]
        # Ajouter les suggestions à la liste
        for word in suggestions:
            suggestions_list.insert(END, word)

def select_suggestion(event):
    # Insère la suggestion sélectionnée dans la barre de recherche
    if suggestions_list.curselection():
        selected = suggestions_list.get(suggestions_list.curselection())
        search_var.set(selected)
def remove_selected_item():
    selected_text = search_var.get()
    
    if selected_text in noms:
        global compteur_essais 
        compteur_essais +=1
        if compteur_essais >= 6:
            pass
        else:
            noms.remove(selected_text)
            
            search_var.set("")  # Vide la barre de recherche
            update_suggestions()  # Met à jour la liste
            print(f"'{selected_text}' a été supprimé de la liste") 
            
def enter_pressed(event=None):  # event=None pour gérer les appels avec ou sans événement
    if search_var.get():  # Ne rien faire si la barre de recherche est vide
        global compteur_essais
        if compteur_essais < 6:
            create_answer(programme.get_infos_prof(search_var.get()), tableau_recherche)
            remove_selected_item()

def create_search_bar(window, noms):
    global search_var, suggestions_list

    search_var = StringVar() # Variable pour stocker le texte de recherche
    search_var.trace_add("write", lambda *args: update_suggestions()) # trace est une méthode qui "espionne" la variable. Dès qu'elle est modifiée, elle appelle une fonction.

    # Frame principal pour la barre de recherche et le bouton
    main_frame = Frame(window, padx=20, pady=20)
    main_frame.pack()

    # Sous-frame pour la barre de recherche et le bouton
    search_button_frame = Frame(main_frame)
    search_button_frame.pack(fill=X)

    # Barre de recherche
    search_entry = Entry(
        search_button_frame, 
        textvariable=search_var, 
        width=40, 
        font=('Arial', 12)
    )
    search_entry.pack(side=LEFT, fill=X, expand=True)

    # Bouton d'entrer(confirmation)
    enter_button = Button(
        search_button_frame, 
        text="Entrer", 
        command= lambda:(create_answer(programme.get_infos_prof(search_var.get()), tableau_recherche), remove_selected_item()),
        bg="#ff9999",
        font=('Arial', 12)
    )
    enter_button.pack(side=RIGHT, padx=(10, 0))

    # Liste des suggestions
    suggestions_frame = Frame(main_frame)
    suggestions_frame.pack(fill=X)
    suggestions_list = Listbox(
        suggestions_frame, 
        width=40, 
        height=6, 
        font=('Arial', 12)
    )

    # Lier la sélection dans la liste à la barre de recherche
    suggestions_list.bind("<<ListboxSelect>>", select_suggestion)

    # Bind de la touche Entrée
    search_entry.bind("<Return>", lambda event: enter_pressed())
    
Create_Welcome_page()
Main_window.mainloop()