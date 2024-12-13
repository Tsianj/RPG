### **Instructions**

#### **1. Initialisation de l’inventaire**

- Créez une liste appelée `inventaire`. Chaque élément de la liste est un dictionnaire représentant un produit avec les clés suivantes :
  - `nom` : Le nom du produit (type `str`).
  - `quantite` : La quantité disponible (type `int`).
  - `prix` : Le prix unitaire (type `float`).

Exemple :

```python
inventaire = [
    {"nom": "Boules de Noël", "quantite": 50, "prix": 1.5},
    {"nom": "Guirlandes", "quantite": 30, "prix": 3.0},
    {"nom": "Sapin de Noël", "quantite": 10, "prix": 25.0}
]
```

#### **2. Afficher l’inventaire**

- Écrivez une fonction `afficher_inventaire` qui parcourt la liste et affiche chaque produit avec son nom, sa quantité et son prix.

#### **3. Ajouter un produit**

- Écrivez une fonction `ajouter_produit` qui permet à l’utilisateur d’ajouter un nouveau produit à l’inventaire.
- L’utilisateur doit fournir :
  - Le nom du produit.
  - La quantité.
  - Le prix.
- Si le produit existe déjà, mettez à jour sa quantitée.

#### **4. Supprimer un produit**

- Écrivez une fonction `supprimer_produit` qui permet à l’utilisateur de supprimer un produit de l’inventaire.
- Si le produit n’existe pas, affichez un message d’erreur.

#### **5. Modifier la quantité d’un produit**

- Écrivez une fonction `modifier_quantite` qui permet de changer la quantité d’un produit existant.
- L’utilisateur fournit :
  - Le nom du produit.
  - La nouvelle quantité.
- Si le produit n’existe pas, affichez un message d’erreur.

#### **6. Rechercher un produit**

- Écrivez une fonction `rechercher_produit` qui permet de vérifier si un produit est présent dans l’inventaire.
- Affichez ses détails s’il est trouvé, sinon affichez un message indiquant qu’il n’existe pas.

#### **7. Calculer la valeur totale de l’inventaire**

- Écrivez une fonction `valeur_totale_inventaire` qui calcule la valeur totale de l’inventaire.

### **Menu principal**

Créez un menu qui permet à l’utilisateur de choisir une action parmi les suivantes :

1. Afficher l’inventaire.
2. Ajouter un produit.
3. Supprimer un produit.
4. Modifier la quantité d’un produit.
5. Rechercher un produit.
6. Calculer la valeur totale de l’inventaire.
7. Quitter le programme.

Chaque choix doit appeler la fonction correspondante. Le menu doit se répéter tant que l’utilisateur ne choisit pas de quitter.
