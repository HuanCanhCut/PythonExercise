import math

def ht_skcp(n):
    scp = []
    for i in range(2, n + 1):
        if (float(math.sqrt(i)).is_integer() != True): 
            scp.append(i)
    return scp

n = int(input('Nhập n : '))

print(f'Các số chính phương từ 2 => n là : {ht_skcp(n)}')
