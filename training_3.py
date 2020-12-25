
# ///////////////////////////////////////////////////////////////////
#                          Les structures de données.
# ///////////////////////////////////////////////////////////////////


Il existe quatre types de collection de données dans le langage de programmation Python:

    - List est une collection ordonnée, modifiable et indexée. Autorise les membres en double.
        mylist = [value1, value2,...]
    - Tuple est une collection ordonnée, immuable et indexée. Autorise les membres en double.
        mytuple = (value1, value2,...)
    - Set est une collection non ordonnée, modifiable et non indexée. Aucun membre en double.
        myset = {value1, value2,...}
    - Dictionary est une collection non ordonnée, modifiable et indexée. Aucun membre en double.
        thisdict = {
            "key1": "value1",
            "key2": "value2",...
            }

# -------------------------------------------lists-------------------------------------------------------------

mylist = [1,2,-8]                           # list of numbers
mylist = [True, False]                      # list of booleans
mylist = [9, "banana", -5.6, True]          # list of strings
mylist = ["pomme", "banane", "cerise"]      # list of strings

# affichr la list (on remarque qu'elle est ordonnée)
print(mylist)

# parcourir la list
for x in mylist:
    print(x)

# Access Items
print(mylist[1])                # Indexing
print(mylist[-1])               # Negative Indexing
print(mylist[2:5])              # Range of Indexes
print(mylist[:4])
print(mylist[:2])

# Change Item Value (on remarque qu'elle est modifiable)
mylist[1] = "cerise"

# ajouter une nouvelle valeur (on remarque qu'elle autorise les membres en double)
mylist.append("banane")
print(mylist)

# Check if Item Exists
if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")

# List Length
print(len(mylist))

# Remove Item
mylist.remove("banane")

# Join Two Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# -------------------------------------------Dictionaries-------------------------------------------------------------

mydict = {
    "fruit_1": "pomme",
    "fruit_2": "banane",
    "fruit_3": "cerise"
    }      # dictionaries of strings


# afficher la dictionaries (on remarque qu'elle est ordonnée)
print(mydict)

# parcourir la list
for x in mydict:
    print("the key is: ", x)
    print("the value is: ", mydict[x])

# # Indexing
print("fruit_1 est: ", mydict["fruit_1"])

# Change Values (on remarque qu'elle est modifiable et indexée , donc on doit changer toute la set)
mydict["fruit_1"] = "banane"

# ajouter une nouvelle valeur (on remarque qu'elle autorise pas les membres en double, il ecrase la l'ancienne valeur)
mydict["fruit_1"] = "haha"
print(mydict)

islemdict.pop("fruit_1")







# ///////////////////////////////////////////////////////////////////
#                             Function
# ///////////////////////////////////////////////////////////////////
# Une fonction est un bloc de code qui ne s'exécute que lorsqu'il est appelé.

# Vous pouvez transmettre des données, appelées paramètres, à une fonction.

# Une fonction peut renvoyer des données en conséquence.

# ------------------------------------------------------------------------------------------------------
# Creating a Function
def nom_fonction():
    # Code de la fonction
# Code hors fonction

def my_function():
  print("Hello from a learn and joy function")

# Calling a Function
my_function()


# Arguments or Parameters (kifkiffff)
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Islem", "Merzoug")

# Arbitrary Arguments, *args
# Si vous ne savez pas combien d'arguments seront passés à votre fonction,
# ajoutez un * avant le nom du paramètre dans la définition de la fonction.
# De cette façon, la fonction recevra un tuple d'arguments,
def my_function(*kids):  # dans cette exemple "kids" est un tuple
  print("The youngest child is " + kids[3])

my_function("Islem", "Assem", "Manel", "Amine")

# Keyword Arguments
def my_function(child3, child2, child1, child4):
  print("The youngest child is " + child4)

my_function(child1 = "Islem", child2 = "Assem", child3 = "Manel", child4 = "Amine")

# Arbitrary Keyword Arguments, **kwargs
# Si vous ne savez pas combien d'arguments de mot-clé seront passés à votre fonction,
# ajoutez deux astérisques: ** avant le nom du paramètre dans la définition de la fonction.
# De cette façon, la fonction recevra un dictionnaire d'arguments,

def my_function(**kid):# dans cette exemple "kids" est un enregistrement
  print("His last name is " + kid["lname"])

my_function(fname = "Islem", lname = "Merzoug")

# Parameter par defaut
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
# Renvoyer un résultat
# return True # Renverra toujours la même valeur.
# return var # Où var est une variable définit précédemment. La valeur renvoyée peut alors être différente.
# return input("Sélection: ") # On peut également renvoyer le résultat d'une autre fonction.
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def cube(n):
    return n ** 3

def volumeSphere(r):
    r_int = int(r)
    return 4 * 3.1416 * cube(r_int) / 3

r = input('Entrez la valeur du rayon : ')
print('Le volume de cette sphere vaut', volumeSphere(r))

# The pass Statement
# function definitions cannot be empty,
# but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def my_function():
    pass






# ///////////////////////////////////////////////////////////////////
#                          Gestion des exceptions.
# ///////////////////////////////////////////////////////////////////

# Exception Handling ( Gestion des exceptions )
# Lorsqu'une erreur se produit, ou une exception comme nous l'appelons,
# Python s'arrête normalement et génère un message d'erreur.

# Ces exceptions peuvent être gérées à l'aide de l'instruction try:
# ---------------------------------------------------------------------------------------

# Python Try Except

# Le bloc try vous permet de tester un bloc de code pour les erreurs.
# Le bloc except vous permet de gérer l'erreur.
# Le bloc finally vous permet d'exécuter du code, quel que soit le résultat des blocs try et except.

# ---------------------------------------------------------------------------------------
# exemple
try:
  print(x)
except:
  print("An exception occurred")

# plusieurs exceptions
# Vous pouvez définir autant de blocs d'exceptions que vous le souhaitez,
# par ex. si vous souhaitez exécuter un bloc de code spécial pour un type d'erreur particulier
# (NameError, SyntaxError, ZeroDivisionError):
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Else
# Vous pouvez utiliser le mot-clé else pour définir un bloc de code à exécuter si aucune erreur n'a été générée:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Finally
# Le bloc finally, s'il est spécifié, sera exécuté indépendamment du fait que le bloc try soulève une erreur ou non.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Lever  une exception
# nous allons créer notre propre exception
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Vous pouvez définir le type d'erreur à signaler et le texte à imprimer à l'utilisateur.
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")



# si le try Lever  une erreur le except s'execute
# Sinon si le try ne vouleve pas d'erreur le else s'execute
# le finally s'execute ( dans tout les cas )

# Les assertions ( PAYANT )
# Les assertions sont un moyen simple de s'assurer, avant de continuer, qu'une condition est respectée.
# En général, on les utilise dans des blocs try … except
assert test
# Si le test renvoie True, l'exécution se poursuit normalement. Sinon, une exceptionAssertionErrorest levée.
var = 5
assert var == 5
assert var == 8

# un exemple plus cool peut etre ?
annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")

