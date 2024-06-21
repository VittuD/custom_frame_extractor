# run_extraction.sh
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <video_file_name>"
    exit 1
fi

docker run -v $(pwd)/input_videos:/app/input_videos -v $(pwd)/output_frames:/app/frames your_dockerhub_username/video-frame-extractor "$1"
