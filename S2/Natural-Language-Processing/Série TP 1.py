
# -*- coding: utf-8 -*- 
""" Déclaration de codage des caractères, utiliser souvent UTF-8, 
pour prendre en charge toutes les langues."""

# Partie 1 – Découvrir Python et sa Syntaxe ---------------------------------------------------

# Affichage
print("Hello, world!")

# ---------------------------

# Lire entrée utilisateur - String
username = input("Enter username:")
print("Username is : ", username)

# Lire entrée utilisateur - Entier
pw = int(input("Enter integer:"))
print("User pw is : ", pw)

# ---------------------------

# Déclaration des variables, pas de déclaration explicite.
# Suffit d'affecter une valeur pour spécifier le type de variable.

x = 5
y = "John"
z = True
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

age = 125 
print("Ttype de age", type(age))
salaire = 3.14
print("Type de salaire", type(salaire))
name = "Ahmed"
print("Type de name", type(name))

# Type Casting - conversion
x = str(3)    # x devient '3'
y = int(3)    # y devient 3
z = float(3)  # z devient 3.0

# Single or double quotes en Python
x = "John"
# same as
x = 'John'

# Assignation multiple de variables 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# ---------------------------

# String Formatting
age = 36
name = "John"

print("His name is", name, ". He is ", age, "years old.")

# Or
print(f"His name is {name}. He is {age} years old.")


# ---------------------------

# Python Datatypes - List

ls = [1, 2, 31, 4, 10, 98, 458]
print("Type de ls: ", type(ls))
print("Liste: ", ls)

# Ajouter un element à la liste
ls.append(5)
print(ls)

# Supprimer un element de la liste
ls.remove(5)
print(ls)

# Supprimer le dernier element de la liste et le retourner
last = ls.pop()
print(last, ls)

# List length
print(len(ls))

# Acces a list element by index
print(ls[1])

# Indice négatif : dernier element de la liste
print(ls[-1])

# Changer element
ls[2] = 35
print(ls)

# Sort list
ls.sort()
print(ls)

# Liste de mots
wordlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print (wordlist)

# List slicing
wordlist_slice = wordlist[2:5]
print(wordlist_slice)

print(wordlist[:4])

print(wordlist[2:])

# Une autre liste
other = ["abc", 34, True, 40, "male"]
print(other, len(other))

# Unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# ---------------------------

# Python Datatypes - Dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

print(car.keys())
print(car.values())

items = car.items()
print(items)

print(car["brand"])

print(len(car))

car["color"] = "white"
car["year"] = 2020
print(car)


# ---------------------------

# Python Datatypes - Set & Tuple

myset = {"apple", "banana", "cherry"}
print(myset)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# ---------------------------

# Structure de contrôle - if..elif..else

a = 33
b = 200
if b > a:
    # Attention aux tabulations/indentation (4 espaces)
    print("b is greater than a")

if b > a:
print("b is greater than a") # indentation error

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
    
# Tester si un élément appartient à une liste
a = 5
if a in ls:
    print("a existe dans la liste")

# ---------------------------

# Les boucles  - for loop

for x in range(0, 10, 1):
  print(x)

for x in range(10):
  print(x)

wordlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for word in wordlist:
    print (word)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in car.items():
  print(x, y)

for x in car.values():
  print(x)

# ---------------------------

# Les boucles  - while loop
i = 1
while i < 6:
  print(i)
  i += 1

# ---------------------------

# Les fonctions - Déclaration et appel

def my_func():
  print("Hello from a function")

my_func()

def other_func(name):
  print("Hello,", name)

other_func("Emil")
other_func("Tobias")

def mult_func(x):
  return 5 * x

prod = mult_func(10)
print(prod)


# Partie 2 – Quelques programmes ---------------------------------------------------

# Programme python qui permet de calculer le nombre d'occurrence d'un caractère dans un string
chaine = "Le TAL est l’ensemble des méthodes et des programmes..."
mycar= "e"
cpt = 0

for c in chaine:
    if c == caractere:
        cpt += 1

print(f"le caractère {mycar} existe {cpt} fois.")


# Programme python qui permet de calculer la fréquence des caractères dans un texte

input_string = "Le TAL est l’ensemble des méthodes et des programmes..."

frequencies = {} 

for char in input_string:    
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1   

print(frequencies)

# ---------------------------

# Programme python qui permet de calculer la fréquence des mots dans un texte 

input_string = "Programme python qui permet de calculer la fréquence des mots dans un texte de mots"

wordlist = input_string.split()

wordfreq = {} 

for word in wordlist:    
   if word in wordfreq: 
      wordfreq[word] += 1
   else: 
      wordfreq[word] = 1   

print(wordfreq)

# Les 6 mots les plus fréquents
print(sorted(wordfreq, key=wordfreq.get, reverse=True)[:6])


# ---------------------------

# Exercice

mylist = [25, 4, 87, 25, 945, 2, 8, 7, 21, 6]
print(mylist)

new_list = []
for n in mylist:
    if n % 2 != 0 and n not in new_list :
        new_list.append(n)
print(new_list)

if mylist[-1] < mylist[-2]:
    mylist.pop()
print(mylist)

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
    "speed": [120, 180, 220]
}
print(thisdict)

myset = set()
for k in thisdict.keys():
    myset.add(k)
print(myset)

mystr = "Hello, Python !"
for c in mystr:
    print(c)

def remove_char(mystr, n):
    if n > len(mystr):
        return None
    return mystr[n:]

print(remove_char("pynative", 4))
print(remove_char("pynative", 2))
print(remove_char("pynative", 15))