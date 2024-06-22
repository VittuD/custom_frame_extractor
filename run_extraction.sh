#!/bin/sh
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <video_file_name> <container_name>"
    exit 1
fi

VIDEO_FILE_NAME=$1
CONTAINER_NAME=$2

# Check if the container already exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Container $CONTAINER_NAME already exists. Starting and attaching to the existing container."
    docker start $CONTAINER_NAME
    docker exec $CONTAINER_NAME /bin/bash -c "export VIDEO_FILE_NAME=$VIDEO_FILE_NAME; python extract_frames.py"
else
    echo "Creating and starting a new container named $CONTAINER_NAME."
    docker run --name $CONTAINER_NAME -e VIDEO_FILE_NAME="$VIDEO_FILE_NAME" -d -v $(pwd)/input_videos:/app/input_videos -v $(pwd)/output_frames:/app/output_frames davidevitturini/frame-extractor
    docker exec $CONTAINER_NAME python extract_frames.py
fi
exit 0
