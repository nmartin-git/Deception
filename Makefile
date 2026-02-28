all: up

up:
	mkdir -p /home/nmartin/data/wordpress
	mkdir -p /home/nmartin/data/mariadb
	docker compose -f srcs/docker-compose.yml up -d --build

down:
	docker compose -f srcs/docker-compose.yml down

clean: down
	docker system prune -af

fclean: clean
	rm -rf /home/nmartin/data/wordpress/*
	rm -rf /home/nmartin/data/mariadb/*

re: fclean all