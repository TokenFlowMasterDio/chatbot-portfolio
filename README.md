Chatbot Project

Welcome to the Chatbot Project! This chatbot, built using Meta's Llama-3.2-1B model, is designed to handle customer service queries with natural language responses. It is a portfolio-worthy project that showcases skills in AI integration, Flask backend development, and web deployment.

Features

AI-Powered Responses:

Utilizes Meta’s Llama-3.2-1B model for natural, intelligent responses.

Incorporates Few-Shot Prompting for customized and concise replies.

Post-Processing:

Removes repetitive or redundant sentences for improved clarity.

Scope Limitation:

Provides helpful fallback responses for out-of-scope queries.

Interactive Frontend:

Simple and intuitive HTML interface for user interaction.

Deployment Ready:

Backend is Flask-based and can be hosted on platforms like Render or AWS.

Installation

Prerequisites

Python 3.9 or higher

Virtual environment tools (e.g., venv or virtualenv)

Required Python libraries: Flask, Transformers, PyTorch, Gunicorn

Steps

Clone the repository:

git clone git@github.com:your-username/chatbot-portfolio.git
cd chatbot-portfolio

Set up a virtual environment:

python -m venv chatbot_env
source chatbot_env/bin/activate  # On macOS/Linux
chatbot_env\Scripts\activate   # On Windows

Install dependencies:

pip install -r requirements.txt

Run the Flask server:

python app.py

Open the frontend:

Navigate to index.html in your browser.

Interact with the chatbot by typing a message and clicking "Send."

File Structure

chatbot-portfolio/
├── app.py               # Backend Flask server
├── index.html           # Frontend user interface
├── script.js            # JavaScript for connecting frontend to backend
├── requirements.txt     # Python dependencies
├── .gitignore           # Excludes unnecessary files from Git
├── model_setup.py       # Llama model setup script
└── README.md            # Project documentation

Deployment

Backend Deployment

Create an account on Render or another hosting platform.

Connect your GitHub repository to the hosting platform.

Configure the deployment settings:

Start Command: gunicorn app:app

Environment: Python 3.9+

Frontend Hosting

Host the index.html file on GitHub Pages or another static hosting platform.

Update the script.js file to point to your hosted backend's URL.

Example Interaction

User: Who are you?

Chatbot: I am a chatbot designed to assist with customer service queries. How can I help you today?

Technologies Used

Programming Language: Python

AI Model: Meta Llama-3.2-1B via Hugging Face Transformers

Backend Framework: Flask

Frontend: HTML, JavaScript

Hosting: Render for backend, GitHub Pages for frontend

Future Improvements

Add user authentication for a personalized experience.

Expand the chatbot’s scope to handle more complex queries.

Integrate with third-party APIs for enhanced functionality.

Credits

<<<<<<< HEAD
Developed by Nijee Duncan. Special thanks to OpenAI’s guidance in building this project.
=======
Developed by Nijee Duncan. Special thanks to OpenAI’s guidance in building this project.
>>>>>>> 73b0a364fd509b2daec54e547bd31b3f7521952f

License

This project is licensed under the MIT License. See LICENSE for more details.

Thank you for checking out this project! If you have any questions or suggestions, feel free to reach out or open an issue in the repository.

