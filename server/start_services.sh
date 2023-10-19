#!/bin/sh

# Start your bot
python main.py &

# Start RQ worker
rq worker &

# Keep script running
wait
