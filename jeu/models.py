# faire une classe pour centraliser les rèlges du jeu 
class CombatRules : 
# récupérer la db 
    def __init__(self, data):
# nom du personnage
        self.name = data.get ("nom", "Inconnu")
# santé max 
        self.max_hp = int (data.get ("Max hp", 100))
# santé actuelle 
        self.hp = int (data.get ("hp", self.max_hp))
# attaque
        self.atk = int (data.get ("atk", 10))
# défense
        self.defense = int (data.get ("defense", 5))

# Vérifier si le personnage est vivant
    def is_alive(self):
        return self.hp > 0

# système de dégats : 
    def take_damage(self, attacker_atk):
        damage = attacker_atk - self.defense
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            