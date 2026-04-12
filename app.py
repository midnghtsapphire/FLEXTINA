from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/agent', methods=['POST'])
def run_agent():
    data = request.get_json()
    niche = data.get('niche', '')
    prompt = data.get('prompt', '')
    
    # TODO: Integrate with agent system
    result = f"Processing niche: {niche} with prompt: {prompt}"
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)