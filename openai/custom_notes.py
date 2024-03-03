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


def Custom_Notes(notes: str, subject: str, numOfCards: str):
    client = OpenAI(api_key = API_KEY)
    
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professor, skilled in explaining a vast amount of different school subjects"},
            {"role": "user", 
            "content": "Generate " + numOfCards + 
            " flash cards based on the provided text deliminated by triple backticks and organize the front and back in a JSON format with the front being a question and the back being the answer: ```" + 
            notes + "```."}
        ]
    )

    return completion.choices[0].message


""" client = OpenAI(api_key = API_KEY)
#OpenAI.api_key = "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"
numOfCards = "10"
subject = "English"

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a professor, skilled in explaining a vast amount of different school subjects"},
    {"role": "user", "content": "Generate " + numOfCards + " flash cards to help me study for "+ subject + " and organize the front and back in a JSON format"}
  ]
)

print(completion.choices[0].message) """
