# learn_django_rest

Il s'agit d'une API ayant 2 routes:

* route file qui permet d'uploader un fichier et afficher: name, file size, content type.

* route job qui lancer une tâche asynchrone (avec Celery et redis comme broker) sur un fichier pour supprimer tous les mots ayant un fréquence supérieure à un paramètre envoyé dans l'url.

  - champs "status" montre l'état de la tâche : "IDLE" "WORKING" ou "DONE"

  - champs "result" montre resultat de la tâche.
