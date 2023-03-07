# Docker compose instructions for WordPress in Raspberry Pi
Non-official guide


## What is WordPress?

> WordPress is one of the most versatile open source content management systems on the market. WordPress is built for high performance and is scalable to many servers, has easy integration via REST, JSON, SOAP and other formats, and features a whopping 15,000 plugins to extend and customize the application for just about any type of website.

[https://www.wordpress.org/](https://www.wordpress.org/)

## TL;DR for test purposes only

```console
$ curl -sSL https://raw.githubusercontent.com/jpeant/rasbi-docker-wordpress/main/wordpress-stack.yml
$ docker-compose -f wordpress-stack.yml up
```

Access your application at *http://your-ip:8080/*

## Images used in this compose

The recommended way to get the WordPress Docker Image is to pull the prebuilt image from the [Docker Hub Registry](https://hub.docker.com/_/wordpress).

```console
$ docker pull wordpress:latest
```

For the database we are using MariaDB and it is equivalent for MySql. You can view the [list of available versions](https://hub.docker.com/_/mariadb) in the Docker Hub Registry.

```console
$ docker pull mariadb:latest
```
