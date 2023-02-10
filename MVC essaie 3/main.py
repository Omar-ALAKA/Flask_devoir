# Import de la fonction create_app depuis le module app
from app import create_app

# Création de l'application Flask en appelant la fonction create_app
app = create_app()

# Condition qui vérifie si le fichier en cours d'exécution est le fichier principal
if __name__ == "__main__":
    # Démarrage de l'application Flask avec le paramètre debug activé
    app.run(debug=True)
