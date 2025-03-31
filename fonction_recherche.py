import tkinter as tk

def update_suggestions(*args):
    # Met à jour la liste des suggestions en fonction du texte saisi
    search_term = search_var.get().lower()
    # Cacher la liste si le champ est vide
    if not search_term:
        suggestions_list.pack_forget()
    else:
        # Afficher la liste et mettre à jour les suggestions
        suggestions_list.pack()
        suggestions_list.delete(0, tk.END)  # Effacer les anciennes suggestions
        # Filtrer les mots qui commencent par le texte saisi
        suggestions = [word for word in teacher_list if word.lower().startswith(search_term)]
        # Ajouter les suggestions à la liste
        for word in suggestions:
            suggestions_list.insert(tk.END, word)

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
        print(f"'{selected_text}' a été supprimé de la liste")  # Feedback



# Liste de nom de proffesseur
teacher_list = [
    "Meunier", "Salomon", "Hertz", "Grelu", "Chassel", "Riton", "Philliams", "Saint-Paul", "Salaun", "Petit-jean",
    "Mignot", "Pellion", "Lugern", "Bidault", "Weber"
]

# Création de la fenêtre principale
window = tk.Tk()
window.title("Teacherdle")
window.geometry("500x300")

# Variable pour stocker le texte de recherche
search_var = tk.StringVar()
search_var.trace_add("write", update_suggestions) # trace est une méthode qui "espionne" la variable. Dès qu'elle est modifiée, elle appelle une fonction.

# Frame principal pour la barre de recherche et le bouton
main_frame = tk.Frame(window, padx=20, pady=20)
main_frame.pack()

# Sous-frame pour la barre de recherche et le bouton
search_button_frame = tk.Frame(main_frame)
search_button_frame.pack(fill=tk.X)

# Barre de recherche
search_entry = tk.Entry(
    search_button_frame, 
    textvariable=search_var, 
    width=40, 
    font=('Arial', 12)
)
search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Bouton d'entrer(confirmation)
enter_button = tk.Button(
    search_button_frame, 
    text="Entrer", 
    command=remove_selected_item,
    bg="#ff9999",
    font=('Arial', 12)
)
enter_button.pack(side=tk.RIGHT, padx=(10, 0))

# Liste des suggestions
suggestions_frame = tk.Frame(main_frame)
suggestions_frame.pack(fill=tk.X)
suggestions_list = tk.Listbox(
    suggestions_frame, 
    width=40, 
    height=6, 
    font=('Arial', 12)
)

# Lier la sélection dans la liste à la barre de recherche
suggestions_list.bind("<<ListboxSelect>>", select_suggestion)

# Bind de la touche Entrée
search_entry.bind("<Return>", lambda event: remove_selected_item())

# Lancement de l'application
window.mainloop()