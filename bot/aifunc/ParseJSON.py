import json
import sys


def cleanUpString(dirtyStr):
	begin = dirtyStr.find('[')
	end = dirtyStr.rfind(']')
	return dirtyStr[begin:end+1]


def formatFlashcard(response):
	#Iterate through the list of dictionaries, formating them and placing the formated string in a list
	final = []
	#Remove preciding and trailing text from the gpt response string
	clean = cleanUpString(response)
	#check if a list or single dictionary with the list
	for card in json.loads(clean):
		front = card["front"]
		back = card["back"]
		final.append(f'{front}\n\n||{back}||')

	return final


'''
testDict1 = {
  "flashcards": [
    {
      "card_number": 1,
      "front": "What does the Pythagorean theorem state?",
      "back": "The Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. This can be written as: a² + b² = c²."
    },
    {
      "card_number": 2,
      "front": "What is the quadratic formula?",
      "back": "The quadratic formula is used to solve quadratic equations and is given by: x = [-b ± sqrt(b² - 4ac)] / (2a)"
    },
    {
      "card_number": 3,
      "front": "Define 'Prime Number'",
      "back": "A Prime Number can be divided evenly only by 1 or itself. And it must be a whole number greater than 1."
    },
    {
      "card_number": 4,
      "front": "What is the formula for the area of a circle?",
      "back": "The formula for the area of a circle is πr², where r represents the radius of the circle."
    },
    {
      "card_number": 5,
      "front": "What is a derivative in calculus?",
      "back": "In calculus, a derivative measures how a function changes as its input changes. Loosely speaking, a derivative can be thought of as how much one quantity is changing in response to changes in some other quantity."
    }
  ]
}
'''

#print(formatFlashcard(testDict1))
#print(formatFlashcard(testDict2))



