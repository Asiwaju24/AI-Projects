# OpenCV Project README

This repository contains various Python scripts related to computer vision, face recognition, security systems, and AI assistants using OpenCV and other libraries.

## Files Overview

### Face Detection and Recognition
- **alert.py**: Real-time face detection using webcam. Captures video, detects faces with Haar cascades, draws rectangles around detected faces, and prints "Face detected!" to console. Displays live video feed.
- **Face Recognition.py**: Similar to alert.py, performs real-time face detection from webcam, draws blue rectangles around faces, and shows the video feed.
- **face_detect.py**: Loads a trained face recognition model and tests it on a specific image (Ryan Reynolds). Detects faces and predicts the person's label with confidence score.
- **face_train.py**: Trains a face recognition model using images from the `images/` folder. Processes images for each person (Messi, Elon, Bezoz, Ryan, Canu), extracts face features, and saves the trained model to `face_trained.yml`.
- **haarcascade_frontalface_default.xml**: Haar cascade classifier XML file for frontal face detection, used by various scripts.

### Security Systems
- **newsecurity.py**: Motion detection security camera. Captures webcam feed, detects motion by comparing frames, and plays a siren sound (`siren.wav`) when significant movement is detected.
- **security.py**: Similar motion detection script, but uses Windows beep sound instead of an audio file when motion is detected.

### AI and Chatbot
- **model_train.py**: Prepares data for training an intent classification model. Loads intents from `intent.json`, processes patterns and tags into training sentences and labels for machine learning.
- **intent.json**: JSON file containing chatbot intents, including patterns (user inputs) and responses for tags like greeting, goodbye, thanks, etc.
- **New Ai.py**: AI assistant script (possibly for Android). Uses Vosk for speech recognition, handles voice commands like playing songs on YouTube or fetching Wikipedia info.

### Miscellaneous
- **import cv2.py**: Basic face detection script similar to alert.py, imports OpenCV and starts webcam face detection.
- **images/**: Folder containing subfolders with images of people (Bezoz, Canu, Elon, Messi, Ryan) used for training the face recognition model.

## Dependencies
- OpenCV (cv2)
- NumPy
- scikit-learn (for model_train.py)
- Vosk (for New Ai.py)
- pyttsx3 (for New Ai.py)
- simpleaudio (for newsecurity.py)
- winsound (built-in for security.py)
- jnius (for Android integration in New Ai.py)
- pywhatkit (for YouTube playback)
- wikipedia (for info retrieval)

## Usage
Run individual scripts with Python (e.g., `python face_train.py` to train the model, then `python face_detect.py` to test recognition).