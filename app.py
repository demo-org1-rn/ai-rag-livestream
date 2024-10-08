from flask import Flask, render_template, request
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os

############################################
# Put your keys, endpoints, and model name in the .env file
############################################

# Load environment variables from .env file
load_dotenv()

# Get the Azure OpenAI credentials and model name from the environment variables
AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AOAI_KEY = os.getenv("AZURE_OPENAI_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# Get the Azure Search credentials and index name from the environment variables
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")


# Set up the client for AI Chat
client = AzureOpenAI(
    api_key=AOAI_KEY,
    azure_endpoint=AOAI_ENDPOINT,
    api_version="2024-05-01-preview",
)
search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY),
    index_name=AZURE_SEARCH_INDEX,
    )


# PUT YOUR IMPORTS HERE


# PUT YOUR CONSTANTS HERE



# PUT YOUR CODE FOR CREATING YOUR AI AND SEARCH CLIENTS HERE



# PUT YOUR CODE FOR GETTING YOUR AI ANSWER INSIDE THIS FUNCTION
def get_response(question, message_history=[]):
   
  # 
  # AI CODE GOES IN HERE
  #

  return answer, message_history + [{"role": "user", "content": question}]





############################################
######## THIS IS THE WEB APP CODE  #########
############################################

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)


# This is the route for the home page (it links to the pages we'll create)
@app.get('/')
def index():
  # Return a page that links to these three pages /test-ai, /ask, /chat
  return """<a href="/test-ai">Test AI</a> <br> 
            <a href="/ask">Ask</a> <br> 
            <a href="/chat">Chat</a>"""

# Put the extra routes here






# This is for when there is not a matching route. 
@app.errorhandler(404)
def handle_404(e):
    return '<h1>404</h1><p>File not found!</p><img src="https://httpcats.com/404.jpg" alt="cat in box" width=400>', 404


if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=8080)