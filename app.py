from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
from google import genai
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Configure AI API
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Erlaube Aufrufe von deinem externen Frontend


@app.route("/")
def health():
    return "Backend läuft", 200


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()

    if not question:
        return jsonify({"error": "Keine Frage übergeben"}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
        )
        answer_text = response.text
        return jsonify({"answer": answer_text})
    except Exception:
        # Auf PythonAnywhere siehst du den genauen Fehler im Error-Log
        return jsonify({"error": "Fehler bei der AI-Anfrage"}), 500


if __name__ == "__main__":
    # Für lokales Testen. Auf PythonAnywhere wird die App über WSGI gestartet.
    app.run(debug=True)