x=int(input("finansman geliri giriniz"))
y=int(input("pazar geliri giriniz"))
z=int(input("kira geliri giriniz"))
a=int(input("ücret giriniz"))
b=int(input("finansman gideri giriniz"))
c=int(input("pazar gideri giriniz"))
d=int(input("kira gideri giriniz"))
e=int(input("muhasebe gideri giriniz"))
def gelirhesapla(x,y,z):
    global toplamgelir
    toplamgelir=x+y+z
    return toplamgelir
def giderhesaplama(a,b,c,d,e):
    global toplamgider
    toplamgider=a+b+c+d+e
    return toplamgider
def kar(toplamgelir,toplamgider):
    kar=toplamgelir-toplamgider
    if kar>1000:
        print("karlı bir iş")
    elif kar==1000:
        print("denge")
    else:
        print("zarar")

toplamgelir=gelirhesapla(x,y,z)
toplamgider=giderhesaplama(a,b,c,d,e)
kar(toplamgelir,toplamgider)
