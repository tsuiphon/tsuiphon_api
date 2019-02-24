## セットアップ

virtualenvとpython3がインストールされてるかの確認
```
which python3
which virtualenv
```

入ってない場合はインストール(Mac)
```
brew install python3
pip install virtualenv
```

プロジェクトのディレクトリを作成。
```
mkdir tsuiphon_project
cd tsuiphon_project
```

virtualenvで環境を新たに作る。`/usr/local/bin/python3`はpython3の場所。
```
virtualenv --python=/usr/local/bin/python3 --no-site-packages env
source env/bin/activate
```

ソースをクローン
```
git clone https://github.com/tsuiphon/tsuiphon_api_django.git
```

依存パッケージのインストール
```
pip install -r tsuiphon_api_django/requirements.txt
```

`default_secret.json`をベースに`secret.json`を設定する。
```
cp tsuiphon_api_django/tsuiphon_api_django/default_secret.json tsuiphon_api_django/tsuiphon_api_django/secret.json
vi tsuiphon_api_django/tsuiphon_api_django/secret.json
```
編集方法の補足
- consumer keyとconsumer secretを設定。
- django_secretは予測不可能なランダムな文字列を設定。

データベースのマイグレーション
```
cd tsuiphon_api_django
python manage.py migrate
```

## 起動方法
```
python manage.py runserver
```

## url
- トップページ:http://127.0.0.1:8000/
- トーク画面:http://127.0.0.1:8000/talk_page/

## コード修正時の確認事項

### 新たなパッケージをインストールする場合
新たなパッケージをインストールとき以下を実行。
```buildoutcfg
rm requirements.txt
pip freeze > requirements.txt
```

### 新たなモデルの追加
```
vi ./hoge/models.py# models.pyの編集
python manage.py makemigrations 
python manage.py migrate
```
トラブルシューティング:
https://trybeetle.com/en/detail/4/
