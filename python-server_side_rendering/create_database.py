import sqlite3
 
def create_database():
    # Connexion au fichier products.db (le crée s'il n'existe pas)
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
 
    # Création de la table Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id       INTEGER PRIMARY KEY,
            name     TEXT    NOT NULL,
            category TEXT    NOT NULL,
            price    REAL    NOT NULL
        )
    ''')
 
    # Insertion des produits (on vérifie d'abord que la table est vide)
    cursor.execute("SELECT COUNT(*) FROM Products")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop',      'Electronics', 799.99),
            (2, 'Coffee Mug',  'Home Goods',   15.99),
            (3, 'Headphones',  'Electronics', 149.99),
            (4, 'Notebook',    'Stationery',    4.99),
            (5, 'Desk Lamp',   'Home Goods',   34.99)
        ''')
 
    conn.commit()
    conn.close()
    print("✅ Base de données créée avec succès !")
 
if __name__ == '__main__':
    create_database()