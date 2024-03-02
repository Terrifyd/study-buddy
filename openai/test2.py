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
numOfCards = "10"
subject = "English"

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a professor, skilled in explaining a vast amount of different school subjects"},
    {"role": "user", "content": "Generate" + numOfCards + "flash cards to help me study for"+ subject + " and organize the front and back in a JSON format"}
  ]
)

print(completion.choices[0].message)