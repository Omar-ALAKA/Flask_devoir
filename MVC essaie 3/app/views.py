# Importation des modules nécessaires à partir de Flask et Flask-Login
from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Importation du modèle "Note" et du module "db"
from .models import Note
from . import db

# Définition d'un blueprint "views"
views = Blueprint('views', __name__)

# Définition de la route "/home" qui est protégée par la fonction de connexion de Flask-Login
@views.route('/home')
@login_required 
def home():
    # Affichage de la page "home.html" en fournissant les informations de l'utilisateur actuel
    return render_template("home.html", user=current_user)

# Définition de la route "/"
@views.route('/')
def index():
    # Affichage de la page "index.html"
    return render_template("index.html")
