import create_database 
import sqlite3
import del_database
import random

#lors du premier lancement, mettre en commentaire la ligne suivante
del_database.delete_table()

co = sqlite3.connect("TeacherdleDB.db") #recuperation du connecteur
cu = co.cursor() #recuperation du curseur

create_database.initialisation_table(co,cu)# on initialise la table avec ces deux éléments
def get_infos_prof(name):
    finals_info = []
    infos = cu.execute("SELECT * FROM Teachers WHERE name=?", (name,))
    filtered_info = infos.fetchall()
    for i in filtered_info:
        finals_info.append(list(i[1:]))
    return finals_info

def send_names():
    teacher_list = []
    names = cu.execute("""SELECT name FROM Teachers""")
    names_filtrés= names.fetchall()
    for i in range(len(names_filtrés)):
        teacher_list.append(names_filtrés[i][0])
    return teacher_list

def numbers_profs():
    numbers = cu.execute("SELECT id FROM Teachers")
    numbers_filtrés = numbers.fetchall()
    return len(numbers_filtrés)
    
def get_subject_prof(citation):
    res = cu.execute("SELECT Subject FROM Teachers WHERE name=?",(citation[0][2],))
    subject = res.fetchall()

    return (subject[0][0])
    
def choice_teachers():
#fin de la mise en place, on commence le jeu
    numb = cu.execute("SELECT COUNT(*) from Teachers")
    numbfetch = numb.fetchall()
    print(numbfetch[0][0])
    a = random.randint(1,numbfetch[0][0])    #choix d un id de professeur aléatoire
    target = cu.execute("SELECT * from Teachers WHERE id={}".format(a)) 
    name_target = target.fetchall()   #on récupère le nom du professeur "cible" et on le montre pour l'instant
    target_teacher = name_target[0]
    print(target_teacher[1]) #voici le prof que l on veut (son nom)
    target2 = get_infos_prof(target_teacher[1])[0]
    
    return target2

def choice_citations():
    numb = cu.execute("SELECT COUNT(*) from Citations")
    numbfetch = numb.fetchall()
    print(numbfetch[0][0])
    a = random.randint(1,numbfetch[0][0])
    citation = cu.execute("SELECT * from Citations WHERE id_cit=?",(a,))
    citation_filtrees = citation.fetchall()
    print(citation_filtrees)
    
    return citation_filtrees

def count_max_same_initial():
    names = send_names()
    initials = [name[0].upper() for name in names if name]  #Liste contenant les initiales (lettres majuscules) de tous les noms dans la liste names.
    counter_letters = {}  # dictionnaire vide
    for letter in initials:
        if letter in counter_letters:
            counter_letters[letter] += 1  # si déjà présent, on incrémente
        else:
            counter_letters[letter] = 1   # sinon, on l’ajoute avec 1
    
    max_count = max(counter_letters.values())  # récupère la valeur max du dictionnaire
    return max_count
