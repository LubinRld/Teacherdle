import sqlite3

conn = sqlite3.connect('TeacherdleDB.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE Teachers (
    id TEXT NOT NULL PRIMARY KEY,
    Genre TEXT NOT NULL,
    Hair_status_above_nose TEXT NOT NULL,
    Hair_status_below_nose TEXT NOT NULL,
    Region TEXT NOT NULL,
    Thesis TEXT NOT NULL,
    Type TEXT NOT NULL,
    Subject TEXT NOT NULL,
    Fonction TEXTE NOT NULL);"""
)
cur.execute("""CREATE TABLE Citations (
    id_cit INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Text TEXT NOT NULL,
    Teacher TEXT NOT NULL CONSTRAINT FK_teachers_citations REFERENCES Teachers(id)
);
            
            
            
            """)