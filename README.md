# Sign Language Examination System

This is a web application for conducting sign language examinations. Users can select a question from a list, answer it using sign language, and submit their response. The system captures the sign language input through the user's webcam and records the answers for evaluation.

## Features

- Select a question from a list of available questions.
- Answer the question using sign language captured through the webcam.
- Submit the answer for evaluation.
- View a success message after successfully submitting an answer.
- Automatically move to the next question after submitting an answer.

## Technologies Used

- Flask: Web framework for Python used to build the backend server.
- HTML/CSS: Frontend markup and styling for the web pages.
- JavaScript: Used for client-side functionality such as accessing the webcam and handling form submissions.
- OpenCV and MediaPipe: Libraries for processing and analyzing sign language input captured from the webcam.

## Setup Instructions

1. Clone the repository to your local machine:
git clone https://github.com/your-username/sign-language-examination-system.git

2. Install the required dependencies:
pip install -r requirements.txt

3. Run the Flask application:
python main.py

4. Access the application in your web browser at `http://localhost:5000/`.

## File Structure

- `main.py`: Flask application code for handling routes and requests.
- `Function.py`: Contains functions for processing sign language input.
- `templates/index.html`: HTML template for the frontend.
- `questions.txt`: File containing a list of questions for the examination.
- `answers.txt`: File to store recorded answers.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
