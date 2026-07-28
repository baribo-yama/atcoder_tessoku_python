#!/bin/bash
problem_name=$1
test_dir=test/${problem_name}
base_url_hyphen="tessoku-book" # 鉄則本固定にする場合

# テストディレクトリがなければダウンロード
if [ ! -d "${test_dir}" ]; then
    # まずはファイル名そのままで試す
    oj dl -d "${test_dir}" "https://atcoder.jp/contests/${base_url_hyphen}/tasks/${problem_name}"

    # 失敗（404）したら、末尾の数字を削って再試行（鉄則本対策）
    if [ $? -ne 0 ]; then
        # 数字を削った名前（例: tessoku_book_a01 -> tessoku_book_a）
        short_name=$(echo $problem_name | sed 's/[0-9]*$//')
        oj dl -d "${test_dir}" "https://atcoder.jp/contests/${base_url_hyphen}/tasks/${short_name}"
    fi
fi

# 実行
oj test -c "python3 problems/${problem_name}.py" -d "${test_dir}"
