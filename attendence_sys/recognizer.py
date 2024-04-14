
# import face_recognition
# import numpy as np
# import cv2
# import os


# def Recognizer(details):
#     video = cv2.VideoCapture(0)

#     known_face_encodings = []
#     known_face_names = []

#     # Construct image directory path using f-strings
#     image_dir = f"{os.path.dirname(os.path.abspath(__file__))}/static/images/Student_Images/{details['branch']}/{details['year']}/{details['section']}"

#     # Load known face encodings outside the loop
#     for root, _, files in os.walk(image_dir):
#         for file in files:
#             if file.endswith('jpg') or file.endswith('png'):
#                 path = os.path.join(root, file)
#                 img = face_recognition.load_image_file(path)
#                 img_encoding = face_recognition.face_encodings(img)[0]
#                 known_face_names.append(file[:len(file) - 4])
#                 known_face_encodings.append(img_encoding)

#     face_locations = []
#     face_encodings = []
#     names = []

#     while True:
#         check, frame = video.read()
#         small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
#         rgb_small_frame = small_frame[:, :, ::-1]

#         face_locations = face_recognition.face_locations(rgb_small_frame)

#         # Combine face recognition steps into one call
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)

#             if True in matches:
#                 # Find the index of the first match for name lookup
#                 first_match_index = matches.index(True)
#                 name = known_face_names[first_match_index]
#                 names.append(name)
#                 break  # Exit the loop after finding a match

#         for (top, right, bottom, left), name in zip(face_locations, names):
#             top *= 2
#             right *= 2
#             bottom *= 2
#             left *= 2

#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(frame, name, (left, top), font, 0.8, (255, 255, 255), 1)

#         cv2.imshow("Face Recognition Panel", frame)

#         if cv2.waitKey(1) == ord('s'):
#             break

#     video.release()
#     cv2.destroyAllWindows()
#     return names

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
    # Perform face recognition logic here (e.g., compare with known faces)
    # For simplicity, I'm just returning a random name from known_face_names list
    return np.random.choice(known_face_names)

# Usage example
# details = {
#     'branch': 'your_branch',
#     'year': 'your_year',
#     'section': 'your_section'
# }
# names = Recognizer(details)
# print(names)  # Replace with your desired output handling
