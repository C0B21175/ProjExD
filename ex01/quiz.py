import random
r = random.randint(0,2)
def shutudai(i):
    s_l = ["サザエの旦那の名前は？","カツオの妹の名前は？ ","タラオはカツオから見てどんな関係？"]
    ans1 = []
    ans2 = []
    ans3 = []    
    print(f"問題：\n{s_l[i]}")
    a = input("答えるんだ：")
    if i == 0 and a in ans1:
        return 

print(shutudai(r)) 

