from openai import OpenAI
import os
from dotenv import load_dotenv



'''
notesGptCallFlashcards:
        Purpose: Calls the GPT-4 API with the given subject, number as strings, and a document of notes, and returns a JSON.
        Params:
                numOfCards: Number of Flashcards user wants generated.
                subject: Subject the user wants the flashcards to be made about.
		notes: Document of notes the user wants the flashcards to be based off of.
        Returns: Response of the GPT-4 in the format of a JSON
'''
def notesGptCallFlashcards(notes: str, subject: str, numOfCards: str):
	'''cardFormat = [ {"id": <card number>, "front": "<front of the card>", "back": "<back of the card>"}, ...]'''

	# Get the value of OPENAI_API_KEY
	load_dotenv()
	API_KEY = os.getenv('OPENAI_API_KEY')
	if API_KEY is None:
		print("Error: OPENAI_API_KEY is not set.")
	else:
		print("OPENAI_API_KEY:", API_KEY)
	client = OpenAI(api_key = API_KEY)

	completion = client.chat.completions.create(
          model="gpt-4",
	  messages=[
	    {"role": "system", "content": "You are a professor, skilled in explaining a vast amount of different school subjects"},
	    {"role": "user", "content": "Generate " + numOfCards + ''' flash cards based on the provided text deliminated by triple backticks and organize the front and back in a single JSON format delaminated by the square braces: [ {"id": <card number>, "front": "<front of the card>", "back": "<back of the card>"}, ...]. ```''' + 
	    notes + "```."}
	  ]
	)

	return completion.choices[0].message.content



'''
notesGptCallKahoot:
        Purpose: Calls the GPT-4 API with the given subject, number, and a document of notes as strings and returns a JSON
        Params:
                numOfQuestions: Number of Kahoot question user wants generated.
                subject: Subject the user wants the flashcards to be made about.
		notes: Document of notes the user wants the Kahoot to be based off of.
        Returns: Response of the GPT-4 in the format of a JSON
'''
def notesGptCallKahoot(notes, subject, numOfQuestions):
	# Get the value of OPENAI_API_KEY
	load_dotenv()
	API_KEY = os.getenv('OPENAI_API_KEY')
	if API_KEY is None:
    		print("Error: OPENAI_API_KEY is not set.")
	else:
    		print("OPENAI_API_KEY:", API_KEY)
	client = OpenAI(api_key = API_KEY)

	completion = client.chat.completions.create(
	  model="gpt-4",
	  messages=[
	    {"role": "system", "content": "You are a professor, skilled in explaining a vast amount of different school subjects"},
	    {"role": "user", "content": "Generate "+ numOfQuestions +" four answer multiple choice questions about "+ subject +" based on the provided text deliminated by the triple backticks and organize the four answers in a single JSON format with the question, the answer, and the three fake answers:```"+
	    notes +"```."}
	  ]
	)

	return completion.choices[0].message.content




#-=== Legacy Code ===-#
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
