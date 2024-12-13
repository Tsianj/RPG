import random

def creer_personnage(nom, classe):
    """Crée un nouveau personnage avec les attributs de base"""
    return {
        "nom": nom,
        "classe": classe,
        "niveau": 1,
        "points_de_vie": 100,
        "inventaire": [
            {"nom": "potion de soin", "quantité": 3}
        ]
    }

def ajouter_objet(personnage, nom_objet, quantite=1):
    """Ajoute un objet à l'inventaire du personnage"""
    for item in personnage["inventaire"]:
        if item["nom"] == nom_objet:
            item["quantité"] += quantite
            return
    
    personnage["inventaire"].append({
        "nom": nom_objet,
        "quantité": quantite
    })

def monter_niveau(personnage):
    """Fait monter le personnage d'un niveau"""
    personnage["niveau"] += 1
    personnage["points_de_vie"] += 20
    print(f"{personnage['nom']} passe au niveau {personnage['niveau']}!")

def utiliser_potion(personnage):
    """Utilise une potion de soin si disponible"""
    for item in personnage["inventaire"]:
        if item["nom"] == "potion de soin" and item["quantité"] > 0:
            soin = random.randint(1, 50)
            personnage["points_de_vie"] += soin
            item["quantité"] -= 1
            print(f"{personnage['nom']} se soigne de {soin} points de vie!")
            return True
    print("Pas de potion disponible!")
    return False

def afficher_personnage(personnage):
    """Affiche les détails du personnage"""
    print("\n=== Détails du personnage ===")
    print(f"Nom: {personnage['nom']}")
    print(f"Classe: {personnage['classe']}")
    print(f"Niveau: {personnage['niveau']}")
    print(f"Points de vie: {personnage['points_de_vie']}")
    print("\nInventaire:")
    for item in personnage["inventaire"]:
        print(f"- {item['nom']}: {item['quantité']}")
    print("==========================\n")

def attaquer(attaquant, defenseur):
    """Gère l'attaque entre deux personnages"""
    degats = 10 * attaquant["niveau"]
    defenseur["points_de_vie"] -= degats
    print(f"{attaquant['nom']} inflige {degats} points de dégâts à {defenseur['nom']}!")
    
    # Vérifie si le défenseur est mort
    if defenseur["points_de_vie"] <= 0:
        print(f"{defenseur['nom']} est vaincu!")
        # Transfert de l'inventaire
        for item_defenseur in defenseur["inventaire"]:
            ajouter_objet(attaquant, item_defenseur["nom"], item_defenseur["quantité"])
        defenseur["inventaire"] = []
        return True
    return False

# Test du code
if __name__ == "__main__":
    # Création des personnages
    hero = creer_personnage("Aragorn", "Guerrier")
    ennemi = creer_personnage("Gobelin", "Monstre")
    
    # Test des fonctions
    afficher_personnage(hero)
    
    ajouter_objet(hero, "épée", 1)
    ajouter_objet(hero, "potion de soin", 2)
    
    monter_niveau(hero)
    utiliser_potion(hero)
    
    afficher_personnage(hero)
    
    # Test du combat
    attaquer(hero, ennemi)
    afficher_personnage(ennemi)