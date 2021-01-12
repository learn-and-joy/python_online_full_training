
# rappel
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplace(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

a = Point(1, 2)
b = Point(3, 4)

# affichons le contenu de l'objet
print(a)
print(a.__dict__)

# Avant le deplacement
print("a : x =", a.x, "y =", a.y)
print("b : x =", b.x, "y =", b.y)

a.deplace(3, 5)
b.deplace(-1, -2)

# Apres le deplacement
print("a : x =", a.x, "y =", a.y)
print("b : x =", b.x, "y =", b.y)

# Mais, on peut modifier le contenu des Propriétés de notres classe
# a partir de l'exterieur de la classe comme suit

print(a.x)
a.x = 5

# Donc on encapsule:
# "" publics
# "_" protected (on verra son utilité quand on passera a l'heritage)
# "__" private ( attribut ou methode a utiliser seulement a l'interieur de la classe elle meme )
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def deplace(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy

    def affiche(self):
        print("abscisse =", self.__x, "ordonnee =", self.__y)

a = Point(2, 4)
a.affiche()

a.deplace(1, 3)
a.affiche()

a.x = 5
a.affiche()   # le x ne cange pas car il est privé


# Créeons les getters et les setters
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

a = Point(3, 7)

print(a._Point__x) # ne jamais laisser quelqu'un faire ça (grosse faille)

print("a : abscisse =", a.get_x())
print("a : ordonnee =", a.get_y())
a.set_x(6)
a.set_y(10)
print("a : abscisse =", a.get_x())
print("a : ordonnee =", a.get_y())




# ///////////////////////////////////////////////////////////////////
#               Heritage simple  et Héritage multiple
# ///////////////////////////////////////////////////////////////////
class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def printPersonName(self):
    print(self.firstname, self.lastname)

p1 = Person("Islem", "Merzoug")
p1.printPersonName()

class Employee(Person):
  pass

e1 = Employee("Mike", "Olsen")
e1.printPersonName()

class Student(Person):
  pass

s1 = Student("Mike", "Olsen")
s1.printPersonName()


# ///////////////////////////

class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def printPersonName(self):
    print(self.firstname, self.lastname)

p1 = Person("Islem", "Merzoug")
p1.printPersonName()


class Employee(Person):
  def __init__(self, firstname, lastname):
    Person.__init__(self, firstname, lastname)

e1 = Employee("Assem", "Merzoug")
e1.printPersonName()


# /////////////////////////////

class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, firstname, lastname, year):
    super().__init__(firstname, lastname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

s1 = Student("Mike", "Olsen", 2019)
s1.welcome()

# ///////////////////////////////heritage multiple////////////////////////////////////

class Humain:
    def __init__(self):
        print("C'est un humain")


class Person(Humain):
    def __init__(self):
        super().__init__()
        print("C'est une persone")

class Employee(Person, Humain):
    def __init__(self, firstname, lastname):
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname

    def printPersonName(self):
        print(self.firstname, self.lastname)

e1 = Employee("Abdelkader", "Korso")
e1.printPersonName()


# ///////////////////////////////////////////////////////////////////
#                    With Inheritance vs without inheritence
# ///////////////////////////////////////////////////////////////////
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

s1 = Square(10)
print(s1.area())
print(s1.perimeter())



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Ici, nous déclarons que la classe Square hérite de la classe Rectangle
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

s2 = Square(10)
print(s2.area())
print(s2.perimeter())
        




# ///////////////////////////////////////////////////////////////////
#                    Polymorphisme
# ///////////////////////////////////////////////////////////////////




# Exemple de fonctions polymorphes intégrées:
# len() being used for a string
print(len("Learn and joy"))

# len() being used for a list
print(len([1, 2, 3]))

# len() being used for a dict
print(len({
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}))



# Polymorphisme avec les méthodes de classe:
class Algeria():
    def capital(self):
        print("Alger la capitale d'Algérie")

    def language(self):
        print("Arabe et tmazight.")

    def type(self):
        print("Alger est un pays en développement.")


class USA():
    def capital(self):
        print("Washington, D.C. est la capitale des États-Unis.")

    def language(self):
        print("L'anglais est la langue principale des États-Unis.")

    def type(self):
        print("Les USA est un pays développé.")


obj_alg = Algeria()
obj_usa = USA()

obj_alg.capital()
obj_alg.language()
obj_alg.type()

obj_usa.capital()
obj_usa.language()
obj_usa.type()



# Polymorphisme avec héritage:
# Ce processus de réimplémentation d'une méthode dans la classe fille est connu sous le nom de remplacement de méthode Method Overriding (Method Overriding)
class Oiseau:
    def intro(self):
        print("Il existe de nombreux types d'oiseaux.")

    def vol(self):
        print("La plupart des oiseaux peuvent voler mais certains ne le peuvent pas.")


class Moineau(Oiseau):
    def vol(self):
        print("Les moineaux peuvent voler")


class Autruche(Oiseau):
    def vol(self):
        print("Les autruches ne peuvent pas voler.")


obj_oiseau = Oiseau()
obj_moi = Moineau()
obj_aut = Autruche()

obj_oiseau.intro()
obj_oiseau.vol()

obj_moi.intro()
obj_moi.vol()

obj_aut.intro()
obj_aut.vol()




# Le polymorphisme avec fonction
class French:
    def greeting(self):
        print("Bonjour")

class English:
    def greeting(self):
        print("Hello")

class Arabe:
    def greeting(self):
        print("سلام")


class Tamazight:
    def greeting(self):
        print("Azul")

def intro(language):
    language.greeting()


obj_en = English()
obj_fr = French()
obj_ar = Arabe()
obj_ta = Tamazight()

intro(obj_en)
intro(obj_fr)
intro(obj_ar)
intro(obj_ta)
