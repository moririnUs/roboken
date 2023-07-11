import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 認証情報ファイルへのパスを設定します
credentials_path = 'disbot-392501-93dc06974db8.json'

# スコープと認証情報を指定してクライアントを作成します
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
client = gspread.authorize(credentials)

# スプレッドシートのキーを指定してシートを開きます
spreadsheet_key = 'your-spreadsheet-key'
sheet = client.open_by_key(spreadsheet_key).sheet1

# データを読み込む
data = sheet.get_all_records()

# データを表示する
for row in data:
    print(row)