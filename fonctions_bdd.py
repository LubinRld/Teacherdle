import create_database 
import sqlite3
import del_database
import random

#lors du premier lancement, mettre en commentaire la ligne suivante
del_database.delete_table()

co = sqlite3.connect("TeacherdleDB.db") #recuperation du connecteur
cu = co.cursor() #recuperation du curseur

create_database.initialisation_table(co,cu)# on initialise la table avec ces deux éléments
def get_infos_prof(nom):
    infos_finales = []
    infos = cu.execute("SELECT * FROM Teachers WHERE nom=?", (nom,))
    infos_filtrées = infos.fetchall()
    for i in infos_filtrées:
        infos_finales.append(list(i[1:]))
    return infos_finales

def envoie_noms():
    teacher_list = []
    noms = cu.execute("""SELECT nom FROM Teachers""")
    noms_filtrés= noms.fetchall()
    for i in range(len(noms_filtrés)):
        teacher_list.append(noms_filtrés[i][0])
    return teacher_list

def nombres_profs():
    nombre = cu.execute("SELECT id FROM Teachers")
    nombre_filtrés = nombre.fetchall()
    return len(nombre_filtrés)
    
def get_subject_prof(citation):
    res = cu.execute("SELECT Subject FROM Teachers WHERE nom=?",(citation[0][2],))
    subject = res.fetchall()

    return (subject[0][0])
    
def choix_prof():
#fin de la mise en place, on commence le jeu
    a = random.randint(1,28)    #choix d un id de professeur aléatoire
    objectif = cu.execute("SELECT * from Teachers WHERE id={}".format(a)) 
    nom_objectif = objectif.fetchall()   #on récupère le nom du professeur "cible" et on le montre pour l'instant
    PROF_RECHERCHE = nom_objectif[0]
    print(PROF_RECHERCHE[1]) #voici le prof que l on veut (son nom)
    cible = get_infos_prof(PROF_RECHERCHE[1])[0]
    
    return cible

def choix_citations():
    a = random.randint(1,15)
    citation = cu.execute("SELECT * from Citations WHERE id_cit=?",(a,))
    citation_filtrees = citation.fetchall()
    print(citation_filtrees)
    
    return citation_filtrees
