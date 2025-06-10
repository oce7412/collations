from flask import Flask

app = Flask(__name__)

athletes = {
    "Amandine": {"saumon fumé", "dés de jambon", "fruits de mer"},
    "Maurène": {"fruits de mer"},
    "Titia": {""},
    "Laura": {""},
    "Maaike": {"émincés de poulet", "jambon blanc", "jambon cru", "fruits de mer"},
    "Lotte": {"thon", "carottes râpées", "salade", "sauce au yaourt"},
    "Valentina": {"oeufs brouillés", "mayonnaise"},
    "Michaela": {"fruits de mer", "saumon", "saumon fumé"},
    "Danielle": {"pâtes"},
    "Emilia": {"pâtes"},
    "Marjolein": {""},
    "Clémence": {"mayonnaise"},
    "Océane": {"salade", "noix", "jambon cru", "guacamole"},
}

recipes = {
    "Salade riz-thon": {"riz", "thon", "maïs", "avocat" "sauce au yaourt"},
    "Salade de pâtes au pesto": {"pâtes", "pesto", "jambon blanc", "tomates", "mozzarella"},
    "Pâtes au saumon": {"pâtes", "saumon"},
    "Salade riz-saumon": {"riz", "saumon fumé", "sauce au yaourt", "concombre", "carottes râpées"},
    "Salade de poulet": {"riz", "émincés de poulet", "tomates", "mozzarella"},
    "Salade de boulgour": {"boulgour", "émincés de poulet", "feta", "raisins secs", "concombre"},
    "Salade façon piémontaise": {"pommes de terre", "dés de jambon", "oeufs durs", "tomates", "sauce au yaourt"},
    "Salade pomme de terre & thon": {"pommes de terre", "thon", "oeufs durs", "tomates", "sauce au yaourt"},
    "Salade méditerranéenne": {"riz", "lentilles vertes", "concombre", "feta", "tomates cerises"},
    "Salade italienne": {"gnocchis", "jambon cru", "mozzarella", "tomates cerises"},
    "Salade niçoise": {"riz", "thon", "oeuf", "tomates cerises", "haricots verts"},
    "Salade poulet-crudités": {"pâtes", "émincés de poulet", "tomates", "salade", "sauce au yaourt"},
    "Salade jambon fromage" : {"pâtes", "jambon blanc", "dés de fromage", "tomates", "salade"},
    "Salade chèvre-miel" : {"pâtes", "fromage de chèvre", "jambon blanc", "miel"},
    "Salade façon taboulé" : {"semoule", "émincés de poulet", "tomates", "concombre"},
    "Salade jambon cru-noix" : {"boulgour", "noix", "jambon cru", "figues séchées"},
    "Poulet curry" : {"riz", "émincés de poulet", "fromage blanc", "curry"},
    "Burritos façon chili" : {"wrap", "riz", "émincés de poulet", "fromage blanc", "curry", "tomates", "haricots rouges"},
    "Riz cantonais" : {"riz", "oeufs brouillés", "dés de jambon", "petits pois"},
    "Salade de patates douces au poulet" : {"patates douces", "radis", "émincés de poulet", "sauce au yaourt", "avocat"},
    "Salade de patates douces au thon" : {"patates douces", "thon", "sauce au yaourt", "petits pois", "avocat"},
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

@app.route("/", methods=["GET", "POST"])
def home():
    recettes_compatibles = None
    if request.method == "POST":
        noms = request.form.get("athletes", "")
        presents = [n.strip() for n in noms.split(",") if n.strip()]
        recettes_compatibles = recettes_possibles(presents)
    return render_template("index.html", recettes=recettes_compatibles)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
