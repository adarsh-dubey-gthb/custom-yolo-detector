import cv2
from ultralytics import YOLO

model_path = r'C:\Users\Admin\runs\detect\yolov8n_custom5\weights\best.pt'
model = YOLO(model_path)


image_path = r'C:\Users\Admin\Downloads\raimond-klavins-uAk731NvaJo-unsplash.jpg' 

results = model(image_path)

annotated_image = results[0].plot()

cv2.imshow("Custom Detection", annotated_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()