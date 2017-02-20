#coding: utf-8

#Je fais tout le nécessaire pour lire un fichier .csv tel que vu en classe.

import csv
import re

fichier = "concordia1.csv"
f1 = open(fichier)

lignes = csv.reader(f1)

#J'exclu la première ligne qui correspond aux titre des colonnes dans le tableau.
next(lignes)

#Je défini deux variables dans lesquelles je vais stocker des informations plus tard dans ma loop.
genre = []
nbPages = []

#Je construit un dictionnaire qui me servira à remplacer les chiffres romains par des chiffres arabes en vérifiant certains documents qui ont des erreurs dans la graphie des chiffres romains pour m'assurer de leur réelle signification.
r = {
  "i":"1","ii":"2","iii":"3","iiii":"4","iv":"4","ivx":"4","v":"5","vi":"6","vii":"7","viii":"8","viiii":"9","ix":"9","x":"10","xi":"11","xii":"12","xiii":"13","xiv":"14","xIv":"14","xv":"15","xvi":"16","xvii":"17","xviii":"18","xix":"19","xx":"20","xxi":"21","xxii":"22","xxiii":"23","xxiv":"24","xxv":"25","xxvi":"26","xxvii":"27","xxviii":"28","xxix":"29","xxx":"30","xxxi":"31", "xxxii":"32", "xxxiii":"33","xxxiv":"34","xxxv":"35","xxxvii":"37","xxxviii":"38","vix":"9","xliv":"44","xlvii":"47","xlix":"49"
  
}

#Je débute ma loop.

for ligne in lignes:
  #Pour ma variable nom, j'inverse nom et prénom tel que présenté dans le csv.
  nom = "{} {}".format(ligne[1],ligne[0])
  #Le titre est le 3e élément de chaque ligne.
  titre = ligne[2]
  #La longueure du titre se calcule avec un len.
  longTitre = len(ligne[2])
  #J'isole la section qui a trait à la pagination (romaine et arabe).
  pages = ligne[5]
  
  #Si la section débute avec un chiffre arabe.   
  if pages.startswith(("1","2","3","4","5","6","7","8","9","0")):
    #Je ne garde que les trois premiers caractères que je convertie en integer pour éventuellement les additionner pour faire un total des pages.
      nbPages = int(pages[0:3])
      
  #Si la section débute par un chiffre romain.   
  if pages.startswith(("i","x","v")):
       #J'isole chaque composate de la "pagination" pour en dégager la numératie romaine.
       pagination = pages.split(',',1)
       romain = pagination[0]
       #Je fais correspondre le string romain à son équivalence arabe dans le dictionnaire (essaie-erreur avec un print pour les mauvaises graphies dans le csv).
       rom = int(r[romain])
       #J'isole ensuite la section de la "pagination" qui comprend la graphie arabe.
       arabes = pagination[1]
       arabe = arabes.split()
       a = arabe[0]
       #Je nettoie cette section pour ne conserver que les chiffres que je converti en integer.
       a1 = re.sub("[^0-9]","", a)
       a2 = a1.strip()
       #Petit hack ici: j'ai dû aller jouer dans le csv à quelques fois pour remplacer des "<vide> leaves" par des "0 leaves" pour facilier la conversion en integer.
       nbPages = int(a2)
       #J'additionne les deux integer pour faire la somme des pages.
       sum = nbPages + rom
  
  #Si la section du genre de document (mémoire ou maîtrise) contient un «M.», c'est un mémoire.
  if "M." in ligne[6]:
      genre = "Le mémoire"
      
      #Sinon, c'est une thèse. 
  else:
         genre = "La thèse"
         
  #Je print avec le format demandé dans les consignes du travail.
  print("{} de {} compte {} pages. Son titre est {} ({} caratères).".format(genre,nom,sum,titre,longTitre))
  
  #Pour une raison que j'ignore, mais que je soupçonne en lien avec la "priorité des opérations" de ma loop, mon script ne fonctionne pas très bien pour le "genre" de document jusqu'à une centaine de ligne et ensuite tout va bien...
