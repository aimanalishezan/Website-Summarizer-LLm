import requests
from bs4 import BeautifulSoup
import ollama
import sys

# Ensure UTF-8 encoding in the terminal
sys.stdout.reconfigure(encoding='utf-8')

# Define the model
Model = "CognitiveComputations/dolphin-llama3.1"

# Create a class to handle web scraping
class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        self.title = soup.title.string if soup.title else "No title found"
        
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            
            # Clean extracted text to prevent broken words
            self.text = ' '.join(soup.body.get_text(separator="\n", strip=True).split())
        else:
            self.text = "No body content found"

# Define system prompt
system_prompt = "You are an assistant that analyzes website content and provides a short summary."

def user_prompt_for(website):
    return f"Title: {website.title}\n\nContent:\n{website.text}\n\nSummarize this."

def messages_for(website):
    return [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt_for(website)}]

def summarize(url):
    website = Website(url)
    print("Extracted Text:\n", website.text)  # Debugging output
    messages = messages_for(website)
    response = ollama.chat(model=Model, messages=messages)
    return response['message']['content']

def display_summary(url):
    summary = summarize(url)
    print("\n" + "="*50)
    print(f" Summary of: {url} ")
    print("="*50)
    print(summary)
    print("="*50 + "\n")

# Run the script
display_summary("https://dinajpur.polytech.gov.bd/site/page/0e0b86a4-8e61-4989-bf87-9ca6f377ba47/-")
