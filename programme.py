import create_database 
import sqlite3
import del_database
import connectorandcursor
#lors du premier lancement, mettre en commentaire la ligne suivante
del_database.delete_table()

co = connectorandcursor.con()
cu = connectorandcursor.cur()

create_database.initialisation_table(co,cu)

res = cu.execute("SELECT id FROM Teachers")
resultar_requete = res.fetchall()

