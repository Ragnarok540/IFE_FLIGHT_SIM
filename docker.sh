#!/bin/bash
# exec docker for the backend

docker build -t edgar/ife-flight-sim .

docker run -p 5000:5000 edgar/ife-flight-sim:latest
