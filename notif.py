import os
import time
from datetime import date
from datetime import datetime as dt

import pandas as pd

#from datetime import timedelta as delta

cwd = os.getcwd             # директория \ расположение файла 
os.chdir("c:/Users/Desktop/Trust")

file = 'fut_notif.xlsx'
xl = pd.ExcelFile(file)     # чтение файла

#print(xl.sheet_names)      # просмотр листов книги
df = xl.parse('Лист1')      # Парсинг первого листа
#print(df)                   # Вывод

curdate = date.today()     # сегодняшняя дата
print(f'curent date ---> {curdate}')                 # Вывод

#df['ФИО'].loc[df.index[1]]  # получение ячейки с ИМЕНЕМ под индексом 1

dfSize = len(df)

def Namelist(df, Size):
    arr = list(range(0,Size))
    for i in range(0, Size):
        arr[i] = (df['ФИО'].loc[df.index[i]])
    return arr

def FiredDate(df, Size):
    arr = list(range(0,Size))
    for i in range(0, Size):
        #arr[i] = dt.strftime(df['Дата убытия'].loc[df.index[i]], "%Y-%m-%d")
        arr[i] = dt.strftime(df['Дата убытия'].loc[df.index[i]], "%d-%m-%Y")
    return arr

def SpaceList(Size):
    arr = list(range(0,Size))
    for i in range(0, Size):
        y = 70
        if i > 0:
            arr[i] = arr[i - 1] + 45
        else:
            arr[i] = y
    return arr

Name = Namelist(df, dfSize)
Fired = FiredDate(df, dfSize)


print(f'Name ---> {Name[1]}')
print(f'Fired date ---> {Fired[1]}')


UnixOD = 86400      # Unix 24 часа
unix = time.mktime(curdate.timetuple())     # Перевод сегоднешней даты в Unix формат
print(f'unix curent date ---> {unix}')

tomrow = date.fromtimestamp(unix + UnixOD)  # Перевод их Unix.(Сегодняшняя дата Unix + 24 Unix = Заврашняя дата Unix)   
print(f'tomrow date ---> {tomrow}') 

i = 0
FiredList =[]
FiredNameList =[]

for i in range(len(Name)):    
    if dt.strptime(dt.strftime(tomrow, '%d-%m-%Y'), '%d-%m-%Y') == dt.strptime(Fired[i], '%d-%m-%Y'):
        FiredList.append(Fired[i])
        FiredNameList.append(Name[i])

#print('1') if dt.strptime(dt.strftime(tomrow, '%Y-%m-%d'), '%Y-%m-%d') == dt.strptime(Fired[1], '%Y-%m-%d') else print('2')

LenList = len(FiredList)
Space = SpaceList(LenList)


print(type(FiredList)) 
print(FiredList[0].replace('-', '.')) 
print(f'Fired List ---> {FiredList}') 
print(f'Fired Name List ---> {FiredNameList}') 
print(f'Space List ---> {Space}') 

