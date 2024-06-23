# Video Frame Extractor Guide

This guide will help you extract frames from a video using Docker and a simple Python script. Follow the steps below to get started.

## Prerequisites

1. **Docker**: Ensure Docker is installed on your machine. You can download and install Docker from [here](https://www.docker.com/get-started).
2. **Git**: Ensure Git is installed on your machine. You can download and install Git from [here](https://git-scm.com/).

## Setup

### 1. Clone the Repository

Open a terminal (or command prompt) and run the following command to clone the repository:

```sh
git clone https://github.com/VittuD/custom_frame_extractor.git
```

This will create a directory named `custom_frame_extractor`.

### 2. Navigate to the Directory

Navigate to the `custom_frame_extractor` directory:

```sh
cd custom_frame_extractor
```

### 3. Directory Structure

Ensure your directory structure looks like this:

```
custom_frame_extractor/
├── Dockerfile
├── requirements.txt
├── extract_frames.py
├── run_extraction.sh
├── input_videos/
└── output_frames/
└── ...
```

- **input_videos**: This folder will contain the videos you want to process.
- **output_frames**: This folder will store the extracted frames.

## Using the Frame Extractor

### 1. Place Your Video in the Input Folder

Copy the video file you want to process into the `input_videos` folder. For example, if your video file is named `example.mp4`, place it inside the `input_videos` directory.

### 2. Run the Extraction Script

Open a terminal (or command prompt) and ensure you are in the `custom_frame_extractor` directory. Then, run the extraction script with the name of your video file.

```sh
sh run_extraction.sh example.mp4
```

Replace `example.mp4` with the name of your video file.

### 3. View the Extracted Frames

After the script completes, you will find the extracted frames inside the `output_frames` folder. The frames will be stored in a subfolder named after your video file (without the extension).

For example:
```
output_frames/
└── example/
    ├── frame0000.jpg
    ├── frame0001.jpg
    ├── frame0002.jpg
    └── ...
```

# Updating the Repository

If there are updates to the repository, follow these steps to ensure you have the latest version of the scripts and other files.

## Steps to Update

1. **Navigate to the Local Repository**:
   - Open a terminal and navigate to the local repository directory.
     ```sh
     cd path_to_your_local_repository
     ```

2. **Pull the Latest Changes**:
   - Fetch and merge the latest changes from the remote repository.
     ```sh
     git pull origin main
     ```

3. **Pull the Latest Docker Image** (if necessary):
   - If there were changes to the `Dockerfile` or other dependencies, pull the new Docker image.
     ```sh
     docker pull davidevitturini/frame-extractor
     ```
     
## Troubleshooting

### Common Issues

1. **Docker Not Installed**: Ensure Docker is installed and running on your machine.
2. **File Not Found**: Make sure the video file name is correct and placed in the `input_videos` folder.
3. **Permissions**: You might need to run the terminal or command prompt with administrative privileges.
4. **Cannot Execute 'run_extraction.sh'**: Make sure the `run_extraction.sh` script has execute permissions. You can set this by running:

```sh
chmod +x run_extraction.sh
``` 

### Getting Help

If you encounter any issues or have questions, please reach out to [my institutional email](mailto:davide.vitturini@edu.unito.it) or refer to the Docker documentation for troubleshooting tips.
