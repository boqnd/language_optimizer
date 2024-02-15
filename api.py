from flask import Flask, request, jsonify
from translator import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    translator = Translator(text)
    translated_text = translator.translate()
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)