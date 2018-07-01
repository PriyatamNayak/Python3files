import logging
import sys
print(sys.version)
#print(dir(logging))
try:
	log_format = "%(levelname)s %(asctime)s : %(message)s"
	logging.basicConfig(filename = "logging_test.log",
						level = logging.DEBUG,
						format = log_format,
						#filemode = "w", can be changed to write,read, read binary, write binary, append binary  default: append mode
						)
	logger = logging.getLogger()
	logger.info("logging files")
	print("logger level: {}".format(logger.level))
	print("logged successfully")
except:
	raise
#NOTSET = 0
#DEBUG = 10
#INFO = 20
#WARNING = 30
#ERROR = 40
#CRITICAL = 50
