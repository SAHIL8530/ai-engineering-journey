import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEY KIDHAR HAI")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

role="user"
prompt="SUGGEST ME A NAME FOR MY HOTEL only 1 name"

#SYSTEM ROLE
message_system = {
    "role": "system",
    "content": "YOUR AN BRAND MANAGER WHO SUGGESTS DIFFERENT NAMES FOR HOTELS"
}
message = {
    "role": role,
    "content":prompt
}

messages = [message_system,message]
#TEMPERATURE BY DEFAULT 0 MEANS SAFE MODE RANGE IS 0-2
response = client.chat.completions.create(model=model, messages=messages , temperature=2)
print(response)

print("#############")

answer= response.choices[0].message.content
print(answer)


