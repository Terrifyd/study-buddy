from aifunc import gptCall, ParseJSON

result = gptCall.gptCallKahoot("3", "The Revolutionary War")

print(ParseJSON.formatKahoot(result))
