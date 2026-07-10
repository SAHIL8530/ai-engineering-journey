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
prompt1 ="Hi"
prompt2 ="Explain time travel in detail"
prompt3 ="Write a 1000 word essay on machine learning"

prompts =[prompt1,prompt2,prompt3]

for prompt in prompts:
    message = {
    "role": role,
    "content":prompt
}
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages )
    usage = response.usage
    print(f"Prompts: {prompt} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")
    



#message = {
 #   "role": role,
  #  "content":prompt
#}

#messages = [message_system,message]
#TEMPERATURE BY DEFAULT 0 MEANS SAFE MODE RANGE IS 0-2
#response = client.chat.completions.create(model=model, messages=messages , temperature=2)
#print(response)

#print("#############")

#answer= response.choices[0].message.content
#print(answer)


