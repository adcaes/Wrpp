import logging
from config import *

def loggerInit(appId):
	logger = logging.getLogger(str(appId))
	hdlr = logging.FileHandler(LOGGING_FILE + str(appId))
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr) 
	logger.setLevel(LOGGING_LEVEL)
	return logger
