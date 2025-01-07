from time import sleep

from openai import OpenAI
from pydantic import BaseModel

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

waited = 0
while True:
    try:
        client = OpenAI(
            api_key=openai_api_key,
            base_url=openai_api_base,
        )
        completion = client.completions.create(model="model",
                                               prompt="San Francisco is a")
        print("Completion result:", completion)
        break
    except Exception as error:
        print(error)
        sleep(60*2)
        waited += 2
        print("Waited time(min): ", waited)


