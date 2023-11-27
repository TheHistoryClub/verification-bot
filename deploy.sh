#!/bin/bash
echo "Starting the container"
docker run -d verfication-bot
sleep 60
echo "Sending SIGKILL to container"
docker stop --signal SIGKILL verfication-bot
