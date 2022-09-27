import random
t_sum = random.randint(1,26)
k_sum = random.randint(1,t_sum-1)
def moji(t,k):
    t_lst = []
    t_lst1 = []
    k_lst = []
    k_lst1 = []
    for i in range(65,91):    
        t_lst.append(i)
    random.sample(t_lst,k) 
    for t in t_lst:
       if t not in t_lst:
          t_lst1.append(t)
    print(t_lst)

    for j in range(k):
        j = random.choice(t_lst)
        k_lst.append(j)
    for k in k_lst:
        if k not in k_lst:
            k_lst1.append(k)
    print(k_lst1)

print(moji(t_sum,k_sum))       
            
