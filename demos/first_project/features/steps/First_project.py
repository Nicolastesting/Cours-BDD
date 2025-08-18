import time
import logging
from behave import given, when, then

# Création d'un logger pour enregistrer tous les évènements du programme
logger = logging.getLogger("First_project")
logger.setLevel(logging.INFO)

# Création d'un formatteur commun
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Création du handler (gestionnaire de sortie)
file_handler = logging.FileHandler('first_project.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)    # Niveau de log minimum à enregistrer dans le fichier
file_handler.setFormatter(formatter)

# Ajout du handler au logger
logger.addHandler(file_handler)

@given("J'ouvre mon terminal")
def open_terminal(context):
    print("j'ouvre mon terminal")
    logger.info("j'ouvre mon terminal")
    time.sleep(2)

@when("Je me déplace dans le répertoire C:\\Users\\andre")
def deplace_dans_repertoire(context):
    print("Je me déplace dans le répertoire C:\\Users\\andre")
    logger.info("Je me déplace dans le répertoire C:\\Users\\andre")
    time.sleep(2)

@when("J'affiche le contenu avec 'ls -la'")
def affiche_contenu(context):
    print("J'affiche le contenu avec 'ls -la'")
    logger.info("J'affiche le contenu avec 'ls -la'")
    time.sleep(2)

@when("Je regarde le contenu du répertoire")
def regarder_contenu_repertoire(context):
    print("Je regarde le contenu du répertoire")
    logger.info("Je regarde le contenu du répertoire")
    time.sleep(2)

@then("je ferme le répertoire")
def ferme_repertoire(context):
    print("je ferme le répertoire")
    logger.info("je ferme le répertoire")
    time.sleep(2)