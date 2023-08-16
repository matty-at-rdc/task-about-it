import sys
import argparse

from redis import Redis
from rq import Queue, Worker

def start_worker(queue_name, worker_class=Worker, burst=False):
    worker_name = f"{queue_name}-worker"

    redis_connection = Redis(host="localhost", port=5379, db=0)
    q = Queue(queue_name, connection=redis_connection)
    w = worker_class([q], connection=redis_connection, name=worker_name)
    w.work(burst=burst)


def main():
    parser = argparse.ArgumentParser(description='This is a simple RQ worker program that creates a worker for the supplied RQ queue name')
    parser.add_argument('name', type=str, help='The queue you wish the worker to consume from')

    args = parser.parse_args()
    name = args.name

    print(f"Name provided was: {name}")

    if name not in ("high", "medium", "low"):
        sys.exit(1)
    else:
        start_worker(name)
        
if __name__ == "__main__":
    main()