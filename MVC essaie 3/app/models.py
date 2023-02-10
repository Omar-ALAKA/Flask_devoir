#Importation des modules nécessaires

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#Définition de la classe Note

class Note(db.Model):
# Définition des colonnes de la table Note
    id = db.Column(db.Integer, primary_key=True) # L'identifiant unique de la note
    data = db.Column(db.String(10000)) # La donnée de la note
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # La date de création de la note
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # L'identifiant de l'utilisateur associé à la note

#Définition de la classe User

class User(db.Model, UserMixin):
# Définition des colonnes de la table User
    id = db.Column(db.Integer, primary_key=True) # L'identifiant unique de l'utilisateur
    nom = db.Column(db.String(200)) # Le nom de l'utilisateur
    prenom = db.Column(db.String(200)) # Le prénom de l'utilisateur
    email = db.Column(db.String(100), unique=True) # L'adresse e-mail de l'utilisateur
    username = db.Column(db.String(100)) # Le nom d'utilisateur de l'utilisateur
    password = db.Column(db.String(100)) # Le mot de passe de l'utilisateur
    notes = db.relationship('Note') # Relation entre les utilisateurs et les notes

#Les classes Note et User définissent les modèles pour les tables notes et users dans la base de données.
#La classe User hérite de la classe UserMixin pour permettre la gestion de l'authentification de l'utilisateur via Flask-Login.
#La colonne user_id dans la table notes établit la relation entre les notes et les utilisateurs dans la base de données.