## Understand what services are provided by the stack.

Inception provides many services:

 -  Nginx (Web Server) who handle the traffic and SSL certificate, work as a server.
 -  Wordpress (Application) who handle the first website.
 -  MariaDB (Database) who is the database of the website.
 -  Redis (Performance) who is a cache-handler, make the website faster.
 -  FTP (File Management) who is capable to download/upload files of the website's data.
 -  Adminer (Database Management) who permits to see the data stored in the database.
 -  Static (Aditionnal Website) who presents quicly the project on a website.
 -  Monitor (Monitoring) who inpects logs and running container on live.

## Start and stop the project.

To start the project, build images and run containers, you just have to put this command in the root of the project:
```bash
make up
```

To stop the containers, put this command, also in the root of the project:
```bash
make down
```

## Access the website and the administration panel.

The website is enable at the URL `nmartin.42.fr`.
To access the administration panel, put `nmartin.42.fr/wp-admin` in the navigator.

## Locate and manage credentials.

Non-credentials information are in the `.env` file.
To enforce security, credentials are declared in a `secrets/` folder.
Containing `FTP_PASSWORD`, `MYSQL_PASSWORD`, `MYSQL_ROOT_PASSWORD`, `WP_ADMIN_PASSWORD` and `WP_PASSWORD`
environment variables in their respectives files.

## Check that the services are running correctly.

Each services are working on their respective containers.
To see wich containers are currently running, docker got a command:

```bash
docker ps
```
