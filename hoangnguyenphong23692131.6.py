# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:03:28 2024

@author: Student
"""

print("kiem tra 3 canh")
a=float(input("nhap a:"))
b=float(input("nhap b:"))
c=float(input("nhap c:"))
if a+b>c and a+c>b and b+c>a:
    if a*a ==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print(a,b,c,"la 3 canh cua tam giac vuong")
    elif a==b and b==c:
        print(a,b,c,"la 3 canh cua tam giac deu")
    elif a==b or b==c or c==a:
        print(a,b,c,"la 3 canh cua tam giac can")
    else:
        print(a,b,c,"la 3 canh cua tam giac thuong")
else:
        print(a,b,c,"khong la 3 canh cua 1 tam giac")
