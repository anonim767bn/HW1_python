number = int(input())
x = number//10
i = number%10
return1 = ""

if(x==10):
    print("C")
    # если количество 10ков = 10, то мы выводим С
elif(x==9):
    return1 += "XC"
    # если десятков 9, то добавляем в строчную переменную ХС
elif(x>=4):
    return1 += "X" if x == 4 else ""
    # если количество 10 равно 4, то мы добавляем Х перед L, 
    # в остальных случаях добавляем  после L столько X, насколько количесво 10ков превышает5 
    return1 += "L"
    return1 += "X"*(x-5)


if(i>=4 and i<=8):
    return1 += "I" if i == 4 else ""
    return1 += "V"
    return1 += "I" * (i-5)
elif(x==9):
    return1 += "IX"
    # для единиц используем схожий метод
print(return1)