from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Get the value of OPENAI_API_KEY
API_KEY = os.getenv('OPENAI_API_KEY')
if API_KEY is None:
    print("Error: OPENAI_API_KEY is not set.")
else:
    print("OPENAI_API_KEY:", API_KEY)

client = OpenAI(api_key = API_KEY)
#OpenAI.api_key = "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"

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)