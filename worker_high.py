from redis import Redis
from rq import Queue, Worker

Q = "high"
NAME = f"{Q}-worker"

redis_connection = Redis(host="localhost", port=5379, db=0)
q = Queue(Q, connection=redis_connection)
w = Worker([q], connection=redis_connection, name=NAME)
w.work()
