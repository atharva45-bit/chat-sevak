from flask import Flask, render_template, request, jsonify
from rules import get_bot_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)
    user_message = data.get('message', '') if data else ''
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)
