import cv2
import numpy as np

from attendance_system import mark_attendance
from config import CAMERA_INDEX

marked_students = set()

cap = cv2.VideoCapture(CAMERA_INDEX)

# Load trained model
model = cv2.face.LBPHFaceRecognizer_create()
model.read("face_model.yml")

# Load labels
label_map = np.load("labels.npy", allow_pickle=True).item()

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]

        # Resize (same as training)
        face = cv2.resize(face, (200, 200))

        label, confidence = model.predict(face)
        cv2.putText(frame,
            f"{label_map.get(label)} {confidence:.2f}",
            (x, y-40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2)

        if confidence < 50:
            name = label_map.get(label, "Unknown")
            display_text = name

            # Mark attendance automatically
            if name not in marked_students:
                mark_attendance(name)
                marked_students.add(name)

        else:
            display_text = "Unknown"

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Show name
        cv2.putText(frame, display_text, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()