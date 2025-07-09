# doable.

A minimalistic AI-powered website to generate step-by-step business guides for young entrepreneurs.

## Features
- Multi-page frontend (Home, About, FAQs, Get Started, Guide)
- Flask backend for AI and PDF features
- Gemini API integration (add your API key)
- Download guide as PDF

## Local Setup

1. **Clone the repository**
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **(Optional) Install wkhtmltopdf** for PDF support:
   - Download from https://wkhtmltopdf.org/downloads.html
   - Make sure it's in your PATH
4. **Run the app:**
   ```
   python app.py
   ```
5. **Open `index.html` in your browser**

## Gemini API Setup
- Get your Gemini API key from Google Cloud Console
- Add integration in `app.py` where indicated
- Set your API key as an environment variable on Render

## Deploying on Render
1. **Push your code to GitHub**
2. **Create a new Web Service on [Render](https://render.com/):**
   - Connect your GitHub repo
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python app.py`
   - Add environment variable for your Gemini API key
3. **Visit your Render URL to use your site!**

## Notes
- You can update the frontend design at any time by editing the HTML/CSS files.
- For help, ask your AI assistant!
