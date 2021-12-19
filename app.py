# Import the flask module for the application
from flask import Flask, request

# Import the redis module for the application
import redis
from rq import Queue

# Create the application directory
app = Flask(__name__)

# Make a connection of the queue and redis
r = redis.Redis()
q = Queue(connection=r)

# Logging
import logging.config
from logsetup import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
logger.warning('Started app.py!')

from tasks import task_in_background

@app.route("/task")
def add_task():
    if request.args.get("n"):
        job = q.enqueue(task_in_background, request.args.get("n"))
        q_len = len(q)
        print(job)
        return f"The task {job.id} is added into the task queue at {job.enqueued_at}. {q_len} task in the queue"

    return "Add a task by specifing n=something"
 
if __name__ == "__main__":
    app.run()
