from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)

# ══════════════════════════════════════════════════════════
#  FONCTIONS DE LECTURE DES DONNÉES
# ══════════════════════════════════════════════════════════

def read_json():
    """Lit les produits depuis products.json"""
    with open("products.json", "r") as f:
        return json.load(f)  # Retourne une liste de dicts


def read_csv():
    """Lit les produits depuis products.csv"""
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)  # Chaque ligne devient un dict
        for row in reader:
            products.append({
                "id":       int(row["id"]),
                "name":     row["name"],
                "category": row["category"],
                "price":    float(row["price"])
            })
    return products


def read_sql():
    """Lit les produits depuis la base de données SQLite products.db"""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()  # Retourne une liste de tuples

    conn.close()

    # Convertit chaque tuple en dictionnaire pour le template Jinja
    products = []
    for row in rows:
        products.append({
            "id":       row[0],
            "name":     row[1],
            "category": row[2],
            "price":    row[3]
        })
    return products


# ══════════════════════════════════════════════════════════
#  ROUTE PRINCIPALE
# ══════════════════════════════════════════════════════════

@app.route("/products")
def products():
    # 1. Récupère les paramètres de l'URL
    source     = request.args.get("source")  # 'json', 'csv' ou 'sql'
    product_id = request.args.get("id")      # optionnel

    # 2. Vérifie que source est valide
    if source not in ("json", "csv", "sql"):
        return render_template(
            "product_display.html",
            error="Wrong source. Please use 'json', 'csv' or 'sql'.",
            products=[],
            source=source
        )

    # 3. Lit les données selon la source choisie
    try:
        if source == "json":
            data = read_json()
        elif source == "csv":
            data = read_csv()
        elif source == "sql":
            data = read_sql()

    except FileNotFoundError:
        return render_template(
            "product_display.html",
            error=f"File not found for source '{source}'.",
            products=[],
            source=source
        )
    except sqlite3.Error as e:
        return render_template(
            "product_display.html",
            error=f"Database error: {str(e)}",
            products=[],
            source=source
        )

    # 4. Filtre par id si fourni
    if product_id is not None:
        data = [p for p in data if str(p["id"]) == product_id]

        if not data:
            return render_template(
                "product_display.html",
                error=f"Product not found (id={product_id}).",
                products=[],
                source=source
            )

    # 5. Affiche les produits
    return render_template(
        "product_display.html",
        products=data,
        error=None,
        source=source
    )


# ══════════════════════════════════════════════════════════
#  LANCEMENT
# ══════════════════════════════════════════════════════════

if __name__ == "__main__":
    app.run(debug=True)