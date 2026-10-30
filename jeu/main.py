# afficher le menu du jeu : 
def show_menu():
    print ("JEU RPG !")
    # commencer la partie 
    print ("1. Commencer la partie")
    # afficher le classement 
    print ("2. Afficher le classement")
    # quitter le jeu 
    print ("3. Quitter le jeu")


# affichace du classement :
def show_scoreboard(): 
    print ("CLASSEMENT DES JOUEURS :")
    # récupérer les scores des joueurs dans la base de données

    # affichage en rang / pseudo / score / date de la partie
    # si aucun score n'a été enregistré, afficher un message "aucun score enregistré"

# si le joueur choisit de commencer la partie, lancer le jeu
# si le joueur choisit d'afficher le classement, afficher le classement et revenir au menu principal
# si le joueur choisit de quitter le jeu, fermer l'application