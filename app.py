from microsoft_sync import sync_prospect_to_microsoft
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from config import Config
from extensions import init_extensions, db
from models import (
    Commercial,
    Potentiel,
    Modele,
    Version,
    Couleur,
    Interieur,
    Motorisation,
    Financement,
    Canal,
    DetailCanal,
    Prospect
)

app = Flask(__name__)
app.config.from_object(Config)

# Initialisation des extensions
init_extensions(app)


# =====================================================
# INSERTION DES DONNEES PAR DEFAUT
# =====================================================

def insert_defaults():

    # -------------------------
    # COMMERCIAUX
    # -------------------------

    commerciaux = [
        "Mouna",
        "Driss",
        "Omar",
        "Amal",
        "Siham",
        "Khalil"
    ]

    for nom in commerciaux:
        if not Commercial.query.filter_by(nom=nom).first():
            db.session.add(Commercial(nom=nom))

    # -------------------------
    # POTENTIEL
    # -------------------------

    potentiels = [
        "Opportunité",
        "Affaire chaude",
        "Commande"
    ]

    for nom in potentiels:
        if not Potentiel.query.filter_by(nom=nom).first():
            db.session.add(Potentiel(nom=nom))

    # -------------------------
    # MODELES
    # -------------------------

    modeles = [
        "Seal 4",
        "Seal 5",
        "Atto 2",
        "Atto 3",
        "Seagull",
        "Han",
        "Sealion 7",
        "Sealion 5"
    ]

    for nom in modeles:
        if not Modele.query.filter_by(nom=nom).first():
            db.session.add(Modele(nom=nom))

    # -------------------------
    # VERSIONS
    # -------------------------

    versions = [
        "Comfort",
        "Design",
        "Design Sport",
        "Design AWD"
    ]

    for nom in versions:
        if not Version.query.filter_by(nom=nom).first():
            db.session.add(Version(nom=nom))

    # -------------------------
    # COULEURS
    # -------------------------

    couleurs = [
        "White",
        "Time Grey",
        "Smokey Grey",
        "Black",
        "Atlantis Grey",
        "Cyan Blue",
        "Green",
        "ND"
    ]

    for nom in couleurs:
        if not Couleur.query.filter_by(nom=nom).first():
            db.session.add(Couleur(nom=nom))

    # -------------------------
    # INTERIEURS
    # -------------------------

    interieurs = [
        "Brown Black",
        "Black",
        "Beige",
        "ND"
    ]

    for nom in interieurs:
        if not Interieur.query.filter_by(nom=nom).first():
            db.session.add(Interieur(nom=nom))

    # -------------------------
    # MOTORISATION
    # -------------------------

    motorisations = [
        "PHEV",
        "EV"
    ]

    for nom in motorisations:
        if not Motorisation.query.filter_by(nom=nom).first():
            db.session.add(Motorisation(nom=nom))

    # -------------------------
    # FINANCEMENT
    # -------------------------

    financements = [
        "Comptant",
        "Wafasalaf",
        "Sofac",
        "Vivalis",
        "Epder",
        "Salafin",
        "Banque Islamique",
        "Organisme de leasing",
        "ND"
    ]

    for nom in financements:
        if not Financement.query.filter_by(nom=nom).first():
            db.session.add(Financement(nom=nom))

    # -------------------------
    # CANAL
    # -------------------------

    canaux = [
        "Showroom",
        "Leads",
        "Planning",
        "Prospection terrain",
        "Recommandation"
    ]

    for nom in canaux:
        if not Canal.query.filter_by(nom=nom).first():
            db.session.add(Canal(nom=nom))

    # -------------------------
    # DETAIL CANAL
    # -------------------------

    details = [
        "Affichage",
        "Client BYD",
        "Réseaux sociaux",
        "Autre"
    ]

    for nom in details:
        if not DetailCanal.query.filter_by(nom=nom).first():
            db.session.add(DetailCanal(nom=nom))

    db.session.commit()


# =====================================================
# CREATION DE LA BASE
# =====================================================

with app.app_context():
    db.create_all()


# =====================================================
# ROUTES
# =====================================================

