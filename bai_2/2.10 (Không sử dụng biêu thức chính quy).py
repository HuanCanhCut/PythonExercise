# Code thuẩn không sử dụng biểu thức chính quy

## huanmeomeo@gmail.com
## huanmeomeo : Tiền tố
## gmail.com : domain
## sau @ : Hậu tố

while(True):
    emailValue = input('Vui lòng nhập email của bạn : ').strip()

    # check invalid email
    if (' ' in emailValue):
        print('Trong email có khoảng cách, Vui lòng nhập lại !')
    
    if('@' in emailValue):
        indexA = emailValue.index('@')
        
        # prefix : Tiền tố
        # postfix : Hậu tố
        emailPrefix = emailValue[0: indexA]
        emailPostFix = emailValue[indexA + 1: ]

        if(emailPrefix != ''):
            if ('.' in emailPostFix):
                dot = emailPostFix.index('.')
                domainPrefix = emailPostFix[0 : dot]
                domainPostfix = emailPostFix[dot + 1: ]
                if (domainPrefix != '') and (domainPostfix != ''):
                        print('Email Valid')
                        break
                if (domainPostfix == ''):
                    print('Domain thiếu hậu tố')
            else :
                print('Domain invalid')
        else :
            print(' Không thấy sự xuất hiện của tiền tố, vui lòng nhập lại')
    else :
        print('@ không có trong email, vui lòng nhập lại')
    



 