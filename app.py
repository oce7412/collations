from flask import Flask, render_template, request

app = Flask(__name__)


athletes = {
    "Amandine": {"saumon fumé", "dés de jambon", "fruits de mer"},
    "Maurène": {"fruits de mer"},
    "Titia": {""},
    "Laura": {""},
    "Maaike": {"émincés de poulet", "jambon blanc", "jambon cru", "fruits de mer"},
    "Lotte": {"thon", "carottes râpées", "salade", "sauce au yaourt"},
    "Valentina": {""},
    "Michaela": {"fruits de mer", "saumon", "saumon fumé"},
    "Danielle": {"pâtes"},
    "Emilia": {"pasta"},
    "Marjolein": {""},
    "Clémence": {"mayonnaise"},
    "Océane": {"salade", "noix", "jambon cru"},
}

recipes = {
    "Salade riz-thon": {"riz", "thon", "maïs", "avocat" "sauce au yaourt"},
    "Salade de pâtes au pesto": {"pâtes", "pesto", "jambon blanc", "tomates", "mozzarella"},
    "Pâtes au saumon": {"pâtes", "saumon"},
    "Salade riz-saumon": {"riz", "saumon fumé", "sauce au yaourt", "concombre", "carottes râpées"},
    "Salade de poulet": {"riz", "émincés de poulet", "tomates", "mozzarella"},
    "Salade de boulgour": {"boulgour", "émincés de poulet", "feta", "raisins secs", "concombre"},
    "Salade de pomme de terre": {"pommes de terre", "dés de jambon", "oeufs durs", "tomates"},
    "Salade méditerranéenne": {"riz", "lentilles vertes", "concombre", "feta", "tomates cerises"},
    "Salade italienne": {"gnocchis", "jambon cru", "mozzarella", "tomates cerises"},
    "Salade niçoise": {"riz", "thon", "oeuf", "tomates cerises", "haricots verts"},
    "Salade poulet-crudités": {"pâtes", "émincés de poulet", "tomates", "salade", "sauce au yaourt"},
    "Salade jambon fromage" : {"pâtes", "jambon blanc", "dés de fromage", "tomates", "salade"},
    "Salade chèvre-miel" : {"pâtes", "fromage de chèvre", "jambon blanc", "miel"},
    "Salade façon taboulé" : {"semoule", "émincés de poulet", "tomates", "concombre"},
    "Salade jambon cru-noix" : {"boulgour", "noix", "jambon cru", "figues séchées"}
}

def recettes_possibles(presents):
    blacklist = athletes[presents[0]]
    print(blacklist)
    for i in range (1, len(presents)):
        blacklist = blacklist.union(athletes[presents[i]])
    valides = []
    for recette, ingredients in recipes.items():
        if not ingredients & blacklist:
            valides.append(recette)
    return valides

@app.route("/", methods=["GET", "HEAD"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)