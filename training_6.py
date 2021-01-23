# ///////////////////////////////////////////////////////////////////
#                    Abstract Class and Abstract Method
# ///////////////////////////////////////////////////////////////////
# ABC: Abstract Base Classes
# abstractmethod
# Une classe abstraite peut être considérée comme un modèle pour d'autres classes. Il vous permet de créer un ensemble de méthodes qui doivent être créées dans
# toutes les classes enfants construites à partir de la classe abstraite. Une classe qui contient une ou plusieurs méthodes abstraites est appelée une classe abstraite.
# Une méthode abstraite est une méthode qui a une déclaration mais qui n'a pas d'implémentation. Pendant que nous concevons de grandes unités fonctionnelles,
# nous utilisons une classe abstraite. Lorsque nous voulons fournir une interface commune pour différentes implémentations d'un composant, nous utilisons une classe abstraite.

from abc import ABC, abstractmethod

class Polygon(ABC):

    # abstract method
    @abstractmethod
    def numOfSides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def numOfSides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def numOfSides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def numOfSides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def numOfSides(self):
        print("I have 4 sides")

    # Driver code


R = Triangle()
R.numOfSides()

K = Quadrilateral()
K.numOfSides()

R = Pentagon()
R.numOfSides()

K = Hexagon()
K.numOfSides()







# ///////////////////////////////////////////////////////////////////
#                    Les décorateurs
# ///////////////////////////////////////////////////////////////////
# Le décorateur peut modifier le comportement:

# definir un decorateur
def salut_decorator(function):
    # inner1 est une fonction Wrapper dans dont l'argument est appelé

    # La fonction inner peut accéder au local externe
    # fonctions comme dans ce cas "function"
    def inner():
        print("Bonjour, c'est avant l'exécution de la fonction")

        function()

        print("C'est après l'exécution de la fonction")

    return inner


# définir une fonction, à appeler à l'intérieur de la fonction salut_decorator
def function_used():
    print("This is inside the function !!")


# passing 'function_used' inside the
# décorateur pour contrôler son comportement
function_used = salut_decorator(function_used)

# appeler la fonction
function_used()


# --------------------------------------------------------------------

# rappel:
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

myFun('learn', 'and', 'joy', first="Learn", mid="And", last="Joy")









# --------------------------------------------------------------------

# importing libraries
import time
import math

# décorateur pour calculer la durée
# pris par n'importe quelle fonction.
def exectution_time(func):
    # ajout d'arguments à l'intérieur de inner,
    # si la fonction prend des arguments,
    # peut être ajouté comme ceci.
    def inner(*args, **kwargs):
        # stockage du temps avant l'exécution de la fonction
        begin = time.time()

        func(*args, **kwargs)

        # stockage du temps après l'exécution de la fonction
        end = time.time()
        print("Temps total pris en: ", func.__name__, end - begin)

    return inner


# ceci peut être ajouté à n'importe quelle fonction présente,
# dans ce cas pour calculer une factorielle
@exectution_time
def factorial(num):
    # dormir 3 secondes car cela prend moins de temps
    # afin que vous puissiez voir la différence réelle
    time.sleep(3)
    print(math.factorial(num))


# calling the function.
factorial(10)

# ---------------------------------------------------------------

# Et si une fonction renvoie quelque chose?!

def salut_decorator(func):
    def inner(*args, **kwargs):
        print("before Execution")

        # obtenir la valeur retournée
        # func(*args, **kwargs)
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # renvoyer la valeur
        # return func
        return returned_value

    return inner


# ajouter un décorateur à la fonction
@salut_decorator
def sum_two_numbers(a, b):
    print("À l'intérieur de la fonction")
    return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))





















# ///////////////////////////////////////////////////////////////////
#                    Les modules Math et random
# ///////////////////////////////////////////////////////////////////

# -------------------------------La fonction Math-------------------------------
# https://docs.python.org/fr/3.5/library/math.html

import math

print(math.pow(5, 2)) # 5 au carré

5 ** 2 # Pratiquement identique à pow(5, 2)

print(math.sqrt(25)) # Racine carrée de 25 (square root)

print(math.exp(5)) # Exponentielle

print(math.fabs(-3)) # Valeur absolue



