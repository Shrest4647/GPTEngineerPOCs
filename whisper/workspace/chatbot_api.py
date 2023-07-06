import openai

class ChatbotAPI:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def send_message(self, message: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Make reply to user using less than 50 words."},
                {"role": "user", "content": message},
                # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                # {"role": "user", "content": "Where was it played?"}
            ],
            # prompt=f"""### System: You are a conversational chatbot. Reply to human using less than 50 words. You are having a conversation with a human. \nThe human says "{message}"\n### Human: Hi, I am a human. I am having a conversation with a chatbot. \nThe chatbot says """,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
            timeout=10,
        )
        # print("Response:", response)
        return response.choices[0].message.content.strip()
