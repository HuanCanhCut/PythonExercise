L = []

i = 1
while True:
    num = input(f'Nhập số thứ {i} : ')
    if not num: 
        break
    L.append(num)

    i += 1 

L.sort(reverse=False)
print(f'Danh sách theo thứ tự tăng dần là : {L}')

L.sort(reverse=True)
print(f'Danh sách theo thứ tự giảm dần là : {L}')