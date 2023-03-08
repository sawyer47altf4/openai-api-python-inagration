import openai
import random
#put your api key in
openai.api_key = "TOKEN"

# prompt for the API to generate text
prompt = input("prompt for ai:")
leave_list = ["bye", "thank you for your time", "thank you for useing [place-holder]"]
if prompt == "q":
  print(random.choice(leave_list))
  quit
if prompt == "c":
  print(random.choice(leave_list))
  quit
  
# generate text with the OpenAI GPT-3 API
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=100,
  n=1,
  stop=None,
  temperature=0.7,
)

# print the generated text
print(response.choices[0].text)
