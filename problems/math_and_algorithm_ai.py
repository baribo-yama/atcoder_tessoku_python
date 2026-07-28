n, q = map(int, input().split())

# n : 日数
# q : 入力数

# n日分の各日来場者が格納される
visitors = list(map(int, input().split()))

# --- 1. 前処理：累積和配列の作成 (O(N)) ---
# 0日目の人数=0を格納するので、
# [0] * n ではなく、一つ追加した [0] * (n + 1)にする
# あとからs[l]やs[r]と指定したときにインデックスと番号がぴったり合う
# s[i] = 1日目からi日目までの合計
s = [0] * (n + 1)

# 1日目からn日目までの人数の累積和を出す
for i in range(1, n + 1):
    # 1つ前とvisitors[i]の値を足していく（一つ前と現在を足す）
    s[i] = s[i - 1] + visitors[i - 1]

# --- 2. クエリ処理 (O(Q)) ---
# クエリ処理（q分の入力）
for _ in range(1, q + 1):
    l, r = map(int, input().split())
    print(s[r] - s[l - 1])
