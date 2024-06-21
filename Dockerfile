FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY extract_frames.py extract_frames.py

# Create a directory for input videos
RUN mkdir /app/input_videos

# Set the default command to run the Python script with arguments
ENTRYPOINT ["python", "extract_frames.py"]
