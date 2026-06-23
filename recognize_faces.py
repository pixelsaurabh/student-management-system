import cv2
import numpy as np
from config import CAMERA_INDEX

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

        # Convert label to name
        name = label_map.get(label, "Unknown")

        # Confidence control
        if confidence < 80:
            display_text = f"{name}"
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