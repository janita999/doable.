from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import pdfkit

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Placeholder for Gemini API integration
import requests
import os

def generate_guide(data):
    api_key = os.environ.get('GEMINI_API_KEY')
    prompt = (
        f"Create a detailed, step-by-step guide for a young entrepreneur (age group: {data.get('age_group')}) "
        f"who wants to start a {data.get('business_type')} in {data.get('location')}. "
        f"Business idea: {data.get('business_ideas')}. "
        f"Time commitment: {data.get('time_commitment')} hours/week. "
        f"Budget: {data.get('budget')}. "
        f"Skills/interests: {data.get('skills_interests')}. "
        f"Additional details: {data.get('additional_details')}. "
        "The guide should be actionable, detailed, and tailored to their background. "
        "Include as many steps as needed, with practical instructions and tips."
    )
    response = requests.post(
        "https://generativelanguage.googleapis.com/v1/models/gemini-1.0-pro-latest:generateContent",
        params={"key": api_key},
        json={
            "contents": [{"parts": [{"text": prompt}]}]
        }
    )
    result = response.json()
    print(result)  # Debug: see the actual response

    if "candidates" in result:
        guide = result['candidates'][0]['content']['parts'][0]['text']
    elif "error" in result:
        guide = f"Error from Gemini API: {result['error'].get('message', 'Unknown error')}"
    else:
        guide = "Unexpected response from Gemini API."
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
