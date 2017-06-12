import csv

# ファイルを書き込み用に開く　newline=''として改行コードの自動変換を抑制する
with open('top_cities.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, ['rank', 'city', 'population'])
    writer.writeheader() # 1行目のヘッダーを出力する
    # writerows()で複数の行を一度に出力する　引数は辞書のリスト
    writer.writerows([
        {'rank': 1, 'city': '上海', 'population': 123},
        {'rank': 2, 'city': 'カラチ', 'population': 123},
        {'rank': 3, 'city': '天津', 'population': 123},
        {'rank': 4, 'city': 'イスタンブル', 'population': 123},
        {'rank': 5, 'city': '北京', 'population': 123},
    ])