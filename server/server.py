from flask import Flask, request, jsonify
import util
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) 

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    print(image_data)

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/')
def home():
    return 'Hello, Images!'

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
      # Use the environment variable for port (Render will set it automatically)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)