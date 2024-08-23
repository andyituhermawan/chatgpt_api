import requests

class ChatGPT3:
    """
    Class to interact with OpenAI's ChatGPT-3 model via API.
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
            # Check if 'choices' key exists and if it has the expected content
            if 'choices' in output and len(output['choices']) > 0:
                print(output['choices'][0]['text'])
            else:
                print("Unexpected response format:", output)
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
                exec(self.context, globals())  # Be careful with exec for security reasons
            else:
                print("Unexpected response format:", output)
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def tampilkan_kode_terakhir(self):
        print(self.context)

    def reset_context(self):
        self.context = None
