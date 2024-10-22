# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:36:15 2024

#18-dars: WHILE VA RO'YXATLAR

@author: Diyor
"""

print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)
    
    
    
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False
