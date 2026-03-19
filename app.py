from flask import Flask, render_template, request, jsonify
from utils.detector import detect_scam

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze_text", methods=["POST"])
def analyze_text():
    data = request.json
    text = data.get("text", "").lower().strip()

    print("Received:", text)  

    if not text:
        return jsonify({
            "status": "⚠️ No Speech",
            "risk": 0,
            "reasons": ["No input detected"]
        })

    result = detect_scam(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)