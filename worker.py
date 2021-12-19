from os import environ

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import redis
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = environ.get('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        print(conn)
        worker = Worker(list(map(Queue, listen)))
        worker.work()
