# Traffic Analysis using YoloV8 & ByteTrack

This script performs traffic flow analysis using YOLOv8, an object-detection method and
ByteTrack, a simple yet effective online multi-object tracking method. It uses the
supervision package for multiple tasks such as tracking, annotations, etc.

https://github.com/roboflow/supervision/assets/26109316/c9436828-9fbf-4c25-ae8c-60e9c81b3900

<br>

## 💻 Install

- The project uses poetry for dependecy management. 
- Set up poetry and run the command below to install required dependencies
    ```bash
    poetry install
    ```

- Active the virtual environment
    ```bash
    source .venv/bin/activate
    ```

- Download `traffic_analysis.pt` and `traffic_analysis.mov` files

    ```bash
    ./setup.sh
    ```

<br>

## 🛠️ Script Arguments

- Ultralytics

    - `--source_weights_path`: Required. Specifies the path to the YOLO model's weights
        file, which is essential for the object detection process. This file contains the
        data that the model uses to identify objects in the video.

    - `--source_video_path`: Required. The path to the source video file that will be
        analyzed. This is the input video on which traffic flow analysis will be performed.

    - `--target_video_path` (optional): The path to save the output video with
        annotations. If not specified, the processed video will be displayed in real-time
        without being saved.

    - `--confidence_threshold` (optional): Sets the confidence threshold for the YOLO
        model to filter detections. Default is `0.3`. This determines how confident the
        model should be to recognize an object in the video.

    - `--iou_threshold` (optional): Specifies the IOU (Intersection Over Union) threshold
        for the model. Default is 0.7. This value is used to manage object detection
        accuracy, particularly in distinguishing between different objects.

<br>

## ⚙️ Run

- Ultralytics

    ```bash
    poetry run python3.9 main.py \
        --source_weights_path data/traffic_analysis.pt \
        --source_video_path data/traffic_analysis.mov \
        --confidence_threshold 0.3 \
        --iou_threshold 0.5 \
        --target_video_path data/traffic_analysis_result.mov
    ```
