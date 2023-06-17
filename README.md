# Compose File Vhost Creator

This image is designed to be run alongside the nginxproxy/nginx-proxy Docker container. It recursively checks a target directory for compose files with a VIRTUAL_HOST environment variable and creates the corresponding vhost file in the target vhost directory. It also has the option to create a Linode domain record if the `LINODE_INTEGRATION` flag is set to `True`.

## Usage

A default config file has been provided to you. Please copy this file from `defaultConfig.py` to `vhostPopConfig.py` and edit it.

1. Make sure you have the necessary prerequisites installed.
2. Set the `LINODE_INTEGRATION` flag to `True` if you want to enable Linode domain record creation. Set it to `False` if not needed.
    - If you do choose Linode API integration:
      - You'll need to create a personal access token.
      - You'll need to set the appropriate variables in `vhostPopConfig`.
3. Run the script.

### Docker compose
A sample compose file has been provided. 

## Functionality
- Writes the default initial host file if it doesn't exist.
- Checks for the `VIRTUAL_HOST` environment variable in all found compose files.
- If a `VIRTUAL_HOST` is present and the corresponding vhost file doesn't exist, it creates it using the default.
- If `LINODE_INTEGRATION` is enabled, it attempts to create the Linode domain record for the vhost.
