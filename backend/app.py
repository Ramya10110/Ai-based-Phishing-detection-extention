from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    return [
        len(url),
        url.count('.'),
        url.count('-'),
        int('https' in url),
        int('@' in url),
        int(bool(re.search(r'\d', url))),
        len(domain),
        int('login' in url.lower()),
        int('verify' in url.lower()),
        int('secure' in url.lower())
    ]

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()

    if not data or 'url' not in data:
        return jsonify({"result": "Error"})

    url = data['url']
    features = extract_features(url)

    probability = model.predict_proba([features])[0][1]

    if probability > 0.7:
        result = f"⚠️ Phishing Website (Risk: {round(probability*100,2)}%)"
    else:
        result = f"✅ Safe Website (Risk: {round(probability*100,2)}%)"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)