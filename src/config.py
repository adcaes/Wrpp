import logging

#BASIC
APP_TOP_DIR='/home/adria/Wrpp/'
APP_URL='http://www.wrpp.me/'
LOAD_BALANCER_PORT = 80

#SHORT URL GENERATION
ALPHABET='0123456789abcdefghijklmnopqrstuvwxyz'

#CACHE
MAX_CACHE_ENTRIES = 10

#DB
DB_ADDRESS = ['127.0.0.1:21201', '127.0.0.1:21202']

#LOAD BALANCING 
#Number of Servers can not be bigger than alphabet size
SERVERS = [('127.0.0.1', 8888), ('127.0.0.1', 8889)]
HOST = 0
PORT = 1
PREFIXES = ALPHABET[:len(SERVERS)]

#LOGGING_FILE
LOGGING_FILE = APP_TOP_DIR + '/logs/'
LOGGING_LEVEL = logging.DEBUG  # or (DEBUG, INFO, WARNING, ERROR, CRITICAL).
