import pandas as pd

print("projet python lancé")

#Charger les données csv
df = pd.read_csv("C:/Users/User/Desktop/EFREI/projet_prenom/datas/raw/prenoms-2025-nat_csv/prenoms-2025-nat.csv", sep = ";")

print(df.isna().sum())
df = df.dropna(subset = ["prenom"])
print(df.isna().sum())
df = df.loc[df["periode"] >= 1990]
print(df["periode"].min)
print(df["periode"].max)
print(df.shape)

df.to_csv("datas/processed/prenoms_clean.csv", sep = ";", index = False)
