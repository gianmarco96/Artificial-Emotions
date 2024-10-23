from flask import Flask, render_template, request, jsonify
import requests
from openai import OpenAI
import os
import json

client = OpenAI()

app = Flask(__name__)

img_folder_path = "C:\\Users\\amrcmeu\\Documents\\AE\\appScripts\\static\\imgs"
json_foler_path = "C:\\Users\\amrcmeu\\Documents\\AE\\appScripts\\static\\json\\data.json"

#client.api_key = 'your_openai_api_key'  # Replace this with your actual API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')

@app.route('/exhibition')
def exhibition():
    images = [f for f in os.listdir(img_folder_path) if os.path.isfile(os.path.join(img_folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    with open(json_foler_path) as f:
        json_data = json.load(f)
        num_of_imgs = len(json_data)
        # print (jsonify(json_data))

    return render_template('exhibition.html', images=images, json_data=json_data, num_of_imgs=num_of_imgs)

@app.route('/generate', methods=['POST'])
def generate():
    prompt_ = request.form['prompt']
    # Storing the user_prompt here to be saved later in the json structure
    user_prompt = prompt_ 
    # I need to create a json library with 'number':'int of the image it refers to' and 'prompt' 'actual given prompt'
    prompt_ = prompt_ + ". The image MUST be in black and white and a vectorised image."
    print(prompt_)
    
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt_,
            size="1024x1024",
            quality="standard",
            n=1,
            )
        
        print (response)
        image_url = response.data[0].url
        image_file = requests.get(image_url)

        # List all items in the specified folder
        imgs = os.listdir(img_folder_path)
        
        # Count the number of items
        num_imgs = len(imgs) + 1
        file_name = "img" + "_t" + str(num_imgs) + ".PNG"

        image_path = os.path.join(img_folder_path, file_name)

        with open(image_path, 'wb') as f:
            f.write(image_file.content)

        prompt_data = { str(num_imgs) : user_prompt}

        # Load existing data from the file
        prompts = read_json_file()

        # Here we append the new data
        prompts.update(prompt_data)

        # Write the updated data back to the file
        write_json_file(prompts)

        return render_template('index.html', image_url=image_url)
        
        
        
    except Exception as e:
        print(e)
        return 'Error generating image', 500
    # finally:
    #     return render_template('index.html', image_url=image_url)

@app.route('/info',)
def info():
    return render_template('info.html')



# Helper function to read from the JSON file
def read_json_file():
    if os.path.exists(json_foler_path):
        with open(json_foler_path, 'r') as file:
            return json.load(file)
    else:
        return {}

# Helper function to write to the JSON file
def write_json_file(data):
    with open(json_foler_path, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    app.run(debug=True)
