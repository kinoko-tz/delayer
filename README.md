# delay-response-server

## なにこれ

非同期処理の練習用の、時間がかかるAPIリクエストを再現したAPIサーバ。

## 必要なもの

* docker
* docker-compose

## サーバー起動方法

1. `git clone https://github.com/iroha-abc/delay-response-server.git`
1. `cd delay-response-server`
1. `docker-compose up -d`

## API仕様

### URL

`http://localhost:5000/delay/v1/{delayTime}`

### リクエスト

|パラメータ種|パラメータ名|型|説明|
| -- | -- | -- | -- |
|クエリパラメータ|delayTime|Number|指定秒数後にレスポンスを返す。|

### レスポンス

レスポンスはjsonで返される。

|key名|型|説明|
| -- | -- | -- |
|id|String|uuid|
|delayTime|Number|指定された秒数をそのまま返す。|
|callCount|Number|1~1000でこのURLが呼び出された回数を返却する。1001回目は1を返す。|

### 注意

起動した際のwarningにもある通り、flaskのデバック環境で起動するので、公開はしないでください。
