# Deception
_This project has been created as part of the 42 curriculum by nmartin._

---

## 📋 Table of Contents

- [Description](#description)
- [Architecture](#architecture)
- [Instructions](#instructions)
  - [Prerequisites](#prerequisites)
  - [Installation & Usage](#commands)
- [Resources](#resources)
- [Services](#services)
- [Virtual Machines vs Docker](#virtual-machines-vs-docker)
- [Secrets vs Environment Variables](#secrets-vs-environment-variables)
- [Docker Network vs Host Network](#docker-network-vs-host-network)
- [Docker Volumes vs Bind Mounts](#docker-volumes-vs-bind-mounts)

---

## 📖 Description

**Inception** is a Docker-based infrastructure project that implements a complete web service stack using containerization. The goal is to set up a WordPress website with NGINX as a reverse proxy, MariaDB as the database, and additional services (Redis cache, FTP server, Adminer, static website, and monitoring tools).

### Goals

- Learn Docker containerization and orchestration
- Understand network isolation and service communication
- Implement security best practices (TLS, secrets management)
- Build services from scratch using official base images
- Master Docker Compose for multi-container applications

### Key Features

- ✅ **NGINX** with TLSv1.3 on port 443
- ✅ **WordPress** with PHP-FPM
- ✅ **MariaDB** database
- ✅ **Redis** caching layer
- ✅ **FTP Server** for file management
- ✅ **Adminer** for database administration
- ✅ **Static Website** (architecture du projet)
- ✅ **Container Monitoring** (custom service)

---

## 🏗️ Architecture
```schema
┌────────────────────────────────────────────────────┐
│              Host Machine (Debian)                 │
│                                                    │
│  ┌────────────────────────────────────────────┐    │
│  │     Docker Network: inception (bridge)     │    │
│  │                                            │    │
│  │   ┌──────────┐   ┌──────────┐              │    │
│  │   │  NGINX   │   │WordPress │              │    │
│  │   │  :443    │──▶│  :9000   │              │    │
│  │   │ (TLSv1.3)│   │ (PHP-FPM)│              │    │
│  │   └──────────┘   └─────┬────┘              │    │
│  │        │               │                   │    │
│  │        │               ▼                   │    │
│  │        │         ┌──────────┐              │    │
│  │        │         │ MariaDB  │              │    │
│  │        │         │  :3306   │              │    │
│  │        │         │ (MySQL)  │              │    │
│  │        │         └──────────┘              │    │
│  │        │                │                  │    │
│  │        │                │                  │    │
│  │   ┌────┴─────┬──────────┴───┬─────────┐    │    │
│  │   │          │              │         │    │    │
│  │   ▼          ▼              ▼         ▼    │    │
│  │ ┌─────┐  ┌────────┐  ┌───────┐  ┌─────┐    │    │
│  │ │Redis│  │Adminer │  │  FTP  │  │Stats│    │    │
│  │ │:6379│  │ :8080  │  │  :21  │  │:8081│    │    │
│  │ └─────┘  └────────┘  └───────┘  └─────┘    │    │
│  │                                            │    │
│  │              ┌──────────┐                  │    │
│  │              │ Monitor  │                  │    │
│  │              │  :5000   │                  │    │
│  │              └──────────┘                  │    │
│  └────────────────────────────────────────────┘    │
│                                                    │
│  Docker Volumes:                                   │
│  ├─ wordpress_data  → /var/www/html                │
│  ├─ mariadb_data    → /var/lib/mysql               │
│  ├─ redis_data      → /data                        │
│  ├─ ftp_data        → /home/ftpuser                │
│  ├─ static_data     → /var/www/html                │
│  └─ adminer_data    → /var/www/html                │
└────────────────────────────────────────────────────┘
```
---

## 🚀 Instructions

### Prerequisites

- Linux/Unix system (Debian/Ubuntu recommended)
- Docker Engine (≥ 20.10)
- Docker Compose (≥ 2.0)
- Make
- OpenSSL (for SSL certificate generation)

### Commands

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/inception.git
cd inception
```

2. **Build and run**

```bash
make
```

3. **Stop all services**

```bash
make down
```

4. **Rebuild all containers**
```bash
make down
```

5. **Clean everything (including volumes)**

```bash
make fclean
```

6. **Access points**

-  WordPress: bash https://nmartin.42.fr
-  WordPress Admin: https://nmartin.42.fr/wp-admin
-  Adminer: https://adminer.nmartin.42.fr
-  Static Site: https://static.nmartin.42.fr
-  Monitor: http://localhost:5000
-  FTP: (installer filezilla)
```bash
filezilla
```

## 📚 Ressources

### Guides & Documentation
-  [OpenClassrooms](https://openclassrooms.com/fr/courses/8431896-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker)
-  [DevSecOps](https://blog.stephane-robert.info/docs/conteneurisation/)

### IA
 -  Github Copilot (Claude sonnet 4.5)
    -  Set a project roadmap
    -  Assistance to elaborate Dockerfiles and Scripts
    -  Explaining project's concepts

---

---

## Services

### 1. NGINX
- **Base image:** `debian:bookworm`
- **Role:** Reverse proxy and TLS termination
- **Port:** 443 (HTTPS)
- **Features:** TLSv1.2/TLSv1.3, SSL certificate, proxies to WordPress
- **Dockerfile:** `srcs/requirements/nginx/Dockerfile`

### 2. WordPress + PHP-FPM
- **Base image:** `debian:bookworm`
- **Role:** Content Management System
- **Port:** 9000 (PHP-FPM, internal)
- **Features:** PHP 8.2, WordPress CLI, Redis cache integration
- **Dockerfile:** `srcs/requirements/wordpress/Dockerfile`

### 3. MariaDB
- **Base image:** `debian:bookworm`
- **Role:** Relational database
- **Port:** 3306 (internal)
- **Features:** MySQL 10.11, persistent storage, automated setup
- **Dockerfile:** `srcs/requirements/mariadb/Dockerfile`

---

## Bonus Services

### 4. Redis
- **Base image:** `debian:bookworm`
- **Role:** Object caching for WordPress
- **Port:** 6379 (internal)
- **Features:** In-memory cache, improves performance by 40-60%
- **Dockerfile:** `srcs/requirements/bonus/redis/Dockerfile`

### 5. FTP Server (vsftpd)
- **Base image:** `debian:bookworm`
- **Role:** File transfer protocol server
- **Port:** 21
- **Features:** Upload files to WordPress, user authentication
- **Dockerfile:** `srcs/requirements/bonus/ftp/Dockerfile`

### 6. Adminer
- **Base image:** `debian:bookworm`
- **Role:** Web-based database management
- **Port:** 8080
- **Features:** Lightweight phpMyAdmin alternative, SQL queries
- **Dockerfile:** `srcs/requirements/bonus/adminer/Dockerfile`

### 7. Static Website
- **Base image:** `debian:bookworm`
- **Role:** Static portfolio/CV website
- **Port:** 8081
- **Features:** NGINX serving HTML/CSS/JS
- **Dockerfile:** `srcs/requirements/bonus/static/Dockerfile`

### 8. Container Monitor (ctop)
- **Base image:** `debian:bookworm`
- **Role:** Real-time container monitoring
- **Port:** 5000
- **Features:** Web dashboard, live logs, container status
- **Dockerfile:** `srcs/requirements/bonus/ctop/Dockerfile`

---

## 🖥️ Virtual Machines vs Docker

### Comparison Table
```table
| Aspect              | Virtual Machines                               | Docker (Chosen)                                 |
|---------------------|------------------------------------------------|-------------------------------------------------|
| **Isolation Level** | Complete OS isolation with hypervisor          | Process-level isolation using kernel namespaces |
| **Resource Usage**  | Heavy (GB of RAM per VM)                       | Lightweight (MB per container)                  |
| **Startup Time**    | Minutes (full OS boot)                         | Seconds (process start)                         |
| **Disk Space**      | Large (full OS images)                         | Small (layered filesystem)                      |
| **Portability**     | Low (hypervisor-dependent)                     | High (runs anywhere with Docker)                |
| **Performance**     | Overhead from virtualization                   | Near-native performance                         |
| **Use Case**        | Full OS testing, legacy apps, strong isolation | Microservices, modern apps, CI/CD               |
| **Scalability**     | Limited by hardware                            | Highly scalable                                 |
| **Management**      | Complex (OS updates, patching)                 | Simple (container images)                       |
```

### Why Docker for Inception

✅ **Lightweight Architecture**
- Run 7+ services on a single machine without heavy resource consumption
- Each container uses only the resources it needs
- Shared kernel reduces memory footprint

✅ **Fast Deployment and Iteration**
- Containers start in seconds vs minutes for VMs
- Quick rebuild and restart cycles during development
- Instant rollback to previous versions

✅ **Reproducibility**
- Same environment across development, testing, and production
- Dockerfiles ensure consistent builds
- No "works on my machine" problems

✅ **Microservices Architecture**
- Each service runs in isolation
- Independent scaling and updates
- Clear separation of concerns (NGINX, WordPress, MariaDB)

✅ **Industry Standard**
- Docker is the de facto standard for containerization
- Essential skill for modern DevOps and system administration
- Large ecosystem of tools and community support

✅ **Resource Efficiency**
- Host machine: 4GB RAM can run all services
- VM equivalent would need 16GB+ RAM
- Lower energy consumption and infrastructure costs

### When VMs Would Be Better

❌ **Not Suitable for Inception:**
- Need complete OS isolation (different kernels)
- Running untrusted code requiring maximum security
- Legacy applications requiring specific OS versions
- Testing different operating systems

### Inception Use Case

Docker is perfect for this project because we're running multiple modern services that share the same kernel, need to communicate efficiently, and benefit from rapid deployment cycles during development.

---

## 🔐 Secrets vs Environment Variables

### Comparison Table
```table
| Method                    | Security Level | Visibility                                | Rotation   | Use Case                | Implementation               |
|---------------------------|----------------|-------------------------------------------|------------|-------------------------|------------------------------|
| **Environment Variables** | ⚠️ Low         | Visible in `docker inspect`, process list | Manual     | Non-sensitive config    | `.env` file                  |
| **Docker Secrets**        | ✅ High        | Encrypted at rest, in transit             | API-driven | Passwords, keys, tokens | Docker Swarm/Compose         |
| **External Vault**        | ✅ Very High   | Never stored in container                 | Automated  | Production secrets      | HashiCorp Vault, AWS Secrets |
```

### Chosen Approach:

### Environment Variables with `.env` File for non-credentials and `secrets/` Folder for credentials

✅ **Simplicity for Learning Projects**
- Easy to understand and debug
- No additional infrastructure required
- Clear visibility during development

✅ **No Docker Swarm Requirement**
- Docker Secrets require Swarm mode
- This is a single-host setup
- Swarm adds unnecessary complexity for this use case

✅ **Easy Configuration Management**
- Simple to modify values during development
- No need to redeploy secrets
- Quick testing of different configurations

✅ **Security enforcment**
 -  Splitted sensitive contents
 -  Separation between credentials and non-credentials informations

# Docker Network vs Host Network

## Comparison Table 

```table
| Mode                | Isolation         | DNS Resolution  | Port Conflicts        | Performance      | Security | Use Case             |
|---------------------|-------------------|-----------------|-----------------------|------------------|----------|----------------------|
| **Bridge Network**  | ✅ Full isolation | ✅ Built-in DNS | ❌ No conflicts       | Slight overhead  | ✅ High  | Multi-container apps |
| **Host Network**    | ❌ Shares host    | ❌ Manual IP    | ✅ Possible conflicts | Fastest          | ⚠️ Lower | Single container     |
| **Overlay Network** | ✅ Multi-host     | ✅ Built-in DNS | ❌ No conflicts       | Network overhead | ✅ High  | Swarm/Kubernetes     |
```

## Chosen Approach: Docker Bridge Network (`inception`)

### Why This Choice

✅ **Container Isolation**
- Containers can't access host services directly
- Network namespace isolation prevents interference
- Only exposed ports are accessible from outside
- Internal services (MariaDB) completely hidden from host

✅ **Built-in DNS Resolution**
- Containers communicate by service name
- No need for IP address management
- Automatic service discovery

**Example:**
```yaml
# WordPress connects to MariaDB by name
WORDPRESS_DB_HOST=mariadb:3306  # Not 172.18.0.3:3306

# NGINX proxies to WordPress by name
fastcgi_pass wordpress:9000;     # Not localhost:9000
```

✅ **Security Benefits**
 -  Default deny: containers can't reach each other unless connected
 -  Explicit network membership required
 -  Easy firewall rules at network level
 -  Reduced attack surface

✅ **Flexibility and Scalability**
 -  Easy to add/remove services without affecting host
 -  Multiple isolated networks possible
 -  Service-to-service communication without port mapping
 -  Simple to replicate on different hosts EOF

## Docker Volumes vs Bind Mounts

### Comparison Table

```table
| Feature                 | Docker Volumes (Chosen)         | Bind Mounts                     |
|-------------------------|---------------------------------|---------------------------------|
| **Management**          | ✅ Docker CLI (`docker volume`) | ⚠️ Manual filesystem            |
| **Portability**         | ✅ Platform-independent paths   | ❌ Host-specific absolute paths |
| **Backup**              | ✅ `docker volume backup`       | ⚠️ Manual tar/rsync             |
| **Performance**         | ✅ Optimized by Docker          | Depends on host FS              |
| **Permissions**         | ✅ Docker-managed               | ⚠️ Manual chmod/chown           |
| **Visibility**          | `docker volume ls`              | Must know host paths            |
| **Container Isolation** | ✅ Outside container filesystem | ⚠️ Direct host access           |
| **Windows/Mac**         | ✅ Handles FS differences       | ⚠️ Permission issues            |
```

### Chosen Approach: Docker Named Volumes

### Why This Choice

✅ **Portability Across Hosts**
```yaml
# Works on any host - Docker manages the path
volumes:
  wordpress_data:
    driver: local

# vs Bind Mount - host-specific path
volumes:
  - /home/user/wordpress:/var/www/html  # Breaks on different machines
```

✅ **Docker-Managed Lifecycle**
```bash

# Easy management
docker volume ls                    # List all volumes
docker volume inspect wordpress_data # View details
docker volume prune                 # Clean unused volumes

# Easy backup
docker run --rm -v wordpress_data:/data -v $(pwd):/backup \
  alpine tar czf /backup/wordpress.tar.gz /data
```

✅ **Subject Requirement**

  -  Inception project mandates Docker volumes
  -  Learning industry-standard practices
  -  Better understanding of containerized storage EOF

