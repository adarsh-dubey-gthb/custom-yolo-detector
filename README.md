# Custom Object Detector using YOLOv8
Visit this link to see the video demonstration - https://notebooklm.google.com/notebook/4a62bfc1-020a-49e6-975c-153eddfa9162?artifactId=c3f1ff51-e0b9-4689-9f75-ce665ac6dd69
This project is a practical demonstration of fine-tuning a pre-trained **YOLOv8** model to detect custom objects. The model is trained on a small, custom dataset to identify specific items, showcasing the entire workflow from data annotation to inference.




---

## 📋 Table of Contents
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Dataset](#-dataset)
- [Setup and Installation](#-setup-and-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)

---

## ✨ Features
- Utilizes the state-of-the-art YOLOv8 model for object detection.
- Demonstrates transfer learning by fine-tuning a pre-trained model.
- Includes clear scripts for both training (`train.py`) and prediction (`predict.py`).
- Complete workflow from data preparation to running live inference.

---

## 🛠️ Technologies Used
- **Python 3.10+**
- **PyTorch**
- **Ultralytics YOLOv8**
- **OpenCV**
- **LabelImg** (for annotation)

---

## 🖼️ Dataset
The model was trained on a small, custom-annotated dataset. The goal is to detect the following 5 classes:

- `balloon`
- `icecream`
- `coffee_setup`
- `rose`
- `rubiks_cube`

The dataset is structured in the required YOLO format, with separate folders for training and validation images and their corresponding label files.

---

## ⚙️ Setup and Installation

Follow these steps to set up the project locally.

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/custom-yolo-detector.git](https://github.com/your-username/custom-yolo-detector.git)
cd custom-yolo-detector
