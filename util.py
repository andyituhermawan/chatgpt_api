import requests

class ChatGPT:
    """
    Class for accessing ChatGPT via the OpenAI API.
    """
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=1000, temperature=0.1):
        self.url = "https://api.openai.com/v1/chat/completions"
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        self.conversation_history = []

    def ngobrol(self, text):
        self.conversation_history.append({"role": "user", "content": text})
        data = {
            "model": self.model,
            "messages": self.conversation_history,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        output = response.json()['choices'][0]['message']['content']
        self.conversation_history.append({"role": "assistant", "content": output})
        print(output)

    def ngoding(self, text):
        self.conversation_history.append({"role": "user", "content": text})
        data = {
            "model": self.model,
            "messages": self.conversation_history,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        output = response.json()['choices'][0]['message']['content']
        self.conversation_history.append({"role": "assistant", "content": output})
        exec(output, globals())

    def tampilkan_kode_terakhir(self):
        if self.conversation_history:
            last_response = self.conversation_history[-1]["content"]
            print(last_response)
        else:
            print("Tidak ada kode yang ditemukan.")

    def reset_context(self):
        self.conversation_history = []

# Example usage:
# api_key = "your_openai_api_key"
# chatgpt = ChatGPT(api_key)
# chatgpt.ngobrol("Hello, how are you?")
# chatgpt.ngoding("Print 'Hello World' in Python.")
# chatgpt.tampilkan_kode_terakhir()
# chatgpt.reset_context()
