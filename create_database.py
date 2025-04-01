import sqlite3
import connectorandcursor

def initialisation_table(connection,cursor):
    
    
    cursor.execute("""CREATE TABLE Teachers (
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL ,
        Genre TEXT NOT NULL,
        Hair_status TEXT NOT NULL,
        Region TEXT NOT NULL,
        Thesis TEXT NOT NULL,
        Type TEXT NOT NULL,
        Subject TEXT NOT NULL,
        Fonction TEXTE NOT NULL)"""
    )
    cursor.execute("""CREATE TABLE Citations (
        id_cit INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Text TEXT NOT NULL,
        Teacher TEXT NOT NULL CONSTRAINT FK_teachers_citations REFERENCES Teachers(id))
        """)
    cursor.execute("""INSERT INTO Teachers VALUES (1,"test1","test1","test1","test1","test1","test1","test1","test1")
                ,(2,"test2","test2","test2","test2","test2","test2","test2","test2")
    
    """)
    connection.commit()

#données à rentrer bien évidemment