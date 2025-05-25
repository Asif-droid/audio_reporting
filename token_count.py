from google import genai

import os
from dotenv import load_dotenv
load_dotenv()
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

    with open('./wavs/speech_2.wav', 'rb') as f:
        audio_bytes = f.read()

    response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        'Describe this audio clip',
        types.Part.from_bytes(
        data=audio_bytes,
        mime_type='audio/wav',
        )
    ]
    )

    print(response.text)
    print(response.usage_metadata)




audio_read()