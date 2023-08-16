import re
from rq import SimpleWorker

from task_about_it.main import submit_job, high
from task_about_it.worker import start_worker

from task_about_it.lib.tasks import process_user

def test_submit_job(capsys):
    submit_job(high, process_user, "Matt Cale")
    captured_a = capsys.readouterr()
    assert captured_a.out == "Result status is: queued\n"
    start_worker("high", worker_class=SimpleWorker, burst=True)
    captured_b = capsys.readouterr()
    print(captured_b)
    assert re.search("Execution time for processing user: Matt Cale was:", captured_b.out)