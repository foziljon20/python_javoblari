# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:10:51 2024

Dasturlash asoslari

#17-dars: Input() va WHILE

@author: Diyor
"""
#input()
#ism = input("Ismingiz nima?")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida?"
#yosh = input(savol)
#yosh = int(yosh)
#height = input("Bo'yingiz necha metr?")
#height = float(height)


#while()

#son = 1
#while son<=5:
#    print(son, end='')
#    son += 1 


#while and input
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting"
#savol += "(dastur to'xtatish uchun 'exit' deb yozing): "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
#print( 'Dastur tugadi ')


# # ishora
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting"
#savol += "(dastur to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#        print(float(qiymat)**2)
#print( 'Dastur to\'xtadi ')


# # break while

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting"
#savol += "(dastur to'xtatish uchun 'exit' deb yozing): "

#while True:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break
#    else:
#        print(float(qiymat)**2)
#print('Dastur tugadi!')

# # break for

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        break
#    print(f"{Son} ning kvadrati {son**2} ga teng")

# CONTINUE

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        break
#    print(f"{son} ning kvadrati {son**2} ga teng")

# # Continue while

#son = 0
#while son<10:
#    son += 1
#    if son%2==0:
#        continue
#    else:
#        print(son)
        
# infinite loop

#son = 0
#while son<10:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)

#son = 0
#while son<10:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)
   

#son = 1
#while son>0:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)


son = 0
while son<10:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)














