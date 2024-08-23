import requests

class ChatGPT3:
    """
    Kelas untuk mengakses model ChatGPT-3 dari OpenAI melalui API.
    """
    def __init__(self, 
                 api_key,
                 model="text-davinci-003",
                 max_tokens=1000,
                 temperature=0.1):

        self.url = "https://api.openai.com/v1/completions"
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
            "prompt": text,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        
        if response.status_code == 200:
            output = response.json()
            # Cek apakah 'choices' ada dan memiliki konten yang diharapkan
            if 'choices' in output and len(output['choices']) > 0:
                print(output['choices'][0]['text'])
            else:
                print("Format respons tidak terduga:", output)
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def ngoding(self, text):
        if self.context is not None:
            text = f"dari kode : \n {self.context} \n " + text
        data = { 
            "model": self.model,
            "prompt": text,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        
        if response.status_code == 200:
            output = response.json()
            if 'choices' in output and len(output['choices']) > 0:
                self.context = output['choices'][0]['text']
                print(self.context)
                exec(self.context, globals())  # Berhati-hati dengan exec untuk alasan keamanan
            else:
                print("Format respons tidak terduga:", output)
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def tampilkan_kode_terakhir(self):
        print(self.context)

    def reset_context(self):
        self.context = None
