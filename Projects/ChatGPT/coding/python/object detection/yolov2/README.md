# YOLOv3 Object Detection

This repository contains scripts and resources for performing object detection using the YOLOv3 model with OpenCV. It includes pre-trained weights, configuration files, class labels, and a script to process and detect objects in images from a specified directory.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/visibly0ptimistic/Codecademy/tree/main/Projects/ChatGPT/coding/python/object%20detection/yolov2
    cd yolov3-object-detection
    ```

2. Install the required Python packages:

    ```sh
    pip install opencv-python numpy
    ```

3. Ensure that the `yolov3.weights`, `yolov3.cfg`, and `coco.names` files are present in the directory.

Download the necessary files:
yolov3.weights: <https://pjreddie.com/media/files/yolov3.weights>
yolov3.cfg: <https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg>
coco.names: <https://github.com/pjreddie/darknet/blob/master/data/coco.names>

## Usage

1. Place your input images in the `images` directory. The script supports images with `.jpeg`, `.jpg`, and `.png` extensions.

2. Run the detection script:

    ```sh
    python detect.py
    ```

3. The script will process each image in the `images` directory, perform object detection, and display the results with bounding boxes and labels.

## Customization

- **Confidence Threshold:** The confidence threshold for detecting objects is set to 0.3. You can adjust this value in the script to control the sensitivity of detections.

- **NMS Threshold:** The Non-Maximum Suppression (NMS) threshold is set to 0.3. You can adjust this value in the script to control the overlap of bounding boxes.

- **Bounding Box Color:** The color of the bounding boxes and labels is set to cyan. You can change this color in the script by modifying the `color` variable.

## Example

Here's an example of running the detection script and the output:

1. Place an image (`example.jpg`) in the `images` directory.
2. Run the detection script:

    ```sh
    python detect.py
    ```

3. The script will display the image with detected objects, bounding boxes, and labels.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
