### add a user to the docker groups
``` sudo usermod -aG docker ${USER} ```

### used disc space
```du -hs * | sort -rh | head -10```


### find if a port is being used
```netstat -ano | grep 443```