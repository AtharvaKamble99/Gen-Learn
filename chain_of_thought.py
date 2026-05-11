from openai import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv()
import json

client= OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


system_prompt="""
    You're are an expert AI Assistant in resolving user queries using chain of thought . 
    You work on START,PLAN & EXECUTE steps.
    You need to first PLAN what is needed to be done . The PLAN can be of multiple steps . 
    Once you think enough PLAN is done , then you can move to the EXECUTE step .


    Rules:
    - Strictly follow of the given JSON output format .
    - Only run 1 step at a time . 
    - The sequence is START (where the user provides the input) , PLAN (Can be of multiple steps ) and
    finally the EXECUTE step , it will be the last step . 


    Output JSON Format :
    {"step":{"START"|"PLAN"|"EXECUTE"},"content":"string"}


    example: 
    START : CAN you solve 2 + 3 * 9 / 3
    PLAN : {"step" :"PLAN",
    "content":"Seems that the user is intrested in math problem"}
    PLAN : {"step" :"PLAN",
    "content":"Looking at the problem , we can solve it using BODMAS rule"}
    PLAN : {"step" :"PLAN",
    "content":"Yes,BODMAS is the correct method to move forward with"}
    PLAN : {"step" :"PLAN",
    "content":"According to BODMAS, First division will be performed, so 9/3 -> 3 "}
    PLAN : {"step" :"PLAN", 
    "content":"the next step would be multiplication ,so the equation would be 3 * 3 -> 9 "}
    PLAN : {"step" :"PLAN",
    "content":"the next step would be addition ,so the equation would be 2 + 9 -> 11 "}
    EXECUTE : {"step" :"EXECUTE",
    "content":"So, the output of the equation would be 11 . Thank you , Don't trouble me again :) 67 ! "}
"""


message_history=[
    {"role":"system","content":system_prompt},
]

user_query = input("👉")

message_history.append({"role":"user","content" : user_query})

while(True):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type" : "json_schema"},   
        messages=message_history
    )
    raw_res=response.choices[0].message.content

    message_history.append({"role":"assistant","content" : raw_res})
    
    parsed_res=json.loads(raw_res)
    if(parsed_res.get("step")=="START") :
        print("🧠   \tStarting phase : ",parsed_res.get("content"))
        continue
    if(parsed_res.get("step")=="PLAN") :
        print("⚒️   \tbuild started : ", parsed_res.get("content"))
        continue 
    if(parsed_res.get("step")=="EXECUTE") :
        print("😌   \tbuild completed : ", parsed_res.get("content"))
        break

    
     
