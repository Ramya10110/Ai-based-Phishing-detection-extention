🔐 AI-Powered Phishing Detection Chrome Extension
🚀 Overview

This project is a real-time phishing detection system built as a Chrome extension using Machine Learning and cybersecurity principles.

It analyzes the current website’s URL, extracts meaningful security features, and predicts whether the site is Safe, Suspicious, or Phishing with a risk score.

💡 Features
🌐 Real-time URL analysis
🧠 Machine Learning-based detection (Random Forest)
🔍 Feature extraction from URLs (domain, structure, keywords)
⚠️ Risk classification:
✅ Safe
⚠️ Suspicious
🚨 Phishing
📊 Risk percentage display
🔗 Chrome Extension integration
🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript (Chrome Extension)
Backend: Python, Flask
Machine Learning: Scikit-learn (Random Forest)
Others: Flask-CORS, Pandas
🧠 How It Works
User opens a website
Extension captures the current URL
URL is sent to Flask backend
Backend:
Extracts features (length, domain, keywords, etc.)
Feeds into trained ML model
Model returns probability score
Extension displays result instantly
📁 Project Structure
ai-based-phishing-detection/
│
├── backend/
│   ├── app.py
│   ├── train.py
│   ├── phishing.csv
│   └── model.pkl
│
└── extension/
    ├── manifest.json
    ├── popup.html
    ├── popup.js
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-link>
cd ai-based-phishing-detection/backend
2️⃣ Install Dependencies
pip install pandas scikit-learn flask flask-cors
3️⃣ Train Model
python train.py
4️⃣ Run Backend
python app.py
5️⃣ Load Chrome Extension
Go to chrome://extensions/
Enable Developer Mode
Click Load Unpacked
Select the extension/ folder
🧪 Testing

Try with:

✅ Safe Sites
https://google.com
https://github.com
⚠️ Suspicious URLs
http://secure-login-paypal.com
http://verify-bank-account.com
⚠️ Limitations
Uses a small dataset (limited accuracy)
Only analyzes URL-based features
Does not check page content or reputation APIs
🔥 Future Improvements
🔍 HTML & login form analysis (Fake Login Detector)
🌐 Integration with Google Safe Browsing API
📊 Larger phishing dataset (100K+ URLs)
🧠 Deep learning-based detection
🎨 Improved UI/UX
💙 Learning Outcome

This project helped in understanding:

Real-world phishing techniques
Feature engineering in cybersecurity
ML model integration with web applications
Browser extension development
📌 Author

Ramya K
Cybersecurity Enthusiast | AI & ML Learner

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or improve it!
