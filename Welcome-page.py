from tkinter import *
import programme
Main_window = Tk()
Main_window.title("Teacherdle")
Main_window.geometry("1080x720")
Main_window.iconbitmap("Logo.ico")
Main_window.config(background='#00e1ff')
Label_Teacherdle = Label(Main_window, text = "Teacherdle", font=("Helvetica", 40), bg='#00e1ff')
Label_Teacherdle.pack(padx=0.5, pady=12)

# Liste de nom de professeur
nom = programme.envoie_noms()
print(nom)
teacher_list =[]
for i in range(len(nom)):
    teacher_list.append(nom[i][0])
print(teacher_list)
def Create_Welcome_page():
    Button_Frame = Frame(Main_window, bg= '#00e1ff')
    Label_Description = Label(Main_window, text = "Devine tes profs de Polytech Dijon",font=("Helvetica", 20), bg='#00e1ff')
    Label_Description.pack(padx=0.5, pady=0.5)
    Classique_button = Button(Button_Frame, text = "Classique", font=("Arial", 30), bg='#00e1ff', width=10, command=lambda:(Button_Frame.destroy(), Label_Description.destroy(), Create_Classic_page()))
    Citation_button = Button(Button_Frame, text = "Citation", font=("Arial", 30), bg= '#00e1ff', width=10, command=lambda:(Button_Frame.destroy(), Label_Description.destroy()))
    Classique_button.pack(padx=10, pady=0)
    Citation_button.pack(padx=10, pady=50)
    Button_Frame.pack(padx=10, pady=70)

def Create_Classic_page():
    create_search_bar(Main_window, teacher_list)

        

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
        suggestions = [word for word in teacher_list if word.lower().startswith(search_term)]
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
    if selected_text in teacher_list:
        teacher_list.remove(selected_text)
        search_var.set("")  # Vide la barre de recherche
        update_suggestions()  # Met à jour la liste
        print(f"'{selected_text}' a été supprimé de la liste") 

def create_search_bar(window, teacher_list):
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
        command=remove_selected_item,
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
    search_entry.bind("<Return>", lambda event: remove_selected_item())
    
Create_Welcome_page()
Main_window.mainloop()