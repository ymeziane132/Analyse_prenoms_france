import pandas as pd

df = pd.read_csv("C:/Users/User/Desktop/EFREI/projet_prenom/datas/processed/prenoms_clean.csv", sep = ";")
""""
#on cherche les 10 prenoms les plus donnés
top_prenom = df.groupby("prenom")["valeur"].sum().sort_values(ascending = False).head(10)
print(top_prenom)

#separé les garcons et les filles

garcons = df[df["sexe"] == 1]
filles = df[df["sexe"] == 2]

#Analyser le prenom yacine dans le temps


def evolution(prenom, valeur):
    resultat = df[df["prenom"] == prenom].groupby("periode")[valeur].sum()

    return(resultat)
evolution_yacine = evolution("YACINE", "valeur")
print(evolution_yacine)


#Analyser l'année ou le nom YACINE a été le plus donné

def top_annee_yacine(prenom, valeur):
    top_annee = df[df["prenom"] == prenom].groupby("periode")[valeur].sum().sort_values(ascending = False).head(1)
    return(top_annee)

#Comparer 3 prenom avec utilisation de isin()

def compare_prenom(prenom, valeur) :
    resultat = df[df["prenom"].isin(prenom)].groupby(["periode", "prenom"])[valeur].sum()
    tableau = resultat.unstack(level ='prenom')
    return(tableau)

prenoms = ["YACINE", "PAUL", "MARIE"]
tableau = compare_prenom(prenoms, "valeur")
print(tableau)

#top 1 par année

def top_1_annee(valeur) :
       
    resultat =  df.groupby(["periode","prenom"])[valeur].sum().groupby(level = "periode").idxmax()
    return resultat

print(top_1_annee("valeur")) 
    
# Determiner les prenoms qui montent et qui baissent

def prenoms_baisse_monte(prenom, annee_debut, annee_fin):
    resultat = df[
        (df["prenom"] == prenom)
        & (df["periode"] >= annee_debut)
        & (df["periode"] <= annee_fin)
    ].groupby("periode")["valeur"].sum()

    valeur_debut = resultat.loc[annee_debut]
    valeur_fin = resultat.loc[annee_fin]

    if valeur_debut < valeur_fin:
        print("Le prénom monte")

    elif valeur_debut > valeur_fin:
        print("Le prénom baisse")

    else:
        print("Le prénom est stable")

prenoms_baisse_monte("YACINE", 1990, 1991)
"""

def evolution_prenom(prenom):
    resultat = df[df["prenom"] == prenom].groupby("periode")["valeur"].sum()
    return resultat

def compare_2prenom(prenom1, prenom2): 
        resultat = df[df["prenom"].isin([prenom1, prenom2])
                      ].groupby(["periode","prenom"])["valeur"].sum()
        tableau = resultat.unstack(level ='prenom')
        return(tableau)

def top10_par_annee(annee):
      resultat = df[df["periode"] == annee].groupby("prenom")["valeur"].sum().sort_values(ascending = False).head(10)
      return resultat

def top1_annee():
      resultat = df.groupby(["periode", "prenom"])["valeur"].sum().groupby(level = "periode").idxmax()
      return resultat

def progression(annee_debut,annee_fin):
      debut = df[df["periode"] == annee_debut].groupby("prenom")["valeur"].sum()
      fin = df[df["periode"] == annee_fin].groupby("prenom")["valeur"].sum()
      debut, fin = debut.align(fin, fill_value = 0)
      resultat = fin - debut
      return resultat

def diff_name_per_year():
      resultat = df.groupby("periode")["prenom"].nunique()
      return resultat
      
def prenoms_mixte():
      resultat = df.groupby("prenom")["sexe"].nunique()
      nb_sexe = resultat[resultat == 2]
      return nb_sexe

def equilibre():
      resultat = df.groupby(["prenom", "sexe"])["valeur"].sum().unstack()
      resultat_mixte = resultat.dropna()
      ecart = (resultat_mixte[1] - resultat_mixte[2]) / (resultat_mixte[1] +resultat_mixte[2])
      ecart = ecart.abs().sort_values() *100
      return ecart

print(equilibre())