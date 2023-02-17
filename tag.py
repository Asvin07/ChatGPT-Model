API_key='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'
import openai
import os
os.environ['OPENAI_Key']=API_key
openai.api_key=os.environ['OPENAI_Key']

def generate_tags(text):
    prompt = (f"tag generator for: {text}")

    completions = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=200,
        n=1,
    )

    message = completions.choices[0].text
    tags = message.strip().split(',')
    return tags

text = []
while True:
    line = input()
    if line:
        text.append(line)
    else:
        break
text = " ".join(text)

tags = generate_tags(text)

tags = " ".join(tags)
print(tags)
