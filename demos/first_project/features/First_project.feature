Feature: Mon ppremier projet BDD 

    L'objectif de ce fichier est de découvrir la syntaxe de base en Gherkin en Python avec Behave.

    Scenario: test de mon permier scénario 

        Given J'ouvre mon terminal "Powershell"
        When Je me déplace dans le répertoire "C:\Users\andre"
        And J'affiche le contenu avec "dir"
        And Je regarde le contenu du répertoire
        Then je ferme le répertoire
