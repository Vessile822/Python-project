# 輸入第一列含有一個正整數 T (T < 30)，用來表示接下來有 T 組測資。
# 每組測試資料共 1 + N 列，
# 第一列含有一個正整數 N (N < 50)，用來表示牆壁的數目。
# 第 2 ~ N + 1 列皆含有一個非負整數，用來表示 N 面牆壁的高度。

# 在跳躍的過程當中，high jump 代表小明跳到了一面較高的牆，反之，low jump 代表小明跳到了一面較低的牆。
# 2019/5/27


T = int(input("組數:"))
sum_arr = []

if 0<T<31:
    for i in range(T):
        N = int(input("牆壁數目:"))
        wall_arr = []
        if 0<N<51:
            for j in range(N):
                x = int(input("高度:"))
                wall_arr.append(x)
            H_jump = 0
            L_jump = 0
            for k in range(N-1):
                if wall_arr[k]>wall_arr[k+1]:
                    L_jump +=1
                elif wall_arr[k]<wall_arr[k+1]:
                    H_jump +=1     
            sum_arr.append(H_jump)
            sum_arr.append(L_jump)
        else:
            print("0 0")
            break
else:
    print("0 0")

while 0<N<51:
    s = 0
    for i in range(T):
        print(sum_arr[s],sum_arr[s+1])
        s += 2
    else:
        break


# list_t = []
# t = int(input("請輸入T組測資: "))
# for i in range(t):
#     high = 0
#     low = 0
#     list_n = []
#     n = int(input("輸入牆壁面數: "))
#     list_n.append(int(input("牆壁高度: ")))
#     temp = list_n[0]
#     for j in range(1, n):
#         list_n.append(int(input("牆壁高度: ")))
#         if(list_n[j] > temp):
#             high += 1
#         if(list_n[j] < temp):
#             low += 1
#         temp = list_n[j]
#     list_t = list_t + [high, low]
# k = 0
# for i in range(t):
#     print(list_t[k], list_t[k+1])
#     k += 2