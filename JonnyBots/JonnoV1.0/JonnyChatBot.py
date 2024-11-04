from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key:", openai.api_key)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bot():
    if request.method == "POST":
        user_msg = request.values.get('Body', '').lower()
        response = MessagingResponse()

        try:
            print("Making OpenAI API request...")
            openai_response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a nice guy from West Virginia. You have a master's degree in creative writing for nonfiction and a master's in project management. You're funny in a Lisa Kudrow kind of way and you're polite, but stern and honest about people when necessary. You're a part of LGBTQIA but believe people aren't so different from one another. You believe anything is possible with the right amount of grit."},
                    {"role": "user", "content": user_msg}
                ],
                max_tokens=50
            )
            print("OpenAI API response:", openai_response)  # Print full response for debugging
            bot_reply = openai_response['choices'][0]['message']['content'].strip()
            formatted_reply = f"*Response:* {bot_reply}"
            
            print("Formatted bot reply:", formatted_reply)
        except Exception as e:
            print(f"Error from OpenAI API: {e}")
            formatted_reply = "Sorry, nobody's home right now."

        response.message(formatted_reply)
        return str(response)
    else:
        return "This is the chatbot endpoint. Please send a POST request to interact with the bot."

if __name__ == "__main__":
    app.run(debug=True)