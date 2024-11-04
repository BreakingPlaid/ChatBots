# WhatsApp Chatbot with Flask, Twilio, and OpenAI

If for whatever crazy reason you'd like to build a bot too, here are some directions to try to follow along.

This repository contains a WhatsApp chatbot built using Flask, Twilio, and OpenAI's GPT-4 model. The bot responds to WhatsApp messages with generated responses based on user input, formatted for WhatsApp's messaging style.

## Features

- Responds to user messages on WhatsApp
- Utilizes OpenAI's GPT-4 model for generating responses
- Configurable via environment variables for secure API key handling

---

## Prerequisites

- Python 3.7+
- A [Twilio](https://www.twilio.com) account with access to the WhatsApp Sandbox
- An [OpenAI](https://platform.openai.com) account with API access

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies:

python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
.'\'.venv\Scripts\activate    # On Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Create a .env File
In the root directory, create a .env file to securely store your API keys and environment variables:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Set Up Twilio WhatsApp Sandbox
Log into your Twilio Console.
Navigate to the WhatsApp Sandbox section.
Copy the provided Sandbox number (e.g., whatsapp:+14552558555.
Set up your "When a message comes in" webhook with an ngrok URL, which we’ll configure in the next steps.

### 6. Run Ngrok to Expose Local Server
To receive webhooks from Twilio on your local Flask server, use ngrok to expose the server.

Download and install ngrok if you haven't already.

In a new terminal, run:
```
ngrok http 5000
```

Copy the HTTPS forwarding URL provided by ngrok (e.g., https://abcd1234.ngrok.io).

Paste this URL into Twilio’s "When a message comes in" field in the WhatsApp Sandbox settings, followed by a / (e.g., https://abcd1234.ngrok.io/).

### 7. Run the Flask App
In the project directory, start the Flask application:
```
python JonnyChatBot.py
```
The server will be accessible on http://127.0.0.1:5000, and ngrok will route external requests from Twilio to this server.