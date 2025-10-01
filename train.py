from ultralytics import YOLO

# Load a pre-trained model
# We use a pre-trained model like 'yolov8n.pt' (nano version) to leverage transfer learning.
# This model has already learned basic features from a large dataset (COCO).
model = YOLO('yolov8n.pt')

# Train the model using your custom dataset
def main():
    results = model.train(
        data='D:/gfg/custom_yolo_detector/dataset/data.yaml',  # Path to your data.yaml file
        epochs=100,          # Number of training epochs (cycles through the entire dataset)
        imgsz=640,           # Image size for training
        name='yolov8n_custom' # Name of the experiment folder
    )

if __name__ == '__main__':
    main()