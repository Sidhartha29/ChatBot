from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the Google API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if the API key exists
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY not set in environment variables")

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model once
model = genai.GenerativeModel('gemini-2.0-flash')

# Start a chat session (keep it global to maintain history per server run)
chat = model.start_chat(history=[])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    user_message = request.json.get('message')
    if user_message.lower() == 'quit':
        return jsonify({'reply': 'Goodbye!'})
    
    try:
        # Send user input to the generative AI model
        response = chat.send_message(user_message)
        reply = response.text
    except Exception as e:
        reply = f"An error occurred: {str(e)}"
    
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
