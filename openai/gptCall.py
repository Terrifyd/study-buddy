from openai import OpenAI
import os
from dotenv import load_dotenv


def gptCallFlashcards(numOfCards, subject):
	#Load the environment variables
	load_dotenv()
	# Get the value of OPENAI_API_KEY
	API_KEY = os.getenv('OPENAI_API_KEY')
	#Check if the environment variable was correctly found, else return None
	if API_KEY is None:
    		print("Error: OPENAI_API_KEY is not set.")
	else:
    		print("OPENAI_API_KEY:", API_KEY)

	client = OpenAI(api_key = API_KEY)
	completion = client.chat.completions.create(
  	  model="gpt-4",
  	  messages=[
    	    {"role": "system", "content": "You are a professor, skilled in explaining a vast amount of different school subjects"},
    	    {"role": "user", "content": "Generate " + numOfCards + " flash cards to help me study for "+ subject + " and organize the front and back in a JSON format"}
  	  ]
	)
	print(completion.choices[0].message)

def gptCallKahoot(numOfQuestions, subject):
	load_dotenv()
	API_KEY = os.getenv("OPENAI_API_KEY")
	if API_KEY is None:
		print("Error: OPENAI_API_KEY is not set.")
	else:
		print("OPENAI_API_KEY:", API_KEY)

	client = OpenAI(api_key = API_KEY)
	completion = client.chat.completions.create(
	  model="gpt-4",
	  messages=[
	    {"role": "system", "content": "You are a professor, skilled in explaining a vast amount of different school subjects"},
	    {"role": "user", "content": "Generate "+ numOfQuestions +" four answer multiple choice question about "+ subject +" and organize the four answers in a JSON format with the question, the answer, and the three fake answers"}
	  ]
	)
	print(completion.choices[0].message)

gptCallFlashcards("5", "American History")
gptCallKahoot("1", "American History")
