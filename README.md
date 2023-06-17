# Vhost Pop
### Compose File Vhost Creator With Linode API Integration

This image is designed to be run alongside the nginxproxy/nginx-proxy Docker container. It recursively checks a target directory for compose files with a VIRTUAL_HOST environment variable and creates the corresponding vhost file in the target vhost directory. It also has the option to create a Linode domain record if the `LINODE_INTEGRATION` flag is set to `True`.

## Usage

A default config file has been provided to you. Please copy this file from `defaultConfig.py` to `vhostPopConfig.py` and edit it.

### Directory structure
The app assumes a directory structure like this:
```
   .
   |-containers
   |---nginx
   |-----vhost.d
   |---container1
   |-----compose.yml
   |---container3
   |-----compose.yml
   |---container3
   |-----compose.yml
   
```

Where `containers` is where you mount `/app/containers`.

It will find **all** docker-compose.yml or compose.yml files in all directories under this path. 

***The script searches for a string matching `VIRTUAL_HOST=` in compose files.***
On the off chance this string exists for other purposes in any of your compose files, this will break things.

### Docker run
Example:

```
docker run --name vhostPop -d \ 
-v /path/to/containers:/app/containers \
-v /path/to/vhost.d:/app/containers/nginx/vhost.d \
-v /path/to/vhostPopConfig.py:/app/vhostPop/vhostPopConfig.py \
isame/vhostpop:latest
```

### Docker compose
A sample compose file has been provided. After editing it with the appropriate mounts, simply run `docker compose up -d`.

## Functionality
- Writes the default initial host file if it doesn't exist.
- Checks for the `VIRTUAL_HOST` environment variable in all found compose files.
- If a `VIRTUAL_HOST` is present and the corresponding vhost file doesn't exist, it creates it by copying the default.
- If `LINODE_INTEGRATION` is enabled, it attempts to create the Linode domain record for the vhost.
