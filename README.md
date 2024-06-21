# task_manager

## Tests Unitaires

### Introduction

Ce projet inclut une suite de tests unitaires pour s'assurer que les différentes fonctionnalités du gestionnaire de tâches (`TaskManager`) fonctionnent correctement. Les tests sont écrits en utilisant le module `unittest` de Python.

### Structure des Tests

Les tests unitaires sont organisés dans une classe `TestTaskManager` qui hérite de `unittest.TestCase`. Chaque méthode de test vérifie une fonctionnalité spécifique de la classe `TaskManager`.

### Exécution des Tests

Pour exécuter les tests unitaires, utilisez la commande suivante à partir de la racine du projet :

```sh
python -m unittest discover -s tests

