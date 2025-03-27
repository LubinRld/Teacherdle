import sqlite3
import create_database
import del_database

#lors du premier lancement, mettre en commentaire la ligne suivante
del_database.delete_table()
create_database.initialisation_table()
con = sqlite3.connect('TeacherdleDB.db')
cur = con.cursor()
res = cur.execute("SELECT id FROM Teachers")
res.fetchall()
print(res)
