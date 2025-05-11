# Gunicorn configuration file
import multiprocessing

# Bind to 0.0.0.0:8000
bind = "127.0.0.1:5000"

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Set timeout to 60 seconds
timeout = 60

# Enable access logging
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log errors to stdout
loglevel = "info"

# Preload the application
preload_app = True 