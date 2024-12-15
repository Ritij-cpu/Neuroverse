# NeuroVerse: NLP-Based Desktop Application

**NeuroVerse** is a GUI-based desktop application that integrates multiple Natural Language Processing (NLP) features. Currently, it offers:

- **User Authentication**: Allows users to register and log in.
- **Image Generation**: Uses NLP to generate images based on user prompts via an API.
- **Future Features**: Plans to include Named Entity Recognition (NER), emotion prediction, and other NLP-based tools.

## Features
- **Login and Registration**: User authentication with a secure registration process using a local JSON database.
- **Image Generation**: Generate images based on textual prompts via the `nlpcloud` API.
- **Future NLP Integrations**: NER and emotion prediction features are planned.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Ritij-cpu/Neuroverse.git
    ```

2. Install the required dependencies:
    ```bash
    pip install nlpcloud
    ```

3. Ensure that the following files are present in the project directory:
    - `app.py`: Main file that launches the GUI and connects all features.
    - `myapi.py`: Handles communication with the [NLP Cloud](https://nlpcloud.io/) API for image generation using Stable Diffusion.
    - `mydb.py`: Manages user data, including registration, login, and storing user credentials using a local JSON database.
    - `db.json`: Local file that stores user data (name, email, and password).

## Usage

1. Run the `app.py` file to launch the application:
    ```bash
    python app.py
    ```

2. The application will start with a login window:
    - **Login**: Enter your registered email and password.
    - **Register**: New users can create an account by entering their details.

3. After logging in, you can access the following features:
    - **Image Generation**: Enter a text prompt to generate an image.
    - **Logout**: Return to the login screen.

## Code Structure

- `app.py`: Main file that launches the GUI and connects all features.
- `myapi.py`: Handles communication with the [NLP Cloud](https://nlpcloud.io/) API for image generation using Stable Diffusion.
- `mydb.py`: Manages user data, including registration, login, and storing user credentials using a local JSON database.
- `db.json`: Stores user information, including name, email, and password.

### `myapi.py` - API for Image Generation

This file contains the class `API`, which handles image generation using the NLP Cloud API. The `image_generation` method takes a text prompt and returns an image based on that prompt.

```python
import nlpcloud

class API:
    def __init__(self):
        self.client = nlpcloud.Client("stable-diffusion", "67ee92a07a11daf205627520df4076cd3a7550ef", gpu=True)

    def image_generation(self, text):
        response = self.client.image_generation(text)
        return response
mydb.py - Database for User Data
This file contains the Database class, which handles user registration, login, and storing credentials in a local JSON database (db.json).
import json

class Database:

    def add_data(self, name, email, password):
        with open('db.json', 'r') as rf:
            database = json.load(rf)

        if email in database:
            return 0
        else:
            database[email] = [name, password]
            with open('db.json', 'w') as wf:
                json.dump(database, wf)
            return 1

    def search(self, email, password):
        with open('db.json', 'r') as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Stable Diffusion: For providing an API for image generation.
Tkinter: For enabling the creation of the user interface.
nlpcloud: For providing the API to integrate Stable Diffusion into the application.

