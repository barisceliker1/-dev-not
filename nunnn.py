import numpy as np
import sys
import time

#liste=[1,2,3] #normal pythonliste
#numpyliste=np.array([1,2,3]) #numpy dizi
#for e in liste:
 #   print(e)
#for e in numpyliste:
 #   print(e)
#liste=range(1000)
#print(sys.getsizeof(5)*len(liste))#listenin hafızasında
#numpyliste=np.arange(1000)

#print(numpyliste.nbytes)

#boyut=100000
#python liste

#liste=range(boyut)
#liste1=range(boyut)
#numpy dizi
#numpydizi1=np.arange(boyut)
#numpydizi2=np.arange(boyut)

#zamann=time.time()
#sonuc=[(x+y) for x,y in zip (liste,liste1)]
#print("python liste zaman:",(time.time()-zamann)*100,"ms")
#baslangic=time.time()
#sonuc=numpydizi1+numpydizi2
#print("numpy liste zamanı:",(time.time()-baslangic)*100,"ms")
#liste=[1,2,3]
#numpyliste=np.array([1,2,3])
#print(liste+liste)
#python liste toplama
#print(numpyliste+numpyliste)
#print(liste*3)
#print(numpyliste*3)
#print(numpyliste**2)
#print(np.sqrt(numpyliste))
#print(np.log(numpyliste))
#print(np.exp(numpyliste))
#print(numpyliste[0])
#print(numpyliste[1])
#print(numpyliste[2])
#numpyliste=np.array([[1,2,3],[4,5,7],[7,4,2]])
#print(numpyliste[1][1])
#print(numpyliste.ndim)
#print(numpyliste.dtype) #tür
#print(numpyliste.size) # eleman sayısı
#print(numpyliste.itemsize)
#print(numpyliste.shape)
#numpyliste=np.arange(1,5,0.5)
#print(numpyliste)
#numpyliste2=np.linspace(1,5,10)
#print(numpyliste2)
#numpyliste=np.zeros((2,3))#tüm elemanları 0 lan dizi
#numpyliste2=np.ones((3,4))
#print(numpyliste)
#print(numpyliste2)
#numpyliste3=np.empty((2,3))
#print(numpyliste3)
#print(numpyliste.shape)
numpyliste=np.array([[1,2],[2,5],[7,9]])
#print(numpyliste.shape)
#print(numpyliste.reshape(2,3))
#print(numpyliste.ravel())#dizi içerisindeki tüm elemanları birleştirerek tek bir dizi haline yazmay
#matematiksel işlemler
#print(numpyliste.max())#dizinin en yüksek değer
#print(numpyliste.min())#dizinin en küçük değeri
#print(numpyliste.sum())#dizinin elemanları toplamı
#print(np.average(numpyliste))
#print(numpyliste.sum(axis=0))# diizdeki stüunlardaki elemanların toplamı
#print(numpyliste.sum(axis=1))
#print(np.std(numpyliste))
#print(numpyliste[1,1])
#print(numpyliste[0:2,1])
numpyliste=np.array([[1,2,3],[5,3,9],[7,8,9]])
for e in numpyliste.flat:
    print(e)
    
