import time
import logging
from behave import *

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

@given("J'ouvre mon terminal {shell}")
def open_terminal(context, shell):
    print(f"P: j'ouvre mon terminal {shell}")
    logger.info(f"j'ouvre mon terminal {shell}")
    time.sleep(2)

@when("Je me déplace dans le répertoire {path}")
def deplace_dans_repertoire(context, path):
    print(f"P: Je me déplace dans le répertoire {path}")
    logger.info(f"Je me déplace dans le répertoire {path}")
    time.sleep(2)

@when("J'affiche le contenu avec {cmd}")
def affiche_contenu(context, cmd):
    print(f"P: J'affiche le contenu avec {cmd}")
    logger.info(f"J'affiche le contenu avec {cmd}")
    for row in context.table:
        logger.info(f"J'affiche la ligne {row['Type']} {row ['Nom']}")
    time.sleep(2)

@when("Je regarde le contenu du répertoire")
def regarder_contenu_repertoire(context):
    print("P: Je regarde le contenu du répertoire")
    logger.info("Je regarde le contenu du répertoire")
    time.sleep(2)

@then("je ferme le répertoire")
def ferme_repertoire(context):
    print("P: je ferme le répertoire")
    logger.info("je ferme le répertoire")
    time.sleep(2)