a = int(input())
b = int(input())

if(a==0 and b!=0):
    print("NO")
    # здесь мы проверяем, если уравнение на подобии 0х + 5 = 0, то оно решений не имеет
elif(a==0 and b==0):
    print("INF")
    # а если уравнение похоже на 0х + 0 = 0, то оно имеет бесконечно много решений
else:
    if(-b%a!=0):
        print("NO")
    else:
        print((-b)/a)
# и наконец во всех остальных случаях, мы просто вычисляем х, за исключение случаев, когда х нецелое число(видно из примера, что программа должна выводить NO)

