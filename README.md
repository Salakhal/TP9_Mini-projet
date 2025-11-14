# Mini-projet Python : Gestion d'une boutique

## Objectif

Ce mini-projet a pour objectif de mettre en pratique la **programmation orientée objet** en Python et l'accès à une base de données pour gérer des entités métiers. Il permet de comparer l'utilisation de **SQLite** (base embarquée) et **MySQL** (base distante).

---

## Structure du projet

```
projet_boutique/
│
├─ models.py     # Classes Produit et Client
├─ sqlite_dao.py   # Gestion de la base SQLite
├─ main.py    # Menu CLI pour tester les opérations CRUD

```
---

## Étapes du projet

### 1. Définition des classes

- **Produit** : id, nom, prix
- **Client** : id, nom, email
- Chaque classe contient un constructeur et une méthode `__str__()` pour un affichage lisible.

### 2. Connexion SQLite

- Base SQLite : `boutique.db`
- Module `sqlite_dao.py` avec les fonctions :
  - `ajouter_produit(produit)`
  - `lister_produits()`
  - `modifier_prix_produit(id, prix)`
  - `ajouter_client(client)`
  - `lister_clients()`
  - `rechercher_client_par_email(email)`


## 3. Fichier principal `main.py`

Le fichier `main.py` propose un **menu CLI simple** pour tester toutes les opérations CRUD.

Il est possible de basculer entre **SQLite** et **MySQL** en important le module correspondant (`sqlite_dao` ou `mysql_dao`).

### Fonctionnalités implémentées

- Ajouter un produit ou un client
- Lister tous les produits ou clients
- Rechercher un client par email
- Modifier le prix d’un produit
- Gestion des erreurs basiques (ex: client non trouvé)

  ##  Exemple d’exécution (image)
 
Voici un exemple de l'exécution du programme (screenshot) :

<img width="657" height="634" alt="image" src="https://github.com/user-attachments/assets/04cc16f8-a715-4b79-9a19-4d727f9abb53" />
<img width="748" height="626" alt="image" src="https://github.com/user-attachments/assets/dcee5988-6ad4-4e87-b176-34bed682760c" />
<img width="763" height="629" alt="image" src="https://github.com/user-attachments/assets/c8dc8058-3d5d-49a2-9ef7-e40dd85398e9" />
<img width="514" height="256" alt="image" src="https://github.com/user-attachments/assets/dc5e9226-2cc0-4de0-b4ea-55c535e1ead0" />