# -------------------------------La fonction random-------------------------------
import random
print(random.random())

# La fonction randrange prend trois paramètres :
    # la marge inférieure de l'intervalle ;
    # la marge supérieure de l'intervalle ;
    # l'écart entre chaque valeur de l'intervalle (1par défaut), pas incluse.

print(random.randrange(5, 10, 2))

# La fonctionrandintprend deux paramètres :
    # là encore, la marge inférieure de l'intervalle ;
    # la marge supérieure de l'intervalle, cette fois incluse.

print(random.randint(1, 6))

print(random.choice(['a', 'b', 'k', 'p', 'i', 'w', 'z']))

# Elle prend en paramètre une séquence et la mélange
liste = ['a', 'b', 'k', 'p', 'i', 'w', 'z']
random.shuffle(liste)
print(liste)




# ///////////////////////////////////////////////////////////////////
#                    La modularité
# ///////////////////////////////////////////////////////////////////
# Je vous invite à consulter l'aide pour le module: os.path
import os

# Le chemin d’accès absolu se rapporte toujours au dossier parent du serveur (racine).

# le chemin d’accès absolu en hard code

# Les langages de programmation qui ont leurs racines dans UNIX et le langage de programmation C, tels que Python, utilisent la barre oblique inverse (\) comme caractère d'échappement.
# Par exemple, \n correspond à un retour chariot. Comme les chemins peuvent contenir des barres obliques inverses,
# vous devez empêcher l'utilisation de la barre oblique inverse comme caractère d'échappement.
# Une technique courante consiste à utiliser un caractère d'échappement pour la barre oblique inversée, comme suit :
path = "C:\\Users\\MIRAGE\\Desktop\\Learnandjoy\\Cours\\E-Learning\\python\\paid_trainings\\code"

# Une autre méthode consiste à convertir les chemins en chaînes brutes Python à l'aide de la directive r, comme illustré ci-dessous.
# Cela indique à Python d'ignorer les barres obliques inverses.
path = r"C:\Users\MIRAGE\Desktop\Learnandjoy\Cours\E-Learning\python\paid_trainings\code"

# dirname(p)  →   Retourne le dossier parent de l'élément
path = os.path.dirname(__file__)
print(path)

# le chemin d’accès relatif en hard code
# par exemple
path = r"..\code\session_one\quiz_one.py"








# abspath(path)   →   Retourne un chemin absolu
print(os.path.abspath("."))

filename = os.path.join(path, 'relative/path/to/file/you/want')
print(filename)

# dirname(p)  →   Retourne le dossier parent de l'élément
print(os.path.dirname(path))

# basename(p)  →   Retourne le dernier élément d'un chemin
print(os.path.basename(path))

# join(path, s)  →   Ajoute un élément au chemin passé en paramètre
print(os.path.join(path, "func"))

# split(p)  →   Fractionne un chemin d'accès. Retourne un tuple
print(os.path.split(path))

# listdir(p)  →   Retourne la liste des elements d'un répertoire
print(os.listdir(path))










# testPuissance.py
# go to File | Invalidate Caches... and restarting PyCharm helps.

# Exemple : on importe une seule fonction
from puissance import carre

a = 5
u = carre(a)
print("le carre vaut", u)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Exemple : on importe explicitement les deux fonctions

from puissance import carre, cube

a = 5
u = carre(a)
print("le carre vaut", u)
v = cube(a)
print("le cube vaut", v)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Exemple : on importe toutes les fonctions

from puissance import *
# L’importation de toutes les fonctions avec * est fortement déconseillée.
# En effet, elle ne permet pas d’avoir une vision claire des fonctions qui ont été importées.
# Ceci est donc une source potentielle d’erreurs.

a = 5
u = carre(a)
print("le carre vaut", u)
v = cube(a)
print("le cube vaut", v)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Exemple : on importe le module

import puissance

a = 5
u = puissance.carre(a)
print("le carre vaut", u)
v = puissance.cube(a)
print("le cube vaut", v)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Exemple : on importe le module et on lui donne un alias

import puissance as pu
a = 5
u = pu.carre(a)
print("le carre vaut", u)
v = pu.cube(a)
print("le cube vaut", v)
