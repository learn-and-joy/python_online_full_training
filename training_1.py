# _______________________l'interpreteur Python______________________

>>> premier pas avec l'interpreteur Python
# erreur

>>> 7
7

>>> 9.5
9.5

# Addition, soustraction, multiplication, division (+, -, *, /)
>>> 3.2 + 1 # Addition
4.2
>>> 7 - 3 # Soustraction
4
>>> 6 * 5 # Multiplication
30
>>> 1 / 3 # Division
0.3333333333333333


# le python retourne un float comme resultat d'une devision
>>> 10 / 5
2.0
>>> 10 / 3
3.3333333333333335

# Division entière
>>> 10 // 3
3
>>>

# Modulo
>>> 10%3
1

# La puissance
>>> 2 ** 3
8

# Vous avez sans doute remarqué le # suivi de texte. Ceci s’appelle un commentaire. Le dièse
# informe Python que tout ce qui se trouve sur la même ligne après lui ne le concerne pas

"""
Un commentaire
sur plusieurs lignes que Python ignorera
"""

# _______________________coder dans des fichiers python______________________

Ecrire son code dans des fichiers
connaitre la liste des mots clé dans python
connaire la liste des variables sous python


#L’encodage
L’encodage est la façon dont les ordinateurs se représentent le texte. Il existe de nombreux
encodages différents, et donc des représentations différentes. Python a besoin de savoir dans
quel encodage vous travaillez pour pouvoir lire correctement votre fichier.

# Généralement sous Windows
-*-coding:Latin-1 -*
# Généralement sou Linux ou Mac ( par default )
-*-coding:Utf-8 -*

# Variables
# le "=" est un operateur d'affectation
# nous ne sommes pas obligés d'utiliser ";" comme marque de fin d'instruction, 
# le retour a la ligne c'est la plus utilisée
a = 5
print(a) # Affiche 5
b = 8.2
print(a + b) # Affiche 13.2
print(a) # Affiche 5
a = 10
print(a) # Affiche 10
a = b + 1
print(a) # Affiche 9.2
c = 1
c = c + 3 # c vaut 4

# un petit racouris
a, b = 4, 5.2 # a vaut 4 et b vaut 5.2

# Supposons que l’on souhaite intervertir les valeurs de a et b. La première idée qui pourrait
# surgir est :
a = b
b = a
# or
c = a
a = b
b = c
# ou mieux:
a, b = b, a

# Les types de données
print(type(1)) # Affiche <class 'int'>
print(type(1.0)) # Affiche <class 'float'>

# Les chaînes de caractères
chaine = 'Et voilà du texte'
chaine2 = "Et encore du texte"
chaine3 = """Toujours plus de texte mais sur plusieurs lignes"""
# Ces trois types de délimiteurs différents ont une utilité :
# chaine = 'Aujourd'hui' # Erreur
# chaine2 = "J'ai cassé Python"
# chaine3 = """Demain,
# je le réparerai"""

# mais il existe un caractère bien utile qui va nous sauver : le backslash \. a utiliser avant le délimiteur.
chaine = 'Nous l\'avons'
chaine2 = "\"réparé\""
# NB: \n signifie donc « retour à la ligne » pour Python.
print('Bonjour,\nVisiteur')
