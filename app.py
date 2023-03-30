from flask import Flask
import openai 
import os
app = Flask(__name__)
API_key='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'
os.environ['OPENAI_Key']=API_key
openai.api_key=os.environ['OPENAI_Key']
@app.route('/api/<string:text>', methods = ['GET', 'POST'])
def generate_tags(text):
    print("working")
    if(request.method == 'GET'):
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
def get_trending_tags():
    url = "https://best-hashtags.com/hashtag/travel/" 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tag_elements = soup.find_all("a", class_="tag") 
    trending_tags = [element.text.lower() for element in tag_elements]
    return trending_tags

def filter_tags(tags, trending_tags):
    filtered_tags = [tag for tag in tags if tag.lower() in trending_tags]
    return jsonify({'data': filtered_tags})
@app.route('/asvin', methods = ['GET', 'POST'])
def get_trending_tags():
    print("working")
    return jsonify({'data': "asvin"})
    
if _name_ == "_main_":
    app = create_app()
    app.run(debug=True)