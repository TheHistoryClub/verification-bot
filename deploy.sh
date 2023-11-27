#!/bin/bash
echo "Starting the container"
docker run --name bot -d verfication-bot
sleep 21480
echo "Sending SIGKILL to container"
docker stop --signal SIGKILL bot
