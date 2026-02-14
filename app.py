from flask import Flask, jsonify
import requests

app = Flask(__name__)

USERNAME = "kristianstauding"

def get_followers():
    url = f"https://www.tiktok.com/@{USERNAME}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    html = response.text

    marker = '"followerCount":'
    start = html.find(marker) + len(marker)
    end = html.find(',', start)
    followers = int(html[start:end])

    return followers

@app.route("/")
def home():
    return "TikTok Counter Running"

@app.route("/followers")
def followers():
    return jsonify({
        "followers": get_followers()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
