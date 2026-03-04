# Deception
_This project has been created as part of the 42 curriculum by nmartin._

---

## 📋 Table of Contents

- [Description](#description)
- [Architecture](#architecture)
- [Instructions](#instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Services](#services)
- [Technical Choices](#technical-choices)
  - [Virtual Machines vs Docker](#virtual-machines-vs-docker)
  - [Secrets vs Environment Variables](#secrets-vs-environment-variables)
  - [Docker Network vs Host Network](#docker-network-vs-host-network)
  - [Docker Volumes vs Bind Mounts](#docker-volumes-vs-bind-mounts)
- [Project Structure](#project-structure)
- [Resources](#resources)
- [AI Usage](#ai-usage)

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
```bash
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

### Installation

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
