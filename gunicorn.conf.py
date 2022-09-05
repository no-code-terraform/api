import os

import tfmaker

wsgi_app = 'tfmaker.wsgi:application'

#
# Server Socket
# https://docs.gunicorn.org/en/latest/settings.html#server-socket
#

bind = f"{os.environ.get('WSGI_HOST', '127.0.0.1')}:{os.environ.get('WSGI_PORT', '8000')}"
backlog = 2048

#
# Worker Processes
# https://docs.gunicorn.org/en/latest/settings.html#worker-processes
#

workers = 1
worker_class = 'sync'
threads = 1
worker_connections = 1000
max_requests = 0
max_requests_jitter = 0
timeout = 30
graceful_timeout = 30
keepalive = 2

#
# Debugging
# https://docs.gunicorn.org/en/latest/settings.html#debugging
#

spew = False
check_config = False
print_config = False

#
# Logging
# https://docs.gunicorn.org/en/latest/settings.html#logging
#

accesslog = '-'
errorlog = '-'
loglevel = 'critical'

#
# Process Naming
# https://docs.gunicorn.org/en/latest/settings.html#process-naming
#

proc_name = 'gunicorn_tfmaker'
default_proc_name = 'gunicorn'

#
# Security
# https://docs.gunicorn.org/en/latest/settings.html#security
#

limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

#
# Server mechanics
# https://docs.gunicorn.org/en/latest/settings.html#server-hooks
#

daemon = False
raw_env = [
    'DJANGO_SETTINGS_MODULE=tfmaker.settings',
]
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None


#
# Server Hooks
# https://docs.gunicorn.org/en/stable/settings.html#server-hooks
#

def on_starting(server):
    tfmaker.bootstrap()
