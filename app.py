from flask import Flask, request, jsonify
from flask_cors import CORS
from model import CareerRecommender

app = Flask(__name__)
CORS(app)

recommender = CareerRecommender()

@app.route('/api/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()

        result = recommender.get_recommendation(data)

        return jsonify({
            "status": "success",
            "recommended_career": result
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