@app.route("/", methods=["GET", "POST"])
def index():

    commerciaux = Commercial.query.order_by(Commercial.nom).all()

    potentiels = Potentiel.query.order_by(Potentiel.nom).all()

    modeles = Modele.query.order_by(Modele.nom).all()

    versions = Version.query.order_by(Version.nom).all()

    couleurs = Couleur.query.order_by(Couleur.nom).all()

    interieurs = Interieur.query.order_by(Interieur.nom).all()

    motorisations = Motorisation.query.order_by(Motorisation.nom).all()

    financements = Financement.query.order_by(Financement.nom).all()

    canaux = Canal.query.order_by(Canal.nom).all()

    details = DetailCanal.query.order_by(DetailCanal.nom).all()


    if request.method == "POST":

        date_obj = datetime.strptime(
            request.form.get("date_contact"),
            "%Y-%m-%d"
        ).date()

        prospect = Prospect(
            annee=date_obj.year,
            mois=date_obj.strftime("%m"),
            date_contact=date_obj,
            commercial_id=int(request.form.get("commercial")),
            nom_client=request.form.get("nom_client").upper(),
            prenom_client=request.form.get("prenom_client").upper(),
            telephone=request.form.get("telephone"),
            email=request.form.get("email").lower() if request.form.get("email") else None,
            ville=request.form.get("ville").upper() if request.form.get("ville") else None,
            potentiel_id=int(request.form.get("potentiel")),
            modele_id=int(request.form.get("modele")),
            version_id=int(request.form.get("version")),
            couleur_id=int(request.form.get("couleur")) if request.form.get("couleur") else None,
            interieur_id=int(request.form.get("interieur")) if request.form.get("interieur") else None,
            motorisation_id=int(request.form.get("motorisation")) if request.form.get("motorisation") else None,
            financement_id=int(request.form.get("financement")) if request.form.get("financement") else None,
            canal_id=int(request.form.get("canal")) if request.form.get("canal") else None,
            detail_canal_id=int(request.form.get("detail_canal")) if request.form.get("detail_canal") else None,
            commentaire=request.form.get("commentaire")
        )

        db.session.add(prospect)
        db.session.commit()

        flash("Prospect enregistré avec succès.", "success")

        return redirect(url_for("dashboard"))

    return render_template(

        "index.html",

        commerciaux=commerciaux,

        potentiels=potentiels,

        modeles=modeles,

        versions=versions,

        couleurs=couleurs,

        interieurs=interieurs,

        motorisations=motorisations,

        financements=financements,

        canaux=canaux,

        details=details

    )


@app.route("/dashboard")
def dashboard():

    prospects = Prospect.query.order_by(Prospect.id.desc()).all()

    stats_modeles = {}
    stats_commerciaux = {}
    stats_potentiels = {}
    stats_mois = {}

    for prospect in prospects:
        modele = prospect.modele.nom if prospect.modele else "Non défini"
        commercial = prospect.commercial.nom if prospect.commercial else "Non défini"
        potentiel = prospect.potentiel.nom if prospect.potentiel else "Non défini"
        mois = prospect.mois if prospect.mois else "Non défini"

        stats_modeles[modele] = stats_modeles.get(modele, 0) + 1
        stats_commerciaux[commercial] = stats_commerciaux.get(commercial, 0) + 1
        stats_potentiels[potentiel] = stats_potentiels.get(potentiel, 0) + 1
        stats_mois[mois] = stats_mois.get(mois, 0) + 1

    return render_template(
    "dashboard.html",
    prospects=prospects,
    stats_modeles=stats_modeles,
    stats_commerciaux=stats_commerciaux,
    stats_potentiels=stats_potentiels,
    stats_mois=stats_mois,
    modeles=Modele.query.order_by(Modele.nom).all(),
    commerciaux=Commercial.query.order_by(Commercial.nom).all()
)

# =====================================================
# SUPPRIMER UN PROSPECT
# =====================================================
@app.route("/delete/<int:id>", methods=["POST"])
def delete_prospect(id):

    prospect = Prospect.query.get_or_404(id)

    db.session.delete(prospect)
    db.session.commit()

    flash("Prospect supprimé avec succès.", "success")

    return redirect(url_for("dashboard"))


