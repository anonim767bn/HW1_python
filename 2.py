x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if(x2<0>x1 or x2>0<x1):
    if(y2>0<y1 or y2<0>y1):
        print("YES")
    else:print("NO")
else: print("NO")
# если знак х1 совпадает со знаком х2 второго И знак у1 совпадает со знаком у2, то они лежат в одной координатной четверти, а значит выводим YES, 
# в противном случае NO