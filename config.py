import os
from dotenv import load_dotenv

# Charger les variables du fichier .env
load_dotenv()


class Config:
    """
    Configuration générale de l'application
    """

    # ==========================
    # Flask
    # ==========================
    SECRET_KEY = os.getenv("SECRET_KEY", "BYD_SECRET")

    # ==========================
    # Base de données MySQL
    # ==========================
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==========================
    # Uploads
    # ==========================
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    UPLOAD_FOLDER = os.path.join(BASE_DIR, os.getenv("UPLOAD_FOLDER", "uploads"))

    MAX_CONTENT_LENGTH = int(
        os.getenv("MAX_CONTENT_LENGTH", 20 * 1024 * 1024)
    )

    # Types de fichiers autorisés
    ALLOWED_EXTENSIONS = {
        "pdf",
        "doc",
        "docx",
        "xls",
        "xlsx",
        "png",
        "jpg",
        "jpeg"
    }

    # ==========================
    # Mail
    # ==========================
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS") == "True"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    # ==========================
    # Informations Application
    # ==========================
    APP_NAME = os.getenv("APP_NAME", "BYD CRM")
    COMPANY = os.getenv("COMPANY", "Auto Nejma Marrakech")

    DEBUG = os.getenv("DEBUG", "False") == "True"