# NicovideoCellar
ニコ動のマイリストを登録するとローカルのディレクトリにダウンロードします。

## Instration
### 動作要件
+ ffmpegとswftoolsを使えるようにしておいてください
+ python3.4.3 で動作確認済み

### インストール

 `git clone https://github.com/roronya/NicovideoCellar $HOME/.NicovideoCellar`

上記コマンドを実行後

`$HOME/.NicovideoCellar/bin`

をPATHに追加

### 設定
.NicovideoCellar/config.json.distをconfig.jsonにリネームして、ニコ動のログインメールアドレスとパスワードと、ダウンロードしてきたムービーを保存するパスを書き込んむ

### 使い方
`nvc`
