import inspect
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def make_prompt_from_keywords(client, gender, keywords):
    prompt = inspect.cleandoc(f'''[지시]
        dall-e-2에게 넘겨줄 프롬프트를 작성해줘. 프로필 사진용으로 쓸 것이라서 사람 사진이 메인이어야 하고, 최대한 이쁘고 멋있게 나왔으면 좋겠어. 
        뒤에 따라오는 키워드는 프로필을 만들 사람의 특징이야. 키워드를 참고해서 프로필 사진을 만들 수 있는 프롬프트를 작성해줘. 
        프로필 사진용이야. 조금 미화된 느낌이어도 괜찮아. 누가 보더라도 호감이 가고, 멋있고 예쁜 사람이라고 느낄 수 있도록 해줘.
                              
        [성별]
        {gender}

        [제약사항]
        - 영어로 작성해줘
        - 단어를 콤마로 구분해서 작성해줘

        [키워드]
        {keywords}
        '''
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 dall-e에게 넘겨줄 프롬프트를 잘 만드는 AI 비서야."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content


def make_profile_image(prompt):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url


st.title("프사를 만들어봅시다!")
st.caption("몇 가지 키워드를 입력하면, 그에 맞춰 프로필 사진을 만들어드립니다.")

gender = st.radio("성별을 선택해주세요.", ("남성", "여성"))
keywords = st.text_input("키워드를 입력해주세요.(쉼표로 구분해주세요)")
if keywords:
    st.write(f'입력한 키워드: {keywords}')
    with st.spinner('프롬프트를 만들고 있어요...'):
        prompt = make_prompt_from_keywords(client, gender, keywords)

    st.write(prompt)
    
    with st.spinner('프로필 사진을 만들고 있어요...'):
        image_url = make_profile_image(prompt)
        print(image_url)
        st.image(image_url)


