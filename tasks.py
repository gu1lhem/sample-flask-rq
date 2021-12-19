import logging

# Import the time module to include some time delay in the application
import time
logger = logging.getLogger(__name__)

# Create a working task queue
def task_in_background(t):
    # print goes into the runner's sysout, logger goes into the log file.
    print('Started task_in_background.py!')
    logger.info('Started task_in_background.py!')
    delay = 1
    print("Running Task")
    print(f"Simulates the {delay} seconds")

    time.sleep(delay)
    print(len(t))
    print("Completed Task")
    
    return len(t)