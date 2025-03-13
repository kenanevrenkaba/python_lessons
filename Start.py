# print('Merhaba')

# String Format

# urunAdi = uA = 'Elma'
# urunFiyati = uF = 5
# urunMiktarı = uM = 2.5
# odenecekUcret = oU = urunFiyati * urunMiktarı 

# sonuc = str(urunMiktarı) + ' kg '+ urunAdi +' için ödemeniz gereken ücret ' + str(urunFiyati * urunMiktarı) + ' TL.'

# sonuc =  '{} kg {} için ödemeniz gereken ücret {} TL.' .format(uM, uA, oU)

# f-String

# sonuc = f'{uM} kg {uA} için ödemeniz gereken ücret {oU} TL'

# Listeler

urunler = [
    ["Elma ", 5],    # 0. Liste [0. indeks, 1. indeks]
    ["Armut", 10],   # 1. Liste [0. indeks, 1. indeks]
    ["Karpuz", 15],  # 2. Liste [0. indeks, 1. indeks]
    ["Muz", 20],     # 3. Liste [0. indeks, 1. indeks]
]

# print(urunler[0][0])
# print(urunler[0][1])
# print(urunler[3][0])

sonuc = urunler[0][0]

print(sonuc)