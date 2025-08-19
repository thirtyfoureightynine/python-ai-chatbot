from openai import OpenAI
import os, sys

# Use your API key from the environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-4o-mini"  # change to "gpt-4o" for stronger answers

# Conversation history (system prompt + messages)
messages = [
    {"role": "system", "content": "You are a helpful, concise assistant."}
]

print("Chat ready. Type your question and press Enter.")
print("Type 'quit' to exit.\n")

try:
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        # Call the API
        resp = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,       # lower = more focused, higher = more creative
            max_tokens=500         # cap the length of replies
        )

        ai_text = resp.choices[0].message.content
        print("\nAI:\n" + ai_text + "\n")

        # Keep the assistant's reply in the history for context
        messages.append({"role": "assistant", "content": ai_text})

except KeyboardInterrupt:
    print("\nInterrupted. Goodbye!")
    sys.exit(0)
