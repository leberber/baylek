#!/bin/sh
# adding bash at the end to override the docker CMD

docker rm -vf $(docker ps -aq)

docker run -it --name dev dash bash




