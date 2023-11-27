#!/bin/bash
docker run myapp:latest
sleep 60
docker stop --signal SIGKILL myapp:latest
