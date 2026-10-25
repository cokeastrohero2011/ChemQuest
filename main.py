from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

@app.route("/api/molecule", methods=["POST"])
def molecule_proxy():
    """Proxy endpoint for OpenAI API calls to keep API key secure"""
    import requests
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return jsonify({"error": "OPENAI_API_KEY not configured"}), 500
    
    try:
        data = request.get_json()
        
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json=data,
            timeout=30
        )
        
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)