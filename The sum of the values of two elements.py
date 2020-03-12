# Генерируется 3 случайных значения, если сумма значений двух элементов будет равна 3-му вывести ДА
# 3 random values ​​are generated if the sum of the values ​​of two elements is equal to the 3rd; print YES
from random import randint
a=[randint(1,10) for i in range(3)]
if a[0]==a[1]+a[2]:
    print ('yes')
if a[1]==a[0]+a[2]:
    print ('yes')
if a[2]==a[1]+a[0]:
    print ('yes')
print (a)
