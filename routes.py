from flask import render_template, request, redirect, url_for, flash

from app import app
from extensions import db

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
    DetailCanal
)


# =====================================================
# ACCUEIL
# =====================================================

@app.route("/")
def index():

    commerciaux = Commercial.query.filter_by(actif=True).order_by(Commercial.nom).all()

    potentiels = Potentiel.query.filter_by(actif=True).order_by(Potentiel.nom).all()

    modeles = Modele.query.filter_by(actif=True).order_by(Modele.nom).all()

    versions = Version.query.filter_by(actif=True).order_by(Version.nom).all()

    couleurs = Couleur.query.filter_by(actif=True).order_by(Couleur.nom).all()

    interieurs = Interieur.query.filter_by(actif=True).order_by(Interieur.nom).all()

    motorisations = Motorisation.query.filter_by(actif=True).order_by(Motorisation.nom).all()

    financements = Financement.query.filter_by(actif=True).order_by(Financement.nom).all()

    canaux = Canal.query.filter_by(actif=True).order_by(Canal.nom).all()

    detail_canaux = DetailCanal.query.filter_by(actif=True).order_by(DetailCanal.nom).all()

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
        detail_canaux=detail_canaux
    )


# =====================================================
# DASHBOARD
# =====================================================

@app.route("/dashboard")
def dashboard():

    commerciaux = Commercial.query.order_by(Commercial.nom).all()

    return render_template(
        "dashboard.html",
        commerciaux=commerciaux
    )


# =====================================================
# PARAMETRES
# =====================================================

@app.route("/settings")
def settings():

    return render_template(
        "settings.html",

        commerciaux=Commercial.query.order_by(Commercial.nom).all(),

        modeles=Modele.query.order_by(Modele.nom).all(),

        versions=Version.query.order_by(Version.nom).all(),

        couleurs=Couleur.query.order_by(Couleur.nom).all(),

        interieurs=Interieur.query.order_by(Interieur.nom).all(),

        motorisations=Motorisation.query.order_by(Motorisation.nom).all(),

        financements=Financement.query.order_by(Financement.nom).all(),

        canaux=Canal.query.order_by(Canal.nom).all(),

        detail_canaux=DetailCanal.query.order_by(DetailCanal.nom).all(),

        potentiels=Potentiel.query.order_by(Potentiel.nom).all()
    )


# =====================================================
# PAGE AJOUT
# =====================================================

@app.route("/add")
def add():

    return render_template("add_item.html")


# =====================================================
# PAGE MODIFICATION
# =====================================================

@app.route("/edit/<int:id>")
def edit(id):

    return render_template(
        "edit_item.html",
        id=id
    )


# =====================================================
# PAGE CONFIRMATION
# =====================================================

@app.route("/confirmation")
def confirmation():

    return render_template(
        "confirmation.html"
    )