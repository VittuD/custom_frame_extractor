import cv2
import numpy as np
import heapq
import os
import sys

def manage_heap(diff_heap, frame, diff, n):
    """
    Manages a min heap to keep track of the top n frames with the highest difference.
    
    Parameters:
    - diff_heap: A list that is used as a min heap.
    - frame: The current frame being processed.
    - diff: The difference between the current frame and the previous frame.
    - n: The number of top differences to keep in the heap.
    
    Returns:
    - The updated heap.
    """
    heapq.heappush(diff_heap, (diff.mean(), frame))
    while len(diff_heap) > n:
        heapq.heappop(diff_heap)
    return diff_heap

def shot_boundary_detection(video_path, n):
    """
    Detects shot boundaries in a video and returns the frames at those boundaries.
    
    Parameters:
    - video_path: Path to the video file.
    - n: The number of frames to return, based on the highest frame differences.
    
    Returns:
    - A list of frames that are at the detected shot boundaries.
    """
    # Check if the video file exists and is not empty
    if not os.path.exists(video_path) or os.path.getsize(video_path) == 0:
        print(f"Error: Video file does not exist or is empty at path {video_path}")
        return []

    print(f"Analyzing video for shot boundaries: {video_path}")
    shots = []
    cap = cv2.VideoCapture(video_path)
    prev_frame = None
    diff_heap = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print('End of video. Processing complete.')
            break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, frame_gray)
            diff_heap = manage_heap(diff_heap, frame, diff, n)
        prev_frame = frame_gray
    
    cap.release()
    
    shots = [frame for _, frame in diff_heap]
    shots.reverse()  # Reverse to get the frames in the order they appear in the video
    print(f"Found {len(shots)} shot boundaries.")
    return shots

# Main usage example
if __name__ == "__main__":
    
    video_file_name = os.getenv('VIDEO_FILE_NAME')

    if video_file_name == None:
        print("External Usage: set VIDEO_FILE_NAME env variable and run the script.")
        sys.exit(1)
    
    video_path = f'/app/input_videos/{video_file_name}'
    output_dir = '/app/output_frames'
    
    print(f"Preparing to extract frames from {video_file_name}...")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory at {output_dir}")
    
    shots = shot_boundary_detection(video_path, n=18)
    
    for i, frame in enumerate(shots):
        frame_path = os.path.join(output_dir, f'frame_{i}_{video_file_name}.jpg')
        cv2.imwrite(frame_path, frame)
        print(f"Saved frame {i} to {frame_path}")
    exit(0)
        