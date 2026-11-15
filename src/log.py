from datetime import datetime
#1 Record when an analysis occurs
from src.config import LOG

def log_analysis():
    x = datetime.now()
    log_time = x.strftime("%H-%M-%S  %b-%d-%Y")
    message = f"\nanalysis logged: {log_time}"
    with open(LOG, mode="a") as log:
        log.write(message)
