# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:48:12 2024

@author: Student
"""
import math
print("ax^2+bx+c=0")
a= float (input("nhap a"))
b= float (input("nhap b"))
c= float (input("nhap c"))
denta = float()
denta= b*b-4*a*c
if denta <0:
     print("phương trình vô nghiệm") 
elif denta==0:
     x=-b/2*a
     print("x la nghiem kep x la:",x)     
else :
    x1= (-(b)+math.sqrt(denta))/(2*a)
    x2= (-(b)+math.sqrt(denta))/(2*a)
    print("phương trình có 2 nghiệm:")
    print("x1=",x1)
    print("x2=",x2)
    
   
    