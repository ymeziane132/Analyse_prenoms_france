# Analyse des prénoms en France — Python & Data Analysis

## Présentation du projet

Ce projet consiste à explorer et analyser l'évolution des prénoms attribués en France à partir de données statistiques de naissances.

L'objectif est de mettre en pratique les différentes étapes d'un projet de Data Analysis : **nettoyage des données, transformation, analyse statistique et visualisation**.

L'étude repose sur un jeu de données de plus de **724 000 observations**, traité à l'aide de Python, Pandas et Matplotlib.
Source des données

Les données utilisées dans ce projet proviennent de l'INSEE (Institut national de la statistique et des études économiques).

Source officielle : INSEE — [Fichier des prénoms](https://www.insee.fr/fr/statistiques/8595130?sommaire=8595113#titre-bloc-6)

Jeu de données : Fichier national des prénoms

Période : 1900–2025

Format : CSV

Volume : plus de 724 000 observations
## Technologies utilisées

- **Python** : développement des fonctions d'analyse.
- **Pandas** : nettoyage, filtrage, agrégation et transformation des données.
- **Matplotlib** : création de graphiques.
- **Jupyter Notebook** : exploration interactive et visualisation des résultats.
- **Git / GitHub** : versionnement et partage du projet.

## Structure du projet

```text
projet_prenom/
├── datas/
│   └── processed/
│       └── prenoms_clean.csv
├── src/
│   ├── analysis.py
│   ├── clean_data.py
│   ├── main.py
│   ├── main.ipynb
│   └── visualisation.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

Le dossier `datas/raw/`, utilisé pour les données d'origine, est exclu du dépôt GitHub.

## Étapes réalisées

### 1. Préparation et nettoyage des données

- Chargement des données CSV avec `pd.read_csv()`.
- Exploration de la structure du DataFrame avec `shape`, `columns`, `dtypes` et `info()`.
- Identification des valeurs manquantes.
- Suppression des observations contenant des valeurs manquantes avec `dropna()`.
- Exportation des données nettoyées dans `prenoms_clean.csv`.

### 2. Analyse statistique des prénoms

Développement de fonctions Python permettant de réaliser plusieurs analyses :

**Classement des prénoms les plus populaires**
- Agrégation des naissances par prénom avec `groupby()`.
- Calcul des effectifs cumulés.
- Classement décroissant avec `sort_values()`.

**Évolution d'un prénom dans le temps**
- Filtrage des observations selon le prénom.
- Agrégation des effectifs par année.
- Analyse des variations de popularité.

**Comparaison de deux prénoms**
- Sélection de plusieurs prénoms avec `isin()`.
- Regroupement des données par année et par prénom.
- Transformation des résultats avec `unstack()` pour faciliter la comparaison.

**Analyse des prénoms par année**
- Identification des 10 prénoms les plus attribués pour une année donnée.
- Recherche du prénom le plus populaire par année.

**Analyse des prénoms mixtes**
- Agrégation des naissances par prénom et par sexe.
- Identification des prénoms utilisés pour les deux sexes.
- Calcul d'un indicateur d'équilibre entre les effectifs masculins et féminins.

### 3. Visualisation des données

Création de graphiques avec Matplotlib :

- **Line plots** : évolution temporelle d'un prénom.
- **Bar charts horizontaux** : classement des prénoms les plus populaires.
- Visualisation comparative des tendances entre plusieurs prénoms.

Ces représentations permettent d'identifier les tendances et de rendre les résultats plus facilement interprétables.

### 4. Organisation du code

- Séparation des traitements entre plusieurs scripts Python.
- Centralisation des fonctions d'analyse dans `analysis.py`.
- Création d'un script dédié au nettoyage des données.
- Utilisation de notebooks Jupyter pour les analyses exploratoires et les visualisations.



## Prochaines étapes

- [ ] Développer des visualisations supplémentaires : répartition par sexe, tendances décennales et classements historiques.
- [ ] Étudier les prénoms présentant les plus fortes hausses et baisses de popularité.
- [ ] Ajouter des indicateurs statistiques sur la diversité des prénoms au fil du temps.
- [ ] Créer un tableau de bord interactif avec Streamlit ou Plotly.
- [ ] Améliorer la gestion des erreurs et la validation des entrées utilisateur.
- [ ] Ajouter des tests unitaires pour les fonctions d'analyse.
- [ ] Automatiser le pipeline de chargement, de nettoyage et d'analyse.

## Compétences développées

- Manipulation de DataFrames avec Pandas.
- Nettoyage et préparation de données.
- Analyse exploratoire (EDA).
- Agrégation et transformation de données.
- Visualisation de séries temporelles.
- Structuration d'un projet Python.
- Versionnement du code avec Git.

## Utilisation de ChatGPT

J'ai utilisé **ChatGPT comme assistant pédagogique et technique** au cours de ce projet, notamment pour approfondir ma compréhension des fonctionnalités de Pandas, identifier certaines erreurs de programmation et améliorer l'organisation du code.

Cette démarche s'inscrit dans un objectif d'apprentissage pratique de l'analyse de données, avec une attention particulière portée à la compréhension des opérations effectuées et à l'interprétation des résultats.

## Statut du projet

**Première version fonctionnelle — améliorations en cours.**

Les fonctionnalités de nettoyage, d'analyse statistique et de visualisation sont développées. Les prochaines évolutions porteront notamment sur l'interactivité des analyses et la création d'un tableau de bord.
