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
