# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:26:47 2024

@author: Student
"""
print("Nhap so km quang duong di duoc cua ban")
sokm = float(input("so Km da di chuyen"))
x= float()
if sokm <=1:
    x=sokm*20000
    print("so tien phai tra la 20000",x)
elif 1<= sokm <=3:
    x=sokm*13000
    print("so tien phai tra",x)
elif 4<= sokm <= 8:
    x=3*13000+(x-3)*12000
    print("so tien phai tra",x)
elif sokm>8:
    x=3*13000+4*12000+(x-7)*10000
    if x>100000:
        x=x-x*0.08
        print("tien ban duoc giam 8%,so tien phai tra la",x)
else:
    print("so tien cua ban la:",x)
  
    
    
 

