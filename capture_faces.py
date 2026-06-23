import cv2
import os
from config import CAMERA_INDEX

cap = cv2.VideoCapture(CAMERA_INDEX)

# Ask student name
name = input("Enter student name: ")

# Create folder for student
dataset_path = "data"
student_path = os.path.join(dataset_path, name)

if not os.path.exists(student_path):
    os.makedirs(student_path)

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1

        face = frame[y:y+h, x:x+w]

        file_name = os.path.join(student_path, f"{count}.jpg")
        cv2.imwrite(file_name, face)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Capturing Faces", frame)

    # Stop after 50 images OR press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
        break

cap.release()
cv2.destroyAllWindows()

print(f"{count} images saved for {name}")