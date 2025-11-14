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


