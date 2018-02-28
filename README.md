# PracticaDocker
## Autor: Orlandy Ariel Sánchez Acosta.

Práctica final de del curso introducción a Docker, en este se levantará un microframework [Flack](http://flask.pocoo.org/) para crear aplicaciones web con Python. Para crear la aplicación, aparte de Flack, se utiliza la librería [Redis]( https://github.com/andymccurdy/redis-py) para el contenido de la pequeña página que se creará.

La página simplemente es un contador de visitas que se reseteará cuando este sea mayor de 20. Cuando esto pase se le informará al usuario y en su siguiente visita se empezará desde 1 de nuevo.

Para correr la aplicación utilizar el comando:
> docker-compose up

Para acceder la aplicación se hará en [localhost:5000](localhost:5000) o [0.0.0.0:5000](0.0.0.0:5000)
