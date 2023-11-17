def total (a, b) :
    return a + b

def minus (a, b) :
    return a - b

def multiply (a, b) :
    return a * b

def divide (a, b) :
    return a / b

operators = {
    '+': total,
    '-': minus,
    '*': multiply,
    '/': divide,
}

while (True):
    a = input('Nhập vào ký tự a: ')
    b = input('Nhập vào ký tự b: ')
    ch = input('Nhập vào ký tự ch: ')
    
    if (ch in operators) :
        result = operators[ch](float(a), float(b))
        print(f'Kết quả : {int(result)}')
        break
    else : 
        print(f'{ch} không phải là một toán tử')