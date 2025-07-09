from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import pdfkit

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Placeholder for Gemini API integration
def generate_guide(data):
    # Here you would call the Gemini API with user data
    # For now, return a dummy guide
    guide = f"""
    Step 1: Research your business idea: {data.get('business_ideas')}
    Step 2: Assess your skills: {data.get('skills_interests')}
    Step 3: Plan your budget: {data.get('budget')}
    Step 4: Set up in {data.get('location')}
    Step 5: Start your business!
    """
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
