AI-Based Desktop Assistant 💻🤖
A voice-activated desktop assistant that simplifies daily computer tasks using Artificial Intelligence.

Overview
This project is a lightweight, AI-powered desktop assistant built using Python. It understands voice commands and helps automate routine operations such as opening applications, searching the web, sending emails, and providing real-time information like weather, date, or news—all through natural language interaction.

The assistant is designed to run locally, offering quick response times and privacy for personal use without relying on cloud-based services.

Features
🔊 Speech Recognition for natural interaction

🌐 Web search and browser automation

📨 Send emails using SMTP

📅 Tells date, time, and day

🌦️ Fetches real-time weather updates

📂 Opens files and applications

🧠 Expandable with custom commands and skills

Technologies Used
Python

SpeechRecognition

pyttsx3 (Text-to-Speech)

pywhatkit

smtplib

datetime

webbrowser

OS module

OpenWeatherMap API (optional)

Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/ai-desktop-assistant.git
cd ai-desktop-assistant
2. Install dependencies
Make sure Python 3.6+ is installed. Then install required packages:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the assistant
bash
Copy
Edit
python main.py
Make sure your microphone is enabled and accessible by the application.

Basic Commands
Here are a few example commands you can try:

"Open YouTube"

"What is the weather in Delhi?"

"Send an email to John"

"What time is it?"

"Search for Python tutorials"

"Play a song on YouTube"

Project Structure
bash
Copy
Edit
ai-desktop-assistant/
│
├── main.py                # Main script to run the assistant
├── assistant_utils.py     # Helper functions (email, weather, etc.)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── config.py              # API keys and configuration (if needed)
Customization
You can easily extend the assistant with new commands or integrate APIs. The command parsing logic is modular and can be updated in the main.py or a dedicated command handler file.

Disclaimer
This project is intended for educational and personal use. Voice recognition may vary in accuracy based on environment and microphone quality.
