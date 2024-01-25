#!/bin/sh
# adding bash at the end to override the docker CMD

docker rm -vf $(docker ps -aq)

docker run -it -v $HOME/baylek:/baylek  -p 8050:8050 --name dev dash bash




