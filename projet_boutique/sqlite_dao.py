import sqlite3
from models import Produit, Client

DB_FILE = 'boutique.db'

def connexion():
    return sqlite3.connect(DB_FILE)

def creer_tables():
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produit (
            id INTEGER PRIMARY KEY,
            nom TEXT NOT NULL,
            prix REAL NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Client (
            id INTEGER PRIMARY KEY,
            nom TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def ajouter_produit(produit):
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Produit (id, nom, prix) VALUES (?, ?, ?)",
                   (produit.id, produit.nom, produit.prix))
    conn.commit()
    conn.close()

def lister_produits():
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, prix FROM Produit")
    rows = cursor.fetchall()
    conn.close()
    return [Produit(*row) for row in rows]

def ajouter_client(client):
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Client (id, nom, email) VALUES (?, ?, ?)",
                   (client.id, client.nom, client.email))
    conn.commit()
    conn.close()

def lister_clients():
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, email FROM Client")
    rows = cursor.fetchall()
    conn.close()
    return [Client(*row) for row in rows]

def rechercher_client_par_email(email):
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, email FROM Client WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    return Client(*row) if row else None

def modifier_prix_produit(id_produit, nouveau_prix):
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE Produit SET prix = ? WHERE id = ?", (nouveau_prix, id_produit))
    conn.commit()
    conn.close()
