from datetime import datetime
import pymongo

# récupérer la base de données MongoDB
def get_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["game_db"]
    return db

# fonction pour récuprer les scores des joueurs dans la base de données
    # récupérer les scores des joueurs dans la collection "scores"
    # trier les scores du plus grand au plus petit
    # limiter l'affichage aux 10 meilleurs scores
    # afficher le classement des joueurs avec leur pseudo, score et date de la partie