# TP : Jeu de rôle

### Étape 1 : Créer un dictionnaire de personnage

Créez un dictionnaire représentant un personnage avec les clés suivantes :

- **nom**
- **classe**
- **niveau**
- **points_de_vie**
- **inventaire**
  - L'inventaire sera une liste de dictionnaires avec pour clés :
    - **nom**
    - **quantité**

**Remarque : notre personnage commencera avec 3 potions de soin dans l'inventaire.**

## Les fonctions :

### 1. Ajouter des objets à l'inventaire :

- Créez une fonction qui permet d'ajouter un ou plusieurs objets dans l'inventaire.

### 2. Modifier les statistiques :

- Le personnage gagne un niveau et 20 points de vie supplémentaires.

### 3. Utiliser une potion de soin :

Le personnage utilise une "potion de soin".

- Supprimez cet objet de l'inventaire.
- Ajoutez des points de vie aléatoires entre **1** et **50**.

### 4. Créer une fonction pour afficher les détails du personnage :

Définissez une fonction `afficher_personnage(personnage)` qui affiche toutes les informations du personnage.

## Bonus :

Implémentez une fonction `attaquer` qui prend deux personnages et réduit les points de vie du second personnage. Les dégâts infligés sont calculés comme suit :

- **dégâts = 10 × niveau** du personnage attaquant.
- Si le personnage attaqué meurt, alors l'attaquant récupérera l'intégralité de l'inventaire de son adversaire.
