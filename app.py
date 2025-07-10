from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import pdfkit
import requests
import os

def list_gemini_models():
    api_key = os.environ.get('GEMINI_API_KEY')
    response = requests.get(
        "https://generativelanguage.googleapis.com/v1/models",
        params={"key": api_key}
    )
    print("Available models:", response.json())

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Placeholder for Gemini API integration
import requests
import os

import json
import urllib.request

def generate_guide(data):
    api_key = "AIzaSyDtPT1T-7plg6ncewetLEv7xWwdi3VV2pM"  # <-- PUT YOUR GEMINI API KEY HERE
    endpoint = https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyDtPT1T-7plg6ncewetLEv7xWwdi3VV2pM
    prompt = f"""
    Give me a step-by-step business guide based on:
    - Business idea: {data.get('business_ideas')}
    - Skills/Interests: {data.get('skills_interests')}
    - Budget: {data.get('budget')}
    - Location: {data.get('location')}
    """

    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    req = urllib.request.Request(endpoint, data=json.dumps(payload).encode('utf-8'), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            guide = result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        guide = f"Error from Gemini API: {e}"

    return guide

@app.route('/generate-guide', methods=['POST'])
def generate_guide_route():
    data = request.form.to_dict()
    guide = generate_guide(data)
    # Save guide in session or return directly
    return jsonify({'guide': guide})

@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    guide = request.json.get('guide', '')
    # Generate PDF from guide text
    pdf_path = 'guide.pdf'
    pdfkit.from_string(guide, pdf_path)
    return send_file(pdf_path, as_attachment=True)

# Serve frontend files (index.html, etc.)
@app.route('/')
def root():
    return app.send_static_file('index.html')

import os
if __name__ == '__main__':
       port = int(os.environ.get('PORT', 10000))
       app.run(host='0.0.0.0', port=port)
import requests
import os


