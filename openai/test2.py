from openai import OpenAI

client = OpenAI(api_key = "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")
#OpenAI.api_key = "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"
numOfCards = 10

completion = client.chat.completions.create(
  model="gpt-4.0",
  messages=[
    {"role": "system", "content": "You are a professor, skilled in explaining a vast amount of different school subjects"},
    {"role": "user", "content": "Generate" + numOfCards + "flash cards to help me study for"+ subject + " and organize the front and back in a JSON format"}
  ]
)

print(completion.choices[0].message)