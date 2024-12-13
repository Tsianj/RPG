import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

class JeuRPG:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Jeu RPG")
        self.fenetre.geometry("800x600")
        
        # Charger les images des armes
        self.images_armes = {
            "Guerrier": tk.PhotoImage(file="images/guerrier.png"),
            "Archer": tk.PhotoImage(file="images/archer.png"),
            "Mage": tk.PhotoImage(file="images/mage.png")
        }
        
        self.personnages = []
        self.personnage_actuel = None
        self.monstre_actuel = None
        
        self.charger_personnages()
        self.creer_menu_principal()

    def charger_personnages(self):
        """Charge les personnages sauvegardés"""
        if os.path.exists("personnages.json"):
            with open("personnages.json", "r") as f:
                self.personnages = json.load(f)

    def sauvegarder_personnages(self):
        """Sauvegarde les personnages"""
        with open("personnages.json", "w") as f:
            json.dump(self.personnages, f)

    def creer_menu_principal(self):
        """Crée le menu principal"""
        # Nettoyage de la fenêtre
        for widget in self.fenetre.winfo_children():
            widget.destroy()

        # Création des boutons
        frame = ttk.Frame(self.fenetre, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="RPG Game", font=("Arial", 24)).pack(pady=20)

        ttk.Button(frame, text="Créer un personnage", 
                  command=self.afficher_creation_personnage).pack(pady=10)

        charger_btn = ttk.Button(frame, text="Charger un personnage",
                               command=self.afficher_selection_personnage)
        if not self.personnages:
            charger_btn.state(['disabled'])
        charger_btn.pack(pady=10)

    def afficher_creation_personnage(self):
        """Affiche l'écran de création de personnage"""
        for widget in self.fenetre.winfo_children():
            widget.destroy()

        frame = ttk.Frame(self.fenetre, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Création de personnage", font=("Arial", 20)).pack(pady=10)

        # Nom
        ttk.Label(frame, text="Nom:").pack()
        nom_var = tk.StringVar()
        ttk.Entry(frame, textvariable=nom_var).pack()

        # Classe
        ttk.Label(frame, text="Classe:").pack()
        classe_var = tk.StringVar(value="Guerrier")
        classes = ["Guerrier", "Archer", "Mage"]
        for classe in classes:
            ttk.Radiobutton(frame, text=classe, variable=classe_var, 
                          value=classe).pack()

        # Création d'un label pour l'image
        self.label_image = ttk.Label(frame)
        self.label_image.pack(pady=10)

        def mise_a_jour_image(*args):
            classe = classe_var.get()
            self.label_image.configure(image=self.images_armes[classe])

        # Mettre à jour l'image quand la classe change
        classe_var.trace('w', mise_a_jour_image)
        
        # Afficher l'image initiale
        mise_a_jour_image()

        def confirmer():
            nom = nom_var.get()
            classe = classe_var.get()
            if nom:
                # Déterminer l'arme de départ selon la classe
                arme_depart = {
                    "Guerrier": {"nom": "épée", "dégâts": 10},
                    "Archer": {"nom": "arc", "dégâts": 8},
                    "Mage": {"nom": "bâton", "dégâts": 12}
                }[classe]
                
                nouveau_perso = {
                    "nom": nom,
                    "classe": classe,
                    "niveau": 1,
                    "points_de_vie": 100,
                    "inventaire": [
                        {"nom": "potion de soin", "quantité": 3},
                        {"nom": arme_depart["nom"], "quantité": 1, "dégâts": arme_depart["dégâts"]}
                    ]
                }
                self.personnages.append(nouveau_perso)
                self.sauvegarder_personnages()
                self.personnage_actuel = nouveau_perso
                self.afficher_ecran_jeu()
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un nom")

        ttk.Button(frame, text="Créer", command=confirmer).pack(pady=20)
        ttk.Button(frame, text="Retour", command=self.creer_menu_principal).pack()

    def afficher_selection_personnage(self):
        """Affiche l'écran de sélection de personnage"""
        for widget in self.fenetre.winfo_children():
            widget.destroy()

        frame = ttk.Frame(self.fenetre, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Sélection du personnage", 
                 font=("Arial", 20)).pack(pady=10)

        for perso in self.personnages:
            if perso.get("classe") != "Monstre":
                btn = ttk.Button(frame, 
                               text=f"{perso['nom']} - {perso['classe']} (Niveau {perso['niveau']})",
                               command=lambda p=perso: self.selectionner_personnage(p))
                btn.pack(pady=5)

        ttk.Button(frame, text="Retour", command=self.creer_menu_principal).pack(pady=20)

    def selectionner_personnage(self, personnage):
        """Sélectionne un personnage et commence le jeu"""
        self.personnage_actuel = personnage
        self.afficher_ecran_jeu()

    def generer_monstre(self):
        """Génère un nouveau monstre"""
        self.monstre_actuel = {
            "nom": f"Gobelin {random.randint(1,100)}",
            "classe": "Monstre",
            "niveau": 1,
            "points_de_vie": 50,
            "inventaire": [{"nom": "potion de soin", "quantité": 1}]
        }

    def afficher_ecran_jeu(self):
        """Affiche l'écran principal du jeu"""
        for widget in self.fenetre.winfo_children():
            widget.destroy()

        if not self.monstre_actuel:
            self.generer_monstre()

        # Interface de jeu
        frame = ttk.Frame(self.fenetre, padding="20")
        frame.pack(expand=True)

        # Informations du joueur
        ttk.Label(frame, text=f"Joueur: {self.personnage_actuel['nom']}", 
                 font=("Arial", 16)).pack()
        ttk.Label(frame, text=f"PV: {self.personnage_actuel['points_de_vie']}").pack()
        ttk.Label(frame, text=f"Niveau: {self.personnage_actuel['niveau']}").pack()

        # Informations du monstre
        ttk.Label(frame, text=f"\nMonstre: {self.monstre_actuel['nom']}", 
                 font=("Arial", 16)).pack()
        ttk.Label(frame, text=f"PV: {self.monstre_actuel['points_de_vie']}").pack()

        # Boutons d'action
        ttk.Button(frame, text="Attaquer", command=self.attaquer).pack(pady=10)
        ttk.Button(frame, text="Utiliser potion", command=self.utiliser_potion).pack(pady=10)
        ttk.Button(frame, text="Quitter", command=self.creer_menu_principal).pack(pady=10)

    def attaquer(self):
        """Gère l'attaque du joueur vers le monstre et la contre-attaque"""
        # Attaque du joueur
        degats_joueur = random.randint(1, 50)
        self.monstre_actuel["points_de_vie"] -= degats_joueur
        messagebox.showinfo("Attaque", f"Vous infligez {degats_joueur} points de dégâts au monstre!")
        
        # Vérifie si le monstre est vaincu
        if self.monstre_actuel["points_de_vie"] <= 0:
            messagebox.showinfo("Victoire", "Monstre vaincu!")
            self.personnage_actuel["niveau"] += 1
            self.personnage_actuel["points_de_vie"] += 20
            self.ajouter_objet(self.personnage_actuel, "potion de soin", 1)
            self.sauvegarder_personnages()
            self.monstre_actuel = None
        else:
            # Contre-attaque du monstre
            degats_monstre = random.randint(1, 25)
            self.personnage_actuel["points_de_vie"] -= degats_monstre
            messagebox.showinfo("Contre-attaque", 
                              f"Le monstre vous inflige {degats_monstre} points de dégâts!")
            
            # Vérifie si le joueur est vaincu
            if self.personnage_actuel["points_de_vie"] <= 0:
                messagebox.showinfo("Défaite", "Vous avez été vaincu!")
                self.creer_menu_principal()
                return
        
        self.sauvegarder_personnages()
        self.afficher_ecran_jeu()

    def utiliser_potion(self):
        """Utilise une potion de soin"""
        for item in self.personnage_actuel["inventaire"]:
            if item["nom"] == "potion de soin" and item["quantité"] > 0:
                soin = random.randint(1, 50)
                self.personnage_actuel["points_de_vie"] += soin
                item["quantité"] -= 1
                self.sauvegarder_personnages()
                messagebox.showinfo("Soin", f"Vous récupérez {soin} points de vie!")
                self.afficher_ecran_jeu()
                return
        messagebox.showwarning("Attention", "Pas de potion disponible!")

    def ajouter_objet(self, personnage, nom_objet, quantite=1):
        """Ajoute un objet à l'inventaire"""
        for item in personnage["inventaire"]:
            if item["nom"] == nom_objet:
                item["quantité"] += quantite
                return
        personnage["inventaire"].append({"nom": nom_objet, "quantité": quantite})

    def lancer(self):
        """Lance le jeu"""
        self.fenetre.mainloop()

if __name__ == "__main__":
    jeu = JeuRPG()
    jeu.lancer()



