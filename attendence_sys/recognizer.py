import cv2
import numpy as np


def Recognizer(details):
    video = cv2.VideoCapture(0)

    # Load the pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load known faces and their labels
    known_face_names = []
    known_face_encodings = []

    # Construct image directory path
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images', 'Student_Images', details['branch'], details['year'], details['section'])

    # Load known faces and create encodings
    for root, _, files in os.walk(image_dir):
        for file in files:
            if file.endswith('jpg') or file.endswith('png'):
                label = file[:len(file) - 4]  # Extract name (label) from filename
                known_face_names.append(label)
                img_path = os.path.join(root, file)
                img = cv2.imread(img_path)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Use OpenCV's Eigenfaces for face recognition
                # You might need to train your own Eigenface recognizer
                # Refer to OpenCV documentation for training: https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html
                eigenface = cv2.eigenfaces.EigenFaceRecognizer()
                eigenface.load(f"trained_eigenfaces_{details['branch']}_{details['year']}_{details['section']}.xml")  # Replace with your training file path
                encoding = eigenface.eigenvectors_[eigenface.getEigenValueCount() - 1].reshape((eigenface.getEigenValueCount(),))
                known_face_encodings.append(encoding)

    names = []

    while True:
        check, frame = video.read()

        if not check:
            print("Failed to capture frame from webcam")
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Draw rectangle around detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Crop the face region
            face_region = gray[y:y+h, x:x+w]

            # Reshape the face region for Eigenfaces
            face_region = face_region.reshape(-1, 1)

            # Perform face recognition using Eigenfaces
            distances, predicted_label = eigenface.predict(face_region)

            # Set a threshold for confidence (adjust as needed)
            threshold = 8000

            # Check if the predicted label has a low enough distance (high confidence)
            if distances < threshold:
                matched_name = known_face_names[predicted_label]
                names.append(matched_name)
                # Put the recognized name on the frame
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, matched_name, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            else:
                names.append("Unknown")  # Handle cases where no face matches with high confidence

        # Display the frame
        cv2.imshow('Face Recognition Panel', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    return names
