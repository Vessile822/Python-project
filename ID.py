# 將英文字轉換成數字後，共有十一個數字，
# 例如：Y131452080 → 32131452080

# 將這十一個數字依下列規則做乘法：
# 第二個數字乘 9，第三個數字乘 8，第四個數字乘 7，依此類推，直到第十個數字乘 1，

# 10減去 加總後的個位數是檢查碼，檢查碼必須跟原字號尾數一樣
# 這個身份證字號才是正確的字號。


n = input()
D = list(n)
index = 9
temp = 0
total = 0
one = D.pop(0)

for i in range(len(D)):
    temp = (int(D[i])*index)%10
    index = index-1
    total = total+temp 
b = total+int(one)

if (10-(b%10))%10==int(D[9]):
    print("True")
else:
    print("False")
    