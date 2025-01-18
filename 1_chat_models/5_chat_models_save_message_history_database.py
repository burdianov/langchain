import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_firestore import FirestoreChatMessageHistory
from google.cloud import firestore

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

PROJECT_ID = os.getenv("FIRESTORE_PROJECT_ID")
SESSION_ID = "user_session_new"
COLLECTION_NAME = "chat_history"

print("PROJECT_ID: ", PROJECT_ID)

print("Initializing Firestore client...")
client = firestore.Client(project=PROJECT_ID)

print("Initializing Firestore chat message history...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Firestore chat message history initialized.")
print("Current chat history: ", chat_history.messages)

model = ChatOpenAI(model="gpt-4o-mini")

print("Start chatting with the AI. Type 'exit' to end the conversation.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")
