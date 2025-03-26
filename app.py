#import the libraries 
import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import ollama

#define the model
Model = "CognitiveComputations/dolphin-llama3.1"  # Ensure you have this model installed with `ollama pull dolphin-llama3.1`

# Create a class to handle web scraping
class Website:
    "A utility class to represent a website that we have scraped."
    
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Fix typo: use `soup.title`, not `soup.tittle`
        self.title = soup.title.string if soup.title else "No title found"
        
        # Remove irrelevant tags
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = "No body content found"

# Define our system prompt
system_prompt = (
    "You are an assistant that analyzes the contents of a website "
    "and provides a short summary, ignoring text that might be navigation-related."
)

# User prompt function
def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled '{website.title}'.\n\n"
    user_prompt += "The contents of this website are as follows:\n"
    user_prompt += "Please provide a short summary of this website in markdown. "
    user_prompt += "If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

# Combine system and user prompts
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# Function to call the Ollama model
def summarize(url):
    website = Website(url)
    messages = messages_for(website)
    response = ollama.chat(model=Model, messages=messages)
    return response['message']['content']

# Function to display the summary in the terminal
def display_summary(url):
    summary = summarize(url)
    print("\n" + "="*50)
    print(f" Summary of: {url} ")
    print("="*50)
    print(summary)
    print("="*50 + "\n")

# Example usage
display_summary("https://dinajpur.polytech.gov.bd/site/page/0e0b86a4-8e61-4989-bf87-9ca6f377ba47/-")
