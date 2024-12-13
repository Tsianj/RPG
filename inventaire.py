inventaire = [
    {"nom": "Boules de Noël", "quantite": 50, "prix": 1.5},
    {"nom": "Guirlandes", "quantite": 30, "prix": 3.0},
    {"nom": "Sapin de Noël", "quantite": 10, "prix": 25.0}
]

def afficher_menu():
    print("\n=========Menu:=========")
    print("1. Afficher l'inventaire")
    print("2. Ajouter un produit")
    print("3. Supprimer un produit")
    print("4. Quitter")

    choix = input("Choix: ")
    match choix:
        case "1":
            afficher_inventaire()
        case "2":
            ajouter_produit()
        case "3":
            modifier_quantite()
        case "4":
            supprimer_produit()
        case "5":
            rechercher_produit()
        case "6":
            valeur_totale_inventaire()
        case "7":
            quitter()
        case _:
            print("Choix invalide")

def afficher_inventaire():
    for produit in inventaire:
        print(f"{produit['nom']} - Quantité: {produit['quantite']} - Prix: {produit['prix']}")
    bouton_retour()


def ajouter_produit():
    nom = input("Nom du produit: ")
    quantite = int(input("Quantité: "))
    prix = float(input("Prix: "))
    inventaire.append({"nom": nom, "quantite": quantite, "prix": prix})
    print(f"Produit {nom} ajouté à l'inventaire.")
    bouton_retour()

def supprimer_produit():
    nom = input("Nom du produit à supprimer: ")
    for produit in inventaire:
        if produit['nom'] == nom:
            inventaire.remove(produit)
            print(f"Produit {nom} supprimé de l'inventaire.")
            return
    print(f"Produit {nom} non trouvé dans l'inventaire.")
    bouton_retour()

def quitter():
    print("Merci d'avoir utilisé le programme!")

def bouton_retour():
    input("Appuyer sur une touche pour revenir au menu...")
    afficher_menu()

def modifier_quantite():
    nom = input("Nom du produit à modifier: ")
    nouvelle_quantite = int(input("Nouvelle quantité: "))
    for produit in inventaire:
        if produit['nom'] == nom:
            produit['quantite'] = nouvelle_quantite
            print(f"Quantité de {nom} modifiée.")
            return
    print(f"Produit {nom} non trouvé dans l'inventaire.")
    bouton_retour()

def rechercher_produit():
    nom = input("Nom du produit à rechercher: ")
    for produit in inventaire:
        if produit['nom'] == nom:
            print(f"Produit trouvé: {produit}")
            return
    print(f"Produit {nom} non trouvé dans l'inventaire.")
    bouton_retour()

def valeur_totale_inventaire():
    total = 0
    for produit in inventaire:
        total += produit['quantite'] * produit['prix']
    print(f"Valeur totale de l'inventaire: {total}")
    bouton_retour()


afficher_menu()






