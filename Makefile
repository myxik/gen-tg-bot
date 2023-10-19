build-db:
	docker build -f server/Dockerfile.db -t postgresdb .

build-server:
	docker build -f server/Dockerfile.server -t server .

build-image-server:
	docker build -f image_gen/Dockerfile.gen -t image_server .

run-server:
	docker run --rm -it --net=host -v images:/images --name=server server

run-db:
	docker run --rm -it -p 5432:5432 --name=db postgresdb

run-image-server:
	docker run --rm -it --gpus all --net=host --name=image_server image_server