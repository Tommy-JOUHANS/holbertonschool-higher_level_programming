#!/usr/bin/python
from flask import Flask, request, render_template
import json
import csv
import os

app = Flask(__name__)

# ─────────────────────────────────────────────
# Fonctions de lecture des fichiers
# ─────────────────────────────────────────────

def read_json():
    """Lit et retourne les produits depuis products.json"""
    with open("products.json", "r") as f:
        return json.load(f)  # Retourne une liste de dictionnaires


def read_csv():
    """Lit et retourne les produits depuis products.csv"""
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)  # Lit chaque ligne comme un dictionnaire
        for row in reader:
            # Convertit les types : id en int, price en float
            products.append({
                "id":       int(row["id"]),
                "name":     row["name"],
                "category": row["category"],
                "price":    float(row["price"])
            })
    return products


# ─────────────────────────────────────────────
# Route principale
# ─────────────────────────────────────────────

@app.route("/products")
def products():
    # 1. Récupère les paramètres de l'URL
    source     = request.args.get("source")   # 'json' ou 'csv'
    product_id = request.args.get("id")       # optionnel

    # 2. Vérifie que source est valide
    if source not in ("json", "csv"):
        return render_template(
            "product_display.html",
            error="Wrong source. Please use 'json' or 'csv'.",
            products=[]
        )

    # 3. Lit les données depuis le bon fichier
    if source == "json":
        data = read_json()
    else:
        data = read_csv()

    # 4. Filtre par id si fourni
    if product_id is not None:
        data = [p for p in data if str(p["id"]) == product_id]

        if not data:
            return render_template(
                "product_display.html",
                error=f"Product not found (id={product_id}).",
                products=[]
            )

    # 5. Affiche les produits
    return render_template("product_display.html", products=data, error=None)


# ─────────────────────────────────────────────
# Lancement de l'application
# ─────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)