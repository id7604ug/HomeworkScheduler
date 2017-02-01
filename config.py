# This file sets up part of sqlalchemy
DEBUG = False     # Turns logging features on for code. Separate to the in-browser debugger and code-relaucher.
SQLALCHEMY_DATABASE_URI = 'sqlite:///schedule.db'   # /// relative path to this app.    # //// absolute path to somewhere on file system
SECRET_KEY = 'sEcReTkEy'
SEND_FILE_MAX_AGE_DEFAULT = 30 # How long to cache static files for. Working??
