#Условие: пользовотель вводит координаты точек на оси ОХ и ОУ, определить входят ли указанные точки в радус круга
#Condition: the user enters the coordinates of the points on the axis OX and OY, to determine whether the specified points are included in the circle radius
n=int(input("сколько точек?"))
r=int(input("радиус круга"))
a=0
b=0
i=0
for i in range (1,n+1):
    x=int(input("X"))
    y=int(input("Y"))
    if (x-a)**2+(y-b)**2<r**2:
        print ("vxodiat")
    if (x-a)**2+(y-b)**2>r**2:
        print ("nevxodiat")
