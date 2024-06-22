FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libgl1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY extract_frames.py extract_frames.py

# Create directories for input videos and output frames
RUN mkdir /app/input_videos
RUN mkdir /app/output_frames

# Set the default command to run the Python script with arguments
ENTRYPOINT ["python", "extract_frames.py"]
