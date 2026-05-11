from google import genai 
from dotenv import load_dotenv
import os 
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# for model in client.models.list():
#     print(model.name)


response = client.models.generate_content(
    model='gemini-2.5-flash',contents="Do you know my name"
)

print(response.text)