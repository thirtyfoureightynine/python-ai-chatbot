🧑‍💻 AI Chat Assistant (Python + OpenAI API)

An interactive command-line chatbot built in Python using the OpenAI API
.
The app lets you ask questions, get AI-generated answers, and maintain context across a conversation all from your (Windows) terminal.

✨ Features

💬 Interactive chat: type your question, get instant AI replies.

🧠 Context memory: the chatbot remembers the conversation.

🔒 Secure API key: loaded via environment variable (not hardcoded).

🎛️ Configurable: adjust model, creativity (temperature), and reply length (max_tokens).

🚪 Easy exit: type quit or exit to leave the chat.

🚀 Demo

Example usage in PowerShell:

PS C:\Users\YourName\Desktop> python app.py
Chat ready. Type your question and press Enter.
Type 'quit' to exit.

You: Hello, what can you do?
AI:
I can answer your questions, explain concepts, write text, and help with problem-solving.

You: Write a haiku about the sea.
AI:
Waves crash endlessly,  
Moonlight dances on the tide,  
Whispers call the deep.

⚙️ Setup
1. Clone the repo
git clone https://github.com/yourusername/python-ai-chatbot.git
cd python-ai-chatbot

2. Install dependencies

Make sure you have Python 3.10+
 installed.
Then install the OpenAI library:

pip install openai

3. Set your API key

In PowerShell (Windows):

setx OPENAI_API_KEY "your_api_key_here"


Reopen PowerShell and confirm:

echo $env:OPENAI_API_KEY


On Mac/Linux:

export OPENAI_API_KEY="your_api_key_here"

4. Run the chatbot
python app.py

🛠️ Code Overview

The main loop:

while True:
    user_input = input("You: ")
    if user_input.lower() in {"quit", "exit"}:
        break

    messages.append({"role": "user", "content": user_input})
    resp = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    ai_text = resp.choices[0].message.content
    print("AI:", ai_text)
    messages.append({"role": "assistant", "content": ai_text})

📚 Learning Highlights

Installed and configured Python & pip

Managed environment variables securely

Connected to the OpenAI API

Handled errors (e.g. quota, missing PATH)

Built an interactive chat loop with memory

📌 Next Steps

Add /save command to export chat history.

Add /clear command to reset context mid-conversation.

Try different models (e.g. gpt-4o for more advanced responses).

📝 License

This project is open source under the MIT License
.
