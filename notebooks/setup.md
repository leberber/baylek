### running jupyter lab from container
When starting the container expose port 8888 `-p 8888:8888` and execute

```jupyter lab --ip 0.0.0.0 --port 8888 --no-browser --allow-root```

### generate prisma schema
```notebooks# prisma generate --schema=./../prisma/schema.prisma```



