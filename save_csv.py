import csv

# ファイルを書き込み用に開く　newline=''として改行コードの自動変換を抑制する
with open('top_cities.csv', 'w', newline='') as f:
    writer = csv.writer(f) # csv.writerはファイルオブジェクトを引数に指定する
    writer.writerow(['rank', 'city', 'population']) # 1行目のヘッダーを取得する
    # writerows()で複数の行を一度に出力する　引数はリストのリスト
    writer.writerows([
        [1, '上海', 123],
        [2, 'カラチ', 123],
        [3, '北京', 123],
        [4, '天津', 123],
        [5, 'イスタンブル', 123],
    ])