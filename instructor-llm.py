import instructor
import openai
from pydantic import BaseModel
groq_api_key = "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"
client = openai.OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)
client = instructor.from_openai(client)


class Person(BaseModel):
    name: str
    age: int
    place: str
    college: str

result = client.chat.completions.create(
    model="llama3-8b-8192",
    # messages=[
    #     {"role": "user", "content": "My name is Yuvapriya. I come from Pondy.I am 19 years old. I am studying at AIAT College"}
    # ],
    messages=[
         {"role": "user", "content": input("Enter your details:") }
     ],
    response_model=Person,
)

print(result)
