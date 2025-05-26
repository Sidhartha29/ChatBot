from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure the Google API key (replace with your actual key)
GOOGLE_API_KEY = "AIzaSyCsbQb-Nejtln5r_IhroqZm5d3Qm1goC9I"
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
