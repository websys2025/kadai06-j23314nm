import requests

# スマートフォン保有率の統計を取得するプログラム
# 使用データ: 全国消費実態調査（e-Stat）
# エンドポイント: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# 統計表ID(statsDataId)：0003345395
# 目的：スマートフォンの保有世帯数や割合を取得
# 機能：
# - メタ情報、注釈、解説などを含めたデータ取得
# - JSON形式で結果を表示

# APIキー
APP_ID = "7092a46efe787eba5fa04e5a8dfa25e9a0cd9135"

# e-Stat APIのURL
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# リクエストパラメータ設定
params = {
    "appId": APP_ID,               # APIキー
    "statsDataId": "0003345395",   # スマートフォン保有状況の統計表ID
    "lang": "J",                   # 日本語で取得
    "metaGetFlg": "Y",             # メタ情報を取得
    "cntGetFlg": "N",              # 件数情報を取得しない
    "explanationGetFlg": "Y",      # 解説を取得
    "annotationGetFlg": "Y",       # 注釈を取得
    "sectionHeaderFlg": "1",       # セクションヘッダーを表示
    "replaceSpChars": "0"          # 特殊文字の変換なし
}

# APIリクエストを送信
response = requests.get(API_URL, params=params)

# レスポンスをJSON形式で表示
print(response.json())
