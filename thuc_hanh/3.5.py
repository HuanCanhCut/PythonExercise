n = int(input('nhập vào phần tử danh sách (1<n<1000): '))
if 1 < n < 1000:
    x = int(input('nhập vào số x: '))
    tich = 1
    danhSach = []

    for i in range(2,n + 1):
        danhSach.append(i)
        tich *= i

    print(danhSach)
    print('tổng các phần tử trong danh sách trên là: ',sum(danhSach))
    print('tích của các phần tử trong danh sách là ', tich)
    if x in danhSach:
        print('trong danh sách trên có phần tử  bằng x') 
    is_sort = True
    trungBinhCong = 0

    for i in range(1,len(danhSach)):
        trungBinhCong = sum(danhSach) / len(danhSach)
        if danhSach[i] < danhSach[i-1]:
            is_sort = False 

    if is_sort == True:
        print('danh sách theo thứ tự tăng dần')

    print('Trung binhf cong :' , trungBinhCong)
            
    
else:
    print('vui lòng nhập phần tử 1<n<100')