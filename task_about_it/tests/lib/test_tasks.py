import re
from task_about_it.lib.tasks import process_user

def test_process_user(capsys):
    process_user("Matt Cale")
    captured = capsys.readouterr()
    match = re.search("Execution time for processing user: Matt Cale", captured.out)
    assert match, "expected output not found in stdout"