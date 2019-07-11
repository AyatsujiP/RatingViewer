# NCS Rating Viewer

## 概要
NCSレーティングのプレーヤーごとの過去の履歴などを見られるようにするものです。
現在は機能が少なめですが、FIDEのレーティングページのようなものにすることを想定しています。

## 使い方
クローンした後、manage.pyのあるディレクトリに移動して、以下を実行してください。

    manage.py migrate

db.sqlite3が作成されます。
データベース内のMembersとRatingsテーブルに、それぞれスキーマどおりにメンバーとレーティングを入れてください。
(氏名が含まれるため、データベースとしては配布しません)

基本的に、以下のSQLを参考に入れてください。


    INSERT INTO ratings (id, ncs_id, rating, update_month) VALUES ([通番], [NCSID],[レーティング],[レーティングの更新日(yyyy-mm-dd)])
    INSERT INTO members (id, ncs_id,name_alphabet,name_kanji) VALUES ([通番], [NCSID],[アルファベット氏名],[漢字氏名])


その後、以下を実行してください。

    manage.py runserver