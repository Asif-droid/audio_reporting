from google import genai

import os
from dotenv import load_dotenv
load_dotenv()
prompt="""

You are an expert in extracting structured information from disaster reports. Analyze the following text and extract the following details in JSON format:

{
  "Name": "[if mentioned, otherwise empty]",
  "District": "[inferred from location details]",
  "Upazila": "[if mentioned, otherwise empty]",
  "Union": "[specific place mentioned]",
  "Gender": "[inferred from pronouns or names]",
  "Year": "[if mentioned, otherwise empty]",
  "Disaster Type": "[type of disaster described]",
  "Incident/Loss/Damages": "[specific damages mentioned]",
  "Loss Amount": "[quantified losses mentioned]"
}

Rules:
** return the values in English. if info is in Bangla convert into English **
1. Only include fields that can be reasonably inferred from the text
2. For numeric values like losses, extract just the number
3. For disaster type, use standard terms like "flood", "storm", "earthquake","flash flood", "droughts", "cyclone" etc. Infer form the text.
4. Infer occupation and gender from the speakers description.
5. For location, infer the most specific place mentioned with respect to Bnagladesh
You can also use the internet for this task.
** make sure all the values in English. if info is in Bangla convert into English **


"""
key=os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=key)
def audio_upload():
    myfile = client.files.upload(file="./speech_2.ogg")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=["Describe this audio clip", myfile]
    )

    print(response.text)


def audio_read():
    from google.genai import types

    with open('./given_data/report_1.aac', 'rb') as f:
        audio_bytes = f.read()

    response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        prompt,
        types.Part.from_bytes(
        data=audio_bytes,
        mime_type='audio/wav',
        )
    ]
    )

    print(response.text)
    print(response.usage_metadata)




audio_read()