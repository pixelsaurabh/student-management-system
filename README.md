# Student Management System

A Python-based Student Management System with Face Recognition Attendance.

## Features

- Face registration
- Face model training
- Automatic attendance marking
- Attendance stored in CSV
- Prevents duplicate attendance

## Technologies Used

- Python
- OpenCV
- NumPy

## Project Structure

student_management_system/

│

├── attendance/

│ └── attendance.csv

│

├── data/

├── face_model.yml

├── labels.npy

├── capture_faces.py

├── train_model.py

├── recognize_faces.py

├── attendance_system.py

## How to Run

### Capture Faces

```bash
python capture_faces.py
```

### Train Model

```bash
python train_model.py
```

### Recognize Faces

```bash
python recognize_faces.py
```

### Mark Attendance

```bash
python attendance_system.py
```


---
