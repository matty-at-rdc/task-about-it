# Task About It 📥

## What is it?

It's another demo of how to start using RQ.

## How do I use it?

- Have Poetry
- Have PyEnv
- Install deps in Poetry Venv Shell
- Start Redis `run-redis.sh`
- Add jobs to the RQ queues (`low` `medium` and `high`)
    - `python main.py simulate`
- Inspect the job IDs
    - `python main.py info`
- Process the jobs using RQ workers
    - `python worker.py high`
    - `python worker.py medium`
    - `python worker.py low`