# ChatBot
AI-Powered ChatBot using Flask &amp; Google Gemini API

**Presentation: AI-Powered ChatBot Web Application**

---

### 1: Title

**AI-Powered ChatBot with Google Gemini API**
Created using Flask and a Modern Frontend

---

### 2: Objective

* Build a responsive web chatbot.
* Use Google's Gemini 2.0 Flash model via API.
* Support markdown, themes, and 3D backgrounds.
* Provide persistent chat history and quick replies.

---

### 3: Backend Overview (Flask)

* Python-based backend using Flask
* Routes:

  * `/`: Loads chatbot frontend
  * `/chat`: Handles message POST requests
* Integration with Google Generative AI:

```python
import google.generativeai as genai
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])
```

* Message flow: user -> Flask -> Gemini API -> response -> user

---

### 4: Frontend UI Overview

* Built with HTML, CSS, and Vanilla JS
* Elements:

  * `#chatbox` to display conversation
  * `#inputForm` to enter and send messages
  * Emoji picker and quick replies
  * Theme toggle and 3D background

---

### 5: Interactive Features

* **Markdown Support**: Parses `**bold**`, `*italic*`, `code`, and links
* **Vanta.js Globe**: Background animation for engagement
* **Theme Toggle**: Switch between dark/light mode
* **Quick Replies**: Offers suggestions post-response
* **Persistent Chat**: Uses `localStorage`

---

### 6: Styling and Layout

* Responsive layout using Flexbox
* Sidebar (optional, removed in some versions)
* Colors and fonts for readability
* Adaptive UI for mobile devices

---

### Slide 7: Key JavaScript Logic

```js
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const message = userInput.value.trim();
  appendMessage('user', message);
  const res = await fetch('/chat', {...});
  const data = await res.json();
  appendMessage('bot', data.reply);
});
```

* Append messages dynamically
* Fetch response from Flask `/chat`

---

### 8: Deployment & Security

* Secure API key via environment variables
* Deploy with:

  * PythonAnywhere
  * Render.com
  * Dockerized Flask App
* Use HTTPS and CORS configuration as needed

---

### 9: Improvements & Extensions

* Add session-based user chat
* Store conversations in DB (MongoDB, SQLite)
* Enable speech-to-text and text-to-speech
* Add login/authentication layer

---

### 10: Summary

* Combines Flask, Generative AI, and modern frontend
* Flexible, extendable architecture
* Interactive, user-friendly experience

---

### 11: Demo & Q\&A

* Live demonstration (if applicable)
* Questions and future discussions

---
