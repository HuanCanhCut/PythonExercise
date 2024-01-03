from datetime import  datetime

date = datetime.now()


birth = int((input('Nhập vào năm sinh của bạn : ')))
currentYear = date.year

data = [
    {
        'age': 60,
        'class': 'Người Già'
    }, 
    {
        'age': 40,
        'class': 'Trung Niên'
    },
    {
        'age': 18,
        'class': 'Thanh Niên'
    },
    {
        'age': 10,
        'class': 'Thiếu niên'
    },
    {
        'age': 0,
        'class': 'Nhi Đồng'
    }
]

def ageCalc (nam):
    if (nam < 1900 or nam > currentYear):
        return
    
    age = currentYear - birth
    for item in data:
        if (age >= item['age']):
            return item['class']
    
print(f'Tầng lớp của người đó là {ageCalc(birth)}')