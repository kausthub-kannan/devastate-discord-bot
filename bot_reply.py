import os
from dotenv import load_dotenv
import random
import json
import requests
import urllib.request

# Get the Hugging face Token
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Set params for the request
API_URL = "https://api-inference.huggingface.co/models/pranavpsv/gpt2-genre-story-generator"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Stroy generation function
def story_generator(input_text):
    payload ={
        "inputs": input_text,
        "min_length": random.randint(1000,100000)
    }
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    output = json.loads(response.content.decode("utf-8"))
    output = output[0]["generated_text"]
    return output

# Meme generation function
async def get_meme():
    content = requests.get("https://api.pymeme.repl.co").text
    data = json.loads(content)
    return data