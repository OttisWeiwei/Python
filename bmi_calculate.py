# bmi = weight(kg) / height(m) ^ 2 
weight = float(input("請輸入體重:"))
height = float(input("請輸入身高:"))
bmi = weight / (height / 100) ** 2
print("你的體重是" + str(weight))
print("你的身高是" + str(height))
print("bmi是" + str(bmi))

#  >, >=, <, <=, ==
if bmi > 25:
    print("過重")
    print("需要少吃一點")
else:
    print("正常")
print("你已經很努力囉!")
