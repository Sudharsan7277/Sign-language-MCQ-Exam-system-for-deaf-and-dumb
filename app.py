from flask import Flask, render_template, request
import numpy as np
import mediapipe as mp
import cv2 as cv
from Function import persons_input, get_fram

app = Flask(__name__)

# Load questions from file
def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = file.readlines()
    return questions

# Function to capture sign language input
def capture_sign_language():
    holy_hands = mp.solutions.hands
    recognized_word = ""
    cap = cv.VideoCapture(0)  # Initialize capture object
    with holy_hands.Hands(max_num_hands=1) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            # To improve performance, optionally mark the image as not writeable
            image.flags.writeable = False
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

            # Images shape
            imgH, imgW = image.shape[:2]
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Get Hand Coordinates (HC values)
                    hand_coordinate = []
                    for index, landmark in enumerate(hand_landmarks.landmark):
                        x_coordinate, y_coordinate = int(landmark.x * imgW), int(landmark.y * imgH)
                        hand_coordinate.append([index, x_coordinate, y_coordinate])
                    hand_coordinate = np.array(hand_coordinate)
                    # Working on image
                    recognized_word = persons_input(hand_coordinate)
                    image = get_fram(image, hand_coordinate, recognized_word)
                    cv.imshow('Sign Language detection', cv.flip(image, 1))
                    if recognized_word:
                        cv.waitKey(3000)  # Wait for 3 seconds to allow the user to see the sign
                        return recognized_word

            # Display camera feed
            cv.imshow('Sign Language detection', cv.flip(image, 1))
            key = cv.waitKey(1)
            if key == ord('q'):  # Press 'q' to exit
                break

    cap.release()  # Release capture object
    cv.destroyAllWindows()

# Store answers
def store_answer(question, answer, file_path):
    with open(file_path, 'a') as file:
        file.write(f"{question.strip()}: {answer}\n")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        return render_template('index.html', question=question)
    else:
        questions = load_questions('questions.txt')
        return render_template('index.html', questions=questions)

@app.route('/answer', methods=['POST'])
def answer():
    question = request.form['question']
    recognized_word = capture_sign_language()
    store_answer(question, recognized_word, 'answers.txt')
    return render_template('index.html', message='Answer recorded successfully.')

if __name__ == "__main__":
    app.run(debug=True)
