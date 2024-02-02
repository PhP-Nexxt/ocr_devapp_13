# Guide d'utilisation

[![ci-cd](https://github.com/PhP-Nexxt/ocr_devapp_13/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/PhP-Nexxt/ocr_devapp_13/actions/workflows/ci_cd.yml)

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


#### 2. Sans docker

##### 2.1. Cloner le dépot github :

```bash
$ git clone git@github.com:PhP-Nexxt/ocr_devapp_13.git
$ cd ocr_devapp_13
```

##### 2.2. Copier le fichier .env.sample en tant que .env

```bash
$ cp .env.sample .env
```

Modifiez les variables d'environnement dans le fichier `.env` selon vos besoins.

##### 2.3. Creer et activez un environnement virtuel

```bash
$ python3 -m venv venv && source venv/bin/activate
``` 

##### 2.4 Installer le fichier requirement.txt

```bash
$ (venv) pip install -r requirement.txt
```

##### 2.5 Appliquez les migrations

```bash
(venv)$ python manage.py migrate
(venv)$ python manage.py createsuperuser
```

##### 2.6 Lancer le projet 

```bash
(venv)$ python manage.py runserver
```

l'application sera accessible à l'adresse:

- http://127.0.0.1:8000/


## Environnement de production

Pour la mise en production de ce projet, j'ai du utiliser un vps(machine virtuelle) avec une distribution Ubuntu 22.04 sur laquelle j'ai préalablement installé docker et dockercompose.

Pour la suite nous aurons besoin de la clé ssh privée du serveur, ainsi que le nom d'utilisateur.

Depuis le setting github du projet, il faudra ajouter les variables secretes telles que USERNAME_SERVEUR, SERVER_PRIVATE_KEY, les informations de connexion à notre dockerhub et les variables d'environnement du projet.

Une fois ces elements configurés, le pipeline se charge du reste.

Ce pipe line est constitué de 5 étapes, dépendantes l'une aprés l'autres.

## Documentation

La documentation de ce projet est disponible, via readthedoc à l'adresse suivante :

- https://ocr-devapp-13.readthedocs.io/en/latest/#

## Realisé avec

Ce projet a été développé en utilisant les technologies suivantes :

-   ![Python Badge](https://img.shields.io/badge/Python-3.11-blue?logo=python)

-   ![Django Badge](https://img.shields.io/badge/Django-4.2.7-green?logo=django)

-   ![Docker Badge](https://img.shields.io/badge/Docker-20.10-blue?logo=docker)

-   ![Docker Compose Badge](https://img.shields.io/badge/Docker%20Compose-2.2.3-blue?logo=docker)

-   ![Nginx Badge](https://img.shields.io/badge/Nginx-1.25-orange?logo=nginx)

-   ![Ubuntu Badge](https://img.shields.io/badge/Ubuntu-22.04-blue?logo=ubuntu)

-   ![GitHub Actions Badge](https://img.shields.io/badge/GitHub%20Actions-green?logo=github-actions)






