from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


prompt = '''[지시]
dall-e에게 넘겨줄 프롬프트를 작성해줘. 프로필 사진용으로 쓸 것이라서 이쁘고 멋있게 나왔으면 좋겠어. 키워드에 나오는 목록을 참고해서 프롬프트를 작성해줘.

[제약사항]
- 영어로 작성해줘
- 단어를 콤마로 구분해서 작성해줘

[키워드]
python, 개발자, 커피
'''

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "너는 dall-e에게 넘겨줄 프롬프트를 잘 만드는 AI 비서야."},
        {"role": "user", "content": prompt},
    ]
)

print(response)
print('-------')
print(response.choices[0].message.content)