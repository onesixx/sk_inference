from openai import OpenAI
from dotenv import load_dotenv

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "이 이미지를 묘사해줘."},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F21691F36543AA6FD26",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
