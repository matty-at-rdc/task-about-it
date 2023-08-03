import json
import argparse

from redis import Redis
from rq import Queue
from faker import Faker

from lib.tasks import process_user

fake = Faker()
redis_connection = Redis(host="localhost", port=5379, db=0)

high = Queue("high", connection=redis_connection)
medium = Queue("medium", connection=redis_connection)
low = Queue("low", connection=redis_connection)


def get_user():
    first_name = fake.first_name()
    last_name = fake.last_name()
    return f"{first_name} {last_name}"


def submit_job(q, func, func_args):
    result = q.enqueue(func, func_args)
    print(f"Result status is: {result.get_status()}")



def simulate_traffic():
    print("Will create 30 tasks for RQ workers to process on 3 different queues...")
    for _ in range(10):
        submit_job(high, process_user, get_user())
    for _ in range(10):
        submit_job(medium, process_user, get_user())
    for _ in range(10):
        submit_job(low, process_user, get_user())


def get_queue_info(q):
    return q.get_job_ids()


def get_all_queues_info():
    high_jobs = get_queue_info(high)
    medium_jobs = get_queue_info(medium)
    low_jobs = get_queue_info(low)

    print("All high queue jobs:")
    [print(j_id) for j_id in high_jobs]
    
    print("All medium queue jobs:")
    [print(j_id) for j_id in medium_jobs]
    
    print("All low queue jobs:")
    [print(j_id) for j_id in low_jobs]


def main():
    parser = argparse.ArgumentParser(description='This is a simple program that demonstrates some of what RQ can do!')
    parser.add_argument('command', type=str, help='The command you wish to run')

    args = parser.parse_args()
    command = args.command

    print(f"Command was: {command}")

    if command == "simulate":
        simulate_traffic()
    elif command == "info":
        get_all_queues_info()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()


# _job_id = "413f1153-5e09-481c-9cc5-c817efd39d00"
# print("\n\nLet's get the ID of a job and get some information about it...")
# print(f"I'm going use ID: {_job_id}, but beware that after I process this job this code may fail!")
# fetched_job = q.fetch_job(_job_id)
# print(f"The description for the job with id {_job_id} is: {fetched_job.to_dict()['description']}")
