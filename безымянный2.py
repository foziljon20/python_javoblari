# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:15:04 2024
 
#16-dars: Nesting


@author: Diyor
"""

#Lug'atlar ro'yxati

car0 = {
    'model':'lacetti',
    'rang':'oq',
    'yil':'2018',
    'narx':'13000',
    'km':'50000',
    'karobka':'avtomat'
    }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':'2015',
        'narx':'9000',
        'km':'89000',
        'karobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':'2019',
        'narx':'15000',
        'km':'20000',
        'karobka':'mexanika'
       }

#car = car2
#print(f"{car['model'].title()},"
#      f"{car['rang']} rang,"
#      f"{car['yil']}-yil, {car['narx']}$")

#cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()},"
#          f"{car['rang']} rang,"
#          f"{car['yil']}-yil, {car['narx']}$")

#print(f"{cars[2]['rang'].title()} " 
#       f"{cars[0]['model']}")

#malibus=[]
#for n in range(10):
#    new_car = {
#        'model':'malibu',
#        'rang':None, #rang noaniq
#        'yil':2020 ,
#        'narx':None,
#        'km':0,
#        'korobka':'avto'
#        }
#    malibus.append(new_car)
    
#for malibu in malibus[:3]:
#    malibu['rang']='qizil'

# for malibu in malibus:
#    print(malibu)

#for malibu in malibus[3:6]:
#    malibu['rang']='qora'
    
# for malibu in malibus:
#    print(malibu)

#for malibu in malibus[6:]:
#    malibu['rang']='qora'
#    malibu['korobka']='mexanika'
    
#    for malibu in malibus:
#        if malibu['korobka']=='avto':
#            malibu['narx']==40000
#        else:
#    
    
    
    
    
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in  dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())
        
        
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(f"{til.upper()} ", end='')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    