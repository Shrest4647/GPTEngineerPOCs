import os
from dotenv import load_dotenv
from chatbot_api import ChatbotAPI
from text_to_speech import TextToSpeech

class CommandLineApp:
    def __init__(self, chatbot_api: ChatbotAPI, text_to_speech: TextToSpeech):
        self.chatbot_api = chatbot_api
        self.text_to_speech = text_to_speech

    def run(self):
        while True:
            command = input("Enter a command: ")
            self.process_command(command)

    def process_command(self, command: str):
        if command.lower() == "bye bye":
            print("Goodbye!")
            exit()

        response = self.chatbot_api.send_message(command)
        if response.lower() == "skip":
            print("Skipping the current response...")
            return

        self.text_to_speech.speak(response)

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

# Create instances of ChatbotAPI and TextToSpeech
chatbot_api = ChatbotAPI(api_key)
text_to_speech = TextToSpeech()

# Create an instance of CommandLineApp and run the application
app = CommandLineApp(chatbot_api, text_to_speech)
app.run()
