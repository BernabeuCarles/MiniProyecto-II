Sistema opratiu: Ubuntu 20
Entorn: Visual Code
Versión python: python3


# Proyecto de Python con MongoDB usando Docker

Este proyecto utiliza Docker y Docker Compose para ejecutar una base de datos MongoDB que es consumida por una aplicación en Python.

## Prerrequisitos

Asegúrate de tener instalado lo siguiente en tu sistema:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalación de Docker y Docker Compose

### Instalación de Docker

1. **Actualizar el índice de paquetes APT:**
    ```bash
    sudo apt update
    ```

2. **Instalar paquetes necesarios:**
    ```bash
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```

3. **Agregar la clave GPG oficial de Docker:**
    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

4. **Agregar el repositorio de Docker:**
    ```bash
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    ```

5. **Actualizar el índice de paquetes APT nuevamente:**
    ```bash
    sudo apt update
    ```

6. **Instalar Docker CE (Community Edition):**
    ```bash
    sudo apt install docker-ce
    ```

### Instalación de Docker Compose

1. **Descargar Docker Compose:**
    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

2. **Aplicar permisos ejecutables a Docker Compose:**
    ```bash
    sudo chmod +x /usr/local/bin/docker-compose
    ```

### Inicio contenedor docker

sudo docker-compose up -d

