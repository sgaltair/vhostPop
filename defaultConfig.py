# General config.
DEFAULT_HOST = "example.com"
DEFAULT_VHOST_TEXT = 'proxy_set_header Upgrade $http_upgrade;\nproxy_set_header Connection "upgrade";\nproxy_http_version 1.1;'
TIMESTAMP_FORMAT = "%Y/%m/%d %H:%M: "
LINODE_INTEGRATION = False

# Linode integration config. Only applies if LINODE_INTEGRATION == True.
if LINODE_INTEGRATION == True:
    API_KEY = ""  # Your personal access token from Linode
    DOMAIN_ID = 2278333  # You can find this in the url on the domains page for a domain: https://cloud.linode.com/domains/#######
    TARGET_IP = ""  # The IP of the target host (probably the IP of your Linode server)

# You probably want to leave these alone, as they're integral to the function of the scripts. 
# Paths should be relative to the parent directory. All paths are addressed as ../PATH
CONTAINERS_PATH = "containers"
VHOSTD_PATH = "containers/nginx/vhost.d"
LOG_FILE_PATH = "vhost_pop_logs.log"