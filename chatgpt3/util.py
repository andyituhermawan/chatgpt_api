import requests

class ChatGPT3:
    """
    class untuk akses ChatGPT3 via API
    """
    def __init__(self, 
                 api_key,
                 model="gpt-3.5-turbo",  # gunakan model terbaru
                 max_tokens=1000,
                 temperature=0.1):

        self.url = "https://api.openai.com/v1/chat/completions"
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.context = None
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

    def ngobrol(self, text):
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": text}],  # sesuaikan dengan format API chat terbaru
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        response_json = response.json()
        
        # Cek respons dari API dan tangani kesalahan
        if response.status_code == 200:
            if 'choices' in response_json and len(response_json['choices']) > 0:
                output = response_json['choices'][0]['message']['content']
                print(output)
            else:
                print("Respons tidak mengandung 'choices':", response_json)
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def ngoding(self, text):
        if self.context is not None:
            text = f"dari kode : \n {self.context} \n " + text
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": text}],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        response_json = response.json()
        
        if response.status_code == 200:
            if 'choices' in response_json and len(response_json['choices']) > 0:
                output = response_json['choices'][0]['message']['content']
                self.context = output
                exec(output, globals())
            else:
                print("Respons tidak mengandung 'choices':", response_json)
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def tampilkan_kode_terakhir(self):
        print(self.context)

    def reset_context(self):
        self.context = None
