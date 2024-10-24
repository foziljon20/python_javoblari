# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:02:53 2024

20-dars: Funksiyadan qiymat qaytarish

@author: Diyor
"""


#def toliq_ism_yasa(ism,familiya):
#    """To'liq ism yasovchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    return toliq_ism

#talaba1 =toliq_ism_yasa("olim", "hakimov")
#talaba2 = toliq_ism_yasa("hakim", "olimov")
#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
#print(f"{talaba1} darsga kechikib keldi")



#def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#    if otasining_ismi:
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#    else:
#        toliq_ism = f"{ism} {familiya}"
#    return toliq_ism.title()


#talaba1 =toliq_ism_yasa("olim", "hakimov")
#talaba2 = toliq_ism_yasa("hakim", "olimov", "abrorovich")
#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto = {'kompaniya': kompaniya, 
             'model':model, 
              'rang':rangi, 
              'korobka':korobka, 
              'yil':yili,
              'narx':narxi}
    return avto

avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
#avtolar = [avto1, avto2]
#print('Onlayn bozordagi mavjud avtomashinalar:')
#for avto in avtolar:
#    if avto['narx']:
#        narx = avto['narx']
#    else:
#        narx = "Noma'lum"
#    print(f"{avto['rang']} {avto['model']}. Nraxi: {narx}")
  


#def oraliq(min,max, ):
#    sonlar = []
#    while min<max:
 #       sonlar.append(min)
 #       min +=2
 #   qadam += 2
#    return sonlar
#print(oraliq(0, 10))
#print(oraliq(10, 21))


print("Saytimizdagi avtolar ro'yxatini shakillantiramiz.")
avtolar=[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting ",end='' '\n')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narxi=input("Narxi: ")
    
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
    
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
    
    
print("\nSalonimizdagi avtolar: ")
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narxi: {narx}")
        
















