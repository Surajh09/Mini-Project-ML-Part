# Django Face Detection

## Description
This Django project integrates face detection functionality into a web application. Users can upload images, and the system will detect faces in those images, providing a bounding box around each detected face.

## Installation

1. Clone the repository:
    ```bash[
        git clone https://github.com/Surajh09/Mini-Project-ML-Part.git
    ```
2. Navigate into the project directory:
    ```bash
    cd django-face-detection
    ```
3. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Apply migrations:
    ```bash
    python manage.py migrate
    ```
2. Run the development server:
    ```bash
    python manage.py runserver
    ```
3. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Configuration

1. Ensure that the required environment variables are set. You may need to set environment variables for sensitive information like API keys.
2. Optionally, you can adjust the settings in `settings.py` to customize the behavior of the application.

## Dependencies

- Django: Web framework for building web applications in Python.
- OpenCV: Library for computer vision and machine learning.
- Pillow: Python Imaging Library for image processing.
- [face_recognition](https://github.com/ageitgey/face_recognition): Simple facial recognition library for Python.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or new features to add, feel free to open an issue or create a pull request.
