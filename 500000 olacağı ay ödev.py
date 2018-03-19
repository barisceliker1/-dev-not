sm=500
sf=20
ay=-1
while True:
    sm=sm+(200)
    sf=sf+(10)
    ciro=5000+(sf*sm)
    ay=ay+1
    if ciro>500000:
        yıl=round(ay/12)
        print("cironun 500000 olcağı ay sayısı",ay)
        print("cironun 500000 olacağı yıl sayısı",yıl)
        break

    
