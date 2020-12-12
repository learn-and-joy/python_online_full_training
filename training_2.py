 ///////////////////////////////////////////////////////////////////
#                       Structures conditionnelles
# ///////////////////////////////////////////////////////////////////

# Conversion (Casting)
var = 10
print(type(var)) # Affiche <class 'int'>
var = str(var)
print(type(var)) # Affiche <class 'str'>
var = float(var)
print(type(var)) # Affiche <class 'float'>

# input et output
reponse = input() # Une ligne vide apparait et attend que l'utilisateur entre une information ( raw_input() in version 2.x)
age = input("Age : ") # "Age : " est affiché en début de ligne puis attend une information
# `age` et `reponse` contiennent ce que l'utilisateur a entré
print(reponse) # nous essayons d'afficher le contenu de la variable reponse
print(age) # nous essayons d'afficher le contenu de la variable reponse
# NB: les variables age et réponse sont de type str même si l’utilisateur a entré un nombre. Il ne sera donc pas possible,
# par exemple, de soustraire un nombre à l’âge récupéré. Ah moins que ... ah bah si, il suffit de convertir age en un int.

# donc nous pouvons faire les deux a la fois
num1 = int(input())
num2 = int(input())
print(num1 + num2)

# Prendre plusieurs entrées de l'utilisateur en Python
x, y, z = input("Entrer 3 valeurs: ").split()
print("Le premier est: ", x)
print("Le deuxieme est : ", y)
print("Le troisieme est : ", z)
print()

# taking two inputs at a time et afficher en utilisant la methode format()
a, b = input("Enter a two value: ").split()
print("First number is {} and second number is {}".format(a, b))
print()


#                                       Les structures conditionnelles
age = int(input("Quel est votre âge ? ")) # Souvenez-vous, il faut convertir en un entier
if age > 16: # Si l'âge est strictement supérieur à 16 (ans)
    print("Vous avez plus de 16 ans :)") # Une tabulation (touche Tab = 4 espaces)

# Maintenant, ajoutons quelques éléments :
age = int(input("Quel est votre âge ? "))
if age > 16: # Si l'âge est strictement supérieur à 16 (ans), age > 16 est appelé prédicat
    print("Vous avez plus de 16 ans :)")
elif age < 0: # Si l'âge est strictement inférieur à 0
    print("Tu te moquerais pas de moi ?")
else: # Dans tous les autres cas
    print("Tu es encore un peu jeune")
print("Au revoir")

#                                               Les opérations logiques
# Je vous présente donc le type booléen
vrai = True # Notez bien la majuscule
faux = False # Ici aussi
print(type(vrai)) # Affiche <class 'bool'>

#                    Les Combinaison
# Vous pouvez utiliser plusieurs opérateurs dans une même condition :
print(7 > 5 > 1) # Affiche True
print(7 > 5 < 9 != 10) # Affiche True

# Les opérateurs logiques
# Il est possible d’imbriquer des conditions en écrivant un if dans un if comme ceci :
couleur = "rouge"
poids = 10
if couleur == "rouge":
    if poids > 10:
        print("La couleur est rouge et le poids supérieur à 10")
# Bien qu’utile dans certains cas, dans cet exemple, il serait plus pratique de combiner des prédicats.

# Le ET logique
# Je vais vous montrer la syntaxe Python en reprenant l’exemple précédent :
if couleur == "rouge" and poids > 10:
    print("La couleur est rouge et le poids supérieur à 10")

# Le OU logique
if couleur == "verte" or poids == 15:
    print("La couleur est verte ou le poids égal à 15 ou les deux en même temps")

# Le NON logique
if not (couleur == "bleu" and poids > 20):
    print("Soit la couleur n'est pas bleue ou le poids n'ai pas superieur à 20 ou les deux en même temps")
    # Si la condition est vérifiée, alors on ne peut avoir simultanément couleur == bleu et poids > 20



# ///////////////////////////////////////////////////////////////////
#                             Boucles
# ///////////////////////////////////////////////////////////////////


# ///////////////////////////////Tant que////////////////////////////////////

# Table de multiplication du nombre 3
print(" 1 * 3 =", 1 * 3)
print(" 2 * 3 =", 2 * 3)
print(" 3 * 3 =", 3 * 3)
print(" 4 * 3 =", 4 * 3)
print(" 5 * 3 =", 5 * 3)
print(" 6 * 3 =", 6 * 3)
print(" 7 * 3 =", 7 * 3)
print(" 8 * 3 =", 8 * 3)
print(" 9 * 3 =", 9 * 3)
print("10 * 3 =", 10 * 3)

# nous devons simplifier la donne
nbr = 7
print(" 1 *", nbr, "=", 1 * nbr)
print(" 2 *", nbr, "=", 2 * nbr)
print(" 3 *", nbr, "=", 3 * nbr)
print(" 4 *", nbr, "=", 4 * nbr)
print(" 5 *", nbr, "=", 5 * nbr)
print(" 6 *", nbr, "=", 6 * nbr)
print(" 7 *", nbr, "=", 7 * nbr)
print(" 8 *", nbr, "=", 8 * nbr)
print(" 9 *", nbr, "=", 9 * nbr)
print("10 *", nbr, "=", 10 * nbr)

nbr = 7
print(" 1 *", nbr, "=", 1 * nbr)
print(" 2 *", nbr, "=", 2 * nbr)
print(" 3 *", nbr, "=", 3 * nbr)
print(" 4 *", nbr, "=", 4 * nbr)
print(" 5 *", nbr, "=", 5 * nbr)
print(" 6 *", nbr, "=", 6 * nbr)
print(" 7 *", nbr, "=", 7 * nbr)
print(" 8 *", nbr, "=", 8 * nbr)
print(" 9 *", nbr, "=", 9 * nbr)
print("10 *", nbr, "=", 10 * nbr)
# ce programme reste assez peu pratique et il accomplit une tâche bien répétitive.
# Les programmeurs étant très paresseux, ils préfèrent utiliser les boucles.

# ///////////////////////////////while////////////////////////////////////
# structure de base
while predicat:
Instructions

nbr = 3 # On garde la variable contenant le nombre dont on veut la table de multiplication
i = 1 # C'est notre variable compteur que nous allons incrémenter dans la boucle

while i <= 10: # Tant que i est strictement inférieure à 10
    print(i , "*", nbr, "=", i * nbr)
    i += 1 # On incrémente i de 1 à chaque tour de boucle

# ///////////////////////////////Pour////////////////////////////////////
# avec une chaine de caractere
chaine = "Bonjour les ZER0S"
for l in chaine:
    print(l)
# ---
chaine = "Bonjour les ZER0S"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print(lettre)
    else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
        print("*")

# Le mot-clé break
# L’instruction "break" permet de « casser » l’exécution d’une boucle (while ou for).
# Elle fait sortir de la boucle et passer à l’instruction suivante.
while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break

# Le mot-clé continue
# L’instruction "continue" permet de passer prématurément au tour de boucle suivant.
# Elle fait continuer sur la prochaine itération de la boucle.

i = 1
while i < 4: # Tant que i est inférieure à 20
    if i % 2 == 0:
        i += 1 # On ajoute 4 à i
        print("On incrémente i de 4. i =", i)
        continue # On retourne au while sans exécuter les autres lignes
    print("La variable i =", i)
    i += 1 # Dans le cas classique on ajoute juste 1 à i


