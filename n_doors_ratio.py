import random

total = 100000
win, lose = 0, 0
n = 4

for i in range(total):
    # 準備n個門 [0和1] 0:沒有獎 1:中獎
    doors = [0] * (n-1)
    idx=random.randint(0, len(doors)-1)
    
    # insert(插入位置, 插入值)
    doors.insert(idx, 1)
    # print("準備的門:", doors)
    
    # 隨機選一個門(random) (X)
    idx=random.randint(0, len(doors)-1)
    # print("選到的門:", doors[idx])
    
    # pop(idx):刪除那個index ; pop():刪除最後一個
    doors.pop(idx)
    # print("剩下的門:", doors)
    # 在剩下的門裡面，主持人開一個沒有獎的 (X)
    # remove(值):從左到右找到第一個吻合的值並且移除
    doors.remove(0)
    # print("剩下的門:", doors)
    
    # 扣除剛剛那兩道以後，再選一個帶回家
    idx=random.randint(0, len(doors)-1)
    if doors[idx] == 1:
        # print("中獎")
        win = win + 1
    else:
        # print("沒中獎")
        lose = lose + 1

ratio = win / total
print("贏的機率是:", ratio)
