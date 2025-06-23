import create_database 
import sqlite3
import del_database
import random

del_database.delete_table()

co = sqlite3.connect("TeacherdleDB.db") #recuperation du connecteur
cu = co.cursor() #recuperation du curseur

create_database.initialisation_table(co,cu)# on initialise la table avec ces deux éléments
def get_infos_prof(name):
    finals_info = []
    infos = cu.execute("SELECT * FROM Teachers WHERE name=?", (name,)) #la virgule est nécessaire pour spécifier que c'est un tuple
    filtered_info = infos.fetchall() #fetchall récupère les lignes et les mets sous une liste de tuple
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
    a = random.randint(1,28)    #choix d un id de professeur aléatoire
    target = cu.execute("SELECT * from Teachers WHERE id={}".format(a)) 
    name_target = target.fetchall()   #on récupère le nom du professeur "cible" et on le montre pour l'instant
    target_teacher = name_target[0]
    print(target_teacher[1]) #voici le prof que l on veut (son nom)
    target2 = get_infos_prof(target_teacher[1])[0]
    
    return target2

def choice_citations():
    a = random.randint(1,15)
    citation = cu.execute("SELECT * from Citations WHERE id_cit=?",(a,))
    citation_filtrees = citation.fetchall()
    print(citation_filtrees)
    
    return citation_filtrees
