# s = int(input())
# binary = []

# while s != 0:
#     # あまり
#     mod = s % 2
#     # 商
#     s = s // 2
#     binary.append(mod)

# binary.reverse()  # 取得した二進数を逆順にする
# length = len(binary)

# if length < 10:
#     diff_cnt = 10 - length
#     zero_cnt = "0" * diff_cnt
#     result = "".join(map(str, binary))
#     print(zero_cnt + result)
# else:
#     result = "".join(map(str, binary))
#     print(result)

# 書き換え
s = int(input())
binary = []

while s != 0:
    binary.append(s % 2)
    s //= 2

binary.reverse()
print("".join(map(str, binary)).zfill(10))

# zfill はゼロ埋めしてくれる関数
# zero fill ってことかな
