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




Teacherdle 是一个 Wordle 类型的游戏，也就是说，您必须从一个教师列表中猜出一位教师。
我们使用一个数据库来存储教师的信息（公共数据，不含个人信息）。

要运行游戏，只需克隆 git 目录，然后运行以下命令：
```

pip install pillow
```
这是我们的数据库 UML 图：
![image](https://github.com/user-attachments/assets/8e3337ae-208d-4614-b51c-7964583a9607)

在这个数据库中，我们有教师的信息以及与之相关的语录。


下面是游戏算法的工作原理：
![image](https://github.com/user-attachments/assets/b99424e1-ec4c-43c6-ae8e-da27575bf4c7)




我们还有一个 “引文 ”游戏，让你猜哪位老师说过一句引文，算法基本相同，但尝试三次后会得到提示。
