from flask import Flask, render_template, request

app = Flask(__name__)

athletes = {
    "Amandine": {"saumon fumé", "dés de jambon", "fruits de mer"},
    "Maurène": {"fruits de mer"},
    "Titia": {""},
    "Laura": {""},
    "Maaike": {"émincés de poulet", "jambon blanc", "jambon cru", "dés de jambon", "fruits de mer"},
    "Lotte": {"thon", "carottes râpées", "salade", "sauce au yaourt"},
    "Valentina": {"oeufs brouillés", "mayonnaise"},
    "Michaela": {"fruits de mer", "saumon", "saumon fumé"},
    "Danielle": {"pâtes", "gnocchis", "semoule", "boulgour"},
    "Emilia": {"pâtes", "gnocchis", "semoule", "boulgour"},
    "Marjolein": {""},
    "Clémence": {"mayonnaise"},
    "Océane": {"salade", "noix", "jambon cru", "guacamole", "noix de cajou", "poivrons"},
}

recettes = {
    "Salade riz-thon": {"riz", "thon", "maïs", "avocat" "sauce au yaourt"},
    "Salade de pâtes au pesto": {"pâtes", "pesto", "jambon blanc", "tomates", "mozzarella"},
    "Pâtes au saumon": {"pâtes", "saumon", "fromage blanc"},
    "Salade riz-saumon": {"riz", "saumon fumé", "sauce au yaourt", "concombre", "carottes râpées"},
    "Salade riz-poulet": {"riz", "émincés de poulet", "tomates", "mozzarella"},
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
    "Salade façon couscous" : {"semoule", "émincés de poulet", "carottes cuites", "courgettes cuites", "pois chiches"},
    "Salade jambon cru-noix" : {"quinoa", "noix", "jambon cru", "figues séchées"},
    "Riz au poulet curry" : {"riz", "émincés de poulet", "fromage blanc", "curry"},
    "Burritos façon chili" : {"wrap", "riz", "émincés de poulet", "fromage blanc", "curry", "tomates", "haricots rouges"},
    "Riz cantonais" : {"riz", "oeufs brouillés", "dés de jambon", "petits pois"},
    "Salade de patates douces au poulet" : {"patates douces", "radis", "émincés de poulet", "sauce au yaourt", "avocat"},
    "Salade de patates douces au thon" : {"patates douces", "thon", "sauce au yaourt", "petits pois", "avocat"},
    "Wok au poulet" : {"riz", "émincés de poulet", "poivrons", "sauce soja", "noix de cajou"},
    "Sushi bowl" : {"riz", "saumon fumé", "avocat", "sauce soja", "concombre", "carottes râpées", "mangue"},
    "Salade oeufs-crudités" : {"pâtes", "oeufs durs", "sauce au yaourt", "radis", "concombre", "pommes"},
}

@app.route("/", methods=["GET", "POST"])
def home():
    recettes_trouvees = None
    if request.method == "POST":
        noms = request.form["athletes"]
        presents = [nom.strip() for nom in noms.split(",") if nom.strip()]
        blacklist = set()
        for nom in presents:
            blacklist |= athletes.get(nom, set())
        recettes_trouvees = {
            nom: ingr for nom, ingr in recettes.items()
            if ingr.isdisjoint(blacklist)
        }
    return render_template(
        "index.html",
        recettes=recettes_trouvees,
        tous_athletes=athletes.keys()
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




