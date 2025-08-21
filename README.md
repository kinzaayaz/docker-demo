# Docker Notes

## Dockerfile + Commands
```bash
# ---------------- Dockerfile Example ----------------
FROM baseimage
WORKDIR /dirname
COPY source dest
# example: install dependencies or set environment
RUN some-command
CMD ["python", "app.py"]

# ---------------- Docker Commands ----------------

# Build Docker image (single file with all the dep and lib to run the program)
docker build .

# List all docker images
docker image ls

# Build image with tag
docker build -t mynginx .

# Run container
docker run -d -p 8080:80 mynginx

# Show running containers
docker ps   # current running containers with details

# Stop a container
docker stop container_name

# Running container in detached mode
docker run -d -p 8080:80 mynginx   # -d --> detached mode

# Useful info for container management
docker ps -a                                # list all containers
docker rm container_name                    # remove a container
docker run -d --rm -p 8083:80 mynginx       # auto-remove container when it stops
docker run -d --rm --name desired_name -p 8083:80 mynginx   # give container desired name

# Managing docker images
docker build -t tag_name:version .   # for tagging image

# Deleting images
docker rmi image_name:version
docker rmi image_id

#update project
create image 
docker run -d --rm --name "index" -p 8081:80 index:01

#predefine images
docker pull image_name
(or)
docker pull image_name:version
docker run -p port image_name:version

#docker container with interactive mode
docker run -it image_id

#push image in docker hub
create repo in dockerhub
docker login in terminal
create image 
docker push image_name:tagname

#rename image
docker tag older image_name:version new image_name:tag

#pull image remotely
docker pull image_name:tagname