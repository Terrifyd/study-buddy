from openai import OpenAI
import os
from dotenv import load_dotenv


'''
gptCallFlashcards:
        Purpose: Calls the GPT-4 API with the given subject and number as strings and returns a collection of flashcards.
        Params:
                numOfQuestions: Number of Flashcards question user wants generated.
                subject: Subject the user wants the Flashcards to be made about.
        Returns: Response of the GPT-4 in the format of a JSON.
'''
def gptCallFlashcards(numOfCards: str, subject: str):
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
    	    {"role": "user", "content": "Generate " + numOfCards + " flash cards to help me study for "+ subject + ''' and organize the card number, front, and back in a single JSON format delaminated by the square braces: [ {"id": <card number>, "front": "<front of the card>", "back": "<back of the card>"}, ...]'''}
  	  ]
	)
	return completion.choices[0].message.content


'''
gptCallKahoot: 
	Purpose: Calls the GPT-4 API with the given subject and number as strings and returns number of Kahoot questions.
	Params:
		numOfQuestions: Number of Kahoot question user wants generated.
		subject: Subject the user wants the Kahoot to be made about.
	Returns: Response of the GPT-4 in the format of a JSON.
'''
def gptCallKahoot(numOfQuestions: str, subject: str):
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
	    {"role": "user", "content": "Generate "+ numOfQuestions +" four answer multiple choice question about "+ subject +" and organize the four answers in a single JSON format with the question, the answer, and the three fake answers"}
	  ]
	)
	return completion.choices[0].message.content

