from aifunc import gptCall, ParseJSON

'''
results = ParseJSON.formatFlashcard(gptCall.gptCallFlashcards("5", "Bannana Republics"))

for cards in results:
	print(cards + "\n\n\n")
'''

results = ParseJSON.formatKahoot(gptCall.gptCallKahoot("5", "Child Physcology"))

for ques in results:
	print(ques + "\n\n\n")
