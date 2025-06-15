import requests

# 千葉市の気象データを取得するプログラム
# 使用データ: Tsukumijima.net API（天気予報）
# エンドポイント: https://weather.tsukumijima.net/api/forecast/city/120010
# 目的：千葉市の気象データを取得
# 機能：
# - 今日、明日、明後日の天気、気温、降水確率などのデータを取得
# - JSON形式で結果を表示

# 千葉市の天気データを取得するAPI URL
API_URL = "https://weather.tsukumijima.net/api/forecast/city/120010"

# APIリクエストを送信
response = requests.get(API_URL)

# レスポンスをJSON形式で表示
print(response.json())
