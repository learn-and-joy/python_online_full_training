# ///////////////////////////////////////////////////////////////////
#                    Gérer les chaînes de caractères
# ///////////////////////////////////////////////////////////////////

l = [1, 2, 8, 0]

for i in l:
    print(i)

for i in range(10): # de 0 jusqu'a 10
    print(i)

pour i de 0 a 10 faire
    ecrire(i)

for i in range(3, 10): # de 3 jusqu'a 10
    print(i)

for i in range(3, 10, 2): # de 3 jusqu'a 10 avec un pas de deux
    print(i)



# méthodes de la classe str

def convertir_en_minuscule(chaine):
    minuscule = chaine.lower()
    print(minuscule)


chaine = "LEARN AND JOOOOOOOOOOY !"
convertir_en_minuscule(chaine)

def convertir_en_majuscule(chaine):
    majuscule = chaine.upper()
    print(majuscule)

chaine = "learn and jooooooooooy !"
convertir_en_majuscule(chaine)


def premiere_lettre_en_minuscule(chaine):
    capitalize = chaine.capitalize()
    print(capitalize)

chaine = "learn and jooooooooooy !"
premiere_lettre_en_minuscule(chaine)


def retirer_espaces_debut_fin(chaine):
    result = chaine.strip()
    print(result)

chaine = "     learn and jooooooooooy !        "
retirer_espaces_debut_fin(chaine)

def ajouter_espaces_debut_fin_majuscule(chaine):
    result = chaine.upper().center(30)   # le 30 est le nombre finale de caractraires dans la chaine de caractaire
    print(result)

chaine = "learn andjooooooooooy"
ajouter_espaces_debut_fin_majuscule(chaine)

# rappelle sur la concatination 
age = 21
message = "J'ai " + age + " ans."  #erreur
message = "J'ai " + str(age) + " ans."
print(message)

# Accéder aux caractères d'une chaîne
# imaginons notre chaine de caracteire comme une list de caractraires
chaine = "LEARN AND JOY"
chaine = ["L", "E", "A", "R", "N", "A", "N", "D", "J", "O", "Y"]

# pour acceder au troisième caractère de la chaine on utilise l'indexation
print(chaine[0])
print(chaine[7])
print(chaine[-1])  #neative indexing

# longueur de la chaine 
print(len(chaine))

# Sélection de chaînes
presentation = "salut"
presentation[0:2] # On sélectionne les deux premières lettres
presentation[2:len(presentation)] # On sélectionne la chaîne sauf les deux premières lettres

# Pourquoi ne pas avoir défini cette fonction comme une méthode de la classe str ? Pourquoi ne pourrait-on pas faire chaine.len()?
# on verra sa dans pas long temps ( avec les classes)

# En résumé (syntax):
# Chaque classe définit certaines fonctions, appelées méthodes, qui seront accessibles depuis l'objet grâce à objet.methode(arguments).
# On peut directement accéder à un caractère d'une chaîne grâce au code suivant : chaine[position_dans_la_chaine]
# Il est tout à fait possible de sélectionner une partie de la chaîne grâce au code suivant : chaine[indice_debut:indice_fin]



# ///////////////////////////////////////////////////////////////////
#                    La portée des variables et références
# ///////////////////////////////////////////////////////////////////


Au Python, comme dans la plupart des langages, on trouve des règles qui définissent la portée des variables. 
La portée utilisée dans ce sens c'est « quand et comment les variables sont-elles accessibles ? ».

# Dans nos fonctions, quelles variables sont accessibles ?
var1 = "variable globale"
def print_var():   
    var2 = "variable locale"  
    print("La variable globale = {0}.".format(var1))
    print("La variable locale = {0}.".format(var2))
 
print_var()  
print("La variable locale = {0}.".format(var2))


# La variable a n'est pas passée en paramètre de la fonction print_var. 
# Et pourtant, Python la trouve, tant qu'elle a été définie avant l'appel de la fonction.

# L'espace local:
# Python va regarder dans l'espace local dans lequel la fonction a été appelée. Et là, 
# il trouve bien la variable a et peut donc l'afficher.

# Les variables globales:
var = "variable globale"
def print_var():
    global var #nous avons surchargé la variable globale par une variable locale
    var = "variable locale"  
    print("La variable = {0}.".format(var))
 
print_var()  
print("La variable = {0}.".format(var))


# mettons en place une fonction qui detecte les variables
def test():
    var = "lol"
    print(var)

def detecte_var(nouvelle_valeur):
    """Fonction nous permettant de tester la portée des variables définies dans notre corps de fonction"""

    # On essaye d'afficher la variable var, si elle existe
    try:
        print("Avant l'affectation, notre variable var vaut {0}.".format(var))
    except NameError:
        print("La variable var n'existe pas encore.")
    var = nouvelle_valeur
    print("Après l'affectation, notre variable var vaut {0}.".format(var))

detecte_var("la valeur de var")



# ///////////////////////////////////////////////////////////////////
#                           Classes/Objects
# ///////////////////////////////////////////////////////////////////



# To create a class
class MyClass:
  x = 5

# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    def __init__(self): # Notre méthode constructeur
        """Constructeur de notre classe. Chaque attribut va être instancié
        avec une valeur par défaut... original"""
        
        self.nom = "Dupont"
        self.prenom = "Jean" # Quelle originalité
        self.age = 33 # Cela n'engage à rien
        self.lieu_residence = "Paris"

jean = Personne()
print(jean.nom)
print(jean.prenom)


# //////////////////////////////////////////////////////
class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    def __init__(self):  # Notre méthode constructeur
        """Constructeur de notre classe. Chaque attribut va être instancié
        avec une valeur par défaut... original"""

        self.nom = "Dupont"
        self.prenom = "Jean"  # Quelle originalité
        self.age = 33  # Cela n'engage à rien
        self.lieu_residence = "Paris"


jean = Personne()
print(jean.nom)
print(jean.prenom)
print(jean.age)
print(jean.lieu_residence)


class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self.lieu_residence = "Paris"

bernard = Personne("Islem", "Merzoug")
print(bernard.nom)
print(bernard.prenom)
print(bernard.age)


# /////////////////////////////////////////////////
# exercice pratique
class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        la surface du tableau"""

        print(self.surface)

    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""

tab = TableauNoir()
tab.lire()
tab.ecrire("Salut tout le monde.")
tab.lire()
tab.effacer()
tab.lire()
