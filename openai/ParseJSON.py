import json

# Extracts the substring between start and end (inclusive)
def extract_substring(input: str, start: str, end: str):
    start_ind = input.find(start)
    end_ind = input.find(end)
    if start != -1:
        if end != -1:
            output = input[start_ind : end_ind + len(end)]
            return output
    
    # error handling
    if start == -1:
        print("ERROR could not find start string")
    if end == -1:
        print("ERROR could not find end string")
    return None

def parse(input: str):
    JSON = extract_substring(input, "[", "]")
    Cards = json.loads(JSON)
    print(Cards)


test_input = "Your data is [data here]."
ex_output = """ChatCompletionMessage(content='Here are a set of 10 flashcards in a JSON format for you to study English:\n\n```\n{\n   "flashcards":[\n      {\n         "front":"Define \'Simile\'.",\n         "back":"A figure of speech involving the comparison of one thing with another thing of a different kind, used to make a description more emphatic or vivid."\n      },\n      {\n         "front":"What is a \'Metaphor\'?",\n         "back":"A figure of speech in which a word or phrase is applied to an object or action to which it is not literally applicable."\n      },\n      {\n         "front":"Conjugate the verb \'To Be\' in present simple tense.",\n         "back":"I am, You are, He/She/It is, We are, You are, They are"\n      },\n      {\n         "front":"Give an example of a \'Pronoun\'.",\n         "back":"He, She, It, They, We, You etc."\n      },\n      {\n         "front":"Explain \'Alliteration\'.",\n         "back":"Alliteration is when the same letter or sound at the beginning of closely connected words."\n      },\n      {\n         "front":"What is an \'Adverb\'?",\n         "back":"A word that modifies a verb, an adjective, or another adverb, expressing manner, place, time, or degree."\n      },\n      {\n         "front":"Explain the use of \'Oxford Comma\'.",\n         "back":"The Oxford (or serial) comma is the final comma in a list of things. It is used for clarity to indicate the separate items in the list."\n      },\n      {\n         "front":"Define the term \'Synonym\'.",\n         "back":"A word or phrase that means exactly or nearly the same as another word or phrase in the same language."\n      },\n      {\n         "front":"Provide an example of an \'Antonym\'.",\n         "back":"Hot and Cold, Up and Down, Light and Dark etc."\n      },\n      {\n         "front":"What is the purpose of a \'Conjunction\'?",\n         "back":"A conjunction is a word that connects phrases, clauses or sentences. Examples include \'and\', \'but\', \'or\', etc."\n      }\n   ]\n}\n```', role='assistant', function_call=None, tool_calls=None)"""

# print(parse(test_input))
print(parse(ex_output))