# raspintone

Raspberry Piを使ってkintoneにレコードを登録する。  
ボタンがチェックボックスの選択肢に対応している。

## setup

### make kintone app

1. kintoneアプリをつくる
2. チェックボックスを配置する。選択肢は最大8個まで。フィールドコードは「チェックボックス」
3. アプリでレコード追加とアプリ管理権限をもつAPIトークンを生成する

### raspintone settings

1. `git clone https://github.com/ehimemikan/raspintone.git`
2. `kintone.yml`ファイルをおく
```yaml
url: https://XXXX.cybozu.com
app_id: 作ったアプリのid
token: 作ったアプリで発行したAPIトークン
```

## run

`./raspintone.py`
