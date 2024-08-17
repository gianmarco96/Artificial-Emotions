from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

#client.api_key = 'your_openai_api_key'  # Replace this with your actual API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt_ = request.form['prompt']
    print(prompt_)
    
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt_,
            size="1024x1024",
            quality="standard",
            n=1,
            )
        image_url = response.data[0].url
        #print(image_url)
        return render_template('index.html', image_url=image_url)
    except Exception as e:
        print(e)
        return 'Error generating image', 500

@app.route('/info',)
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)
