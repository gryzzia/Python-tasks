# Условие: генерируются произвольноые значения индекса, после чего они складываются и выводится общее значение
# Condition: arbitrary index values ​​are generated, after which they are added up and the total value is displayed
from random import randint
a=[randint(1,10) for i in range(3)]
c=a[0]+a[1]+a[2]
print (c,a)
