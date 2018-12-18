"""import numpy as np
a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)
d=np.hstack((a,b))
c=np.vstack((a,b)) 
print(c)
print(d)"""


""" başladı a=np.arange(30).reshape(2,15)
b=np.hsplit(a,3)
c=np.vsplit(a,2)
print(b)
print(c) bitti"""
"""a=np.arange(12).reshape(3,4)
b=a>4
print(b)"""

import numpy as np
import matplotlib.pyplot as plt
import csv
"""aylar=["Ocak","Şubat","mart","nisan","mayıs","haziran","temmuz","ağustos","eylül","ekim","kasım","aralık"]
kahvefiyatları=[105,108,150,178,165,145,123,145,135,168,148,129]
cayfiyatları=[78,85,94,105,149,125,113,117,98,99,100,119]

plt.plot(aylar,kahvefiyatları,label="kahve")
plt.plot(aylar,cayfiyatları,label="çay")
plt.xlabel("Aylar")
plt.ylabel("Fiyatları")
plt.title("çay ve kahve fiyatları")
plt.legend()
plt.show()"""
"""x=np.linspace(0,2,100)
plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")
plt.xlabel("x etiketi")
plt.ylabel("y etiketi")
plt.title("Grafik")
plt.legend()
plt.show()"""
""" baş x=np.arange(0.10,0.2)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("x etkieti")
plt.ylabel("y etiketi")
plt.title("Grafik")
plt.legend()
plt.show()"""
"""x=[2,4,6,8,10]
y=[6,7,8,2,4]
x2=[1,3,5,7,9]
y2=[4,8,22,15,12]"""
"""x1=[200,400,650]
degerler=["protein","karbonhidrat","yağ"]
color=["red","yellow","blue"]
plt.axis([0,10,0,23])
plt.bar(x,y,label="ilk değer",color="red")
plt.scatter(x,y,label="ilk değer",color="red")
plt.bar(x2,y2,label="ikinci değer",color="black")
plt.pie(x,labels=degerler,colors=color)
plt.xlabel("x değerleri")
plt.ylabel ("y değerleri")

plt.show()"""
x=[]
y=[]
with open('C:/Users/user/Desktop/new.txt','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
    
plt.plot(x,y,label="fiyatlar")
plt.xlabel("aylar")
plt.ylabel("fiyatlar")
plt.title("aylara göre fiyatlar")
plt.legend()
plt.show()
print(x)