# =====================================================
# MODIFIER UN PROSPECT
# =====================================================

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_prospect(id):

    prospect = Prospect.query.get_or_404(id)

    commerciaux = Commercial.query.order_by(Commercial.nom).all()
    potentiels = Potentiel.query.order_by(Potentiel.nom).all()
    modeles = Modele.query.order_by(Modele.nom).all()
    versions = Version.query.order_by(Version.nom).all()
    couleurs = Couleur.query.order_by(Couleur.nom).all()
    interieurs = Interieur.query.order_by(Interieur.nom).all()
    motorisations = Motorisation.query.order_by(Motorisation.nom).all()
    financements = Financement.query.order_by(Financement.nom).all()
    canaux = Canal.query.order_by(Canal.nom).all()
    details = DetailCanal.query.order_by(DetailCanal.nom).all()

    if request.method == "POST":

        date_obj = datetime.strptime(
            request.form.get("date_contact"),
            "%Y-%m-%d"
        ).date()

        prospect.date_contact = date_obj
        prospect.annee = date_obj.year
        prospect.mois = date_obj.strftime("%m")

        prospect.commercial_id = int(request.form.get("commercial"))
        prospect.nom_client = request.form.get("nom_client").upper()
        prospect.prenom_client = request.form.get("prenom_client").upper()
        prospect.telephone = request.form.get("telephone")
        prospect.email = request.form.get("email").lower() if request.form.get("email") else None
        prospect.ville = request.form.get("ville").upper() if request.form.get("ville") else None
        prospect.potentiel_id = int(request.form.get("potentiel"))
        prospect.modele_id = int(request.form.get("modele"))
        prospect.version_id = int(request.form.get("version"))
        prospect.couleur_id = int(request.form.get("couleur")) if request.form.get("couleur") else None
        prospect.interieur_id = int(request.form.get("interieur")) if request.form.get("interieur") else None
        prospect.motorisation_id = int(request.form.get("motorisation")) if request.form.get("motorisation") else None
        prospect.financement_id = int(request.form.get("financement")) if request.form.get("financement") else None
        prospect.canal_id = int(request.form.get("canal")) if request.form.get("canal") else None
        prospect.detail_canal_id = int(request.form.get("detail_canal")) if request.form.get("detail_canal") else None
        prospect.commentaire = request.form.get("commentaire").upper() if request.form.get("commentaire") else None

        db.session.commit()

        flash("Prospect modifié avec succès.", "success")

        return redirect(url_for("dashboard"))

    return render_template(
        "edit_prospect.html",
        prospect=prospect,
        commerciaux=commerciaux,
        potentiels=potentiels,
        modeles=modeles,
        versions=versions,
        couleurs=couleurs,
        interieurs=interieurs,
        motorisations=motorisations,
        financements=financements,
        canaux=canaux,
        details=details
    )
@app.route("/settings")
def settings():
    commerciaux = Commercial.query.order_by(Commercial.nom).all()

    modeles = Modele.query.order_by(Modele.nom).all()

    versions = Version.query.order_by(Version.nom).all()

    couleurs = Couleur.query.order_by(Couleur.nom).all()

    interieurs = Interieur.query.order_by(Interieur.nom).all()

    motorisations = Motorisation.query.order_by(Motorisation.nom).all()

    financements = Financement.query.order_by(Financement.nom).all()

    canaux = Canal.query.order_by(Canal.nom).all()

    details = DetailCanal.query.order_by(DetailCanal.nom).all()

    potentiels = Potentiel.query.order_by(Potentiel.nom).all()

    return render_template(
        "settings.html",
        commerciaux=commerciaux,
        modeles=modeles,
        versions=versions,
        couleurs=couleurs,
        interieurs=interieurs,
        motorisations=motorisations,
        financements=financements,
        canaux=canaux,
        details=details,
        potentiels=potentiels
    )
@app.route("/commercial/add", methods=["POST"])
def add_commercial():

    nom = request.form.get("nom")

    if nom:

        commercial = Commercial(nom=nom)

        db.session.add(commercial)

        db.session.commit()

        flash("Commercial ajouté avec succès.", "success")

    return redirect(url_for("settings"))
@app.route("/commercial/edit/<int:id>", methods=["GET", "POST"])
def edit_commercial(id):

    commercial = Commercial.query.get_or_404(id)

    if request.method == "POST":

        commercial.nom = request.form.get("nom")

        db.session.commit()

        flash("Commercial modifié avec succès.", "success")

        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier le commercial",
        action=url_for("edit_commercial", id=id),
        valeur=commercial.nom
    ) 
@app.route("/commercial/delete/<int:id>", methods=["POST"])
def delete_commercial(id):

    commercial = Commercial.query.get_or_404(id)

    db.session.delete(commercial)

    db.session.commit()

    flash("Commercial supprimé avec succès.", "success")

    return redirect(url_for("settings"))

# =====================================================
# LANCEMENT
# =====================================================
@app.route("/potentiel/add", methods=["POST"])
def add_potentiel():
    nom = request.form.get("nom")
    if nom:
        db.session.add(Potentiel(nom=nom))
        db.session.commit()
        flash("Potentiel ajouté avec succès.", "success")
    return redirect(url_for("settings"))


