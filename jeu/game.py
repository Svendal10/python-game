# fonctioncomposer son équipe de héros
def composer_equipe_heros():
    # récuperer les informations de la database pour chaque héros (nom, vie, attaque, défense)
    # équipe du joueur vide, 3 héros à choisir 
        # vérifier l'état de l'équipe du joueur 
        # afficher les héros disponibles pour le joueur (faire en sorte que le joueur ne puisse pas choisir 2 fois le même héros)
        # demander au joueur de choisir un héros parmi les héros disponibles
        # ajouter le héros choisi à l'équipe du joueur
        # retirer le héros choisi de la liste des héros disponibles
        # renvoyer l'équipe du joueur une fois que le joueur a choisi 3 héros



# fonction combat entre le joueur et le monstre
def combat() : 
    # attaque du héros sur le monstre : 
       # parcourir les héros vivants 
       # l'équipe du personnage attaque le monstre (calcul des dégats : atk - def = dégats sur pv)
       # afficher les dégats infligés au monstre et sa vie restante
       # si le monstre est mort, terminer le combat
    # attaque du monstre sur le héros :
       # choisir un héros vivant aléatoirement
       # le monstre attaque le héros choisi (calcul des dégats : atk - def = dégats sur pv)
       # afficher les dégats infligés au héros et sa vie restante


# fonction lancer le jeu:
def lancer_jeu():
    # demander le pseudo du joueur
    # lancer la fonction composer son équipe de héros
    # compteur de vague à 0 
    # Boucle infinie tant que le joueur n'a pas perdu :
        # incrémenter le compteur de vague
        # générer un monstre aléatoire en fonction de la vague actuelle
        # afficher les informations du monstre
        # lancer la fonction combat entre le joueur et le monstre
            # tant que le joueur n'a pas perdu, il continue le jeu à l'infini 
    # Si l'équipe du joueur est morte,
        # fin de la boucle infinie et afficher un message de défaite
    # Si le monstre meurt, 
        # valider la vague au compteur de vague et passer à la suivante 
    # fin de la partie 
        # afficher message de défaites, score du joueur 
        # enregistrer le score dans mongoDB avec le pseudo du joueur, le score et la date de la partie
