import random

my = int(input("請輸入 0.剪刀 1.石頭 2.布:"))
com = random.randint(0, 2)
trans = ["剪刀", "石頭", "布"]
print("我出的:", trans[my])
print("電腦出的", trans[com])

if my == (com + 1) % 3:
    print("我贏了!")
elif com == (my + 1) % 3:
    print("我輸了...")
else:
    print("平手")
