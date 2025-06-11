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
    
    
def choix_prof():
#fin de la mise en place, on commence le jeu
    a = random.randint(1,26)    #choix d un id de professeur aléatoire
    objectif = cu.execute("SELECT * from Teachers WHERE id={}".format(a)) 
    print(cu)
    nom_objectif = objectif.fetchall()   #on récupère le nom du professeur "cible" et on le montre pour l'instant
    PROF_RECHERCHE = nom_objectif[0]
    print(PROF_RECHERCHE[1]) #voici le prof que l on veut (son nom)
    cible = get_infos_prof(PROF_RECHERCHE[1])[0]
    
    return cible

"""
    win = 0
    nbr_essais = 5
    while win !=1 and nbr_essais != 0:
       nbr_essais = nbr_essais-1
         guess = input() #on guess
        print(PROF_RECHERCHE[0]) #nom du prof cible
        print(guess) #voila ce que l on guess
        if PROF_RECHERCHE[0] == guess: #on compare si c'est la même chose
            
            for i in range (6):
                print("vrai")
            print("win")
            # fin de buzz si c est win
            
        else: 
            result_guess_not_fetched = cu.execute("SELECT * from Teachers WHERE nom ='{}' ".format(guess)) #les données de notre résultat
            result_guess = result_guess_not_fetched.fetchall()  # le tableau propre de nos données
            print(result_guess) #voici notre guess avec ces infos
            for i in range (6):
                if (result_guess[0])[i] == (tableau_recherche[0])[i]: #algo de verification
                    print("vrai")
                else :
                    print("faux")
            print(" fin des infos, on peut re guess")
            
"""