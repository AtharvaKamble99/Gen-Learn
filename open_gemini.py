from openai import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv()
client =OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        # {
        #  "role":"system",
        #  "content":"You are an expert in Data Structure and Algorithm and you should answer questions only related to it . If asked about something other than that ,respond with sorry I can only answer questions related to DSA . "  
        # },
        {
            "role":"user",
            # "content":"Can you give me the best and worst case complexity of the Binary Search Algorithm ."
            "content":"Give me all the required cases for KKR to quality for IPL play-offs 2026"
        }
    ]
)

print(response.choices[0].message)