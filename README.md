# Guide d'utilisation

Dans ce guide, nous allons vous permettre d'installer et de lancer le projet ocr devapp 13 en local, et dans un environnement de production.

## Environnement local

### Installation

#### 1. Avec docker

Pour exécuter ce projet localement, assurez-vous d'avoir installé Docker et Docker Compose sur votre système. Vous pouvez les installer en suivant les instructions officielles : 

-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

Une fois que Docker et Docker Compose sont installés, suivez ces étapes :

##### 1.1. Cloner le dépot github :

```bash
$ git clone git@github.com:PhP-Nexxt/ocr_devapp_13.git
$ cd ocr_devapp_13
```

##### 1.2. Copier le fichier .env.sample en tant que .env

```bash
$ cp .env.sample .env
```

Modifiez les variables d'environnement dans le fichier `.env` selon vos besoins.

##### 1.3. Construisez les conteneurs docker

```bash
$ docker-compose build
```

##### 1.4. Lancer les containers docker

```bash
$ docker-compose up
# Les deux commandes ci-dessous sont utiles si vous changez de base de données
$ docker-compose  exec web python manage.py migrate
$ docker-compose  exec web python manage.py createsuperuser
```

Les conteneurs Docker seront démarrés, et l'application sera accessible à l'adresse:

- http://localhost
- http://localhost/admin
- http://127.0.0.1
- http://127.0.0.1/admin


