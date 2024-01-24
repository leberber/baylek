#!/bin/sh

docker run --rm  -it \
    -v /home/ubuntu/fullchain.pem:/fullchain.pem \
    -v /home/ubuntu/privkey.pem:/privkey.pem \
    -p 443:443 --name prd dash 


