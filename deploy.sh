#!/bin/bash
echo "Starting the container"
docker run myapp:latest
sleep 60
echo "Sending SIGKILL to container"
docker stop --signal SIGKILL myapp:latest
