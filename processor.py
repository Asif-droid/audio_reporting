from google import genai
import report_gen as reporter
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
import os

key=os.getenv("GOOGLE_API_KEY")
def report(data):
    # reporter.create_report(data)
    print("Report function called with data:", data)



functions = [
        {
            "name" : "report",
            "description": "Generate a report based on the provided data.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "object",
                        "description": "Data to be included in the report.",
                        },   
                },
                "required": ["data"],
            },
        },
    ]
    

def read_prompt(file):
    with open(file, "r") as prompt_file:
        prompt_text = prompt_file.read().strip()
    return prompt_text


client = genai.Client(api_key=key)
tools = types.Tool(function_declarations=functions)
config = types.GenerateContentConfig(tools=[tools])

# myfile = client.files.upload(file="./wavs/speech_2.wav")
prompt= read_prompt("./prompts/report_prompt.txt")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[f"Follow the instruction{prompt}","hdahdkhdnabdabddskjdbadkdnllkjafijiaowjoefb sn msfnsfiwehbfsbkdjwndnfnsadmdliajwbfbnsma"],
    # config=config
)

print(response.text)
print(response)

# if response.candidates[0].content.parts[0].function_call:
#     function_call = response.candidates[0].content.parts[0].function_call
#     print(f"Function to call: {function_call.name}")
#     print(f"Arguments: {function_call.args}")

# if response.function_call:
#     print(response.function_call.name)
#     print(response.function_call.arguments)
#     # Execute your function and get the result
#     result = report(**response.function_call.arguments) # ** unpacks the arguments dictionary
    # Create a user-friendly response and call the model again
    # response2 = model.generate_content(f"Here is the result of {response.function_call.name}: {result}", tools=functions)
    # print(response2.text)

