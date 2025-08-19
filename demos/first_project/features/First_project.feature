Feature: Mon ppremier projet BDD 

    # L'objectif de ce fichier est de découvrir la syntaxe de base en Gherkin en Python avec Behave.

    # Scenario: test de mon permier scénario 

    #     Given J'ouvre mon terminal "Powershell"
    #     When Je me déplace dans le répertoire "C:\Users\andre"
    #     And J'affiche le contenu avec "dir"
    #         |Type      | Nom   |
    #         |Directory | Rep1  |
    #         |File      | File1 |
    #         |Directory | Rep2  |
    #         |Directory | Rep3  |
    #         |File      | File2 |

    #     And Je regarde le contenu du répertoire
    #     Then je ferme le répertoire


Background:

        Given J'ouvre mon terminal <shell>
        When Je me déplace dans le répertoire <path>
        And J'affiche le contenu avec "dir"
            |Type      | Nom   |
            |Directory | Rep1  |
            |File      | File1 |
            |Directory | Rep2  |
            |Directory | Rep3  |
            |File      | File2 |

        And Je regarde le contenu du répertoire
        Then je ferme le répertoire

Scenario Outline: Test d'un jeux de données


        Examples: 
            |shell      | path                  |
            |bash       | /home/andre           |
            |cmd        | c:\users\andre\projet |
            |powershell | c:\users              |
   


Scenario Outline: Manipulation du Background #1

        Examples:
            |shell      | path                  |
            |cmd        | c:\users\andre\projet |


Scenario Outline: Manipulation du Background #2

        Examples:
            |shell      | path                  |
            |bash       | /home/andre           |
