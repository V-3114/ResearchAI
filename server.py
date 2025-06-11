from flask import Flask, render_template, request, jsonify
from gpt import ask_gpt_ai

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_input = data.get('user_input', '')
    print("Received input:", user_input)
    gpt_response = ask_gpt_ai(user_input)
    
    # Send GPT response to frontend
    return jsonify({"response": gpt_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)