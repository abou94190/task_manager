﻿﻿# task_manager #résumé_du_projet
# Documentation générale du projet
Introdution 	
Le projet Task-Manager vise à développer une application de gestion de tâches destinée aux petites et moyennes entreprises (PME). Cette application, conçue en Python, a pour objectif de fournir une solution simple, efficace et robuste pour aider les équipes à organiser et gérer leurs tâches quotidiennes. Ce document présente en détail le contexte, les objectifs, les outils utilisés, les rôles de l'équipe, et les différentes étapes du projet.

                  Partie Gestion du Projet

1.	Contexte du Projet
Le projet vise à développer un gestionnaire de tâches en Python pour les petites et moyennes entreprises (PME). L'objectif est de fournir une solution simple et robuste pour aider les équipes à organiser et gérer leurs tâches quotidiennes de manière efficace.
2.	Objectifs du Projet

	Faciliter la gestion des tâches
-Permettre aux équipes de créer, modifier, attribuer et suivre les tâches de manière efficace.
-Centraliser la gestion des tâches pour éviter les oublis et améliorer la visibilité.

Améliorer la collaboration
-Faciliter la collaboration entre les membres de l'équipe en attribuant clairement les responsabilités.
-Améliorer la communication en permettant le partage facile des informations sur les tâches. 

	Optimiser la Productivité
-Permettre aux PME de gagner du temps en automatisant la gestion quotidienne des tâches.
-Réduire les erreurs liées à la gestion manuelle des tâches.

	Réduire les Coûts
-Offrir une solution open-source en Python pour réduire les coûts d'acquisition et de maintenance.
-Éliminer le besoin de solutions coûteuses et complexes pour la gestion des tâches.

	Assurer la Qualité
-Implémenter des tests unitaires, d'intégration et de performance pour garantir la fiabilité et la robustesse du gestionnaire de tâches.
-Utiliser des pratiques de déploiement continu pour assurer une qualité constante.

	Documentation et Support
-Fournir une documentation complète du code et un guide d'utilisation pour faciliter l'installation, la configuration et l'utilisation du gestionnaire de tâches.
-Offrir un support continu pour résoudre les problèmes et répondre aux besoins des utilisateurs.

	Choix des Outils
	Gestion de projet et Colloboration
    # GitHub : pour le versionnement du code et la gestion des issues.
	# Jira : pour la gestion de projet agile et le suivi des tâches.
	Développement
	# Python : langage de programmation principal.
	# Pytest : pour les tests unitaires et d'intégration.
	# Locust : pour les tests de performance.
	# Selenium : pour les tests fonctionnels.
	# Github Action : pour l'intégration continue.

	Documentation
	#Google Docs : pour la documentation collaborative.
	#Autres Outils : Postman : pour tester les API.

	Présentation de l'Équipe Projet et Rôles
	#Développeurs backend : Amit et Abou
	#Testeurs : Amadou et Ibrahima
	#Product Owner : Amath

3.	RACI
Le modèle RACI est utilisé pour clarifier les responsabilités et les interactions au sein de l'équipe projet, ce qui assure une collaboration efficace et une gestion optimale des tâches.
 
4.	PBS – Product Breakdown Structure

Le PBS décrit la décomposition des produits et sous-produits du projet Task-Manager en éléments plus petits et plus gérables.

                        Partie Programmation

Fonctionnalités du Projet
Gestion des Utilisateurs :
•	Inscription des utilisateurs
•	Connexion des utilisateurs
•	Déconnexion des utilisateurs
•	Mise à jour du profil utilisateur
Gestion des Tâches :
-Ajout de tâches
-Récupération de tâches
-Suppression de tâches
-Marquer les tâches comme terminées
-Modification des tâches
-Affichage de toutes les tâches
Interface Utilisateur :
-Formulaire de connexion
-Formulaire d'inscription
-Formulaire d'ajout de tâche
-Liste des tâches
-Déconnexion
Fonctionnalités Côté Serveur (Flask) :
-Gestion des sessions
-Redirections
-Gestion des formulaires POST
-URLs dynamiques
Documentation des Fichiers Template et Static 
Répertoire Template 
Le répertoire templates contient les fichiers HTML utilisés pour générer les pages web de votre application. Flask utilise le moteur de Template Jinja2 pour rendre ces fichiers HTML dynamiques.
Fichier index.html :
-Affiche la page principale de l'application de gestion des tâches.
-Formulaire d'ajout de tâche.
-Liste des tâches.
-Lien de déconnexion.

Fichier login.html :
-Affiche la page de connexion de l'application.
-Formulaire de connexion.
-Lien vers la page d'inscription.
Fichier register.html :
-Affiche la page d'inscription de l'application.
-Formulaire d'inscription.
-Lien vers la page de connexion.
-Répertoire Static :
Le répertoire static contient les fichiers statiques, tels que les fichiers CSS, JavaScript, et les images utilisés par l'application.

                            Partie Tests

	-Tests Unitaires pour chaque Fonction : unittest, pytest
 		Tests pour la création, la modification, et la suppression des tâches.
 		Tests pour l'inscription, la connexion, et la déconnexion des utilisateurs.

    -Tests d’Intégration : unittest
		Tests pour vérifier l'intégration des différentes parties du système, telles que la base de données et les API.

	-Tests de Performance : Locust
		Tests pour évaluer la performance et la réactivité de l'application sous charge.

-	-Tests Fonctionnels : Selenium
		Tests pour vérifier que toutes les fonctionnalités de l'application fonctionnent comme prévu.

	-Documentation pour chaque Test
		Documentation détaillant de chaque cas de test, les résultats attendus, et les résultats obtenus.

           Partie Automatisation - Intégration Continue

Configuration des outils d'intégration continue avec Github Action pour automatiser les tests et les déploiements.

                            Conclusion
Ce résumé vise à fournir une vue d'ensemble complète du projet Task-Manager, couvrant tous les aspects de la gestion de projet, du développement, des tests et de l'automatisation


























# Gestionnaire de Tâches

## Vue d'ensemble
Le Gestionnaire de Tâches est une application web conçue pour aider les utilisateurs à gérer efficacement leurs tâches. Elle permet aux utilisateurs de créer, lire, mettre à jour et supprimer des tâches via une interface conviviale.

## Fonctionnalités
- Créer de nouvelles tâches
- Voir toutes les tâches
- Mettre à jour les tâches existantes
- Supprimer des tâches

## Installation
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/abou94190/task_manager.git

## Naviguer dans le répertoire du projet :

''bash

cd task_manager

## Installer les dépendances requises :

bash

pip install -r requirements.txt

## Configurer les variables d'environnement en créant un fichier .env :

plaintext

    API_KEY=votre_cle_api_ici

## Utilisation

    Lancer l'application :

    bash

    python app.py

    Accéder à l'application dans votre navigateur web à l'adresse http://localhost:5000.

## Points de terminaison de l'API

    GET /tasks : Récupérer toutes les tâches
    POST /tasks : Créer une nouvelle tâche
    PUT /tasks/
    : Mettre à jour une tâche
    DELETE /tasks/
    : Supprimer une tâche

