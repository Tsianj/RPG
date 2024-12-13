import random

list_personnage = []

def ajouter_objet_inventaire(personnage, objet, quantite):
    for item in personnage['inventaire']:
        if item['nom'] == objet:
            item['quantité'] += quantite
            return
    personnage['inventaire'].append({'nom': objet, 'quantité': quantite})

def utiliser_potion(personnage):
    for item in personnage['inventaire']:
        if item['nom'] == "potion de soin" and item['quantité'] > 0:
            soin = random.randint(1, 50)
            personnage['points_de_vie'] += soin
            item['quantité'] -= 1
            print(f"{personnage['nom']} se soigne de {soin} points de vie!")
            return True
    print("Pas de potion disponible!")
    return False

def monter_niveau(personnage):
    personnage['niveau'] += 1
    personnage['points_de_vie'] += 20
    print(f"{personnage['nom']} passe au niveau {personnage['niveau']}!")

def afficher_personnage(personnage):
    print("\n=== Détails du personnage ===")
    print(f"Nom: {personnage['nom']}")
    print(f"Classe: {personnage['classe']}")
    print(f"Niveau: {personnage['niveau']}")
    print(f"Points de vie: {personnage['points_de_vie']}")
    print("\nInventaire:")
    for item in personnage['inventaire']:
        print(f"- {item['nom']}: {item['quantité']}")
    print("==========================\n")       

def attaquer(attaquant, defenseur):
    degats_base = random.randint(1, 10)
    degats_total = degats_base * attaquant['niveau']
    defenseur['points_de_vie'] -= degats_total
    print(f"{attaquant['nom']} attaque {defenseur['nom']} et lui inflige {degats_total} points de dégâts!")

def est_vivant(personnage):
    return personnage['points_de_vie'] > 0

def generer_monstre(niveau):
    noms_monstres = ["Gobelin", "Troll", "Ogre", "Dragon", "Squelette"]
    monstre = {
        "nom": random.choice(noms_monstres),
        "points_de_vie": 50 * niveau,
        "niveau": niveau,
        "classe": "Monstre",
        "inventaire": []
    }
    return monstre

while True:
    print("==============MENU==============")
    print("1. Créer un personnage")
    print("2. Charger un personnage")
    print("3. Quitter")
    print("=================================")

    choix = input("Choix : ")

    if choix == "1":
        creation_en_cours = True
        while creation_en_cours:
            print("\n=== Création du Personnage ===")
            personnage = {}
            personnage["nom"] = input("Nom : ")
            
            # Choix de la classe
            while True:
                print("\nChoisissez votre classe:")
                print("1. Guerrier (Spécialiste du combat rapproché)")
                print("2. Archer (Expert en attaques à distance)")
                print("3. Mage (Maître des sorts)")
                
                choix_classe = input("Votre choix (1-3): ")
                match choix_classe:
                    case "1":
                        personnage["classe"] = "Guerrier"
                        break
                    case "2":
                        personnage["classe"] = "Archer"
                        break
                    case "3":
                        personnage["classe"] = "Mage"
                        break
                    case _:
                        print("Choix invalide! Veuillez choisir entre 1 et 3.")
            
            personnage["niveau"] = 1
            personnage["points_de_vie"] = 100
            personnage["inventaire"] = [{"nom": "potion de soin", "quantité": 3}]
            list_personnage.append(personnage)
            print(f"\nPersonnage créé avec succès! Vous êtes maintenant un {personnage['classe']}")
            creation_en_cours = False
    elif choix == "2":
        print("\n=== Liste des Personnages ===")
        if not list_personnage:
            print("Aucun personnage n'a été créé")
        else:
            for i, personnage in enumerate(list_personnage, 1):
                print(f"{i}. {personnage['nom']} - Classe: {personnage['classe']} - Niveau: {personnage['niveau']}")
            
            choix_perso = input("\nChoisissez un personnage (numéro) : ")
            try:
                index = int(choix_perso) - 1
                if 0 <= index < len(list_personnage):
                    personnage_choisi = list_personnage[index]
                    print(f"\nVous avez choisi {personnage_choisi['nom']} !")
                    print(f"Points de vie : {personnage_choisi['points_de_vie']}")
                    print("Inventaire :")
                    for item in personnage_choisi['inventaire']:
                        print(f"- {item['nom']} (x{item['quantité']})")
                    
                    en_combat = True
                    monstre = {
                        "nom": "Gobelin",
                        "points_de_vie": 50,
                        "niveau": 1,
                        "classe": "Monstre",
                        "inventaire": []
                    }
                    
                    while en_combat and est_vivant(personnage_choisi) and est_vivant(monstre):
                        print("\n=== Menu Combat ===")
                        print("1. Attaquer")
                        print("2. Utiliser une potion")
                        print("3. Fuir")
                        print(f"\nVos PV: {personnage_choisi['points_de_vie']} | PV du monstre: {monstre['points_de_vie']}")
                        
                        action = input("Choisissez une action : ")
                        
                        match action:
                            case "1":
                                attaquer(personnage_choisi, monstre)
                                if est_vivant(monstre):
                                    attaquer(monstre, personnage_choisi)
                            
                            case "2":
                                utiliser_potion(personnage_choisi)
                                if est_vivant(monstre):
                                    attaquer(monstre, personnage_choisi)
                            
                            case "3":
                                print(f"{personnage_choisi['nom']} fuit le combat!")
                                en_combat = False
                            
                            case _:
                                print("Action invalide!")
                        
                        if not est_vivant(monstre):
                            print(f"\nVictoire! {monstre['nom']} a été vaincu!")
                            if monstre['inventaire']:
                                for item in monstre['inventaire']:
                                    print(f"Vous avez trouvé: {item['nom']} (x{item['quantité']})")
                                    ajouter_objet_inventaire(personnage_choisi, item['nom'], item['quantité'])
                            
                            monter_niveau(personnage_choisi)
                            ajouter_objet_inventaire(personnage_choisi, "potion de soin", 1)
                            print("Vous avez gagné une potion de soin!")
                            
                            afficher_personnage(personnage_choisi)
                            
                            # Demander si le joueur veut continuer
                            choix_suite = input("\nVoulez-vous continuer l'aventure? (o/n): ")
                            if choix_suite.lower() == 'o':
                                print("\nPréparation du prochain combat...")
                                monstre = generer_monstre(personnage_choisi["niveau"])
                            else:
                                en_combat = False
                                print("Retour au menu principal...")
                        
                        elif not est_vivant(personnage_choisi):
                            print(f"\nDéfaite! {personnage_choisi['nom']} a été vaincu!")
                            en_combat = False
                else:
                    print("Numéro de personnage invalide")
            except ValueError:
                print("Veuillez entrer un numéro valide")
    elif choix == "3":
        print("\n=== Au revoir! ===")
        print("Merci d'avoir joué à notre jeu de rôle!")
        print("À bientôt pour de nouvelles aventures!")
        break  # Sort de la boucle while True principale
    else:
        print("Choix invalide")


