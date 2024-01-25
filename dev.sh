#!/bin/sh
# adding bash at the end to override the docker CMD

docker rm -vf $(docker ps -aq)

docker run -it -p 5432:5432 --name dev dash bash