@app.route("/potentiel/edit/<int:id>", methods=["GET", "POST"])
def edit_potentiel(id):
    potentiel = Potentiel.query.get_or_404(id)

    if request.method == "POST":
        potentiel.nom = request.form.get("nom")
        db.session.commit()
        flash("Potentiel modifié avec succès.", "success")
        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier le potentiel",
        action=url_for("edit_potentiel", id=id),
        valeur=potentiel.nom
    )


@app.route("/potentiel/delete/<int:id>", methods=["POST"])
def delete_potentiel(id):
    potentiel = Potentiel.query.get_or_404(id)
    db.session.delete(potentiel)
    db.session.commit()
    flash("Potentiel supprimé avec succès.", "success")
    return redirect(url_for("settings")) 
@app.route("/modele/add", methods=["POST"])
def add_modele():
    nom = request.form.get("nom")
    if nom:
        db.session.add(Modele(nom=nom))
        db.session.commit()
        flash("Modèle ajouté avec succès.", "success")
    return redirect(url_for("settings"))


@app.route("/modele/edit/<int:id>", methods=["GET", "POST"])
def edit_modele(id):
    modele = Modele.query.get_or_404(id)

    if request.method == "POST":
        modele.nom = request.form.get("nom")
        db.session.commit()
        flash("Modèle modifié avec succès.", "success")
        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier le modèle",
        action=url_for("edit_modele", id=id),
        valeur=modele.nom
    )


@app.route("/modele/delete/<int:id>", methods=["POST"])
def delete_modele(id):
    modele = Modele.query.get_or_404(id)
    db.session.delete(modele)
    db.session.commit()
    flash("Modèle supprimé avec succès.", "success")
    return redirect(url_for("settings"))
@app.route("/version/add", methods=["POST"])
def add_version():
    nom = request.form.get("nom")
    if nom:
        db.session.add(Version(nom=nom))
        db.session.commit()
        flash("Version ajoutée avec succès.", "success")
    return redirect(url_for("settings"))


@app.route("/version/edit/<int:id>", methods=["GET", "POST"])
def edit_version(id):
    version = Version.query.get_or_404(id)

    if request.method == "POST":
        version.nom = request.form.get("nom")
        db.session.commit()
        flash("Version modifiée avec succès.", "success")
        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier la version",
        action=url_for("edit_version", id=id),
        valeur=version.nom
    )


@app.route("/version/delete/<int:id>", methods=["POST"])
def delete_version(id):
    version = Version.query.get_or_404(id)
    db.session.delete(version)
    db.session.commit()
    flash("Version supprimée avec succès.", "success")
    return redirect(url_for("settings"))
@app.route("/couleur/add", methods=["POST"])
def add_couleur():
    nom = request.form.get("nom")
    if nom:
        db.session.add(Couleur(nom=nom))
        db.session.commit()
        flash("Couleur ajoutée avec succès.", "success")
    return redirect(url_for("settings"))


@app.route("/couleur/edit/<int:id>", methods=["GET", "POST"])
def edit_couleur(id):
    couleur = Couleur.query.get_or_404(id)

    if request.method == "POST":
        couleur.nom = request.form.get("nom")
        db.session.commit()
        flash("Couleur modifiée avec succès.", "success")
        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier la couleur",
        action=url_for("edit_couleur", id=id),
        valeur=couleur.nom
    )


@app.route("/couleur/delete/<int:id>", methods=["POST"])
def delete_couleur(id):
    couleur = Couleur.query.get_or_404(id)
    db.session.delete(couleur)
    db.session.commit()
    flash("Couleur supprimée avec succès.", "success")
    return redirect(url_for("settings"))
@app.route("/interieur/add", methods=["POST"])
def add_interieur():
    nom = request.form.get("nom")
    if nom:
        db.session.add(Interieur(nom=nom))
        db.session.commit()
        flash("Intérieur ajouté avec succès.", "success")
    return redirect(url_for("settings"))


@app.route("/interieur/edit/<int:id>", methods=["GET", "POST"])
def edit_interieur(id):
    interieur = Interieur.query.get_or_404(id)

    if request.method == "POST":
        interieur.nom = request.form.get("nom")
        db.session.commit()
        flash("Intérieur modifié avec succès.", "success")
        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier l'intérieur",
        action=url_for("edit_interieur", id=id),
        valeur=interieur.nom
    )


