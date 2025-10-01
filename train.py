from ultralytics import YOLO


model = YOLO('yolov8n.pt')

def main():
    results = model.train(
        data='D:/gfg/custom_yolo_detector/dataset/data.yaml',  
        epochs=100,         
        imgsz=640,          
        name='yolov8n_custom' 
    )

if __name__ == '__main__':
    main()
