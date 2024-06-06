import cv2
import numpy as np
import os

# Load the YOLOv3 model from OpenCV
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load the class labels
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Directory containing images
image_dir = "images"

# Loop through all files in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the input image
        image_path = os.path.join(image_dir, filename)
        image = cv2.imread(image_path)

        # Get the image height and width
        height, width = image.shape[:2]

        # Create a blob from the image
        blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), (0, 0, 0), True, crop=False)

        # Set the input to the network
        net.setInput(blob)

        # Perform the forward pass
        outputs = net.getUnconnectedOutLayersNames()
        layerOutputs = net.forward(outputs)

        # Initialize the bounding boxes, confidences, and class IDs lists
        boxes = []
        confidences = []
        class_ids = []

        # Loop over each output layer
        for output in layerOutputs:
            # Loop over each detection
            for detection in output:
                # Extract the scores, class ID, and confidence
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # Filter out weak predictions
                if confidence > 0.3:  # Lowering the confidence threshold
                    # Scale the bounding box coordinates back to the original image dimensions
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Calculate the bounding box coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    # Append the bounding box coordinates, confidence, and class ID to the respective lists
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Perform non-maximum suppression to eliminate redundant bounding boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.3)  # Adjusting the NMS threshold

        # Draw bounding boxes and labels only if objects were detected
        if len(indices) > 0:
            # Loop over the indices
            for i in indices.flatten():
                # Extract the bounding box coordinates, confidence, and class ID
                box = boxes[i]
                confidence = confidences[i]
                class_id = class_ids[i]

                # Draw the bounding box and label on the image
                x, y, w, h = box
                label = f"{classes[class_id]}: {confidence:.2f}"
                color = (255, 255, 0)
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        else:
            print(f"No objects detected in {filename}.")

        # Display the output image
        cv2.imshow("Output", image)
        cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
