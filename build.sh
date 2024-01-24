#!/bin/sh
# delete all containers and images 

# docker rm -vf $(docker ps -aq)
# docker rmi -f $(docker images -aq)

# build a container
docker build . -t dash