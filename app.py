from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

# APIキー
api_key = ""

# ブライトンのチームIDを設定
team_id = 51

# APIからデータを取得する関数
def get_player_stats():
    url = f"https://api-football-v1.p.rapidapi.com/v3/players?team={team_id}"
    querystring = {"league":"39","season":"2022"}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    print(data)
    return data["response"]
# 三笘選手の分が取得できなかったので別に取得
def get_mitoma_stats():
    url = f"https://api-football-v1.p.rapidapi.com/v3/players?team={team_id}"
    querystring = {"league":"39","season":"2022","search":"Mitoma"}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    print(data)
    return data["response"]
# ルートURL
@app.route('/')
def index():
    players = get_player_stats()
    mitoma = get_mitoma_stats()
    return render_template('index.html', players=players,mitoma=mitoma)

if __name__ == '__main__':
    app.run(debug=True)
