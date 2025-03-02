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
        print("Models:", client.models.list())
        print("Done waiting. Model is available!")
        break
    except Exception as error:
        print(error)
        sleep(60*2)
        waited += 2
        print("Waited time(min): ", waited)


