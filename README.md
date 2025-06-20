# Teacherdle
For English informations, you can go [here](#English-Version) : 

Teacherdle est un jeu de type Wordle, c'est à dire que l'on doit deviner un professeur de l'école parmi une liste des autres.
Nous utilisons une base de données pour stocker les informations sur les professeurs (données publiques, rien de personnel)

Pour faire fonctionner le jeu, il suffit de cloner le répertoire git, et d'effectuer la commande :
```

pip install pillow

```
Voici notre diagramme UML de la Base de donnée :
![image](https://github.com/user-attachments/assets/8e3337ae-208d-4614-b51c-7964583a9607)

Dans cette base de donnée, nous avons les informations sur les professeurs, ainsi que les citations qui leurs sont associées.


Voici le fonctionnement de l'algorithme de jeu :
![image](https://github.com/user-attachments/assets/b99424e1-ec4c-43c6-ae8e-da27575bf4c7)




Nous avons aussi le jeu des citations, ou l'on doit deviner quel professeur a dit une citation, l'algorithme de jeu est globalement le même, on a juste un oindice aux bout de trois essais.









<a name="English-Version"></a>
# English Version

Teacherdle is a Wordle-like game, which means that you hav to guess a Teachers from the engineering school among a lis of most of them.
Here, we're using a database to stock and use the data about each teachers (only public data, nothing personal or private)

Before starting, you need to install pillow : 
```

pip install pillow

```

UML diagramm of our database

![image](https://github.com/user-attachments/assets/9c019b0d-b48e-4b20-a8ad-12120b50a1fb)

Here is the working of the algorithm :
![image](https://github.com/user-attachments/assets/e392895d-105a-4cc7-89f5-a59f4730201e)

We also got the Game of the Citations, where you must guess who says something, it works the same, with, in addition, you get a hint after 3 unsuccessfull tries



