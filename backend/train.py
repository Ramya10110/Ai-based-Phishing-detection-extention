import pandas as pd
import re
from urllib.parse import urlparse
from sklearn.ensemble import RandomForestClassifier
import pickle

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

data = pd.read_csv("phishing.csv")

X = [extract_features(url) for url in data['url']]
y = data['label']

model = RandomForestClassifier(n_estimators=200, max_depth=10)
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved as model.pkl")