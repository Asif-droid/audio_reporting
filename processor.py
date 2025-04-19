from google import genai

def read_prompt(file):
    with open(file, "r") as prompt_file:
        prompt_text = prompt_file.read().strip()
    return prompt_text
client = genai.Client(api_key="api_key")

myfile = client.files.upload(file="./wavs/sample_8.wav")
prompt= read_prompt("./prompts/report_prompt.txt")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[f"Follow the instruction{prompt}", myfile]
)

print(response.text)


