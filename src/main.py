import pandas as pd
import matplotlib.pyplot as plt
from analysis import evolution_prenom, compare_2prenom

#Charger les données csv
df = pd.read_csv("C:/Users/User/Desktop/EFREI/projet_prenom/datas/processed/prenoms_clean.csv", sep = ";")
"""""
print(top_prenom)
print("Analyse du prenm YACINE dans le temps : ", evolution_yacine)
print("l'année ou yacine est le plus apparu est ", (top_annee_yacine("YACINE", "valeur")))
"""
prenom = input("Entrez un prenom à analyser : ")
evolution = evolution_prenom(prenom)
print(evolution)

#graphique du prenom par annee
evolution.plot(kind="line", figsize=(10, 6), marker="o")
plt.xlabel("Année")
plt.ylabel("Nombre de naissances")
plt.legend(title="Prénom")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

#graph pour comparaison entre 2 prenoms

prenom1 = input("Entrez un premier prenom : ")
prenom2 = input("Entrez un second prenom : ")

comparaison = compare_2prenom(prenom1, prenom2)
print(comparaison)

comparaison.plot(kind="line", figsize=(10, 6), marker="o")
plt.xlabel("Année")
plt.ylabel("Nombre de naissances")
plt.legend(title="Prénom")
plt.show()