import create_database 
import sqlite3
import del_database
import connectorandcursor
import random
#lors du premier lancement, mettre en commentaire la ligne suivante
del_database.delete_table()

co = connectorandcursor.con()
cu = connectorandcursor.cur()

create_database.initialisation_table(co,cu)

res = cu.execute("SELECT id FROM Teachers")
resultat_requete = res.fetchall()
print(resultat_requete)
#fin de la mise en place, on commence le jeu
a = random.randint(1, 2)
objectif = cu.execute("SELECT nom from Teachers WHERE id={}".format(a))
Nom_objectif = print(objectif.fetchall())
win = 0
nbr_essais = 5
while win !=1 or nbr_essais != 0:
    nbr_essais -= 1
    #algorithme de jeu
    