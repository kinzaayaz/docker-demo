# Docker Notes

## Dockerfile + Commands + Volumes

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
docker build -t tag_name:version .   # for tagging image

# Deleting images
docker rmi image_name:version
docker rmi image_id


# Run container
docker run -d -p 8080:80 mynginx

# Show running containers
docker ps   # current running containers with details

# Stop a container
docker stop container_name

# Running container in detached mode
docker run -d -p 8080:80 mynginx   # -d --> detached mode(background)

# Useful info for container management
docker ps -a                                # list all containers
docker rm container_name                    # remove a container
docker run -d --rm -p 8083:80 mynginx       # auto-remove container when it stops
docker run -d --rm --name desired_name -p 8083:80 mynginx   # give container desired name

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

# ---------------- push,pull images ----------------

#push image in docker hub
create repo in dockerhub
docker login in terminal
create image 
docker push image_name:tagname

#pull image remotely
docker pull image_name:tagname

# ---------------- rename image ----------------

#rename image
docker tag older image_name:version new image_name:tag


# ---------------- Docker Volumes ----------------

# Create a Volume in a Container
docker run -it --rm -v volumename:/directoryname/ image_id

# Volume Management Commands
docker volume --help              # shows all subcommands
docker volume ls                  # list all volumes
docker volume inspect volumename  # inspect a volume
docker volume rm volumename       # remove a volume

# ---------------- Mount Objects (Bind Mounts) ----------------

# Run container with mount
docker run --rm -v "absolute_path:/directoryname/filename" myapp:02

# ---------------- .dockerignore ----------------

# Add all files you don’t want copied into Docker image
*.log
*.tmp
node_modules
__pycache__/
