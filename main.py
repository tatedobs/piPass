import datetime
import time
from example_search import search
import sys
from id_manager import clear_status
from send import send_attendance

clear_time = datetime.time(7, 48, 0)
start = datetime.time(7, 50, 0)
end_of_first = datetime.time(8, 0, 0)
end_of_tardy = datetime.time(8, 10, 0)

def run_search():
    if(datetime.datetime.now().time() >= clear_time and datetime.datetime.now().time() <= start):
	clear_status()
	time.sleep(120)
    while(datetime.datetime.now().time() >= start and datetime.datetime.now().time() <= end_of_first):
	try:
            search(0)
	    print('present') 
	except KeyboardInterrupt:
	    exit(0)
	except:
	    print('error')
        time.sleep(1)

    while(datetime.datetime.now().time() > end_of_first and datetime.datetime.now().time() <= end_of_tardy):
	try:
  	    search(1)
	    print('tardy')
	except KeyboardInterrupt:
	    exit(0)
	except:
	    print('error')
        time.sleep(1)

    if(datetime.datetime.now().time() > end_of_tardy):
	send_attendance()
	sys.exit()

