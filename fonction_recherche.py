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

# Liste de nom de professeur
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

# Cadre principal
frame = tk.Frame(window)
frame.pack(pady=20)

# Barre de recherche
search_entry = tk.Entry(frame, textvariable=search_var, width=50, font=('Arial', 12))
search_entry.pack()

# Liste des suggestions
suggestions_list = tk.Listbox(frame, width=50, height=5, font=('Arial', 12))

# Lier la sélection dans la liste à la barre de recherche
suggestions_list.bind("<<ListboxSelect>>", select_suggestion)

# Lancement de l'application
window.mainloop()