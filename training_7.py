# ///////////////////////////////////////////////////////////////////
#                     Utilisation des fichiers
# ///////////////////////////////////////////////////////////////////

Modes d'ouvertures:
                    r (lecture seule)
                    w (écriture avec remplacement)
                    a (écriture avec ajout en fin de fichier)
                    x (lecture et écriture)
                    r+ (lecture/écriture dans un meme fichier)

Un chemin relatif en informatique est un chemin qui prend en compte l'emplacement de lecture.
Un chemin absolu est un chemin complet qui peut être lu quelque soit l'emplacement de lecture.



# La fonction open:
# Si d'autres applications, ou d'autres morceaux de votre propre code, souhaitent accéder à ce fichier,
# ils ne pourront pas car le fichier sera déjà ouvert.
fichier = open("fichier_txt.txt", "r")
print(fichier.read())

# Fermeture d'un fichier
fichier.close()

# Lire le contenu d'un fichier
fichier = open("fichier_txt.txt", "a")
fichier.write("\nHello world")
fichier.close()

# Le mot clé with
# Il existe une autre syntaxe plus courte qui permet de s'emanciper du problème de fermeture du fichier: le mot clé with .
with open("fichier_txt.txt", "r") as fichier:
	print(fichier.read())

# Enregistrer un objet dans un fichier
import pickle
with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)

data = {
  "fname":    "Islem Merzoug",
  "age":   22,
  "blabla":   "blabla",
  "blabla_again_xD":   "bah_blabla_once_again"
}
with open('donnees.txt', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(data)

# Récupérer nos objets enregistrés
with open('donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    data_recupere = mon_depickler.load()

# ///////////////////////////////////////////////////////////////////
#                     Python as an API
# ///////////////////////////////////////////////////////////////////
# Download and install "MySQL":
    # https://www.youtube.com/watch?v=WuBcTJnIuzo&ab_channel=ProgrammingKnowledge
# Download and install "MySQL Connector":
    # pip3 install mysql-connector
    # ou bien a partir du website: https://dev.mysql.com/downloads/installer/

# Python-MySql connectivity ERRORS (https://www.youtube.com/watch?v=KdboYKzD9HY&ab_channel=vrajeshdoshi)

# In mysql a database is called Schema

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin"
)

print(mydb)
mycursor = mydb.cursor() #imaginez le curseur comme un pointeur qui pointe vers la BD
# dans nous avons besoin vu que nous pouvons avour plusieurs base dans la meme machine (serveur)

# ----------------------------------------------------------------------------------------------------

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin"
)

print(mydb)
mycursor = mydb.cursor()

# Creating a Database
mycursor.execute("CREATE DATABASE mydatabase")   #mettre une requette sql
# Check if Database Exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)




# -----------------------------------------------CREATE TABLE-----------------------------------------------------

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="mydatabase"
)

print(mydb)
mycursor = mydb.cursor()

# Creating a Table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# Check if Table Exists
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)


# ----------------------------------------------INSERT ONE ROW------------------------------------------------------

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="mydatabase"
)

print(mydb)
mycursor = mydb.cursor()


# Insert Into Table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ('islem', 'Cartier Sghir Bejaia')
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
# Important!: Notez l'instruction: mydb.commit (). Il est nécessaire d'effectuer les modifications, sinon aucune modification n'est apportée à la table.


# ----------------------------------------------INSERT MULTIPLE ROWS------------------------------------------------------


# Insert Multiple Rows
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="mydatabase"
)

print(mydb)
mycursor = mydb.cursor()


# Insert Into Table

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
