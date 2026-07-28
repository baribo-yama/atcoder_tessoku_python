# セットアップ

環境セットアップについては以下のサイトを参照
https://qiita.com/hotpepsi/items/4cf9e6d3f7e8911a9771

注意点：
- atocdder-guiとplaywrightを使った初回のatcoderへのログインで詰まる可能性あり
- playwright経由でatcoderへログインしようとすると、bot扱いされてはじかれるかも

リポジトリ直下に以下のフォルダ、ファイルを準備
- test/
- input.txt



# 使い方

## 準備

まず仮想環境を有効化する

```bash
source .venv/bin/activate
```

競技プログラミングの鉄則　演習問題集
https://atcoder.jp/contests/tessoku-book/tasks/

↑ ここから問題選択して、problems/ に問題URLの末尾URIをファイル名とした.pyファイルを作成する

例えば
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
の問題を解きたい場合は
problems/ に tessoku_book_g.py を作成する

あとはその中で回答コードを書く

## サンプルケース自動テスト
atcoder-guiが自動でテストケース引っ張ってきてくれる
実行するとAC確認ができる

### ショートカット実行
💡.vscode/ のlaunch.jsonとtasks.jsonに実行ショートカット設定あり

ctrl + shift + B
or
ctrl + shift + N

### コマンド実行
例としてtessoku_book_a01.pyを対象
```bash
./cptest.sh tessoku_book_a01
```

## input.txtに任意値いれてテスト実行する方法
input.txtにatcoderの問題の標準入力に合わせた形式で値を入れる
例）

```
8
5
2 3
3 6
5 7
3 7
1 5
```

### ショートカット実行
F5キー　押すだけ
↑デフォルトのデバッグキーかな

### コマンド実行
input.txtに入力値入れる
```bash
python3 problems/[実行したいファイル] < input.txt
```

例：
python3 problems/tessoku_book_d.py < input.txt


# この環境作るために参考にしたサイト
- https://qiita.com/hotpepsi/items/4cf9e6d3f7e8911a9771
