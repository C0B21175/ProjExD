import random
t_sum = random.randint(1,26)
k_sum = random.randint(1,t_sum-1)

def moji(t,k):
    t_1 = []
    t_2 = []
    k_1 = []
    k_2 = []
    for i in range(65,91):    
        t_1.append(i)
    random.sample(t_1,k) 
    for t in t_1:
       if t not in t_1:
          t_2.append(t)
    print(t_1)

    for j in range(k):
        j = random.choice(t_1)
        k_1.append(j)
    for k in k_1:
        if k not in k_1:
            k_2.append(k_1)
    print(k_1)

print(moji(t_sum,k_sum))       
            
