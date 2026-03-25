from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json

    # Score-based system
    dev_score = data.get("coding", 0) + data.get("problem", 0)
    cyber_score = data.get("security", 0) + data.get("network", 0)
    design_score = data.get("design", 0)

    if dev_score >= cyber_score and dev_score >= design_score:
        career = "Software Developer"
    elif cyber_score >= dev_score and cyber_score >= design_score:
        career = "Cybersecurity Analyst"
    else:
        career = "UI/UX Designer"

    return jsonify({
        "career": f"Recommended Career: {career}"
    })

if __name__ == "__main__":
    app.run(debug=True)
