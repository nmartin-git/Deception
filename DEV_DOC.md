## Set up the environment from scratch (prerequisites, configuration files, secrets)

### Prerequisites

- Linux/Unix system (Debian/Ubuntu recommended)
- Docker Engine (≥ 20.10)
- Docker Compose (≥ 2.0)
- Make
- OpenSSL (for SSL certificate generation)

### Secrets

At `srcs/` declare in the `.env` file thoses environment variables:
```environment variables
USER_LOGIN=xxxx
DOMAIN_NAME=xxxx

MYSQL_DATABASE=xxxx
MYSQL_USER=xxxx
MYSQL_HOST=xxxx

WP_TITLE=xxxx

WP_ADMIN_USER=xxxx
WP_ADMIN_EMAIL=xxxx

WP_USER=xxxx
WP_EMAIL=xxxx

FTP_USER=xxxx
```

At root, declare in a `secrets` folder thoses credentials environment variables:
```secrets/ftp_pwd
FTP_PASSWORD=xxxx
```

```secrets/mariadb_pwd
MYSQL_PASSWORD=xxxx
MYSQL_ROOT_PASSWORD=xxxx
```

```secrets/wordpress_pwd
WP_ADMIN_PASSWORD=xxxx
WP_PASSWORD=xxxx
```
 
## Build and launch the project using the Makefile and Docker Compose

To build and launch the project you can use both commands:
```bash
make up
```
Who uses docker command:
```bash
docker compose -f srcs/docker-compose.yml up -d --build
```
That permits to build the images and create/launch respectives containers in only one command.
 
## Use relevant commands to manage the containers and volumes

Their is many commands to manage the containers:

See running containers:
```bash
docker ps
```

Run containers:
```bash
docker compose -f srcs/docker-compose.yml up -d
```

Stop containers:
```bash
docker compose -f srcs/docker-compose.yml down
```

See logs:
```bash
docker compose -f srcs/docker-compose.yml logs
```

To manage volumes:

List all volumes:
```bash
docker volume ls
```

Remove a volume:
```bash
docker rm [volume name]
```

Inspect a volume:
```bash
docker volume inspect [volume name]
```

Remove all volumes:
```bash
docker volume prune --all
```
 
## Identify where the project data is stored and how it persists

Data is stored in the root of the computer, at `data/` folder.
It persists with the docker volumes system who permits to share data between our computer data and container's data.
Container's data are transfered to the `data/` folder, and our computer can access it.