@app.route("/interieur/delete/<int:id>", methods=["POST"])
def delete_interieur(id):
    interieur = Interieur.query.get_or_404(id)
    db.session.delete(interieur)
    db.session.commit()
    flash("Intérieur supprimé avec succès.", "success")
    return redirect(url_for("settings"))
@app.route("/motorisation/add", methods=["POST"])
def add_motorisation():
    nom = request.form.get("nom")
    if nom:
        db.session.add(Motorisation(nom=nom))
        db.session.commit()
        flash("Motorisation ajoutée avec succès.", "success")
    return redirect(url_for("settings"))


@app.route("/motorisation/edit/<int:id>", methods=["GET", "POST"])
def edit_motorisation(id):
    motorisation = Motorisation.query.get_or_404(id)

    if request.method == "POST":
        motorisation.nom = request.form.get("nom")
        db.session.commit()
        flash("Motorisation modifiée avec succès.", "success")
        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier la motorisation",
        action=url_for("edit_motorisation", id=id),
        valeur=motorisation.nom
    )


@app.route("/motorisation/delete/<int:id>", methods=["POST"])
def delete_motorisation(id):
    motorisation = Motorisation.query.get_or_404(id)
    db.session.delete(motorisation)
    db.session.commit()
    flash("Motorisation supprimée avec succès.", "success")
    return redirect(url_for("settings"))
@app.route("/financement/add", methods=["POST"])
def add_financement():
    nom = request.form.get("nom")
    if nom:
        db.session.add(Financement(nom=nom))
        db.session.commit()
        flash("Financement ajouté avec succès.", "success")
    return redirect(url_for("settings"))


@app.route("/financement/edit/<int:id>", methods=["GET", "POST"])
def edit_financement(id):
    financement = Financement.query.get_or_404(id)

    if request.method == "POST":
        financement.nom = request.form.get("nom")
        db.session.commit()
        flash("Financement modifié avec succès.", "success")
        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier le financement",
        action=url_for("edit_financement", id=id),
        valeur=financement.nom
    )


@app.route("/financement/delete/<int:id>", methods=["POST"])
def delete_financement(id):
    financement = Financement.query.get_or_404(id)
    db.session.delete(financement)
    db.session.commit()
    flash("Financement supprimé avec succès.", "success")
    return redirect(url_for("settings"))
@app.route("/canal/add", methods=["POST"])
def add_canal():
    nom = request.form.get("nom")
    if nom:
        db.session.add(Canal(nom=nom))
        db.session.commit()
        flash("Canal ajouté avec succès.", "success")
    return redirect(url_for("settings"))


@app.route("/canal/edit/<int:id>", methods=["GET", "POST"])
def edit_canal(id):
    canal = Canal.query.get_or_404(id)

    if request.method == "POST":
        canal.nom = request.form.get("nom")
        db.session.commit()
        flash("Canal modifié avec succès.", "success")
        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier le canal",
        action=url_for("edit_canal", id=id),
        valeur=canal.nom
    )


@app.route("/canal/delete/<int:id>", methods=["POST"])
def delete_canal(id):
    canal = Canal.query.get_or_404(id)
    db.session.delete(canal)
    db.session.commit()
    flash("Canal supprimé avec succès.", "success")
    return redirect(url_for("settings"))
@app.route("/detail/add", methods=["POST"])
def add_detail():
    nom = request.form.get("nom")
    if nom:
        db.session.add(DetailCanal(nom=nom))
        db.session.commit()
        flash("Détail canal ajouté avec succès.", "success")
    return redirect(url_for("settings"))


@app.route("/detail/edit/<int:id>", methods=["GET", "POST"])
def edit_detail(id):
    detail = DetailCanal.query.get_or_404(id)

    if request.method == "POST":
        detail.nom = request.form.get("nom")
        db.session.commit()
        flash("Détail canal modifié avec succès.", "success")
        return redirect(url_for("settings"))

    return render_template(
        "edit_item.html",
        titre="Modifier le détail canal",
        action=url_for("edit_detail", id=id),
        valeur=detail.nom
    )


@app.route("/detail/delete/<int:id>", methods=["POST"])
def delete_detail(id):
    detail = DetailCanal.query.get_or_404(id)
    db.session.delete(detail)
    db.session.commit()
    flash("Détail canal supprimé avec succès.", "success")
    return redirect(url_for("settings"))

if __name__ == "__main__":
    app.run(debug=True)