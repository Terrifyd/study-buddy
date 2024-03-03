import json
import sys


def formatFlashcard(response):
	#Iterate through the list of dictionaries, formating them and placing the formated string in a list
	final = []
	#check if a list or single dictionary with the list
	if type(response) is dict:
		for item in response:
			response = response[item]

	for card in response:
		front = card["front"]
		back = card["back"]
		final.append(f'{front}\n\n||{back}||')

	return final


testDict1 = [{"id": 1, "front": "This is the front", "back": "This is the back"}, 
	{"id": 2, "front": "This is the front again", "back": "This is the back again"}
]

testDict2 = { "notecards": [{"id": 1, "front": "This is the front", "back": "This is the back"},
        {"id": 2, "front": "This is the front again", "back": "This is the back again"}
] }

print(formatFlashcard(testDict1))
print(formatFlashcard(testDict2))
