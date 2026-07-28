# n, k = map(int, input().split())

# # 1以上n以下でx,y,z　3枚のカードに整数割り振る
# # 1 <= K <= 9000
# # カードx, y, zの3枚
# # x, yの二枚が先に決まれば、z = k - x - y で求められる→ (O(n*2)) で済む (O(n*3))まで回さなくてよくなる

# cnt = 0  # x, y, zの合計がKになる組み合わせの数

# for x in range(1, n + 1):
#     for y in range(1, n + 1):
#         z = k - x - y
#         # ↑ ここですでに x+y+z=k のチェックが完了している
#         # x+y+z=k → z=k-x-y
#         # zが1以上n以下になっているかチェックする
#         # if 1 <= z <= n and ((x + y + z) == k): ←なのでこのx+y+z == k の評価いらない
#         if 1 <= z <= n:
#             cnt += 1

# print(cnt)


# 別回答
n, k = map(int, input().split())
cnt = 0

for x in range(1, n + 1):
    for y in range(1, n + 1):
        z = k - x - y
        # 1 <= z <= n の制約より
        # zが1より小さくなった場合はそれ以降の計算をスキップする
        # 1 <= z のチェックを担当
        if z < 1:
            break

        # z <= n のチェックを担当
        if z <= n:
            cnt += 1

print(cnt)
