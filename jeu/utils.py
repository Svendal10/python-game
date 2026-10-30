from datetime import datetime
import pymongo

# récupérer la base de données MongoDB
def get_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["game_db"]
    return db


#  le pseudo du jouer 
def get_player_pseudo():
    while True :
        pseudo = input("Entrez votre pseudo : ")
        if pseudo.strip() == "":
            print("Le pseudo ne peut pas être vide. Veuillez réessayer.")
        else:
            return pseudo.strip()

# recuperer les heros de la db pour l'equipe du joueur
def get_heroes():
    db = get_db()
    db = get_db()
    return list(db["characters"].find())

# recuperer les monstres de la db aléatoirement 
def get_random_monster():
    db = get_db()
    monsters = list(db["monsters"].find())
    if not monsters:
        return None
    import random
    return random.choice(monsters)

# fonction pour enregistrer le score du joueur dans la base de données
def save_score(pseudo, score):
    db = get_db()
    score_data = {
        "pseudo": pseudo,
        "scores": score,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    db["scores"].insert_one(score_data)


# fonction pour récuprer les scores des joueurs dans la base de donnée
def get_scores(): 
    db = get_db()
    bestscores = db["scores"].find().sort("score", pymongo.DESCENDING).limit(10)
    return list(bestscores)
    # récupérer les scores des joueurs dans la collection "scores"
    # trier les scores du plus grand au plus petit
    # limiter l'affichage aux 10 meilleurs scores
    # afficher le classement des joueurs avec leur pseudo, score et date de la partie