n = int(input())
arr = []
tmp = 2


while (n >= tmp):
    k = n % tmp
    if (k == 0):
        arr.append(str(tmp))#存入陣列
        n = n / tmp         #更新結果
    else:
        tmp = tmp + 1       #除數+1
    
if len(arr) == 1:
    print("True")
else:
    for i in arr:
        print(i)
    

    




       