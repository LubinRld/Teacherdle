import sqlite3
#citation de riton : "on peut intuiter un condensateur plan infini"
def initialisation_table(connection,cursor):
    
    
    cursor.execute("""CREATE TABLE Teachers (
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL , 
        Genre TEXT NOT NULL,
        Thesis TEXT NOT NULL,
        Type TEXT NOT NULL,
        Subject TEXT NOT NULL,     
        Fonction TEXTE NOT NULL)""" 
    )
    #dans l'ordre, il y a : nom du professeur, genre, capillosité, quel originalité, 
    # date de la première thèse, type de prof (CM ou TD), matière enseigné,
    #et enfin la fonction dans l'école (directeur, chargé des 1ère années)

    cursor.execute("""CREATE TABLE Citations (
        id_cit INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Text TEXT NOT NULL,
        Teacher TEXT NOT NULL CONSTRAINT FK_teachers_citations REFERENCES Teachers(id))
        """)
    cursor.execute("""INSERT INTO Teachers (nom, Genre, Thesis, Type, Subject, Fonction) VALUES
('BRACHAIS', 'M', '1996', 'CM ET TD', 'CHIMIE', 'DIRECTEUR GEIPI ET RESPO GEIPI 1'),
('BIDAULT', 'M', '1995', 'CM ET TD', 'PHYSIQUE', 'RESPO LV2'),
('RITON', 'M', '2011', 'CM ET TD', 'MATHEMATIQUES', 'Aucune'),
('MIGNIOT', 'M', '2012', 'CM ET TD', 'INFORMATIQUE', 'Aucune'),
('WEEBER', 'M', '1996', 'CM ET TD ET TP', 'PHYSIQUE', 'Aucune'),
('SALOMON', 'M', '1991', 'TD', 'PHYSIQUE', 'Aucune'),
('SALAUN', 'F', '1996', 'CM ET TD', 'PHYSIQUE', 'RESPO 3A MATERIAUX'),
('HORRIGUE', 'M', '2012', 'CM ET TD', 'MATHEMATIQUES', 'Aucune'),
('SELLAMI', 'F', 'OUI', 'TD ET TP', 'INFORMATIQUE', 'Aucune'),
('LUGUERN', 'M', '2021', 'CM ET TD ET TP', 'ELECTRONIQUE', 'Aucune'),
('PETITJEAN', 'M', '2015', 'CM ET TD', 'MATHEMATIQUES', 'Aucune'),
('CHAMBRION', 'M', '2004', 'CM ET TD', 'MATHEMATIQUES', 'Aucune'),
('GRANDJEAN', 'F', 'NON', 'CM ET TD', 'COMMUNICATION', 'SERVICE COMMUNICATION ET RELATIONS SOCIO ECONOMIQUES'),
('MEUNIER', 'M', 'NON', 'CM ET TD ET TP', 'INFORMATIQUE', 'RELATIONS INTERNATIONALES'),
('SERIER', 'F', 'NON', 'TD ET TP', 'INFORMATIQUE', 'Aucune'),
('KIRGIZOV', 'M', '2014', 'CM ET TD', 'INFORMATIQUE', 'PROF DE RUSSE'),
('BEZE', 'M', 'NON', 'TD ET TP', 'INFORMATIQUE', 'Aucune'),
('SAINT PAUL', 'M', 'NON', 'TD', 'LANGUE', 'Aucune'),
('PHILLIAN', 'F', 'NON', 'TD', 'LANGUE', 'Aucune'),
('GRELU', 'M', '1996', 'CM ET TD', 'PHYSIQUE', 'RESPO GEIPI 2'),
('HERTZ', 'M', '2000', 'CM ET TD', 'PHYSIQUE', 'Aucune'),
('LEMAITRE', 'M', '2014', 'CM ET TD', 'MATHEMATIQUES', 'Aucune'),
('VAGO', 'F', '1998', 'CM ET TD', 'MATHEMATIQUES', 'Aucune'),
('GINHAC', 'M', '1999', 'CM ET TD ET TP', 'INFORMATIQUE', 'Aucune'),
('CHASSEL', 'M', 'NON', 'CM ET TD ET TP', 'INFORMATIQUE', 'Aucune'),
('COILLET', 'M', '2011', 'CM ET TD ET TP', 'PHYSIQUE', 'Aucune'),
('MORPHU', 'M', '2002', 'CM ET TD', 'ELECTRONIQUE ET INFORMATIQUE', 'Aucune');
    """)
    connection.commit()

#données à rentrer bien évidemment