from models import Produit, Client

from sqlite_dao import creer_tables as creer_tables_sqlite, ajouter_produit, lister_produits, \
    ajouter_client, lister_clients, rechercher_client_par_email, modifier_prix_produit
# Pour MySQL, remplacer sqlite_dao par mysql_dao si besoin

def menu():
    print("1. Ajouter produit")
    print("2. Lister produits")
    print("3. Ajouter client")
    print("4. Lister clients")
    print("5. Rechercher client par email")
    print("6. Modifier prix produit")
    print("0. Quitter")
    return input("Choisir une option: ")

def main():
    # Créer les tables SQLite
    creer_tables_sqlite()

    while True:
        choix = menu()
        if choix == "1":
            id = int(input("ID produit: "))
            nom = input("Nom produit: ")
            prix = float(input("Prix produit: "))
            ajouter_produit(Produit(id, nom, prix))
        elif choix == "2":
            for p in lister_produits():
                print(p)
        elif choix == "3":
            id = int(input("ID client: "))
            nom = input("Nom client: ")
            email = input("Email client: ")
            ajouter_client(Client(id, nom, email))
        elif choix == "4":
            for c in lister_clients():
                print(c)
        elif choix == "5":
            email = input("Email du client: ")
            client = rechercher_client_par_email(email)
            print(client if client else "Client non trouvé")
        elif choix == "6":
            id = int(input("ID produit à modifier: "))
            nouveau_prix = float(input("Nouveau prix: "))
            modifier_prix_produit(id, nouveau_prix)
        elif choix == "0":
            break
        else:
            print("Option invalide")

if __name__ == "__main__":
    main()
