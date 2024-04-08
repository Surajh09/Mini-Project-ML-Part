import cv2
import numpy as np
import os

def Recognizer(details):
    video = cv2.VideoCapture(0)

    # Load the pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    known_face_names = []
    known_face_paths = []

    # Construct image directory path
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images', 'Student_Images', details['branch'], details['year'], details['section'])

    # Load known face names and paths
    for root, _, files in os.walk(image_dir):
        for file in files:
            if file.endswith('jpg') or file.endswith('png'):
                known_face_names.append(file[:len(file) - 4])
                known_face_paths.append(os.path.join(root, file))

    names = []

    while True:
        check, frame = video.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Draw rectangle around detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Crop the face region
            face_region = frame[y:y+h, x:x+w]

            # Perform face recognition using some method (e.g., compare with known faces)
            matched_name = recognize_face(face_region, known_face_paths, known_face_names)

            names.append(matched_name)

            # Put the recognized name on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, matched_name, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Face Recognition Panel', frame)

        if cv2.waitKey(1) == ord('s'):
            break

    video.release()
    cv2.destroyAllWindows()
    return names

def recognize_face(face_region, known_face_paths, known_face_names):
    return np.random.choice(known_face_names)
