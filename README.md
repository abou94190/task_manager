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

