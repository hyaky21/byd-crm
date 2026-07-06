from datetime import datetime
from flask_login import UserMixin
from extensions import db


# =====================================================
# UTILISATEURS
# =====================================================

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(50), default="commercial")

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# COMMERCIAUX
# =====================================================

class Commercial(db.Model):
    __tablename__ = "commerciaux"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# POTENTIELS
# =====================================================

class Potentiel(db.Model):
    __tablename__ = "potentiels"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# MODELES
# =====================================================

class Modele(db.Model):
    __tablename__ = "modeles"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# VERSIONS
# =====================================================

class Version(db.Model):
    __tablename__ = "versions"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# COULEURS EXTERIEURES
# =====================================================

class Couleur(db.Model):
    __tablename__ = "couleurs"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# INTERIEURS
# =====================================================

class Interieur(db.Model):
    __tablename__ = "interieurs"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# MOTORISATIONS
# =====================================================

class Motorisation(db.Model):
    __tablename__ = "motorisations"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# FINANCEMENTS
# =====================================================

class Financement(db.Model):
    __tablename__ = "financements"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# CANAUX
# =====================================================

class Canal(db.Model):
    __tablename__ = "canaux"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =====================================================
# DETAIL CANAL
# =====================================================

class DetailCanal(db.Model):
    __tablename__ = "detail_canaux"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(db.String(100), nullable=False, unique=True)

    actif = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
    # =====================================================
# PROSPECTS
# =====================================================

class Prospect(db.Model):
    __tablename__ = "prospects"

    id = db.Column(db.Integer, primary_key=True)

    annee = db.Column(db.Integer, nullable=False)

    mois = db.Column(db.String(30), nullable=False)

    date_contact = db.Column(db.Date, nullable=False)

    commercial_id = db.Column(
        db.Integer,
        db.ForeignKey("commerciaux.id"),
        nullable=False
    )

    nom_client = db.Column(
        db.String(100),
        nullable=False
    )

    prenom_client = db.Column(
        db.String(100),
        nullable=False
    )

    telephone = db.Column(
        db.String(30),
        nullable=False
    )

    email = db.Column(
        db.String(120)
    )

    ville = db.Column(
        db.String(100)
    )

    potentiel_id = db.Column(
        db.Integer,
        db.ForeignKey("potentiels.id"),
        nullable=False
    )

    modele_id = db.Column(
        db.Integer,
        db.ForeignKey("modeles.id"),
        nullable=False
    )

    version_id = db.Column(
        db.Integer,
        db.ForeignKey("versions.id"),
        nullable=False
    )

    couleur_id = db.Column(
        db.Integer,
        db.ForeignKey("couleurs.id")
    )

    interieur_id = db.Column(
        db.Integer,
        db.ForeignKey("interieurs.id")
    )

    motorisation_id = db.Column(
        db.Integer,
        db.ForeignKey("motorisations.id")
    )

    financement_id = db.Column(
        db.Integer,
        db.ForeignKey("financements.id")
    )

    canal_id = db.Column(
        db.Integer,
        db.ForeignKey("canaux.id")
    )

    detail_canal_id = db.Column(
        db.Integer,
        db.ForeignKey("detail_canaux.id")
    )

    commentaire = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    commercial = db.relationship("Commercial")

    potentiel = db.relationship("Potentiel")

    modele = db.relationship("Modele")

    version = db.relationship("Version")

    couleur = db.relationship("Couleur")

    interieur = db.relationship("Interieur")

    motorisation = db.relationship("Motorisation")

    financement = db.relationship("Financement")

    canal = db.relationship("Canal")

    detail_canal = db.relationship("DetailCanal")