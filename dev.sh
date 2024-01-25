#!/bin/sh
# adding bash at the end to override the docker CMD

docker rm -vf $(docker ps -aq)

docker run -it  --env DATABASE_URL=$DATABASE_URL -v $HOME/baylek:/baylek -p 8050:8050 -p 8888:8888  --name dev dash bash




