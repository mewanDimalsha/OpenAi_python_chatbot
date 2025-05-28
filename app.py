import utils.clients
import utils.http_session
import utils.transport
import utils.session
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
client = genai.Client(api_key=GOOGLE_API_KEY)

while True:
    print("Ask a question or type 'exit' to quit:")
    question =  input("User: ")
    if question != "exit":
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=question,
        )
        print("AI: ",response.text)
        
    else:
        print("Ending conversation.")
        break