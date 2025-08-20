for creating docker file:
FROM baseimage
WORKDIR / dirname
COPY source dest
# example: install dependencies or set environment
RUN some-command
CMD ["python", "app.py"]

build docker image:  (single file with all the dep and lib to run the program)
docker build .

list all docker images:
docker image ls
<!-- docker run (image id) -->
build image:
docker build -t mynginx

run container:
docker run -d -p 8080:80 mynginx

docker ps: for current running container with all of its detail
docker stop container_name : to stop container

running container in detavhed mode:
docker run -d -p 8080:80 mynginx (-d--> detached mode)

useful info for container management:
docker ps -a : list all containers
docker rm container_name: to remove a container
docker run -d --rm -p 8083:80 mynginx: when container stops it removes automaticaly (--rm)
docker run -d --rm --name "desired_name" -p 8083:80 mynginx :for giving container desired name

managing docker images:
docker build -t tag_name:version : for tagging image

deleting image:
docker rmi image_name:version : for deleting image
docker image image_id : 
