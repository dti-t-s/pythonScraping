import sys
import urllib.request

url = "https://gihyo.jp/dp/"
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

request = urllib.request.Request(url=url, headers=headers)

#f = urlopen('https://www.yahoo.co.jp/')
f = urllib.request.urlopen(request)
# HTTPヘッダーからエンコーディングを取得する（明示されていない場合はutf-8とする）
encoding = f.info().get_content_charset(failobj='utf-8')
print('encoding:', encoding, file=sys.stderr) # エンコーディングを標準エラー出力に出力する

text = f.read().decode(encoding) # 得られたエンコーディングを指定して文字列にデコードする
print(text) # デコードしたレスポンスボディを標準出力に出力する
